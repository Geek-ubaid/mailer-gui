
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtWebEngineWidgets

class Render(QtWebEngineWidgets.QWebEngineView):
    def __init__(self, html):
        self.html = None
        QtWebEngineWidgets.QWebEngineView.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.setHtml(html)
        self.show()

    def _loadFinished(self, result):
        # what's going on here? how can I get the HTML from toHtml?
        self.page().toHtml(self.callable)
        self.close()

    def callable(self, data):
        self.html = data
        
        
