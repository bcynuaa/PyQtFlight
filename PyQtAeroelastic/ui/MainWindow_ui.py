# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/bcynuaa/Project/PyQtFlight/PyQtAeroelastic/ui/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(955, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.matplotlib_group_box = QtWidgets.QGroupBox(self.centralwidget)
        self.matplotlib_group_box.setObjectName("matplotlib_group_box")
        self.verticalLayout.addWidget(self.matplotlib_group_box)
        self.info_text_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.info_text_browser.setObjectName("info_text_browser")
        self.verticalLayout.addWidget(self.info_text_browser)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.pyvista_group_box = QtWidgets.QGroupBox(self.centralwidget)
        self.pyvista_group_box.setObjectName("pyvista_group_box")
        self.horizontalLayout.addWidget(self.pyvista_group_box)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 955, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAnnimation = QtWidgets.QMenu(self.menuFile)
        self.menuAnnimation.setObjectName("menuAnnimation")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuMulti_Curves_in_New_Window = QtWidgets.QMenu(self.menuView)
        self.menuMulti_Curves_in_New_Window.setObjectName("menuMulti_Curves_in_New_Window")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Data_Path = QtWidgets.QAction(MainWindow)
        self.actionLoad_Data_Path.setObjectName("actionLoad_Data_Path")
        self.actionDisplacement_Magnification = QtWidgets.QAction(MainWindow)
        self.actionDisplacement_Magnification.setObjectName("actionDisplacement_Magnification")
        self.actionShow_Edges = QtWidgets.QAction(MainWindow)
        self.actionShow_Edges.setObjectName("actionShow_Edges")
        self.actionOne_Curve_in_New_Window = QtWidgets.QAction(MainWindow)
        self.actionOne_Curve_in_New_Window.setObjectName("actionOne_Curve_in_New_Window")
        self.actionChange_Scalar = QtWidgets.QAction(MainWindow)
        self.actionChange_Scalar.setObjectName("actionChange_Scalar")
        self.actionNew_Pyvista_Window = QtWidgets.QAction(MainWindow)
        self.actionNew_Pyvista_Window.setObjectName("actionNew_Pyvista_Window")
        self.actionAll_In_One = QtWidgets.QAction(MainWindow)
        self.actionAll_In_One.setObjectName("actionAll_In_One")
        self.actionSplit = QtWidgets.QAction(MainWindow)
        self.actionSplit.setObjectName("actionSplit")
        self.actionClear_Log_Browser = QtWidgets.QAction(MainWindow)
        self.actionClear_Log_Browser.setObjectName("actionClear_Log_Browser")
        self.actionChange_Cmap = QtWidgets.QAction(MainWindow)
        self.actionChange_Cmap.setObjectName("actionChange_Cmap")
        self.actionChange_Scalar_Clim = QtWidgets.QAction(MainWindow)
        self.actionChange_Scalar_Clim.setObjectName("actionChange_Scalar_Clim")
        self.actionAuto_Display = QtWidgets.QAction(MainWindow)
        self.actionAuto_Display.setObjectName("actionAuto_Display")
        self.actionExport_GIF = QtWidgets.QAction(MainWindow)
        self.actionExport_GIF.setObjectName("actionExport_GIF")
        self.actionExport_MP4 = QtWidgets.QAction(MainWindow)
        self.actionExport_MP4.setObjectName("actionExport_MP4")
        self.menuAnnimation.addAction(self.actionExport_GIF)
        self.menuAnnimation.addAction(self.actionExport_MP4)
        self.menuFile.addAction(self.actionLoad_Data_Path)
        self.menuFile.addAction(self.menuAnnimation.menuAction())
        self.menuMulti_Curves_in_New_Window.addAction(self.actionAll_In_One)
        self.menuMulti_Curves_in_New_Window.addAction(self.actionSplit)
        self.menuView.addAction(self.actionNew_Pyvista_Window)
        self.menuView.addAction(self.actionOne_Curve_in_New_Window)
        self.menuView.addAction(self.menuMulti_Curves_in_New_Window.menuAction())
        self.menuView.addAction(self.actionAuto_Display)
        self.menuView.addAction(self.actionClear_Log_Browser)
        self.menuOptions.addAction(self.actionDisplacement_Magnification)
        self.menuOptions.addAction(self.actionShow_Edges)
        self.menuOptions.addAction(self.actionChange_Scalar)
        self.menuOptions.addAction(self.actionChange_Cmap)
        self.menuOptions.addAction(self.actionChange_Scalar_Clim)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.matplotlib_group_box.setTitle(_translate("MainWindow", "广义位移响应曲线-Matplotlib"))
        self.pyvista_group_box.setTitle(_translate("MainWindow", "三维动态模型展示-Pyvista"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAnnimation.setTitle(_translate("MainWindow", "Annimation"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuMulti_Curves_in_New_Window.setTitle(_translate("MainWindow", "Multi-Curves in New Window"))
        self.menuOptions.setTitle(_translate("MainWindow", "Option"))
        self.actionLoad_Data_Path.setText(_translate("MainWindow", "Load Data Path"))
        self.actionDisplacement_Magnification.setText(_translate("MainWindow", "Displacement Magnification"))
        self.actionShow_Edges.setText(_translate("MainWindow", "Show Edges"))
        self.actionOne_Curve_in_New_Window.setText(_translate("MainWindow", "One Curve in New Window "))
        self.actionChange_Scalar.setText(_translate("MainWindow", "Change Scalar"))
        self.actionNew_Pyvista_Window.setText(_translate("MainWindow", "New Pyvista Window"))
        self.actionAll_In_One.setText(_translate("MainWindow", "All In One"))
        self.actionSplit.setText(_translate("MainWindow", "Split"))
        self.actionClear_Log_Browser.setText(_translate("MainWindow", "Clear Log Browser"))
        self.actionChange_Cmap.setText(_translate("MainWindow", "Change Cmap"))
        self.actionChange_Scalar_Clim.setText(_translate("MainWindow", "Change Scalar Clim"))
        self.actionAuto_Display.setText(_translate("MainWindow", "Auto-Display"))
        self.actionExport_GIF.setText(_translate("MainWindow", "Export GIF"))
        self.actionExport_MP4.setText(_translate("MainWindow", "Export MP4"))
