from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Tic Tac Toe")

x_win='XXX'
o_win='OOO'
check_wins=None
list_button=[]
button_click = True
flag = 0
buttons = StringVar()

#function that check the str from each combination
def check_str(str1,str2,str3=None):
    if str1==x_win or str2 ==x_win or str3==x_win:
        return x_win
    elif str1==o_win or str2==o_win or str3==o_win:
        return o_win
    return None

#function that get string from the rows
def check_row():
    row1=list_button[0:3]
    row2=list_button[3:6]
    row3=list_button[6:9]
    return check_str(row1[0]['text']+row1[1]['text']+row1[2]['text'],row2[0]['text']+row2[1]['text']+row2[2]['text'],row3[0]['text']+row3[1]['text']+row3[2]['text'])

#function that get string from the columns
def check_column():
    column1=list_button[0::3]
    column2=list_button[1::3]
    column3=list_button[2::3]
    return check_str(column1[0]['text']+column1[1]['text']+column1[2]['text'],column2[0]['text']+column2[1]['text']+column2[2]['text'],column3[0]['text']+column3[1]['text']+column3[2]['text'])

#function that get string from the slants
def check_slant():
    slant1=list_button[0::4]
    slant2=list_button[2:8:2]
    return check_str(slant1[0]['text']+slant1[1]['text']+slant1[2]['text'],slant2[0]['text']+slant2[1]['text']+slant2[2]['text'])

#function that check if someone win
def check_win():
    row=check_row()
    column=check_column()
    slant=check_slant()
    if row!=None:
        print(row)
        return row
    elif column!=None:
        return column
    elif slant!=None:
        return slant
    return None

#fubction that define all the buttons
def set_buttons():
    global list_button
    button1 = Button(tk, text=" ",font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button1))
    button1.grid(row=3, column=0)

    button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button2))
    button2.grid(row=3, column=1)

    button3 = Button(tk, text=' ',font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button3))
    button3.grid(row=3, column=2)

    button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button4))
    button4.grid(row=4, column=0)

    button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button5))
    button5.grid(row=4, column=1)

    button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button6))
    button6.grid(row=4, column=2)

    button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button7))
    button7.grid(row=5, column=0)

    button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button8))
    button8.grid(row=5, column=1)

    button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button9))
    button9.grid(row=5, column=2)

    button10=Button(tk, text='enter to\nTry again', font='Times 20 bold', fg='black', height=2, width=8, command=reset_game)
    button10.grid(row=6, column=1)
    list_button.extend([button1,button2,button3,button4,button5,button6,button7,button8,button9,button10])

#function that disable all the buttons after the game end
def disable_buttons():
    global list_button
    for i in range(len(list_button)-1):
        list_button[i].configure(state=DISABLED)

#function that enable all the buttons after we want to play again
def enable_buttons():
    global list_button
    for i in range(len(list_button)-1):
        list_button[i].configure(state=NORMAL)

#funtion for play again button
def reset_game():
    global flag,list_button,button_click,check_wins
    for i in range((len(list_button))-1):
        list_button[i]["text"]=" "
    button_click=True
    enable_buttons()
    flag=0
    check_wins=None

#function that define all the buttons in the table
def btnClick(buttons):
    global check_wins,button_click, flag
    if buttons["text"] == " " and button_click == True:
        buttons["text"] = "X"
        win_str = check_win()
        if win_str == x_win:
            tkinter.messagebox.showinfo("Tic-Tac-Toe ","player X WINS")
            disable_buttons()
            check_wins=1
        button_click= False
        flag += 1

    elif buttons["text"] == " " and button_click == False:
        buttons["text"] = "O"
        button_click = True
        win_str = check_win()
        if win_str == o_win:
            tkinter.messagebox.showinfo("Tic-Tac-Toe ","player O WINS")
            disable_buttons()
            check_wins=2
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")
    if flag == 9 and check_wins==None:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
        disable_buttons()

set_buttons()
tk.mainloop()
