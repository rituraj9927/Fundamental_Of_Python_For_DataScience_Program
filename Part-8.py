# lamda functions

# def foo(x):
#     return 2*x
# foo=lambda x:2*x          # another method to create the function
# print(foo(5))


# from tkinter import *
#
#
# def handleClick():
#     strVar.set(strVar2.get())
#
#
# root = Tk()        # Tk is a class and root is an object
#
# # Label(root, text='Coding Calculator').pack()
# label = Label(root, text='Coding Calculator')
# label.pack()
#
# btn = Button(root, text="Click Mee", command=handleClick)
# btn.pack()
#
# strVar = StringVar()
# strVar.set('')                      # setting default value of strVar
# label2 = Label(root, textvariable=strVar)
# label2.pack()
#
# strVar2 = StringVar()
# # text = Text(root).pack                            # to get a text box on the screen and take input from the user
# text = Entry(root, textvariable=strVar2)            # to get input from the user in a line
# text.pack()
#
#
# root.mainloop()


# Simple Calculator from Python

# from tkinter import *
#
# shouldReset = False
#
# def handleClick(btnVal):
#     global shouldReset
#     curr = strVar.get()
#     if btnVal == '=':
#         strVar.set(eval(curr))
#         shouldReset = True
#
#     else:
#         if shouldReset and not (btnVal in ['/','*','+','-','.']):
#             strVar.set(btnVal)
#
#         else:
#             strVar.set(curr+btnVal)
#
#         shouldReset = False
#
#
# window = Tk()
# strVar = StringVar()
# label = Label(window, textvariable=strVar)
# label.grid(row=0, column=0, columnspan=4)
#
# Button(window, text='7', command=lambda: handleClick('7'),
#               width=5,height=2).grid(row=1, column=0)
#
#
# Button(window, text='8', command=lambda: handleClick('8'),
#               width=5,height=2).grid(row=1, column=1)
#
#
# Button(window, text='9', command=lambda: handleClick('9'),
#               width=5,height=2).grid(row=1, column=2)
#
#
# Button(window, text='4', command=lambda: handleClick('4'),
#               width=5,height=2).grid(row=2, column=0)
#
# Button(window, text='5', command=lambda: handleClick('5'),
#               width=5,height=2).grid(row=2, column=1)
#
# Button(window, text='6', command=lambda: handleClick('6'),
#               width=5,height=2).grid(row=2, column=2)
#
# Button(window, text='1', command=lambda: handleClick('1'),
#               width=5,height=2).grid(row=3, column=0)
#
# Button(window, text='2', command=lambda: handleClick('2'),
#               width=5,height=2).grid(row=3, column=1)
#
# Button(window, text='3', command=lambda: handleClick('3'),
#               width=5,height=2).grid(row=3, column=2)
#
# Button(window, text='.', command=lambda: handleClick('.'),
#               width=5,height=2).grid(row=4, column=0)
#
# Button(window, text='0', command=lambda: handleClick('0'),
#               width=5,height=2).grid(row=4, column=1)
#
# Button(window, text='=', command=lambda: handleClick('='),
#               width=5,height=2).grid(row=4, column=2)
#
# Button(window, text='/', command=lambda: handleClick('/'),
#               width=5,height=2).grid(row=1, column=3)
#
# Button(window, text='*', command=lambda: handleClick('*'),
#               width=5,height=2).grid(row=2, column=3)
#
# Button(window, text='-', command=lambda: handleClick('-'),
#               width=5,height=2).grid(row=3, column=3)
#
# Button(window, text='+', command=lambda: handleClick('+'),
#               width=5,height=2).grid(row=4, column=3)
#
# window.mainloop()




























































