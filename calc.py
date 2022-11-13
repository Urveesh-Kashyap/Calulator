from tkinter import *
import math as mt
from pygame import mixer
#import speech_recognition as sp
mixer.init()

# Defining functions :
def click(value):
    entfld = entryfield.get()
    answer=''
    try:
        if value=='C':
            entfld=entfld[0:len(entfld)-1]
            entryfield.delete(0,END)
            entryfield.insert(0,entfld)
            return

        elif value=='CE':
            entryfield.delete(0,END)

        elif value=='√':
            answer = mt.sqrt(eval(entfld))

        elif value=="π":
            answer=mt.pi

        elif value=='cosθ':
            answer=mt.cos(mt.radians(eval(entfld))) # radians converting value into angle.

        elif value=='tanθ':
            answer=mt.tan(mt.radians(eval(entfld)))

        elif value=='sinθ':
            answer=mt.sin(mt.radians(eval(entfld)))

        elif value=='2π':
            answer=2*mt.pi

        elif value=='cosh':
            answer=mt.cosh(eval(entfld))

        elif value=='sinh':
            answer=mt.sinh(eval(entfld))

        elif value=='tanh':
            answer=mt.tanh(eval(entfld))

        elif value == chr(8731):
            answer=eval(entfld)**(1/3)

        elif value == 'x\u02b8':
            entryfield.insert(END,'**') # it will two asteriks for entering value of y
            return

        elif value == 'x\u00B3':
            answer= eval(entfld) ** 3

        elif value == 'x\u00B2':
            answer= eval(entfld) ** 2

        elif value == 'ln':
            answer= mt.log2(eval(entfld))

        elif value == 'deg':
            answer= mt.degrees(eval(entfld))

        elif value == 'rad':
            answer = mt.radians(eval(entfld))

        elif value == 'e':
            answer = mt.e

        elif value == 'log10':
            answer = mt.log10(eval(entfld))

        elif value == 'x!':
            answer = mt.factorial(entfld)

        elif value == chr(247):
            entryfield.insert(END, '/')
            return

        elif value == '=':
           answer = eval(entfld)

        else:
            entryfield.insert(END,value)
            return

        entryfield.delete(0, END)
        entryfield.insert(0, answer)

    except SyntaxError:
        pass

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a, b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def lcm(a,b):
    l=mt.lcm(a,b)
    return l
def hcf(a,b):
    h=mt.gcd(a,b)
    return h

# creating dictionary operations :
operations = {'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add,
              'SUBTRACTION':sub,'DIFFERENCE':sub,'MINUS':sub,'SUBTRACT':sub,
              'PRODUCT':mul,'MULTIPLICATION':mul,'MULTIPLY':mul,
              'DIVISION':div, 'DIV':div,'DIVIDE':div,
              'LCM':lcm, 'HCF': hcf,
              'MOD':mod, 'REMAINDER':mod, 'MODULUS':mod }

def find_numbers(t):
    l=[]
    for num in t:
        try:
            l.append(int(num))
        except ValueError:
            pass
    return l








# Defining Microphone function :

def micoutput():
    mixer.music.load('gta_tone.mp3')
    mixer.music.play()
    sr=sp.Recognizer()
    with sp.Microphone() as m:
        try:
            sr.adjust_for_ambient_noise(m,duration=0.4)
            voice=sr.listen(m)
            text=sr.recognize_google(voice)

            mixer.music.load('out1.wav')
            mixer.music.play()
            text_list=text.split(' ')
            for word in text_list:
                if word.upper() in operations.keys():
                    l=find_numbers(text_list)
                    print(l)
                    result = operations[word.upper()](l[0],l[1])
                    entryfield.delete(0,END)
                    entryfield.insert(END,result)
                else:
                    pass


        except:
            pass





root = Tk()
root.title('Calculator')
root.config(bg='#333333')
root.geometry('511x650+100+100')

# LOGO Calc
logo_image = PhotoImage(file=r"logo.jpeg")
logolabel = Label(root, image=logo_image, bg='#333333')
logolabel.grid (row=0, column=0)

# Creating Entry fields
entryfield = Entry(root, font=('Pally', 25, 'bold'), bg='#333333', fg='white', bd=8,
                   relief=SUNKEN, width=18)
entryfield.grid(row=0, column=0, columnspan=6)  # columnspan will not use just one column it will use
#                                               whole number of columns

# Logo MIC
mic_image = PhotoImage(file='mic.png')
mic_button = Button(root, image=mic_image, bd=0, bg='#333333', activebackground='#333333',command=micoutput)
mic_button.grid(row=0, column=5)

# CREATING BUTTON :
# Creating button text list
button_txt_lst = ['C', 'CE', '√', '+', 'π', 'cosθ', 'tanθ', 'sinθ',
                  '2π', '-', 'tanh', 'sinh','1', '2', '3', '*',
                  chr(8731), 'x\u02b8', '4', '5', '6', chr(247), 'x\u00B2','cosh',
                  '7', '8', '9', '%','x\u00B3', 'deg', '0', '00',
                  '000','=', 'e', '.', 'rad', 'ln', 'log10', '(', ')', 'x!']  # chr8731 = cube root, x\u02b8 = x**y
#                                                                   x\u00B3 = cube of x, x\u00B2 = sq of x, chr(247) = division


# creating variable to store row and column values as it will change the position in loop
rowvalue = 1
columnvalue = 0

# Applying loop to button list
for i in button_txt_lst:
    button = Button(root, width=5, height=2, bd=2, relief=RAISED, text=i, bg='#505050', fg='white',
                    font=('Pally', 18, 'bold'), activebackground='#505050',
                    command=lambda button=i: click(button))
    button.grid(row=rowvalue, column=columnvalue, pady=1)
    columnvalue += 1
    if columnvalue > 5:
        rowvalue += 1
        columnvalue = 0

root.mainloop()
