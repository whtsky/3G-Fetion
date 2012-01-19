# -*- coding: utf-8 -*-

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *
from PySide.QtNetwork import *
from thread import start_new_thread
import config

bestsize = QSize(337, 623)

class Browser(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        #改标题、调整大小
        self.setWindowTitle(u'3G飞信')
        self.setMinimumSize(bestsize)
        self.setMaximumSize(bestsize)
        
        
        self.webView = QWebView(self)
        self.webView.setGeometry(QRect(0, 0, 337, 623))
        self.network_manager = QNetworkAccessManager()
        self.network_manager.setCookieJar(QNetworkCookieJar())
        self.webView.page().setNetworkAccessManager(self.network_manager)
        
        #尝试进行登录
        if config.data is not None:
            accessManager = self.webView.page().networkAccessManager()
            request = QNetworkRequest(QUrl('http://f.10086.cn/im/login/inputpasssubmit1.action'))
            self.reply = accessManager.post(request,QByteArray(config.data))
            self.reply.finished.connect(self.logindone)
        else:
            self.logindone()
        
    '''
    def checkup(self):
        accessManager = self.webView.page().networkAccessManager()
        request = QNetworkRequest(QUrl('http://f.10086.cn/im5/index/html5.action'))
        self.reply = accessManager.get(request)
        self.reply.finished.connect(self.done)
    '''

    def logindone(self):
        self.webView.load(QUrl('http://f.10086.cn/im5/index/html5.action'))
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    ui = Browser()
    app.exec_()
