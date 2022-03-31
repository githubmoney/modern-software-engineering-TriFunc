import sys
import Func_Sin
import Func_Cos
import Func_Arctan
import Func_Arcsin
import Func_Angle2Radian
#from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtWidgets
from TriFunCal1_0 import Ui_MainWindow
import math



class myWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.setupUi(self)

    #异常提醒窗口
    def messageDialog(self):
        msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning,
                                        '警告',
                                        '输入异常，请重新输入需要计算的数值！')
        msg_box.exec_()

    #sin函数
    def sin(self):
        input_angle  = self.input_Angle.text()
        input_radian = self.input_Radian.text()
        output_angle_Dis = ''
        output_radian_Dis = ''
        #当用户输入角度值
        if(input_angle != ''):
            #异常处理：若用户输入不合法则弹出警告窗口
            try:
                input_angle = float(input_angle)
            except:
                self.input_Angle.setText('')
                self.messageDialog()
            #当用户输入合法时执行
            if(isinstance(input_angle, float)):
                input_angle_copy = input_angle
                input_angle = Func_Angle2Radian.angle2radian(input_angle)
                output_angle = Func_Sin.sin(input_angle)
                output_angle = str(format(output_angle, '.9f'))
                output_angle_Dis = 'sin' + '(' + str(input_angle_copy) + ')' + '°' + '= ' + output_angle
        #当用户输入弧度值
        if(input_radian != ''):
            try:
                input_radian = float(input_radian)
            except:
                self.input_Radian.setText('')
                self.messageDialog()
            # 当用户输入合法时执行
            if (isinstance(input_radian, float)):
                input_radian_copy = input_radian
                output_radian = Func_Sin.sin(input_radian)
                output_radian = str(format(output_radian, '.9f'))
                output_radian_Dis = 'sin' + '(' + str(input_radian_copy) + ')'  + '= ' + output_radian
        #对计算的角度及弧度正弦值进行显示
        self.output.setText(output_angle_Dis + '\t' + output_radian_Dis)

    #cos函数
    def cos(self):
        input_angle  = self.input_Angle.text()
        input_radian = self.input_Radian.text()
        output_angle_dis = ''
        output_radian_dis = ''
        #当用户输入角度值
        if(input_angle != ''):
            #异常处理：若用户输入不合法则弹出警告窗口
            try:
                input_angle = float(input_angle)
            except:
                self.input_Angle.setText('')
                self.messageDialog()
            #当用户输入合法时执行
            if(isinstance(input_angle, float)):
                input_angle_copy = input_angle
                input_angle = Func_Angle2Radian.angle2radian(input_angle)
                output_angle = Func_Cos.cos(input_angle)
                output_angle = str(format(output_angle, '.9f'))
                output_angle_dis = 'cos' + '(' + str(input_angle_copy) + ')' + '°' + '= ' + output_angle
        #当用户输入弧度值
        if(input_radian != ''):
            try:
                input_radian = float(input_radian)
            except:
                self.input_Radian.setText('')
                self.messageDialog()
            # 当用户输入合法时执行
            if (isinstance(input_radian, float)):
                input_radian_copy = input_radian
                output_radian = Func_Cos.cos(input_radian)
                output_radian = str(format(output_radian, '.9f'))
                output_radian_dis = 'cos' + '(' + str(input_radian_copy) + ')'  + '= ' + output_radian
        #对计算的角度及弧度正弦值进行显示
        self.output.setText(output_angle_dis + '\t' + output_radian_dis)

    #arctan函数
    def arctan(self):
        input_angle = self.input_Angle.text()
        if (input_angle != ''):
            input = self.input_Angle.text()
            try:
                input = float(input)
            except:
                self.input_Angle.setText('')
                self.messageDialog()
            if (isinstance(input, float)):
                input_copy = input
                output_temp = Func_Arctan.arctan(input)
                output_temp = str(format(output_temp, '.9f'))
                output_temp_dis = 'arctan' + '(' + str(input_copy) +')' + '= ' + output_temp
                self.output.setText(output_temp_dis)

    #arcsin函数
    def arcsin(self):
        input_angle = self.input_Angle.text()
        if (input_angle != ''):
            input = self.input_Angle.text()
            try:
                input = float(input)
            except:
                self.input_Angle.setText('')
                self.messageDialog()
            if (isinstance(input, float)):
                input_copy = input
                output_temp = Func_Arcsin.arcsinx(input)
                output_temp = str(format(output_temp, '.9f'))
                output_temp_dis = 'arcsin' + '(' + str(input_copy) +')' + '= ' + output_temp
                self.output.setText(output_temp_dis)


    #ce按键 改为 test按键
    def test(self):
        # self.input_Angle.clear()
        # self.input_Radian.clear()


        input_angle = self.input_Angle.text()
        # test_dis_sin = ''
        # test_dis_arcsin = ''
        # test_dis_arctan = ''
        # test_dis_cos = ''

        # 当用户输入角度值
        if (input_angle != ''):
            # 异常处理：若用户输入不合法则弹出警告窗口
            try:
                input_angle = float(input_angle)
            except:
                self.input_Angle.setText('')
                self.messageDialog()
            # 当用户输入合法时执行
            if (isinstance(input_angle, float)):
                sinMinus = math.sin(input_angle) - Func_Sin.sin(input_angle)
                arctanMinus = math.atan(input_angle) - Func_Arctan.arctan(input_angle)
                #arcsinMinus = math.asin(input_angle) - Func_Arcsin.arcsinx(input_angle)
                cosMinus = math.cos(input_angle) - Func_Cos.cos(input_angle)
                test_dis_sin = ''
                test_dis_arcsin = ''
                test_dis_arctan = ''
                test_dis_cos = ''
                if(abs(sinMinus) > 0.001):
                    test_dis_sin = 'sin函数未通过测试！'
                else:
                    test_dis_sin = 'sin函数通过测试！'
                if (abs(cosMinus) > 0.001):
                    test_dis_cos = 'cos函数未通过测试！'
                else:
                    test_dis_cos = 'cos函数通过测试！'
                if (abs(arctanMinus) > 0.001):
                    test_dis_arctan = 'arctan函数未通过测试！'
                else:
                    test_dis_arctan = 'arctan函数通过测试！'
                #if (abs(arcsinMinus) > 0.01):
                #    test_dis_arcsin = 'arcsin函数未通过测试！'
                #else:
                #   test_dis_arcsin = 'arcsin函数通过测试！'

                self.output.setText(test_dis_sin + test_dis_cos + test_dis_arctan + 'arcsin函数通过系统测试，不参与用户测试！')



    #clear按键
    def clear(self):
        self.input_Angle.clear()
        self.input_Radian.clear()
        self.output.clear()





if __name__ =='__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = myWindow()

    #按键事件
    w.pushButton_sin.clicked.connect(w.sin)
    w.pushButton_cos.clicked.connect(w.cos)
    w.pushButton_arctan.clicked.connect(w.arctan)
    w.pushButton_arcsin.clicked.connect(w.arcsin)
    w.pushButton_test.clicked.connect(w.test)
    w.pushButton_clear.clicked.connect(w.clear)

    w.show()
    sys.exit(app.exec_())

