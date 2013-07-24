# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_tilemapscalelevels.ui'
#
# Created: Wed Jul 24 09:51:11 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DockWidgetTileMapScaleLevels(object):
    def setupUi(self, DockWidgetTileMapScaleLevels):
        DockWidgetTileMapScaleLevels.setObjectName(_fromUtf8("DockWidgetTileMapScaleLevels"))
        DockWidgetTileMapScaleLevels.resize(261, 309)
        DockWidgetTileMapScaleLevels.setMinimumSize(QtCore.QSize(255, 291))
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
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBoxDatasets)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.buttonLoadOSM = QtGui.QToolButton(self.groupBoxDatasets)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/osm.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonLoadOSM.setIcon(icon)
        self.buttonLoadOSM.setIconSize(QtCore.QSize(32, 32))
        self.buttonLoadOSM.setObjectName(_fromUtf8("buttonLoadOSM"))
        self.horizontalLayout_2.addWidget(self.buttonLoadOSM)
        self.buttonLoadMapQuest = QtGui.QToolButton(self.groupBoxDatasets)
        self.buttonLoadMapQuest.setIcon(icon)
        self.buttonLoadMapQuest.setIconSize(QtCore.QSize(32, 32))
        self.buttonLoadMapQuest.setObjectName(_fromUtf8("buttonLoadMapQuest"))
        self.horizontalLayout_2.addWidget(self.buttonLoadMapQuest)
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
        spacerItem2 = QtGui.QSpacerItem(54, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.groupBoxDatasets)
        DockWidgetTileMapScaleLevels.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidgetTileMapScaleLevels)
        QtCore.QObject.connect(self.sliderZoomlevels, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxZoomlevels.setValue)
        QtCore.QObject.connect(self.spinBoxZoomlevels, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.sliderZoomlevels.setValue)
        QtCore.QMetaObject.connectSlotsByName(DockWidgetTileMapScaleLevels)

    def retranslateUi(self, DockWidgetTileMapScaleLevels):
        DockWidgetTileMapScaleLevels.setWindowTitle(_translate("DockWidgetTileMapScaleLevels", "Tile Map Scale Levels", None))
        self.checkBoxIsActive.setText(_translate("DockWidgetTileMapScaleLevels", "Active", None))
        self.label.setText(_translate("DockWidgetTileMapScaleLevels", "Current Zoomlevel:", None))
        self.labelCurrentZoomlevel.setText(_translate("DockWidgetTileMapScaleLevels", "0", None))
        self.checkBoxUseMercator.setText(_translate("DockWidgetTileMapScaleLevels", "Use World Mercator System", None))
        self.checkBoxUseOnTheFlyTransformation.setText(_translate("DockWidgetTileMapScaleLevels", "Use \'On-The-Fly\' Transformation", None))
        self.groupBox.setTitle(_translate("DockWidgetTileMapScaleLevels", "Zoomlevel", None))
        self.groupBoxDatasets.setTitle(_translate("DockWidgetTileMapScaleLevels", "Datasets", None))
        self.buttonLoadOSM.setToolTip(_translate("DockWidgetTileMapScaleLevels", "Load OSM Layer", None))
        self.buttonLoadOSM.setStatusTip(_translate("DockWidgetTileMapScaleLevels", "Load OSM Layer", None))
        self.buttonLoadOSM.setText(_translate("DockWidgetTileMapScaleLevels", "OSM", None))
        self.buttonLoadMapQuest.setToolTip(_translate("DockWidgetTileMapScaleLevels", "Load MapQuest Layer", None))
        self.buttonLoadMapQuest.setStatusTip(_translate("DockWidgetTileMapScaleLevels", "Load MapQuest Layer", None))
        self.buttonLoadMapQuest.setText(_translate("DockWidgetTileMapScaleLevels", "OSM", None))
        self.buttonLoadGoogleMaps.setToolTip(_translate("DockWidgetTileMapScaleLevels", "Load Google Maps Layer", None))
        self.buttonLoadGoogleMaps.setStatusTip(_translate("DockWidgetTileMapScaleLevels", "Load Google Maps Layer", None))
        self.buttonLoadGoogleMaps.setText(_translate("DockWidgetTileMapScaleLevels", "OSM", None))
        self.buttonLoadGoogleSatellite.setToolTip(_translate("DockWidgetTileMapScaleLevels", "Load Google Satellite Layer", None))
        self.buttonLoadGoogleSatellite.setStatusTip(_translate("DockWidgetTileMapScaleLevels", "Load Google Satellite Layer", None))
        self.buttonLoadGoogleSatellite.setText(_translate("DockWidgetTileMapScaleLevels", "OSM", None))

import resources_rc
