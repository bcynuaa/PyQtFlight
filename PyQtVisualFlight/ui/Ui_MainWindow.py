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


class Ui_PyQtVisualFlight(object):
    def setupUi(self, PyQtVisualFlight):
        if not PyQtVisualFlight.objectName():
            PyQtVisualFlight.setObjectName(u"PyQtVisualFlight")
        PyQtVisualFlight.resize(990, 680)
        self.actionLoad_Domain_Files = QAction(PyQtVisualFlight)
        self.actionLoad_Domain_Files.setObjectName(u"actionLoad_Domain_Files")
        self.actionFlight_Test_Observer = QAction(PyQtVisualFlight)
        self.actionFlight_Test_Observer.setObjectName(u"actionFlight_Test_Observer")
        self.actionSimulation_Observer = QAction(PyQtVisualFlight)
        self.actionSimulation_Observer.setObjectName(u"actionSimulation_Observer")
        self.actionStart_Updating = QAction(PyQtVisualFlight)
        self.actionStart_Updating.setObjectName(u"actionStart_Updating")
        self.actionEnd_Updating = QAction(PyQtVisualFlight)
        self.actionEnd_Updating.setObjectName(u"actionEnd_Updating")
        self.actionFlight_Test_Magnification = QAction(PyQtVisualFlight)
        self.actionFlight_Test_Magnification.setObjectName(u"actionFlight_Test_Magnification")
        self.actionSimulation_Magnification = QAction(PyQtVisualFlight)
        self.actionSimulation_Magnification.setObjectName(u"actionSimulation_Magnification")
        self.centralwidget = QWidget(PyQtVisualFlight)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.flight_test_vertical_layout = QVBoxLayout()
        self.flight_test_vertical_layout.setObjectName(u"flight_test_vertical_layout")
        self.flight_test_group_box = QGroupBox(self.centralwidget)
        self.flight_test_group_box.setObjectName(u"flight_test_group_box")

        self.flight_test_vertical_layout.addWidget(self.flight_test_group_box)

        self.flight_test_tab_widget = QTabWidget(self.centralwidget)
        self.flight_test_tab_widget.setObjectName(u"flight_test_tab_widget")
        self.flight_test_time_domain_tab = QWidget()
        self.flight_test_time_domain_tab.setObjectName(u"flight_test_time_domain_tab")
        self.flight_test_tab_widget.addTab(self.flight_test_time_domain_tab, "")
        self.flight_test_frequency_domain_tab = QWidget()
        self.flight_test_frequency_domain_tab.setObjectName(u"flight_test_frequency_domain_tab")
        self.flight_test_tab_widget.addTab(self.flight_test_frequency_domain_tab, "")

        self.flight_test_vertical_layout.addWidget(self.flight_test_tab_widget)


        self.horizontalLayout.addLayout(self.flight_test_vertical_layout)

        self.simulation_vertical_layout = QVBoxLayout()
        self.simulation_vertical_layout.setObjectName(u"simulation_vertical_layout")
        self.simulation_group_box = QGroupBox(self.centralwidget)
        self.simulation_group_box.setObjectName(u"simulation_group_box")

        self.simulation_vertical_layout.addWidget(self.simulation_group_box)

        self.simulation_tab_widget = QTabWidget(self.centralwidget)
        self.simulation_tab_widget.setObjectName(u"simulation_tab_widget")
        self.simulation_time_domain_tab = QWidget()
        self.simulation_time_domain_tab.setObjectName(u"simulation_time_domain_tab")
        self.simulation_tab_widget.addTab(self.simulation_time_domain_tab, "")
        self.simulation_frequency_domain_tab = QWidget()
        self.simulation_frequency_domain_tab.setObjectName(u"simulation_frequency_domain_tab")
        self.simulation_tab_widget.addTab(self.simulation_frequency_domain_tab, "")

        self.simulation_vertical_layout.addWidget(self.simulation_tab_widget)


        self.horizontalLayout.addLayout(self.simulation_vertical_layout)

        PyQtVisualFlight.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PyQtVisualFlight)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 990, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menuConnect_To_Observer = QMenu(self.menu)
        self.menuConnect_To_Observer.setObjectName(u"menuConnect_To_Observer")
        self.menuOption = QMenu(self.menubar)
        self.menuOption.setObjectName(u"menuOption")
        self.menuMagnification = QMenu(self.menuOption)
        self.menuMagnification.setObjectName(u"menuMagnification")
        PyQtVisualFlight.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PyQtVisualFlight)
        self.statusbar.setObjectName(u"statusbar")
        PyQtVisualFlight.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())
        self.menu.addAction(self.actionLoad_Domain_Files)
        self.menu.addAction(self.menuConnect_To_Observer.menuAction())
        self.menu.addAction(self.actionStart_Updating)
        self.menu.addAction(self.actionEnd_Updating)
        self.menuConnect_To_Observer.addAction(self.actionFlight_Test_Observer)
        self.menuConnect_To_Observer.addAction(self.actionSimulation_Observer)
        self.menuOption.addAction(self.menuMagnification.menuAction())
        self.menuMagnification.addAction(self.actionFlight_Test_Magnification)
        self.menuMagnification.addAction(self.actionSimulation_Magnification)

        self.retranslateUi(PyQtVisualFlight)

        self.flight_test_tab_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(PyQtVisualFlight)
    # setupUi

    def retranslateUi(self, PyQtVisualFlight):
        PyQtVisualFlight.setWindowTitle(QCoreApplication.translate("PyQtVisualFlight", u"MainWindow", None))
        self.actionLoad_Domain_Files.setText(QCoreApplication.translate("PyQtVisualFlight", u"Load Domain Files", None))
        self.actionFlight_Test_Observer.setText(QCoreApplication.translate("PyQtVisualFlight", u"Flight Test Observer", None))
        self.actionSimulation_Observer.setText(QCoreApplication.translate("PyQtVisualFlight", u"Simulation Observer", None))
        self.actionStart_Updating.setText(QCoreApplication.translate("PyQtVisualFlight", u"Start Updating", None))
        self.actionEnd_Updating.setText(QCoreApplication.translate("PyQtVisualFlight", u"End Updating", None))
        self.actionFlight_Test_Magnification.setText(QCoreApplication.translate("PyQtVisualFlight", u"Flight Test Magnification", None))
        self.actionSimulation_Magnification.setText(QCoreApplication.translate("PyQtVisualFlight", u"Simulation Magnification", None))
        self.flight_test_group_box.setTitle(QCoreApplication.translate("PyQtVisualFlight", u"\u8bd5\u98de\u6570\u636e3D\u6a21\u578b\u5c55\u793a\u7a97", None))
        self.flight_test_tab_widget.setTabText(self.flight_test_tab_widget.indexOf(self.flight_test_time_domain_tab), QCoreApplication.translate("PyQtVisualFlight", u"Tab 1", None))
        self.flight_test_tab_widget.setTabText(self.flight_test_tab_widget.indexOf(self.flight_test_frequency_domain_tab), QCoreApplication.translate("PyQtVisualFlight", u"Tab 2", None))
        self.simulation_group_box.setTitle(QCoreApplication.translate("PyQtVisualFlight", u"\u4eff\u771f\u6570\u636e3D\u6a21\u578b\u5c55\u793a\u7a97", None))
        self.simulation_tab_widget.setTabText(self.simulation_tab_widget.indexOf(self.simulation_time_domain_tab), QCoreApplication.translate("PyQtVisualFlight", u"Tab 1", None))
        self.simulation_tab_widget.setTabText(self.simulation_tab_widget.indexOf(self.simulation_frequency_domain_tab), QCoreApplication.translate("PyQtVisualFlight", u"Tab 2", None))
        self.menu.setTitle(QCoreApplication.translate("PyQtVisualFlight", u"File", None))
        self.menuConnect_To_Observer.setTitle(QCoreApplication.translate("PyQtVisualFlight", u"Connect To Observer", None))
        self.menuOption.setTitle(QCoreApplication.translate("PyQtVisualFlight", u"Option", None))
        self.menuMagnification.setTitle(QCoreApplication.translate("PyQtVisualFlight", u"Magnification", None))
    # retranslateUi

