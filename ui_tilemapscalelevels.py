# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_tilemapscalelevels.ui'
#
# Created: Mon Jun 10 17:52:01 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DockWidgetTileMapScaleLevels(object):
    def setupUi(self, DockWidgetTileMapScaleLevels):
        DockWidgetTileMapScaleLevels.setObjectName(_fromUtf8("DockWidgetTileMapScaleLevels"))
        DockWidgetTileMapScaleLevels.resize(261, 309)
        DockWidgetTileMapScaleLevels.setMinimumSize(QtCore.QSize(0, 0))
        DockWidgetTileMapScaleLevels.setMaximumSize(QtCore.QSize(524287, 309))
        DockWidgetTileMapScaleLevels.setFloating(False)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkBoxIsActive = QtGui.QCheckBox(self.dockWidgetContents)
        self.checkBoxIsActive.setChecked(True)
        self.checkBoxIsActive.setTristate(False)
        self.checkBoxIsActive.setObjectName(_fromUtf8("checkBoxIsActive"))
        self.horizontalLayout.addWidget(self.checkBoxIsActive)
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.labelCurrentZoomlevel = QtGui.QLabel(self.dockWidgetContents)
        self.labelCurrentZoomlevel.setMinimumSize(QtCore.QSize(16, 0))
        self.labelCurrentZoomlevel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelCurrentZoomlevel.setObjectName(_fromUtf8("labelCurrentZoomlevel"))
        self.horizontalLayout.addWidget(self.labelCurrentZoomlevel)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.checkBoxUseMercator = QtGui.QCheckBox(self.dockWidgetContents)
        self.checkBoxUseMercator.setChecked(False)
        self.checkBoxUseMercator.setTristate(False)
        self.checkBoxUseMercator.setObjectName(_fromUtf8("checkBoxUseMercator"))
        self.verticalLayout_2.addWidget(self.checkBoxUseMercator)
        self.checkBoxUseOnTheFlyTransformation = QtGui.QCheckBox(self.dockWidgetContents)
        self.checkBoxUseOnTheFlyTransformation.setChecked(False)
        self.checkBoxUseOnTheFlyTransformation.setTristate(False)
        self.checkBoxUseOnTheFlyTransformation.setObjectName(_fromUtf8("checkBoxUseOnTheFlyTransformation"))
        self.verticalLayout_2.addWidget(self.checkBoxUseOnTheFlyTransformation)
        self.groupBox = QtGui.QGroupBox(self.dockWidgetContents)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.sliderZoomlevels = QtGui.QSlider(self.groupBox)
        self.sliderZoomlevels.setMaximum(25)
        self.sliderZoomlevels.setOrientation(QtCore.Qt.Horizontal)
        self.sliderZoomlevels.setObjectName(_fromUtf8("sliderZoomlevels"))
        self.verticalLayout.addWidget(self.sliderZoomlevels)
        self.spinBoxZoomlevels = QtGui.QSpinBox(self.groupBox)
        self.spinBoxZoomlevels.setMaximum(25)
        self.spinBoxZoomlevels.setObjectName(_fromUtf8("spinBoxZoomlevels"))
        self.verticalLayout.addWidget(self.spinBoxZoomlevels)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBoxDatasets = QtGui.QGroupBox(self.dockWidgetContents)
        self.groupBoxDatasets.setObjectName(_fromUtf8("groupBoxDatasets"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBoxDatasets)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.buttonLoadOSM = QtGui.QToolButton(self.groupBoxDatasets)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/osm.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonLoadOSM.setIcon(icon)
        self.buttonLoadOSM.setIconSize(QtCore.QSize(32, 32))
        self.buttonLoadOSM.setObjectName(_fromUtf8("buttonLoadOSM"))
        self.horizontalLayout_2.addWidget(self.buttonLoadOSM)
        self.buttonLoadGoogleMaps = QtGui.QToolButton(self.groupBoxDatasets)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/googlemaps.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonLoadGoogleMaps.setIcon(icon1)
        self.buttonLoadGoogleMaps.setIconSize(QtCore.QSize(32, 32))
        self.buttonLoadGoogleMaps.setObjectName(_fromUtf8("buttonLoadGoogleMaps"))
        self.horizontalLayout_2.addWidget(self.buttonLoadGoogleMaps)
        self.buttonLoadGoogleSatellite = QtGui.QToolButton(self.groupBoxDatasets)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/google_earth.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonLoadGoogleSatellite.setIcon(icon2)
        self.buttonLoadGoogleSatellite.setIconSize(QtCore.QSize(32, 32))
        self.buttonLoadGoogleSatellite.setObjectName(_fromUtf8("buttonLoadGoogleSatellite"))
        self.horizontalLayout_2.addWidget(self.buttonLoadGoogleSatellite)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.groupBoxDatasets)
        DockWidgetTileMapScaleLevels.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidgetTileMapScaleLevels)
        QtCore.QObject.connect(self.sliderZoomlevels, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxZoomlevels.setValue)
        QtCore.QObject.connect(self.spinBoxZoomlevels, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.sliderZoomlevels.setValue)
        QtCore.QMetaObject.connectSlotsByName(DockWidgetTileMapScaleLevels)

    def retranslateUi(self, DockWidgetTileMapScaleLevels):
        DockWidgetTileMapScaleLevels.setWindowTitle(QtGui.QApplication.translate("DockWidgetTileMapScaleLevels", "Tile Map Scale Levels", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxIsActive.setText(QtGui.QApplication.translate("DockWidgetTileMapScaleLevels", "Active", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DockWidgetTileMapScaleLevels", "Current Zoomlevel:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCurrentZoomlevel.setText(QtGui.QApplication.translate("DockWidgetTileMapScaleLevels", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxUseMercator.setText(QtGui.QApplication.translate("DockWidgetTileMapScaleLevels", "Use World Mercator System", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxUseOnTheFlyTransformation.setText(QtGui.QApplication.translate("DockWidgetTileMapScaleLevels", "Use \'On-The-Fly\' Transformation", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DockWidgetTileMapScaleLevels", "Zoomlevel", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxDatasets.setTitle(QtGui.QApplication.translate("DockWidgetTileMapScaleLevels", "Datasets", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonLoadOSM.setToolTip(QtGui.QApplication.translate("DockWidgetTileMapScaleLevels", "Load OSM Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonLoadOSM.setStatusTip(QtGui.QApplication.translate("DockWidgetTileMapScaleLevels", "Load OSM Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonLoadOSM.setText(QtGui.QApplication.translate("DockWidgetTileMapScaleLevels", "OSM", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonLoadGoogleMaps.setToolTip(QtGui.QApplication.translate("DockWidgetTileMapScaleLevels", "Load OSM Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonLoadGoogleMaps.setStatusTip(QtGui.QApplication.translate("DockWidgetTileMapScaleLevels", "Load OSM Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonLoadGoogleMaps.setText(QtGui.QApplication.translate("DockWidgetTileMapScaleLevels", "OSM", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonLoadGoogleSatellite.setToolTip(QtGui.QApplication.translate("DockWidgetTileMapScaleLevels", "Load OSM Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonLoadGoogleSatellite.setStatusTip(QtGui.QApplication.translate("DockWidgetTileMapScaleLevels", "Load OSM Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonLoadGoogleSatellite.setText(QtGui.QApplication.translate("DockWidgetTileMapScaleLevels", "OSM", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc