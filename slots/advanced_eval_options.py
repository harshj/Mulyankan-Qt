
from PyQt4 import QtCore, QtGui

class Ui_Dialog(QtGui.QDialog):
    
    def __init__(self , parent = None):
        QtGui.QDialog.__init__(self)
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
        
        font_input = QtGui.QFont()
        font_input.setFamily("Arial")
        font_input.setPointSize(10)
        
        self.buttonBox = QtGui.QDialogButtonBox(dialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox , 5 ,2 , 1 , 2)
        
        self.label = QtGui.QLabel(dialog)
        self.label.setObjectName("label")
        self.label.setFont(font)
        self.gridLayout.addWidget(self.label , 1 , 1 , 1 , 3)
        
        self.no_of_ques = QtGui.QTextEdit(dialog)
        self.no_of_ques.setObjectName('no_of_ques')
        self.no_of_ques.setFont(font_input)
        self.no_of_ques.setMaximumSize(QtCore.QSize(100, 26))
        self.gridLayout.addWidget(self.no_of_ques , 2 , 1 , 1 , 3)
        
        self.label1 = QtGui.QLabel(dialog)
        self.label1.setObjectName("label1")
        self.label1.setFont(font)
        self.gridLayout.addWidget(self.label1 , 3 , 1, 1 , 3)
        
        self.ques_not_eval = QtGui.QTextEdit(dialog)
        self.ques_not_eval.setObjectName('ques_not_eval')
        self.ques_not_eval.setFont(font_input)
        self.ques_not_eval.setMaximumSize(QtCore.QSize(400, 100))
        self.gridLayout.addWidget(self.ques_not_eval , 4 , 1 , 1 , 3)
        
        

        self.retranslateUi(dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), dialog.reject)
        
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("Result Evaluator Advanced Options")
        self.label.setText( "Number of Questions to be Evaluated :")
        self.label1.setText("Questions not to be Evaluated (seperate multiple with spaces) :")

    def getValues(self):
        no_of_ques =  self.no_of_ques.toPlainText() 
        ques_not_eval = self.ques_not_eval.toPlainText()
        errors = []
        
        if(no_of_ques):
            try:
                no_of_ques = int(no_of_ques)
            except Exception:
                errors.append('Invalid Entry : Enter valid Number of Questions to be Evaluated') 
            
        if(ques_not_eval):
            ques_not_eval = str(ques_not_eval)
            for q in ques_not_eval.split():
                if not q.isdigit():
                    errors.append('Invalid Entry : Questions not to be Evaluated')
                    break;
                    
        return no_of_ques , ques_not_eval, errors
        