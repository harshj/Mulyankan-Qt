#!/usr/lib/env python

import os , subprocess
from PyQt4 import QtCore, QtGui
import advanced_eval_options
from system import result_evaluator , centre_allocator , handle_uploads
from system.constants import NO_OF_QUES

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

class Ui_MainWindow(object):
    
    no_of_ques = NO_OF_QUES;
    ques_not_eval = '' 
    
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(360, 400)
        
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 400))
        MainWindow.setMaximumSize(QtCore.QSize(400, 400))
        
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(9, 10, 340, 330))
        
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        
        self.tabWidget.setMinimumSize(QtCore.QSize(280, 330))
        self.tabWidget.setMaximumSize(QtCore.QSize(380, 280))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        
        self.result_eval_tab = QtGui.QWidget()
        self.result_eval_tab.setObjectName(_fromUtf8("result_eval_tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.result_eval_tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        
        self.label_3 = QtGui.QLabel(self.result_eval_tab)
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Garuda"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        
        font_input = QtGui.QFont()
        font_input.setFamily(_fromUtf8("Arial"))
        font_input.setPointSize(10)        
        
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        
        self.paper_code_list = QtGui.QComboBox(self.result_eval_tab)
        
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paper_code_list.sizePolicy().hasHeightForWidth())
        
        self.paper_code_list.setSizePolicy(sizePolicy)
        self.paper_code_list.setMinimumSize(QtCore.QSize(70, 30))
        self.paper_code_list.setMaximumSize(QtCore.QSize(70, 30))
        self.paper_code_list.setEditable(False)
        self.paper_code_list.setMinimumContentsLength(1)
        self.paper_code_list.setFrame(True)
        self.paper_code_list.setObjectName(_fromUtf8("paper_code_list"))
        self.paper_code_list.addItem(_fromUtf8(""))
        self.paper_code_list.addItem(_fromUtf8(""))
        self.paper_code_list.addItem(_fromUtf8(""))
        self.paper_code_list.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.paper_code_list, 0, 3, 1, 1)
        
        # Response Select button in result_evaluator tab.
        self.response_select = QtGui.QPushButton(self.result_eval_tab)
        self.response_select.setObjectName(_fromUtf8("response_select"))
        self.response_select.clicked.connect( self.select_file )
        self.gridLayout_2.addWidget(self.response_select, 2, 0, 1, 1)
        
        # Response Path label in result_evaluator tab.
        self.response_path = QtGui.QLabel(self.result_eval_tab)
        self.response_path.setEnabled(True)
        self.response_path.setText(_fromUtf8(""))
        self.response_path.setObjectName(_fromUtf8("response_path"))
        self.gridLayout_2.addWidget(self.response_path, 2, 1, 1, 3)
        
        # Key Select button in result_evaluator tab.
        self.key_select = QtGui.QPushButton(self.result_eval_tab)
        self.key_select.setObjectName(_fromUtf8("key_select"))
        self.key_select.setEnabled(False)
        self.key_select.clicked.connect(self.select_file)
        self.gridLayout_2.addWidget(self.key_select, 4, 0, 1, 1)
        
        # Key Path label in result_evaluator tab. 
        self.key_path = QtGui.QLabel(self.result_eval_tab)
        self.key_path.setText(_fromUtf8(""))
        self.key_path.setObjectName(_fromUtf8("key_path"))
        self.gridLayout_2.addWidget(self.key_path, 4, 1, 1, 3)
        
        # Submit button in result_evaluator tab.
        self.result_eval_submit = QtGui.QPushButton(self.result_eval_tab)
        self.result_eval_submit.setMinimumSize(QtCore.QSize(100, 30))
        self.result_eval_submit.setMaximumSize(QtCore.QSize(100, 30))
        self.result_eval_submit.setObjectName(_fromUtf8("result_eval_submit"))
        self.result_eval_submit.clicked.connect( self.result_eval_submit_slot )
        self.result_eval_submit.setEnabled(False)
        self.gridLayout_2.addWidget(self.result_eval_submit, 6, 2, 1, 1)
        
        # Advanced Option button in result_evaluator tab.
        self.re_eval_submit = QtGui.QPushButton(self.result_eval_tab)
        self.re_eval_submit.setMinimumSize(QtCore.QSize(110, 30))
        self.re_eval_submit.setMaximumSize(QtCore.QSize(120, 30))
        self.re_eval_submit.setObjectName(_fromUtf8("re_eval_submit"))
        self.re_eval_submit.setText(_fromUtf8('Advanced Options'))
        self.re_eval_submit.clicked.connect( self.re_eval_submit_slot )
        self.re_eval_submit.setEnabled(False)
        self.gridLayout_2.addWidget(self.re_eval_submit, 5, 2, 1 ,1)
        
        self.label_2 = QtGui.QLabel(self.result_eval_tab)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 3)
        
        self.label = QtGui.QLabel(self.result_eval_tab)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 3)
        
        self.tabWidget.addTab(self.result_eval_tab, _fromUtf8(""))
        

        #########################################################################
        #Centre Allocator Tab.                                                  #
        #########################################################################
        self.center_alloc_tab = QtGui.QWidget()
        self.center_alloc_tab.setObjectName(_fromUtf8("center_alloc_tab"))
        
        self.gridLayout_3 = QtGui.QGridLayout(self.center_alloc_tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        
        self.student_info_select = QtGui.QPushButton(self.center_alloc_tab)
        self.student_info_select.setObjectName(_fromUtf8("student_info_select"))
        self.student_info_select.clicked.connect(self.select_file)
        self.gridLayout_3.addWidget(self.student_info_select, 4, 0, 1, 1)
        
        self.center_info_select = QtGui.QPushButton(self.center_alloc_tab)
        self.center_info_select.setObjectName(_fromUtf8("center_info_select"))
        self.center_info_select.clicked.connect(self.select_file)
        self.center_info_select.setEnabled(False)
        self.gridLayout_3.addWidget(self.center_info_select, 7, 0, 1, 1)
        
        self.center_info_path = QtGui.QLabel(self.center_alloc_tab)
        self.center_info_path.setText(_fromUtf8(""))
        self.center_info_path.setObjectName(_fromUtf8("center_info_path"))
        self.gridLayout_3.addWidget(self.center_info_path, 7, 1, 1, 2)
        
        self.label_7 = QtGui.QLabel(self.center_alloc_tab)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_3.addWidget(self.label_7, 6, 0, 1, 3)
        
        self.label_6 = QtGui.QLabel(self.center_alloc_tab)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 3)
        
        self.student_info_path = QtGui.QLabel(self.center_alloc_tab)
        self.student_info_path.setText(_fromUtf8(""))
        self.student_info_path.setObjectName(_fromUtf8("student_info_path"))
        self.gridLayout_3.addWidget(self.student_info_path, 4, 1, 1, 2)
        
        self.center_alloc_submit = QtGui.QPushButton(self.center_alloc_tab)
        self.center_alloc_submit.setObjectName(_fromUtf8("center_alloc_submit"))
        self.center_alloc_submit.clicked.connect(self.center_alloc_submit_slot)
        self.center_alloc_submit.setEnabled(False)
        self.gridLayout_3.addWidget(self.center_alloc_submit, 8, 1, 1, 1)
        
        self.label_10 = QtGui.QLabel(self.center_alloc_tab)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)
        
        self.paper_code_list_2 = QtGui.QComboBox(self.center_alloc_tab)
        self.paper_code_list_2.setObjectName(_fromUtf8("paper_code_list_2"))
        self.paper_code_list_2.addItem(_fromUtf8(""))
        self.paper_code_list_2.addItem(_fromUtf8(""))
        self.paper_code_list_2.addItem(_fromUtf8(""))
        self.paper_code_list_2.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.paper_code_list_2, 0, 2, 1, 1)
        
        self.tabWidget.addTab(self.center_alloc_tab, _fromUtf8(""))
        
        MainWindow.setCentralWidget(self.centralwidget)
                
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 318, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.showMessage('Ready')
        
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        
        self.actionManage_Paper_Codes = QtGui.QAction(MainWindow)
        self.actionManage_Paper_Codes.setObjectName(_fromUtf8("actionManage_Paper_Codes"))
        
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuEdit.addAction(self.actionManage_Paper_Codes)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        
        QtCore.QObject.connect(self.paper_code_list, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.label_3.setText)
        QtCore.QObject.connect(self.response_select, QtCore.SIGNAL(_fromUtf8("clicked()")), self.response_path.repaint)
        QtCore.QObject.connect(self.key_select, QtCore.SIGNAL(_fromUtf8("clicked()")), self.key_path.repaint)
        QtCore.QObject.connect(self.student_info_select, QtCore.SIGNAL(_fromUtf8("clicked()")), self.student_info_path.repaint)
        QtCore.QObject.connect(self.center_info_select, QtCore.SIGNAL(_fromUtf8("clicked()")), self.center_info_path.repaint)
        QtCore.QObject.connect(self.paper_code_list_2, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.label_10.setText)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MULYANKAN", None))
        
        self.label_3.setText(_translate("MainWindow", "Paper Code :", None))
        
        self.paper_code_list.setItemText(0, _translate("MainWindow", "121", None))
        self.paper_code_list.setItemText(1, _translate("MainWindow", "122", None))
        self.paper_code_list.setItemText(2, _translate("MainWindow", "123", None))
        self.paper_code_list.setItemText(3, _translate("MainWindow", "Manage", None))
        
        self.response_select.setText(_translate("MainWindow", "Select", None))
        
        self.key_select.setText(_translate("MainWindow", "Select", None))
        
        self.result_eval_submit.setText(_translate("MainWindow", "Submit", None))
        
        self.label_2.setText(_translate("MainWindow", "Insert Key File (.txt) :", None))
        
        self.label.setText(_translate("MainWindow", "Insert Response File (.txt) :", None))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.result_eval_tab), _translate("MainWindow", "Result Evaluator", None))
        
        self.student_info_select.setText(_translate("MainWindow", "Select", None))
        
        self.center_info_select.setText(_translate("MainWindow", "Select", None))
        
        self.label_7.setText(_translate("MainWindow", "Insert Center Info. File (.xls) :", None))
        
        self.label_6.setText(_translate("MainWindow", "Insert Student Info File (.xls :)", None))
        
        self.center_alloc_submit.setText(_translate("MainWindow", "Submit", None))
        
        self.label_10.setText(_translate("MainWindow", "Paper Code", None))
        
        self.paper_code_list_2.setItemText(0, _translate("MainWindow", "121", None))
        self.paper_code_list_2.setItemText(1, _translate("MainWindow", "122", None))
        self.paper_code_list_2.setItemText(2, _translate("MainWindow", "123", None))
        self.paper_code_list_2.setItemText(3, _translate("MainWindow", "Manage", None))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.center_alloc_tab), _translate("MainWindow", "Center Allocator", None))
        
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+X", None))
        
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        
        self.actionManage_Paper_Codes.setText(_translate("MainWindow", "Manage Paper Codes", None))
        
    def select_file(self):
        path = QtGui.QFileDialog.getOpenFileName(None , _fromUtf8('Select File') )
         
        button_id = self.MainWindow.sender().objectName()
        
        if(button_id == 'response_select'):
            self.response_path.setText(path)
            
            #Check Extension of file.
            path = path.split(os.sep)
            path = path[ len(path) - 1 ].split('.')
            if( path[ len(path) - 1 ] == 'txt'):
                msg = 'Select Response File : Success'
                self.key_select.setEnabled(True)
            
            else:
                msg = 'Invalid response File : Select .txt file'
            
            self.statusbar.showMessage(msg)
        
        if(button_id == 'key_select'):
            self.key_path.setText(path)
            
            #Check Extension of file.
            path = path.split(os.sep)
            path = path[ len(path) - 1 ].split('.')
            if( path[ len(path) - 1 ] == 'txt'):
                msg = 'Select Key File : Success'
                self.re_eval_submit.setEnabled(True)
                self.result_eval_submit.setEnabled(True)
            
            else:
                msg = 'Invalid key File : Select .txt file'
            
            self.statusbar.showMessage(msg)
            
        if(button_id == 'center_info_select'):
            self.center_info_path.setText(path)
            
            #Check Extension of file.
            path = path.split(os.sep)
            path = path[ len(path) - 1 ].split('.')
            if( path[ len(path) - 1 ] == 'xls'):
                msg = 'Select Center Info File : Success'
                self.center_alloc_submit.setEnabled(True)
            
            else:
                msg = 'Invalid Center Info File : Select .xls file'
            
            self.statusbar.showMessage(msg)
            
        if(button_id == 'student_info_select'):
            self.student_info_path.setText(path)
            
            #Check Extension of file.
            temp_path = path.split(os.sep)
            temp_path = temp_path[ len(temp_path) - 1 ].split('.')
            
            if( temp_path[ len(temp_path) - 1 ] == 'xls'):
                
                errors = handle_uploads.handle_student_info(path)
                if( len(errors) == 0 ):
                    msg = 'Select Student Info File : Success'
                    self.center_info_select.setEnabled(True)
                else:
                    msg = 'Invalid Student Info : '+ errors[0]
            
            else:
                msg = 'Invalid Student Info : Select .xls file'
                
            self.statusbar.showMessage(msg)
            
    def result_eval_submit_slot(self):
        
        if(self.result_eval_submit.text() == 'Submit'):
        
            response_path = self.response_path.text()
            key_path = self.key_path.text()
                
            if(  response_path and key_path ):        
                errors = result_evaluator.evaluate(response_path , key_path , self.ques_not_eval , self.no_of_ques )
                
                if (len(errors) == 0):
                    msg = 'Evaluation Success.'
                    self.result_eval_submit.setText('View Result')
                
                else:
                    msg = 'Evaluation not successfull.'
                    for e in errors:
                        msg = msg + ' ' + e
        
            self.statusbar.showMessage(msg)
            
        if(self.result_eval_submit.text() == 'View Result'):
            
            if(os.name == 'posix'):
                subprocess.call('xdg-open Result.xls' , shell=True)
            
            if(os.name == 'nt'):
                subprocess.call(("cmd \c start Result.xls"))
                
            self.response_path.setText('')
            self.key_path.setText('')
            
            
    def center_alloc_submit_slot(self):
        
        if( self.center_alloc_submit.text() == 'Submit' ):
            
            center_info_path = self.center_info_path.text()
            student_info_path =self.student_info_path.text()
            
            success = centre_allocator.allocate(student_info_path , center_info_path)
            
            if(success):
                msg = 'Roll Number Generation and Center Allocation Success.'
                self.center_alloc_submit.setText('View')
            else:
                msg = 'Roll Number Generation and Center Allocation not Successful.'
                
            self.statusbar.showMessage(msg)
            
        if(self.center_alloc_submit.text() == 'View'):
            
            if(os.name == 'posix'):
                subprocess.call('xdg-open Roll\ Number\ Information.xls' , shell=True)
            
            if(os.name == 'nt'):
                subprocess.call(("cmd \c start Roll Number Information.xls"))
                
            self.response_path.setText('')
            self.key_path.setText('')

        
    def re_eval_submit_slot(self):
        dlg = advanced_eval_options.Ui_Dialog()
        if dlg.exec_() :
            no_of_ques , ques_not_eval , errors = dlg.getValues()
            if no_of_ques:
                self.no_of_ques = no_of_ques
            if  ques_not_eval:
                self.ques_not_eval = ques_not_eval
            if(errors):
                if(len(errors) == 1):
                    msg = errors[0]
                else:
                    msg = 'More than one errors occurred!!!'
            else:
                msg = 'Result Evaluator Advanced options successfully selected.' 
            
            self.statusbar.showMessage(msg)
            
        
                   
        
