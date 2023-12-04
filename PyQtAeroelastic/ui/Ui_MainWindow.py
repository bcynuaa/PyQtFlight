# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(955, 609)
        self.actionLoad_Data_Path = QAction(MainWindow)
        self.actionLoad_Data_Path.setObjectName(u"actionLoad_Data_Path")
        self.actionDisplacement_Magnification = QAction(MainWindow)
        self.actionDisplacement_Magnification.setObjectName(u"actionDisplacement_Magnification")
        self.actionShow_Edges = QAction(MainWindow)
        self.actionShow_Edges.setObjectName(u"actionShow_Edges")
        self.actionOne_Curve_in_New_Window = QAction(MainWindow)
        self.actionOne_Curve_in_New_Window.setObjectName(u"actionOne_Curve_in_New_Window")
        self.actionChange_Scalar = QAction(MainWindow)
        self.actionChange_Scalar.setObjectName(u"actionChange_Scalar")
        self.actionNew_Pyvista_Window = QAction(MainWindow)
        self.actionNew_Pyvista_Window.setObjectName(u"actionNew_Pyvista_Window")
        self.actionAll_In_One = QAction(MainWindow)
        self.actionAll_In_One.setObjectName(u"actionAll_In_One")
        self.actionSplit = QAction(MainWindow)
        self.actionSplit.setObjectName(u"actionSplit")
        self.actionClear_Log_Browser = QAction(MainWindow)
        self.actionClear_Log_Browser.setObjectName(u"actionClear_Log_Browser")
        self.actionChange_Cmap = QAction(MainWindow)
        self.actionChange_Cmap.setObjectName(u"actionChange_Cmap")
        self.actionChange_Scalar_Clim = QAction(MainWindow)
        self.actionChange_Scalar_Clim.setObjectName(u"actionChange_Scalar_Clim")
        self.actionAuto_Display = QAction(MainWindow)
        self.actionAuto_Display.setObjectName(u"actionAuto_Display")
        self.actionExport_GIF = QAction(MainWindow)
        self.actionExport_GIF.setObjectName(u"actionExport_GIF")
        self.actionExport_MP4 = QAction(MainWindow)
        self.actionExport_MP4.setObjectName(u"actionExport_MP4")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.matplotlib_group_box = QGroupBox(self.centralwidget)
        self.matplotlib_group_box.setObjectName(u"matplotlib_group_box")

        self.verticalLayout.addWidget(self.matplotlib_group_box)

        self.info_text_browser = QTextBrowser(self.centralwidget)
        self.info_text_browser.setObjectName(u"info_text_browser")

        self.verticalLayout.addWidget(self.info_text_browser)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.pyvista_group_box = QGroupBox(self.centralwidget)
        self.pyvista_group_box.setObjectName(u"pyvista_group_box")

        self.horizontalLayout.addWidget(self.pyvista_group_box)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 955, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAnnimation = QMenu(self.menuFile)
        self.menuAnnimation.setObjectName(u"menuAnnimation")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuMulti_Curves_in_New_Window = QMenu(self.menuView)
        self.menuMulti_Curves_in_New_Window.setObjectName(u"menuMulti_Curves_in_New_Window")
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuFile.addAction(self.actionLoad_Data_Path)
        self.menuFile.addAction(self.menuAnnimation.menuAction())
        self.menuAnnimation.addAction(self.actionExport_GIF)
        self.menuAnnimation.addAction(self.actionExport_MP4)
        self.menuView.addAction(self.actionNew_Pyvista_Window)
        self.menuView.addAction(self.actionOne_Curve_in_New_Window)
        self.menuView.addAction(self.menuMulti_Curves_in_New_Window.menuAction())
        self.menuView.addAction(self.actionAuto_Display)
        self.menuView.addAction(self.actionClear_Log_Browser)
        self.menuMulti_Curves_in_New_Window.addAction(self.actionAll_In_One)
        self.menuMulti_Curves_in_New_Window.addAction(self.actionSplit)
        self.menuOptions.addAction(self.actionDisplacement_Magnification)
        self.menuOptions.addAction(self.actionShow_Edges)
        self.menuOptions.addAction(self.actionChange_Scalar)
        self.menuOptions.addAction(self.actionChange_Cmap)
        self.menuOptions.addAction(self.actionChange_Scalar_Clim)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLoad_Data_Path.setText(QCoreApplication.translate("MainWindow", u"Load Data Path", None))
        self.actionDisplacement_Magnification.setText(QCoreApplication.translate("MainWindow", u"Displacement Magnification", None))
        self.actionShow_Edges.setText(QCoreApplication.translate("MainWindow", u"Show Edges", None))
        self.actionOne_Curve_in_New_Window.setText(QCoreApplication.translate("MainWindow", u"One Curve in New Window ", None))
        self.actionChange_Scalar.setText(QCoreApplication.translate("MainWindow", u"Change Scalar", None))
        self.actionNew_Pyvista_Window.setText(QCoreApplication.translate("MainWindow", u"New Pyvista Window", None))
        self.actionAll_In_One.setText(QCoreApplication.translate("MainWindow", u"All In One", None))
        self.actionSplit.setText(QCoreApplication.translate("MainWindow", u"Split", None))
        self.actionClear_Log_Browser.setText(QCoreApplication.translate("MainWindow", u"Clear Log Browser", None))
        self.actionChange_Cmap.setText(QCoreApplication.translate("MainWindow", u"Change Cmap", None))
        self.actionChange_Scalar_Clim.setText(QCoreApplication.translate("MainWindow", u"Change Scalar Clim", None))
        self.actionAuto_Display.setText(QCoreApplication.translate("MainWindow", u"Auto-Display", None))
        self.actionExport_GIF.setText(QCoreApplication.translate("MainWindow", u"Export GIF", None))
        self.actionExport_MP4.setText(QCoreApplication.translate("MainWindow", u"Export MP4", None))
        self.matplotlib_group_box.setTitle(QCoreApplication.translate("MainWindow", u"\u5e7f\u4e49\u4f4d\u79fb\u54cd\u5e94\u66f2\u7ebf-Matplotlib", None))
        self.pyvista_group_box.setTitle(QCoreApplication.translate("MainWindow", u"\u4e09\u7ef4\u52a8\u6001\u6a21\u578b\u5c55\u793a-Pyvista", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAnnimation.setTitle(QCoreApplication.translate("MainWindow", u"Annimation", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuMulti_Curves_in_New_Window.setTitle(QCoreApplication.translate("MainWindow", u"Multi-Curves in New Window", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Option", None))
    # retranslateUi

