import string
from tkinter import *

def check():
    upper_case = any([1 if i in string.ascii_uppercase else 0 for i in password.get()])
    lower_case = any([1 if i in string.ascii_lowercase else 0 for i in password.get()])
    special = any([1 if i in string.punctuation else 0 for i in password.get()])
    digits = any([1 if i in string.digits else 0 for i in password.get()])

    length = len(password.get())

    if length >= 10:
        length = True
    else:
        length = False

    characters = [upper_case, lower_case, special, digits, length]

    score = 0
    for i in range(len(characters)):
        if characters[i]:
            score += 1

    checked_password["text"] = 'Надёжность пароля: %s из 5' % score
    if int('%s' % score) <= 2:
        root['bg'],input_passowrd['bg'],btn['bg'],checked_password['bg'] = "red","red","red","red"
    elif int('%s' % score) == 3:
        root['bg'],input_passowrd['bg'],btn['bg'],checked_password['bg'] = "yellow","yellow","yellow","yellow"
    elif int('%s' % score) >= 4:
        root['bg'],input_passowrd['bg'],btn['bg'],checked_password['bg'] = "green","green","green","green"
root = Tk()
root.title("PasswordChecker by _sineD_0")

password = StringVar()

input_passowrd = Entry(textvariable=password)
btn = Button(text="check",command=check)
checked_password = Label(text="")

input_passowrd.pack()
btn.pack()
checked_password.pack()

root.mainloop()