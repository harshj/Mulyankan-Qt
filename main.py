#!/usr/lib/env python


from PyQt4 import QtGui
import slots.mainWindow

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = slots.mainWindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.raise_()
    sys.exit(app.exec_())
