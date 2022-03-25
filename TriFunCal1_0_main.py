import sys
import Func_Sin
#from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtWidgets
from TriFunCal1_0 import Ui_MainWindow



class myWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.setupUi(self)


    def sin(self):
        temp = self.output.text()
        try:
            temp = float(temp)
        except:
            self.output.setText('invalid syntax, check your input!')

        output_temp = Func_Sin.sinx(temp)
        output_temp = str(output_temp)
        self.input.setText(output_temp)


if __name__ =='__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = myWindow()

    w.pushButton_sin.clicked.connect(w.sin)

    w.show()
    sys.exit(app.exec_())

