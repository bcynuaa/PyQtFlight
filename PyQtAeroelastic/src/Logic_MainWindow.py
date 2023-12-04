# coding = "utf-8"
# author: bcynuaa
# date  : 2023/05/04

####################################################################################################
# This file is used to build logic in pyside qt mainwindow

import copy
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui.Ui_MainWindow import *
from src.ThingsInMainWindow import *
from src.Interactive import *
from src.AuxiliaryDialog import *

class MainWindow(Ui_MainWindow, QMainWindow):
    
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.__initialAll()
        pass
    
    def writeToInfoTextBrowser(self, message: str) -> None:
        self.info_text_browser.setFontFamily('times new roman')
        self.info_text_browser.setFontPointSize(12)
        message = SPLIT_LINE + getCurrentTime() + message + SPLIT_LINE
        self.info_text_browser.append(message)
        self.info_text_browser.moveCursor(self.info_text_browser.textCursor().End)
        pass
    
    def __initialAll(self) -> None:
        self.interactive: Interactive = Interactive()
        self.__initialActionTriggered()
        self.__initialInfoTextBrowser()
        self.__initialPyvistaGroupBox()
        self.__initialMatplotlibTabWidget()
        pass
    
    def __initialActionTriggered(self) -> None:
        self.actionLoad_Data_Path.triggered.connect(self.__loadDataPath)
        self.actionExport_GIF.triggered.connect(self.__exportGIF)
        self.actionExport_MP4.triggered.connect(self.__exportMP4)
        
        self.actionNew_Pyvista_Window.triggered.connect(self.__showNewPyvistaWindow)
        self.actionOne_Curve_in_New_Window.triggered.connect(self.__showOneCurveInNewWindow)
        self.actionAll_In_One.triggered.connect(self.__showMultiCurvesInNewWindowAllInOne)
        self.actionSplit.triggered.connect(self.__showMultiCurvesInNewWindowSplit)
        self.actionAuto_Display.triggered.connect(self.__autoDisplay)
        self.actionClear_Log_Browser.triggered.connect(self.__initialInfoTextBrowser)
        
        self.actionDisplacement_Magnification.triggered.connect(self.__setDisplacementMagnification)
        self.actionShow_Edges.triggered.connect(self.__setShowEdges)
        self.actionChange_Scalar.triggered.connect(self.__changeScalar)
        self.actionChange_Cmap.triggered.connect(self.__changeCmap)
        self.actionChange_Scalar_Clim.triggered.connect(self.__changeScalarClim)
        pass
    
    def __initialInfoTextBrowser(self) -> None:
        self.info_text_browser.clear()
        self.info_text_browser.setMinimumHeight(200)
        self.writeToInfoTextBrowser(WELLCOME_INFO)
        self.info_text_browser.moveCursor(self.info_text_browser.textCursor().Start)
        pass
    
    def __initialPyvistaGroupBox(self) -> None:
        self.pyvista_group_box.setMinimumWidth(600)
        self.pyvista_layout = QVBoxLayout(self.pyvista_group_box)
        self.pyvista_layout.addWidget(self.interactive.plotter_interactor)
        pass
    
    def __initialMatplotlibTabWidget(self) -> None:
        self.matplotlib_group_box.setMinimumWidth(400)
        self.matplotlib_layout = QVBoxLayout(self.matplotlib_group_box)
        self.matplotlib_layout.addWidget(self.interactive.matplotlib_canvas_widget.toolbar)
        self.matplotlib_layout.addWidget(self.interactive.matplotlib_canvas_widget.canvas)
        pass
    
    def __loadDataPath(self) -> None:
        data_path: str = QFileDialog.getExistingDirectory(self, "选取模拟数据路径", "./")
        try:
            self.interactive.loadData(data_path)
            self.writeToInfoTextBrowser(self.interactive.multi_blocks.__str__())
            self.writeToInfoTextBrowser("load data from " + data_path)
            pass
        except:
            QMessageBox.critical(self, "错误数据路径", "路径" + data_path + "不是有效数据路径")
            pass
        pass
    
    def __exportGIF(self) -> None:
        skip_step, fps = self.__getSkipStepAndFPS()
        if skip_step == None or fps == None:
            return
            pass
        loop: int = QInputDialog.getInt(self, "loop", "请输入循环次数", 0, 0, 10)[0]
        export_gif_filename: str = QFileDialog.getSaveFileName(
            self,
            "导出GIF",
            "./",
            "GIF (*.gif)"
        )[0]
        multi_blocks: MultiBlocksByGenDis = copy.deepcopy(self.interactive.multi_blocks)
        multi_blocks.setStepByIndex(0)
        plotter: pyvista.Plotter = pyvista.Plotter(
            notebook=False,
            off_screen=True,
        )
        plotter.open_gif(export_gif_filename, fps=fps, loop=loop)
        plotter.add_mesh(
            multi_blocks.unstructured_grid,
            scalars=multi_blocks.active_scalar,
            clim=multi_blocks.scalars_clim_dict[multi_blocks.active_scalar],
            show_edges=self.interactive.whether_show_edges,
            cmap=pyvista.global_theme.cmap
        )
        plotter.camera_position = self.interactive.plotter_interactor.camera_position
        plotter.add_axes()
        plotter.add_bounding_box()
        plotter.write_frame()
        progress_bar_dialog: QProgressDialog = QProgressDialog(
            "正在导出GIF...", "取消", 0, multi_blocks.n_steps, self
        )
        progress_bar_dialog.setWindowTitle("导出GIF")
        progress_bar_dialog.show()
        for step in range(0, multi_blocks.n_steps, skip_step):
            progress_bar_dialog.setValue(step)
            QCoreApplication.processEvents()
            multi_blocks.setStepByIndex(step)
            plotter.add_axes()
            plotter.add_bounding_box()
            plotter.write_frame()
            if progress_bar_dialog.wasCanceled():
                break
                pass
            pass
        plotter.close()
        progress_bar_dialog.setValue(multi_blocks.n_steps)
        self.writeToInfoTextBrowser("export GIF to " + export_gif_filename)
        pass
    
    def __exportMP4(self):
        skip_step, fps = self.__getSkipStepAndFPS()
        if skip_step == None or fps == None:
            return
            pass
        quality_list: list = list(range(1, 11, 1))
        for i in range(len(quality_list)):
            quality_list[i] = str(quality_list[i])
            pass
        quality: int = eval( QInputDialog.getItem(self, "quality", "请选择视频质量", quality_list, 5)[0] )
        export_mp4_filename: str = QFileDialog.getSaveFileName(
            self,
            "导出MP4",
            "./",
            "GIF (*.mp4)"
        )[0]
        multi_blocks: MultiBlocksByGenDis = copy.deepcopy(self.interactive.multi_blocks)
        multi_blocks.setStepByIndex(0)
        plotter: pyvista.Plotter = pyvista.Plotter(
            notebook=False,
            off_screen=True,
        )
        plotter.open_movie(export_mp4_filename, framerate=fps, quality=quality)
        plotter.add_mesh(
            multi_blocks.unstructured_grid,
            scalars=multi_blocks.active_scalar,
            clim=multi_blocks.scalars_clim_dict[multi_blocks.active_scalar],
            show_edges=self.interactive.whether_show_edges,
            cmap=pyvista.global_theme.cmap
        )
        plotter.camera_position = self.interactive.plotter_interactor.camera_position
        plotter.add_axes()
        plotter.add_bounding_box()
        plotter.write_frame()
        progress_bar_dialog: QProgressDialog = QProgressDialog(
            "正在导出MP4...", "取消", 0, multi_blocks.n_steps, self
        )
        progress_bar_dialog.setWindowTitle("导出MP4")
        progress_bar_dialog.show()
        for step in range(0, multi_blocks.n_steps, skip_step):
            progress_bar_dialog.setValue(step)
            QCoreApplication.processEvents()
            multi_blocks.setStepByIndex(step)
            plotter.add_axes()
            plotter.add_bounding_box()
            plotter.write_frame()
            if progress_bar_dialog.wasCanceled():
                break
                pass
            pass
        plotter.close()
        progress_bar_dialog.setValue(multi_blocks.n_steps)
        self.writeToInfoTextBrowser("export mp4 to " + export_mp4_filename)
        pass
    
    def __showNewPyvistaWindow(self) -> None:
        self.interactive.newPyvistaWindow()
        pass
    
    def __showOneCurveInNewWindow(self) -> None:
        item: list = [str(num) for num in list(range(1, self.interactive.multi_blocks.n_q+1))]
        index, ok_pressed = QInputDialog.getItem(self, "绘制广义位移响应", "选择广义位移响应序号", item)
        if ok_pressed == True:
            self.interactive.newMatplotlibOneCurve(int(eval(index))-1)
            pass
        else:
            pass
        self.writeToInfoTextBrowser("show curve " + index + " in new window")
        pass
    
    def __showMultiCurvesInNewWindow(self) -> list:
        string, ok_pressed = QInputDialog.getText(
            self,
            "绘制多条广义位移响应（1-" + str(self.interactive.multi_blocks.n_q) + "）",
            "输入广序号如：1, 3, 4-7, 9"
        )
        if ok_pressed == True:
            index_list_raw: list = stringToIndexList(string)
            index_list: list = list()
            for item in index_list_raw:
                if item < 1 or item > self.interactive.multi_blocks.n_q:
                    QMessageBox.warning(self, "警告", "序号" + str(item) + "不在范围内，已自动剔除")
                    pass
                else:
                    index_list.append(item-1)
                    pass
                pass
            self.writeToInfoTextBrowser(
                "show multi-curves of " + str(np.array(index_list)+1) + " in new window."
            )
            return index_list
        else:
            pass
        pass
    
    def __showMultiCurvesInNewWindowAllInOne(self):
        try:
            self.interactive.newMatplotlibMultiCurvesAllInOne(
                self.__showMultiCurvesInNewWindow()
            )
            pass
        except:
            QMessageBox.critical(self, "格式错误", "输入格式错误，请按照 1, 3, 4-7, 9 输入")
            pass
        pass
    
    def __showMultiCurvesInNewWindowSplit(self):
        try:
            self.interactive.newMatplotlibMultiCurvesSplit(
                self.__showMultiCurvesInNewWindow()
            )
            pass
        except:
            QMessageBox.critical(self, "格式错误", "输入格式错误，请按照 1, 3, 4-7, 9 输入")
            pass
        pass
    
    def __getSkipStepAndFPS(self):
        skip_step, ok_pressed1 = QInputDialog.getInt(
            self,
            "skip step",
            "共" + str(self.interactive.multi_blocks.n_steps) + "步，选择跳跃步数：",
            1, 1, self.interactive.multi_blocks.n_steps, 1
        )
        if ok_pressed1 == True:
            fps, ok_pressed2 = QInputDialog.getDouble(
                self,
                "fps",
                "帧率（这可能会因每步广义位移计算耗时，而不生效）：",
                60,
                0.1, 100
            )
            if ok_pressed2 == True:
                return skip_step, fps
                pass
            pass
        return None, None
        pass
    
    def __autoDisplay(self) -> None:
        skip_step, fps = self.__getSkipStepAndFPS()
        if skip_step != None and fps != None:
            self.interactive.autoDisplay(skip_step, fps)
            self.writeToInfoTextBrowser(
                "auto-displaying with skip step: " + str(skip_step) + " and fps: " + str(fps)
            )
            pass
        pass
    
    def __setDisplacementMagnification(self) -> None:
        magnification, ok_pressed = QInputDialog.getDouble(
            self, "设置位移放大倍数", "请输入位移放大倍数",
            self.interactive.multi_blocks.displacement_magnification,
        )
        if magnification <= 0:
            QMessageBox.warning(self, "警告", "位移放大倍数不能为零或负数")
            magnification = self.interactive.multi_blocks.displacement_magnification
            pass
        if ok_pressed == True:
            magnification = float(magnification)
            self.interactive.multi_blocks.setDisplacementMagnification(magnification)
            pass
        self.writeToInfoTextBrowser("set displacement magnification to " + str(magnification))
        pass
    
    def __setShowEdges(self) -> None:
        whether = QMessageBox.question(self, "选项", "是否显示网格线", QMessageBox.Yes | QMessageBox.No)
        self.interactive.whether_show_edges = True if whether == QMessageBox.StandardButton.Yes else False
        self.interactive.refresh()
        self.writeToInfoTextBrowser("set whether show edges to " + str(self.interactive.whether_show_edges))
        pass
    
    def __changeScalar(self) -> None:
        item, ok_pressed = QInputDialog.getItem(self, "设置云图标量", "选择云图标量", self.interactive.multi_blocks.scalars_clim_dict.keys())
        if ok_pressed == True:
            self.interactive.multi_blocks.setActivatedScalar(item)
            pass
        else:
            pass
        self.interactive.refresh()
        self.writeToInfoTextBrowser("change scalar to " + item)
        pass
    
    def __changeCmap(self) -> None:
        self.writeToInfoTextBrowser(
            r"you may find cmap information in url 'https://matplotlib.org/stable/tutorials/colors/colormaps.html'"
        )
        cmap_chosen_dialog: CmapChosenDialog = CmapChosenDialog(pyvista.global_theme.cmap)
        cmap_chosen_dialog.show()
        cmap_chosen_dialog.exec_()
        current_cmap: str = cmap_chosen_dialog.accept()
        if pyvista.global_theme.cmap == current_cmap:
            pass
        else:
            pyvista.global_theme.cmap = current_cmap
            self.interactive.refresh()
            self.writeToInfoTextBrowser("change cmap to " + current_cmap)
            pass
        pass
    
    def __changeScalarClim(self) -> None:
        set_scalar_clim_dialog: SetScalarClimDialog = SetScalarClimDialog(
            self.interactive.multi_blocks.active_scalar,
            self.interactive.multi_blocks.scalars_clim_dict
        )
        set_scalar_clim_dialog.show()
        set_scalar_clim_dialog.exec_()
        current_scalar, current_scalar_clim = set_scalar_clim_dialog.accept()
        if current_scalar_clim == self.interactive.multi_blocks.scalars_clim_dict[current_scalar]:
            self.writeToInfoTextBrowser("No change to " + current_scalar)
            pass
        else:
            self.interactive.multi_blocks.setScalarClim(current_scalar, current_scalar_clim)
            self.writeToInfoTextBrowser(
                "change scalar clim of "
                + current_scalar + " to range "
                + str(current_scalar_clim)
            )
            self.interactive.refresh()
            pass
        pass

    pass

####################################################################################################