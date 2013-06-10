from ui_tilemapscalelevels import Ui_DockWidgetTileMapScaleLevels

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class TileMapScalePluginDock(QWidget, Ui_DockWidgetTileMapScaleLevels):

    def __init__(self):
        self.setupUi(self)
        self.show()