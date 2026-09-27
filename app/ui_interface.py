# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDockWidget, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QScrollArea, QSizePolicy, QSpinBox, QSplitter,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1243, 798)
        MainWindow.setMinimumSize(QSize(1100, 700))
        MainWindow.setStyleSheet(u"/* Color base general para la ventana principal */\n"
"QMainWindow {\n"
"    background-color: #1b1b27;\n"
"}\n"
"\n"
"/* Contenedor central */\n"
"QWidget#centralwidget {\n"
"    background-color: #1b1b27;\n"
"}\n"
"\n"
"/* Panel lateral de controles (DockWidget) */\n"
"QDockWidget {\n"
"    background-color: #212130;\n"
"    color: #ffffff;\n"
"    border: 1px solid #2a2a3c;\n"
"}\n"
"\n"
"QDockWidget::title {\n"
"    background: #2a2a3c;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"/* Pesta\u00f1as y \u00e1reas de trazado */\n"
"QTabWidget::pane {\n"
"    border: 1px solid #2a2a3c;\n"
"    background-color: #1b1b27;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: #232334;\n"
"    color: #a0a0b0;\n"
"    padding: 8px 16px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #1b1b27;\n"
"    color: #ffffff;\n"
"}")
        self.actionSave_Annotations = QAction(MainWindow)
        self.actionSave_Annotations.setObjectName(u"actionSave_Annotations")
        self.actionLoad_EDF_File = QAction(MainWindow)
        self.actionLoad_EDF_File.setObjectName(u"actionLoad_EDF_File")
        self.actiona = QAction(MainWindow)
        self.actiona.setObjectName(u"actiona")
        self.actionLoad_EDF_File_2 = QAction(MainWindow)
        self.actionLoad_EDF_File_2.setObjectName(u"actionLoad_EDF_File_2")
        self.actionLoad_EDF_File_3 = QAction(MainWindow)
        self.actionLoad_EDF_File_3.setObjectName(u"actionLoad_EDF_File_3")
        self.actionLoad_EDF_File_3.setCheckable(False)
        self.actionSave_Annotations_2 = QAction(MainWindow)
        self.actionSave_Annotations_2.setObjectName(u"actionSave_Annotations_2")
        self.actionExport_Annotations_to_CSV = QAction(MainWindow)
        self.actionExport_Annotations_to_CSV.setObjectName(u"actionExport_Annotations_to_CSV")
        self.actionExport_Clinical_Report = QAction(MainWindow)
        self.actionExport_Clinical_Report.setObjectName(u"actionExport_Clinical_Report")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionMonopolar_Standard_Reference = QAction(MainWindow)
        self.actionMonopolar_Standard_Reference.setObjectName(u"actionMonopolar_Standard_Reference")
        self.actionBipolar_Double_Banana = QAction(MainWindow)
        self.actionBipolar_Double_Banana.setObjectName(u"actionBipolar_Double_Banana")
        self.actionEar_Average_or_Common_Reference = QAction(MainWindow)
        self.actionEar_Average_or_Common_Reference.setObjectName(u"actionEar_Average_or_Common_Reference")
        self.actionRun_Model_Inference = QAction(MainWindow)
        self.actionRun_Model_Inference.setObjectName(u"actionRun_Model_Inference")
        self.actionAdjust_Confidence_Threshold = QAction(MainWindow)
        self.actionAdjust_Confidence_Threshold.setObjectName(u"actionAdjust_Confidence_Threshold")
        self.actionSave_updated_labels = QAction(MainWindow)
        self.actionSave_updated_labels.setObjectName(u"actionSave_updated_labels")
        self.actionReadjust_model = QAction(MainWindow)
        self.actionReadjust_model.setObjectName(u"actionReadjust_model")
        self.actionShow_Manual_Markers = QAction(MainWindow)
        self.actionShow_Manual_Markers.setObjectName(u"actionShow_Manual_Markers")
        self.actionShow_All = QAction(MainWindow)
        self.actionShow_All.setObjectName(u"actionShow_All")
        self.actionShow_All.setCheckable(True)
        self.actionShow_Artifact_Zones = QAction(MainWindow)
        self.actionShow_Artifact_Zones.setObjectName(u"actionShow_Artifact_Zones")
        self.actionShow_Artifact_Zones.setCheckable(True)
        self.actionShow_Seizure_Zones = QAction(MainWindow)
        self.actionShow_Seizure_Zones.setObjectName(u"actionShow_Seizure_Zones")
        self.actionShow_Seizure_Zones.setCheckable(True)
        self.actionShow_Events_Zones = QAction(MainWindow)
        self.actionShow_Events_Zones.setObjectName(u"actionShow_Events_Zones")
        self.actionShow_Events_Zones.setCheckable(True)
        self.actionConfigure_Digital_Filters = QAction(MainWindow)
        self.actionConfigure_Digital_Filters.setObjectName(u"actionConfigure_Digital_Filters")
        self.actionEspa_ol = QAction(MainWindow)
        self.actionEspa_ol.setObjectName(u"actionEspa_ol")
        self.actionEnglish = QAction(MainWindow)
        self.actionEnglish.setObjectName(u"actionEnglish")
        self.actionKeyboard_Shortcuts_Guide = QAction(MainWindow)
        self.actionKeyboard_Shortcuts_Guide.setObjectName(u"actionKeyboard_Shortcuts_Guide")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionOpen_General_Controls = QAction(MainWindow)
        self.actionOpen_General_Controls.setObjectName(u"actionOpen_General_Controls")
        self.actionOpen_Controls = QAction(MainWindow)
        self.actionOpen_Controls.setObjectName(u"actionOpen_Controls")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.eeg_graphicsView = PlotWidget(self.splitter)
        self.eeg_graphicsView.setObjectName(u"eeg_graphicsView")
        self.splitter.addWidget(self.eeg_graphicsView)
        self.assistant_eeg_view = QTabWidget(self.splitter)
        self.assistant_eeg_view.setObjectName(u"assistant_eeg_view")
        self.artifact_module = QWidget()
        self.artifact_module.setObjectName(u"artifact_module")
        self.assistant_eeg_view.addTab(self.artifact_module, "")
        self.seizure_module = QWidget()
        self.seizure_module.setObjectName(u"seizure_module")
        self.assistant_eeg_view.addTab(self.seizure_module, "")
        self.events_module = QWidget()
        self.events_module.setObjectName(u"events_module")
        self.assistant_eeg_view.addTab(self.events_module, "")
        self.epilepsy_module = QWidget()
        self.epilepsy_module.setObjectName(u"epilepsy_module")
        self.assistant_eeg_view.addTab(self.epilepsy_module, "")
        self.splitter.addWidget(self.assistant_eeg_view)

        self.verticalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1243, 19))
        self.menu_Montages = QMenu(self.menuBar)
        self.menu_Montages.setObjectName(u"menu_Montages")
        self.menu_Files = QMenu(self.menuBar)
        self.menu_Files.setObjectName(u"menu_Files")
        self.menu_Assistance = QMenu(self.menuBar)
        self.menu_Assistance.setObjectName(u"menu_Assistance")
        self.menu_View = QMenu(self.menuBar)
        self.menu_View.setObjectName(u"menu_View")
        self.menuShow_AI_Overlays = QMenu(self.menu_View)
        self.menuShow_AI_Overlays.setObjectName(u"menuShow_AI_Overlays")
        self.menu_Tools = QMenu(self.menuBar)
        self.menu_Tools.setObjectName(u"menu_Tools")
        self.menuLanguages = QMenu(self.menu_Tools)
        self.menuLanguages.setObjectName(u"menuLanguages")
        self.menu_Help = QMenu(self.menuBar)
        self.menu_Help.setObjectName(u"menu_Help")
        MainWindow.setMenuBar(self.menuBar)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_3 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.dockWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cmb_gain = QComboBox(self.dockWidgetContents)
        self.cmb_gain.setObjectName(u"cmb_gain")

        self.horizontalLayout.addWidget(self.cmb_gain)

        self.label = QLabel(self.dockWidgetContents)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.spn_time_window = QSpinBox(self.dockWidgetContents)
        self.spn_time_window.setObjectName(u"spn_time_window")

        self.horizontalLayout_2.addWidget(self.spn_time_window)

        self.label_2 = QLabel(self.dockWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.scroll_channels = QScrollArea(self.dockWidgetContents)
        self.scroll_channels.setObjectName(u"scroll_channels")
        self.scroll_channels.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 150, 632))
        self.scroll_channels.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scroll_channels)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dockWidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menu_Files.menuAction())
        self.menuBar.addAction(self.menu_Montages.menuAction())
        self.menuBar.addAction(self.menu_Assistance.menuAction())
        self.menuBar.addAction(self.menu_View.menuAction())
        self.menuBar.addAction(self.menu_Tools.menuAction())
        self.menuBar.addAction(self.menu_Help.menuAction())
        self.menu_Montages.addAction(self.actionMonopolar_Standard_Reference)
        self.menu_Montages.addAction(self.actionBipolar_Double_Banana)
        self.menu_Montages.addAction(self.actionEar_Average_or_Common_Reference)
        self.menu_Files.addAction(self.actionLoad_EDF_File_3)
        self.menu_Files.addAction(self.actionSave_Annotations_2)
        self.menu_Files.addAction(self.actionExport_Annotations_to_CSV)
        self.menu_Files.addAction(self.actionExport_Clinical_Report)
        self.menu_Files.addSeparator()
        self.menu_Files.addAction(self.actionExit)
        self.menu_Assistance.addAction(self.actionRun_Model_Inference)
        self.menu_Assistance.addAction(self.actionAdjust_Confidence_Threshold)
        self.menu_Assistance.addSeparator()
        self.menu_Assistance.addAction(self.actionSave_updated_labels)
        self.menu_Assistance.addAction(self.actionReadjust_model)
        self.menu_View.addAction(self.actionShow_Manual_Markers)
        self.menu_View.addAction(self.menuShow_AI_Overlays.menuAction())
        self.menu_View.addSeparator()
        self.menu_View.addSeparator()
        self.menu_View.addAction(self.actionOpen_Controls)
        self.menuShow_AI_Overlays.addAction(self.actionShow_All)
        self.menuShow_AI_Overlays.addAction(self.actionShow_Artifact_Zones)
        self.menuShow_AI_Overlays.addAction(self.actionShow_Seizure_Zones)
        self.menuShow_AI_Overlays.addAction(self.actionShow_Events_Zones)
        self.menu_Tools.addAction(self.actionConfigure_Digital_Filters)
        self.menu_Tools.addAction(self.menuLanguages.menuAction())
        self.menuLanguages.addAction(self.actionEspa_ol)
        self.menuLanguages.addAction(self.actionEnglish)
        self.menu_Help.addAction(self.actionKeyboard_Shortcuts_Guide)
        self.menu_Help.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.assistant_eeg_view.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSave_Annotations.setText(QCoreApplication.translate("MainWindow", u"Save Annotations", None))
        self.actionLoad_EDF_File.setText(QCoreApplication.translate("MainWindow", u"Save Annotations File", None))
        self.actiona.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.actionLoad_EDF_File_2.setText(QCoreApplication.translate("MainWindow", u"Save Annotations", None))
        self.actionLoad_EDF_File_3.setText(QCoreApplication.translate("MainWindow", u"Load EDF File", None))
        self.actionSave_Annotations_2.setText(QCoreApplication.translate("MainWindow", u"Save Annotations", None))
        self.actionExport_Annotations_to_CSV.setText(QCoreApplication.translate("MainWindow", u"Export Annotations to CSV", None))
        self.actionExport_Clinical_Report.setText(QCoreApplication.translate("MainWindow", u"Export Clinical Report (PDF)", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionMonopolar_Standard_Reference.setText(QCoreApplication.translate("MainWindow", u"Monopolar (Standard Reference)", None))
        self.actionBipolar_Double_Banana.setText(QCoreApplication.translate("MainWindow", u"Bipolar (Double Banana)", None))
        self.actionEar_Average_or_Common_Reference.setText(QCoreApplication.translate("MainWindow", u"Ear Average or Common Reference", None))
        self.actionRun_Model_Inference.setText(QCoreApplication.translate("MainWindow", u"Run Model Inference", None))
        self.actionAdjust_Confidence_Threshold.setText(QCoreApplication.translate("MainWindow", u"Adjust Confidence Threshold", None))
        self.actionSave_updated_labels.setText(QCoreApplication.translate("MainWindow", u"Save updated labels", None))
        self.actionReadjust_model.setText(QCoreApplication.translate("MainWindow", u"Readjust model", None))
        self.actionShow_Manual_Markers.setText(QCoreApplication.translate("MainWindow", u"Show Manual Markers", None))
        self.actionShow_All.setText(QCoreApplication.translate("MainWindow", u"Show All", None))
        self.actionShow_Artifact_Zones.setText(QCoreApplication.translate("MainWindow", u"Show Artifact Zones", None))
        self.actionShow_Seizure_Zones.setText(QCoreApplication.translate("MainWindow", u"Show Seizure Zones", None))
        self.actionShow_Events_Zones.setText(QCoreApplication.translate("MainWindow", u"Show Events Zones", None))
        self.actionConfigure_Digital_Filters.setText(QCoreApplication.translate("MainWindow", u"Configure Digital Filters", None))
        self.actionEspa_ol.setText(QCoreApplication.translate("MainWindow", u"Espa\u00f1ol", None))
        self.actionEnglish.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.actionKeyboard_Shortcuts_Guide.setText(QCoreApplication.translate("MainWindow", u"Keyboard Shortcuts Guide", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionOpen_General_Controls.setText(QCoreApplication.translate("MainWindow", u"Open General Controls", None))
        self.actionOpen_Controls.setText(QCoreApplication.translate("MainWindow", u"Open Controls ", None))
        self.assistant_eeg_view.setTabText(self.assistant_eeg_view.indexOf(self.artifact_module), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.assistant_eeg_view.setTabText(self.assistant_eeg_view.indexOf(self.seizure_module), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.assistant_eeg_view.setTabText(self.assistant_eeg_view.indexOf(self.events_module), QCoreApplication.translate("MainWindow", u"Page", None))
        self.assistant_eeg_view.setTabText(self.assistant_eeg_view.indexOf(self.epilepsy_module), QCoreApplication.translate("MainWindow", u"Page", None))
        self.menu_Montages.setTitle(QCoreApplication.translate("MainWindow", u"&Montages", None))
        self.menu_Files.setTitle(QCoreApplication.translate("MainWindow", u"&Files", None))
        self.menu_Assistance.setTitle(QCoreApplication.translate("MainWindow", u"&Assistance", None))
        self.menu_View.setTitle(QCoreApplication.translate("MainWindow", u"&View", None))
        self.menuShow_AI_Overlays.setTitle(QCoreApplication.translate("MainWindow", u"Show AI Overlays", None))
        self.menu_Tools.setTitle(QCoreApplication.translate("MainWindow", u"&Tools", None))
        self.menuLanguages.setTitle(QCoreApplication.translate("MainWindow", u"Languages", None))
        self.menu_Help.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Display settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sensitivity", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Time base (s)", None))
    # retranslateUi

