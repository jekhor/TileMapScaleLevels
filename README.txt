Description:
------------
If using TMS (TileMapSpecification) datasets like OpenStreetMap, Google Maps or 
Bing Maps you have to set the correct scale to get a sharply picture. Using 
other scales results in an fuzzy picture. This plugin sets the scale to match 
the next TMS scale.

Bugs:
-----
On some operating systems you get a fuzzy picture even if you use the plugin.
I tested this on the same Ubuntu 12.04 OS. Using proprietary gpu drivers I got
a fuzzy image using kde. While using the open source driver there where no
problems. On Mac OSX "Lion" I couldn't get it to work properly.

Installation:
-------------
- use the Python Plugin Downloader inside QGIS
  (Plugins > Fetch Python Plugins...)


manually:
- locate the .qgis folder (hidden folder)
  - Linux: ~/home/.qgis
  - MacOS: in the user folder
  - Windows: Documents and Settings/username/.qgis
- if not still existing, create a "python" folder inside .qgis (without "")
- if not still existing, create a "plugins" folder inside .qgis/python (without "")
- move to TileMapScaleLevels folder into .qgis/python/plugins
- start (or restart) QGIS and activate "Tile Map Scale Plugin" using the QGIS-Pluginmanager
  (Plugins > Manage Plugins)

Contact:
--------
If you have questions, feel free to write a mail: development@datalyze-solutions.com