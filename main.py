from tkinter import *


ui = Tk()
        
ui.configure(background="white")
        
ui.title("GS Calculator")

expression_field = Entry(ui)

expression_field.grid(columnspan=4, ipadx=50)
        

button1 = Button(ui, text=' 1 ', fg='white', bg='black',
                            height=1, width=7)
button1.grid(row=2, column=0)
        
button2 = Button(ui, text=' 2 ', fg='white', bg='black',
                            height=1, width=7)
button2.grid(row=2, column=1)
        
button3 = Button(ui, text=' 3 ', fg='white', bg='black',
                            height=1, width=7)
button3.grid(row=2, column=2)
        
button4 = Button(ui, text=' 4 ', fg='white', bg='black',
                            height=1, width=7)
button4.grid(row=3, column=0)
        
button5 = Button(ui, text=' 5 ', fg='white', bg='black',
                            height=1, width=7)
button5.grid(row=3, column=1)
        
button6 = Button(ui, text=' 6 ', fg='white', bg='black',
                            height=1, width=7)
button6.grid(row=3, column=2)
        
button7 = Button(ui, text=' 7 ', fg='white', bg='black',
                            height=1, width=7)
button7.grid(row=4, column=0)
        
button8 = Button(ui, text=' 8 ', fg='white', bg='black',
                            height=1, width=7)
button8.grid(row=4, column=1)
        
button9 = Button(ui, text=' 9 ', fg='white', bg='black',
                            height=1, width=7)
button9.grid(row=4, column=2)
        
button0 = Button(ui, text=' 0 ', fg='white', bg='black',
                            height=1, width=7)
button0.grid(row=5, column=0)
        
plus = Button(ui, text=' + ', fg='white', bg='black',
                        height=1, width=7)
plus.grid(row=2, column=3)
        
minus = Button(ui, text=' - ', fg='white', bg='black',
                        height=1, width=7)
minus.grid(row=3, column=3)
        
multiply = Button(ui, text=' x ', fg='white', bg='black',
                            height=1, width=7)
multiply.grid(row=4, column=3)
        
divide = Button(ui, text=' / ', fg='white', bg='black',
                        height=1, width=7)
divide.grid(row=5, column=3)
        
equal = Button(ui, text=' = ', fg='white', bg='black',
            height=1, width=7)
equal.grid(row=5, column=2)
ui.mainloop()