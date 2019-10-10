from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDesktopWidget
from warning import Ui_Dialog1

class mywindow1(QtWidgets.QWidget, Ui_Dialog1):
    def  __init__ (self):
        super(mywindow1, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle('问题无解')
        self.center()
        self.setFixedSize(self.width(), self.height())


    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    ui = mywindow1()    
    ui.show()
    sys.exit(app.exec_())