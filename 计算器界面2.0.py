import tkinter as tk
import tkinter.messagebox
import re
# import math
from Func_Arcsin import *
from Func_Arctan import *
from Func_Cos import *
from Func_Sin import *
from Func_Angle2Radian import *
root = tk.Tk()
root.minsize(300, 400)      # 窗口大小300*400
root.resizable(0, 0)
root.title('三角函数计算器')

# 计算器名字
# 运算符号按钮
# 第一行
btnrad = tkinter.Button(root, text='rad', font=('微软雅黑', 20), bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5,
                        command=lambda x='rad': buttonClick1(x))
btnrad.place(x=0, y=85, width=100, height=45)
btnsin = tkinter.Button(root, text='sin', font=('微软雅黑', 20), bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5,
                        command=lambda x='sin': buttonClick1(x))
btnsin.place(x=100, y=85, width=100, height=45)
btncos = tkinter.Button(root, text='cos', font=('微软雅黑', 20), bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5,
                        command=lambda x='cos': buttonClick1(x))
btncos.place(x=200, y=85, width=100, height=45)

# 第二行
btnarcsine = tkinter.Button(root, text='arcsine', font=('微软雅黑', 20), bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5,
                            command=lambda x='arcsine': buttonClick1(x))
btnarcsine.place(x=0, y=130, width=100, height=45)
btnxarctan = tkinter.Button(root, text='arctan', font=('微软雅黑', 20), bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5,
                            command=lambda x='arctan': buttonClick1(x))
btnxarctan.place(x=100, y=130, width=100, height=45)
btnleft = tkinter.Button(root, text='(', font=('微软雅黑', 20), bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5,
                         command=lambda x='(': buttonClick1(x))
btnleft.place(x=200, y=130, width=50, height=45)
btnrigh = tkinter.Button(root, text=')', font=('微软雅黑', 20), bg=('#96CDCD'), fg=('#4F4F4F'), bd=0.5,
                         command=lambda x=')': buttonClick1(x))
btnrigh.place(x=250, y=130, width=50, height=45)
# 第三行

btnac1 = tkinter.Button(root, text='AC', bd=0.5, font=('黑体', 20), fg='orange', command=lambda
                        x='AC': buttonClick1(x))
btnac1.place(x=0, y=175, width=100, height=45)
btnback1 = tkinter.Button(root, text='←', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda
                          x='←': buttonClick1(x))
btnback1.place(x=100, y=175, width=100, height=45)
btnequ1 = tkinter.Button(root, text='=', bg='orange', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5,
                         command=lambda x='=': buttonClick1(x))
btnequ1.place(x=200, y=175, width=100, height=45)
# 第四行
btn71 = tkinter.Button(root, text='7', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda
                       x='7': buttonClick1(x))
btn71.place(x=0, y=220, width=100, height=45)
btn81 = tkinter.Button(root, text='8', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda
                       x='8': buttonClick1(x))
btn81.place(x=100, y=220, width=100, height=45)
btn91 = tkinter.Button(root, text='9', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda
                       x='9': buttonClick1(x))
btn91.place(x=200, y=220, width=100, height=45)
# 第五行
btn41 = tkinter.Button(root, text='4', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda
                       x='4': buttonClick1(x))
btn41.place(x=0, y=265, width=100, height=45)
btn51 = tkinter.Button(root, text='5', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda
                       x='5': buttonClick1(x))
btn51.place(x=100, y=265, width=100, height=45)
btn61 = tkinter.Button(root, text='6', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda
                       x='6': buttonClick1(x))
btn61.place(x=200, y=265, width=100, height=45)
# 第六行
btn11 = tkinter.Button(root, text='1', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda
                       x='1': buttonClick1(x))
btn11.place(x=0, y=310, width=100, height=45)
btn21 = tkinter.Button(root, text='2', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda
                       x='2': buttonClick1(x))
btn21.place(x=100, y=310, width=100, height=45)
btn31 = tkinter.Button(root, text='3', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda
                       x='3': buttonClick1(x))
btn31.place(x=200, y=310, width=100, height=45)
# 第七行
btnpi = tkinter.Button(root, text='π', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda
                       x='π': buttonClick1(x))
btnpi.place(x=0, y=355, width=100, height=45)
# btnpi.flash()
btn01 = tkinter.Button(root, text='0', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda
                       x='0': buttonClick1(x))
btn01.place(x=100, y=355, width=100, height=45)
btnpoint1 = tkinter.Button(root, text='.', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda
                           x='.': buttonClick1(x))
btnpoint1.place(x=200, y=355, width=100, height=45)

contentVar = tkinter.StringVar(root, '')
contentEntry = tkinter.Entry(
    root, textvariable=contentVar, state='readonly', font=("Arial", 12))
contentEntry.place(x=0, y=35, width=300, height=50)


def buttonClick1(btn):
    content = contentVar.get()
    if content.startswith('.'):  # 小数点前加0
        content = '0' + content
    if btn in '0123456789()':
        content += btn
    elif btn == '.':
        lastPart = re.split(r'\+|-|\*|/', content)[-1]
        if '.' in lastPart:
            tk.messagebox.showerror('错误', 'Input Error')
            return
        else:
            content += btn
    elif btn == 'AC':
        content = ''
    elif btn == '=':
        try:
            strsin = r'sin\(\d+\)|sin\(\-?\d+\.\d+\)'
            if 'sin' in content:
                m = re.search(strsin, content)
                if m is not None:
                    exchange = m.group()
                    exchange1 = exchange
                    if '.' in exchange:
                        exchange = re.search("\-?\d+\.\d+", exchange)
                        value = exchange.group()
                        value = str(sin(float(value)))
                        content = content.replace(exchange1, value)
                    else:
                        exchange = re.search("\-?\d+", exchange)
                        value = exchange.group()
                        value = str(sin(float(value)))
                        content = content.replace(exchange1, value)
            strcos = r'cos\(\d+\)|cos\(\-?\d+\.\d+\)'
            if 'cos' in content:
                m = re.search(strcos, content)
                if m is not None:
                    exchange = m.group()
                    exchange1 = exchange
                    if '.' in exchange:
                        exchange = re.search("\-?\d+\.\d+", exchange)
                        value = exchange.group()
                        value = str(cos(float(value)))
                        content = content.replace(exchange1, value)
                    else:
                        exchange = re.search("\-?\d+", exchange)
                        value = exchange.group()
                        value = str(cos(float(value)))
                        content = content.replace(exchange1, value)
            strarcsine = r'arcsine\(\d+\)|arcsine\(\-?\d+\.\d+\)'
            if 'arcsine' in content:
                m = re.search(strarcsine, content)
                if m is not None:
                    exchange = m.group()
                    exchange1 = exchange
                    if '.' in exchange:
                        exchange = re.search("\-?\d+\.\d+", exchange)
                        value = exchange.group()
                        value = str(arcsinx(float(value)))
                        content = content.replace(exchange1, value)
                    else:
                        exchange = re.search("\-?\d+", exchange)
                        value = exchange.group()
                        value = str(arcsinx(float(value)))
                        content = content.replace(exchange1, value)
            strarctan = r'arctan\(\-?\d+\)|arctan\(\-?\d+\.\d+\)'
            if 'arctan' in content:
                m = re.search(strarctan, content)
                if m is not None:
                    exchange = m.group()
                    exchange1 = exchange
                    if '.' in exchange:
                        exchange = re.search("\-?\d+\.\d+", exchange)
                        value = exchange.group()
                        value = str(arctan(float(value)))
                        content = content.replace(exchange1, value)
                    else:
                        exchange = re.search("\-?\d+", exchange)
                        value = exchange.group()
                        value = str(arctan(float(value)))
                        content = content.replace(exchange1, value)
            strrad = r'rad\(\-?\d+\)|rad\(\-?\d+\.\d+\)'
            if 'rad' in content:
                m = re.search(strrad, content)
                if m is not None:
                    exchange = m.group()
                    exchange1 = exchange
                    if '.' in exchange:
                        exchange = re.search("\-?\d+\.\d+", exchange)
                        value = exchange.group()
                        value = str(angle2radian(float(value)))
                        content = content.replace(exchange1, value)
                    else:
                        exchange = re.search("\-?\d+", exchange)
                        value = exchange.group()
                        value = str(angle2radian(float(value)))
                        content = content.replace(exchange1, value)
            value = eval(content)
            content = str(round(value, 10))
        except ZeroDivisionError:
            tk.messagebox.showerror('错误', 'VALUE ERROR')
            return
    elif btn in operators:
        if content.endswith(operators):
            tk.messagebox.showerror('错误', 'FORMAT ERROR')
            return
        content += btn
    elif btn == 'rad':
        content += 'rad'
    elif btn == 'π':
        content += '3.1415926535897932'
    elif btn == 'sin':
        content += 'sin('
    elif btn == 'cos':
        content += 'cos('
    elif btn == 'arcsine':
        content += 'arcsine('
    elif btn == 'arctan':
        content += 'arctan('
    elif btn == '←':  # 如果按下的是退格‘’，则选取当前数字第一位到倒数第二位
        content = content[0:-1]
    contentVar.set(content)
    contentVar.set(content)


operators = ('=', '.')
root.mainloop()
