# Dialog Box to select the file to be viewed.

from PyQt4 import QtCore, QtGui
from os import listdir
import PyQt4

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Ui_Dialog(QtGui.QDialog):
    
    def __init__(self , path , parent = None):
        QtGui.QDialog.__init__(self)
        self.path = path
        self.setupUi(self)
    
    def setupUi(self , dialog):
        dialog.setObjectName("dialog")
        dialog.resize(400 , 300)
        
        self.gridLayout = QtGui.QGridLayout(dialog)
        self.gridLayout.setObjectName("gridLayout")
        
        font = QtGui.QFont()
        font.setFamily("Garuda")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        
        font_file = QtGui.QFont()
        font_file.setFamily("Arial")
        font_file.setPointSize(10)
        
        self.label = QtGui.QLabel(dialog)
        self.label.setObjectName("label")
        self.label.setFont(font)
        self.gridLayout.addWidget(self.label , 1 , 1 , 1 , 3)
        
        self.no_file_label = QtGui.QLabel(dialog)
        self.no_file_label.setObjectName("no_file_label")
        self.no_file_label.setFont(font_file)
        self.gridLayout.addWidget(self.no_file_label , 2 , 1 , 1 , 3)    
        x = 3
        self.dir = listdir(self.path)
        
        self.radioGroup = QtGui.QButtonGroup()
        
        if len(self.dir) == 0:
            self.no_file_label.setText("No files found in the directory!!!")
        
        else:
            for i in xrange(len(self.dir)):
                button = QtGui.QRadioButton( _fromUtf8(self.dir[i]) , dialog )
                self.radioGroup.addButton(button,i)
                self.gridLayout.addWidget(button, x, 1, 1, 3)
                x = x + 1
        
        self.buttonBox = QtGui.QDialogButtonBox(dialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox , x ,2 , 1 , 2)
        
        self.retranslateUi(dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), dialog.reject)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("Choose a file to view")
        self.label.setText("Choose the file to open: ")
        
    def get_filename(self):
        selected_button = self.radioGroup.checkedButton()
        if selected_button:
            return selected_button.text()
        