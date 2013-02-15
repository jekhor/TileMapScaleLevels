# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TileMapScaleLevels
                                 A QGIS plugin
 Set the scale to the next matching Tile Map Scale. Works best with Google Mercator Projection.
                              -------------------
        begin                : 2013-01-23
        copyright            : (C) 2013 by Matthias Ludwig - Datalyze Solutions
        email                : development@datalyze-solutions.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic
from qgis.core import *
import os
import math

# Initialize Qt resources from file resources.py
import resources_rc

class TileMapScaleLevelPlugin:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        
        # initialize plugin directory
        self.plugin_dir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/tilemapscalelevels"
        # initialize locale
        localePath = ""
        locale = QSettings().value("locale/userLocale").toString()[0:2]

        if QFileInfo(self.plugin_dir).exists():
            localePath = self.plugin_dir + "/i18n/tilemapscalelevels_" + locale + ".qm"

        if QFileInfo(localePath).exists():
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/icons/icon.png"),
            u"Tile Map Scale Plugin", self.iface.mainWindow())

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Tile Map Scale Plugin", self.action)
        #QObject.connect(self.action, SIGNAL("triggered()"), self.showDock)
        self.action.triggered.connect(self.showDock)
        
        
	self.workingDir = os.path.dirname(os.path.abspath(__file__))
	self.dock = uic.loadUi(os.path.join(self.workingDir, "ui_tilemapscalelevels.ui"))
	self.iface.addDockWidget(Qt.LeftDockWidgetArea, self.dock)	
               
	self.readStatus()
        QObject.connect(self.canvas, SIGNAL("scaleChanged(double)"), self.scaleChanged)
        #self.canvas.scaleChanged.connect(self.scaleChanged)
	#QObject.connect(self.dock.sliderZoomlevels, SIGNAL("sliderReleased()"), self.sliderReleased)
	self.dock.sliderZoomlevels.sliderReleased.connect(self.sliderReleased)
        #QObject.connect(self.dock.spinBoxZoomlevels, SIGNAL("editingFinished()"), self.editingFinished)
        self.dock.spinBoxZoomlevels.editingFinished.connect(self.editingFinished)
        #QObject.connect(self.dock.checkBoxIsActive, SIGNAL("stateChanged(int)"), self.activationStateChanged)
        self.dock.checkBoxIsActive.stateChanged.connect(self.activationStateChanged)
        #QObject.connect(self.dock.buttonLoadOSM, SIGNAL("clicked()"), self.loadOSM)
        self.dock.buttonLoadOSM.clicked.connect(self.loadOSM)
        
	self.scaleCalculator = TileMapScaleLevels()
	
    def showDock(self):
	if self.dock.isVisible():
	  self.dock.hide()
	else:
	  self.dock.show()
    
    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Tile Map Scale Plugin", self.action)
        self.iface.removeToolBarIcon(self.action)

    def sliderReleased(self):
	zoomlevel = self.dock.sliderZoomlevels.value()
	scale = self.scaleCalculator.getScale(zoomlevel)
	self.scaleChanged(scale)

    def editingFinished(self):
	zoomlevel = self.dock.spinBoxZoomlevels.value()
	scale = self.scaleCalculator.getScale(zoomlevel)
	self.scaleChanged(scale)
	
    def setScaleWithSlider(self):
	pass
      
    def setScaleWithSpinBox(self):
	pass
      
    def loadOSM(self):
	self.iface.addRasterLayer(os.path.join(self.workingDir, "osm_mapnik.xml"), "raster")

    def scaleChanged(self, scale):
	if self.dock.checkBoxIsActive.isChecked():
	    # Disconnect to prevent infinite scaling loop
	    QObject.disconnect(self.canvas, SIGNAL("scaleChanged(double)"), self.scaleChanged)
	    #self.canvas.scaleChanged.disconnect(self.scaleChanged)
	    
	    zoomlevel = self.scaleCalculator.getZoomlevel(scale)
	    if zoomlevel <> None:
		newScale = self.scaleCalculator.getScale(zoomlevel)
		self.canvas.zoomScale(newScale)
		self.dock.labelCurrentZoomlevel.setText(str(zoomlevel))
		self.dock.sliderZoomlevels.setValue(zoomlevel)
	    QObject.connect(self.canvas, SIGNAL("scaleChanged(double)"), self.scaleChanged)
	    #self.canvas.scaleChanged.connect(self.scaleChanged)

    def activationStateChanged(self):
      if self.dock.checkBoxIsActive.isChecked():
	  self.dock.groupBox.show()
      else:
	  self.dock.groupBox.hide()
      self.storeStatus()
      
    def storeStatus(self):
      s = QSettings()
      s.setValue("tilemapscalelevels/active", self.dock.checkBoxIsActive.isChecked() )

    def readStatus(self):
      s = QSettings()
      isActive = s.value("tilemapscalelevels/active", True).toBool()
      self.dock.checkBoxIsActive.setChecked(isActive)
	    

class TileMapScaleLevels:
    import math
    def __init__(self, dpi = 96):
	self.dpi = dpi
	self.inchesPerMeter = 39.37
	self.maxScalePerPixel = 156543.04

    def getScale(self, zoomlevel):
	if zoomlevel < 0:
	    return (self.dpi * self.inchesPerMeter * self.maxScalePerPixel) / (math.pow(2, 0))
	else:
	    zoomlevel = int(zoomlevel)
	    return (self.dpi * self.inchesPerMeter * self.maxScalePerPixel) / (math.pow(2, zoomlevel))
	    
    def getZoomlevel(self, scale):
	if scale <> 0:
	    return int(round(math.log( ((self.dpi * self.inchesPerMeter * self.maxScalePerPixel) / scale), 2 ), 0))