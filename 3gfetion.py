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
            
        self.iconComboBox = QComboBox()
        self.iconComboBox.addItem(QIcon('fetion.ico'), 'Fetion')
        
        #设置菜单及行为
        self.restoreAction = QAction(u'显示窗口', self,triggered=self.showNormal)
        self.quitAction = QAction(u'退出', self,triggered=qApp.quit)
        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(self.restoreAction)
        self.trayIconMenu.addAction(self.quitAction)
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)

        #设置通知区域的ICON
        self.iconComboBox.currentIndexChanged.connect(self.setIcon)
        #通知区域icon显示
        self.iconComboBox.setCurrentIndex(1)
        self.trayIcon.activated.connect(self.iconActivated)
        
    def iconActivated(self, reason):
        if reason in (QSystemTrayIcon.Trigger,QSystemTrayIcon.DoubleClick):
            self.showNormal()
 
    def setIcon(self, index):
        icon = self.iconComboBox.itemIcon(0)
        self.trayIcon.setIcon(icon)
        self.setWindowIcon(icon)
        self.trayIcon.setToolTip(self.iconComboBox.itemText(index))
        
    def closeEvent(self,event):
        # 判断是否为最小化事件
        self.hide()
        self.trayIcon.show()
        event.ignore()
        
    def showNormal(self):
        QWidget.showNormal(self)
        self.trayIcon.hide()
        
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

if __name__ == '__main__':
    app = QApplication([])
    ui = Browser()
    app.exec_()
