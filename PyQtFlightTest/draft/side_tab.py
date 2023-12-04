#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: jyroy
import sys

# ref: 
# - https://www.cnblogs.com/jyroy/p/9457882.html

from PySide2.QtCore import QUrl
# from PySide2.QtWebKitWidgets import QWebView
# import QWebView from PySide2
from PySide2.QtWebEngineWidgets import QWebEngineView as QWebView
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QListWidget,QStackedWidget
from PySide2.QtWidgets import QListWidgetItem
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QHBoxLayout

from PySide2.QtCore import QSize, Qt



class LeftTabWidget(QWidget):
    '''左侧选项栏'''
    def __init__(self):
        super(LeftTabWidget, self).__init__()
        self.setObjectName('LeftTabWidget')

        self.setWindowTitle('LeftTabWidget')
        with open('side_tab.qss', 'r') as f:   #导入QListWidget的qss样式
            self.list_style = f.read()

        self.main_layout = QHBoxLayout(self, spacing=0)     #窗口的整体布局
        self.main_layout.setContentsMargins(0,0,0,0)

        self.left_widget = QListWidget()     #左侧选项列表
        self.left_widget.setStyleSheet(self.list_style)
        self.main_layout.addWidget(self.left_widget)

        self.right_widget = QStackedWidget()
        self.main_layout.addWidget(self.right_widget)

        self._setup_ui()

    def _setup_ui(self):
        '''加载界面ui'''

        self.left_widget.currentRowChanged.connect(self.right_widget.setCurrentIndex)   #list和右侧窗口的index对应绑定

        self.left_widget.setFrameShape(QListWidget.NoFrame)    #去掉边框

        self.left_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  #隐藏滚动条
        self.left_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        list_str = ['岗位需求','专业要求','薪水分布','城市分布']
        url_list = ['job_num_wordcloud.html', 'edu_need.html', 'salary_bar.html', 'edu_salary_bar.html']

        for i in range(4):
            self.item = QListWidgetItem(list_str[i],self.left_widget)   #左侧选项的添加
            self.item.setSizeHint(QSize(30,60))
            self.item.setTextAlignment(Qt.AlignCenter)                  #居中显示

            self.browser = QWebView()                                   #右侧用QWebView来显示html网页
            self.browser.setUrl(QUrl.fromLocalFile('%s' % url_list[i]))
            self.right_widget.addWidget(self.browser)



def main():
    ''' '''
    app = QApplication(sys.argv)

    main_wnd = LeftTabWidget()
    main_wnd.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()