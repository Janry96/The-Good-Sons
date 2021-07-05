from tkinter import *
import math as m

expression = ""
ans = []
 
def press(num):
    global expression
 
    expression = expression + str(num)
 
    equation.set(expression)

def press1(num):
    global expression
    expression = expression + str(num)
    return expression
 
 

def equals():
    try:
 
        global expression
        
        expression = expression.replace('x','*')

        expression = expression.replace('Sin','m.sin')
        expression = expression.replace('Cos','m.cos')
        expression = expression.replace('Tan','m.tan')
        
        expression = expression.replace('acos','m.acos')
        expression = expression.replace('atan','m.atan')
        expression = expression.replace('asin','m.asin')

        expression = expression.replace('^','**')
        expression = expression.replace('log','m.log10')
        expression = expression.replace('e','m.exp')

        if '(' in expression:
            temp = expression.index('(')
            res = expression[:temp]
            if len(res) < 3:
                if res[-1] == '0' or res[-1] == '2' or res[-1] == '3' or res[-1] == '4' or res[-1] == '5' or res[-1] == '6' or res[-1] == '7' or res[-1] == '8' or res[-1] == '9':
                    expression = expression.replace('(', '*(')
            if len(res) >= 3:
                if res[-1] != 'g' and res[-2] != '1' and res[-3] != 'g':
                    if res[-1] == '0' or res[-1] == '2' or res[-1] == '3' or res[-1] == '4' or res[-1] == '5' or res[-1] == '6' or res[-1] == '7' or res[-1] == '8' or res[-1] == '9':
                        expression = expression.replace('(', '*(')



        total = str(eval(expression))
 
        equation.set(total)
        expression = ""
        ans.append(total)

    except:
 
        equation.set(" error ")
        expression = ""
 
def equals1(exp):
    global expression
    expression = exp
    try:

        expression = expression.replace('x','*')

        expression = expression.replace('Sin','m.sin')
        expression = expression.replace('Cos','m.cos')
        expression = expression.replace('Tan','m.tan')
        
        expression = expression.replace('acos','m.acos')
        expression = expression.replace('atan','m.atan')
        expression = expression.replace('asin','m.asin')

        expression = expression.replace('^','**')
        expression = expression.replace('log','m.log10')
        expression = expression.replace('e','m.exp')

        if '(' in expression:
            temp = expression.index('(')
            res = expression[:temp]
            if len(res) < 3:
                if res[-1] == '0' or res[-1] == '2' or res[-1] == '3' or res[-1] == '4' or res[-1] == '5' or res[-1] == '6' or res[-1] == '7' or res[-1] == '8' or res[-1] == '9':
                    expression = expression.replace('(', '*(')
            if len(res) >= 3:
                if res[-1] != 'g' and res[-2] != '1' and res[-3] != 'g':
                    if res[-1] == '0' or res[-1] == '2' or res[-1] == '3' or res[-1] == '4' or res[-1] == '5' or res[-1] == '6' or res[-1] == '7' or res[-1] == '8' or res[-1] == '9':
                        expression = expression.replace('(', '*(')

        

        

        total = str(eval(expression))
 
        return(total)
        
 
        expression = ""
        ans.append(total)
    except:
 
        return(" error ")
        expression = ""    


def clear():
    global expression
    expression = ""
    equation.set("")

def delete():
    global expression
    expression=expression[:-1]
    equation.set(expression)

def answer():
    global expression
    expression = expression + ans[-1]
    equation.set(expression)

    

 
 
if __name__ == "__main__":
    gui = Tk()

    gui.configure(background="black")
 
    gui.title("Good Son's Calculator")

    equation = StringVar()
 
    expression_field = Entry(gui, textvariable=equation)

    expression_field.grid(columnspan=4, ipadx=50, ipady= 4)

    button1 = Button(gui, text=' 1 ', fg='white', bg='black',
                    command=lambda: press(1), height=1, width=7)
    button1.grid(row=4, column=0)
 
    button2 = Button(gui, text=' 2 ', fg='white', bg='black',
                    command=lambda: press(2), height=1, width=7)
    button2.grid(row=4, column=1)
 
    button3 = Button(gui, text=' 3 ', fg='white', bg='black',
                    command=lambda: press(3), height=1, width=7)
    button3.grid(row=4, column=2)
 
    button4 = Button(gui, text=' 4 ', fg='white', bg='black',
                    command=lambda: press(4), height=1, width=7)
    button4.grid(row=5, column=0)
 
    button5 = Button(gui, text=' 5 ', fg='white', bg='black',
                    command=lambda: press(5), height=1, width=7)
    button5.grid(row=5, column=1)
 
    button6 = Button(gui, text=' 6 ', fg='white', bg='black',
                    command=lambda: press(6), height=1, width=7)
    button6.grid(row=5, column=2)
 
    button7 = Button(gui, text=' 7 ', fg='white', bg='black',
                    command=lambda: press(7), height=1, width=7)
    button7.grid(row=6, column=0)
 
    button8 = Button(gui, text=' 8 ', fg='white', bg='black',
                    command=lambda: press(8), height=1, width=7)
    button8.grid(row=6, column=1)
 
    button9 = Button(gui, text=' 9 ', fg='white', bg='black',
                    command=lambda: press(9), height=1, width=7)
    button9.grid(row=6, column=2)
 
    button0 = Button(gui, text=' 0 ', fg='white', bg='black',
                    command=lambda: press(0), height=1, width=7)
    button0.grid(row=7, column=0)
 
    plus = Button(gui, text=' + ', fg='white', bg='black',
                command=lambda: press("+"), height=1, width=7)
    plus.grid(row=4, column=3)
 
    minus = Button(gui, text=' - ', fg='white', bg='black',
                command=lambda: press("-"), height=1, width=7)
    minus.grid(row=5, column=3)
 
    multiply = Button(gui, text=' x ', fg='white', bg='black',
                    command=lambda: press("x"), height=1, width=7)
    multiply.grid(row=6, column=3)
 
    divide = Button(gui, text=' / ', fg='white', bg='black',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=7, column=3)
 
    equal = Button(gui, text=' = ', fg='white', bg='black',
                command=equals, height=1, width=7)
    equal.grid(row=9, column=3)
 
    clear = Button(gui, text='CLEAR', fg='white', bg='black',
                command=clear, height=1, width=7)
    clear.grid(row=2, column=3)
 
    Decimal= Button(gui, text='.', fg='white', bg='black',
                    command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=7, column=1)

    dlt = Button(gui, text='DEL', fg='white', bg='black',
                    command=delete, height=1, width=7)
    dlt.grid(row=3, column=3)

    an = Button(gui, text='ANS', fg='white', bg='black',
                    command=answer, height=1, width=7)
    an.grid(row=9, column=2)

    paren1 = Button(gui, text='(', fg='white', bg='black',
                command=lambda: press("("), height=1, width=7)
    paren1.grid(row=8, column=0)

    paren2 = Button(gui, text=')', fg='white', bg='black',
                command=lambda: press(")"), height=1, width=7)
    paren2.grid(row=8, column=1)

    sin = Button(gui, text='Sin', fg='white', bg='black',
                command=lambda: press("Sin ("), height=1, width=7)
    sin.grid(row=2, column=0)

    cos = Button(gui, text='Cos', fg='white', bg='black',
                command=lambda: press("Cos ("), height=1, width=7)
    cos.grid(row=2, column=1)

    tan = Button(gui, text='Tan', fg='white', bg='black',
                command=lambda: press("Tan ("), height=1, width=7)
    tan.grid(row=2, column=2)

    asin = Button(gui, text='asin', fg='white', bg='black',
                command=lambda: press("asin ("), height=1, width=7)
    asin.grid(row=3, column=0)

    acos = Button(gui, text='acos', fg='white', bg='black',
                command=lambda: press("acos ("), height=1, width=7)
    acos.grid(row=3, column=1)

    atan = Button(gui, text='atan', fg='white', bg='black',
                command=lambda: press("atan ("), height=1, width=7)
    atan.grid(row=3, column=2)

    power = Button(gui, text='^', fg='white', bg='black',
                command=lambda: press("^"), height=1, width=7)
    power.grid(row=8, column=2)

    log = Button(gui, text='log', fg='white', bg='black',
                command=lambda: press("log("), height=1, width=7)
    log.grid(row=7, column=2)

    nroot = Button(gui, text='nroot', fg='white', bg='black',
                command=lambda: press("^ (1/"), height=1, width=7)
    nroot.grid(row=9, column=1)

    eee = Button(gui, text='e^(x)', fg='white', bg='black',
                command=lambda: press("e("), height=1, width=7)
    eee.grid(row=9, column=0)

    square = Button(gui, text='x^2', fg='white', bg='black',
                command=lambda: press("^2"), height=1, width=7)
    square.grid(row=8, column=3)


    gui.mainloop()
