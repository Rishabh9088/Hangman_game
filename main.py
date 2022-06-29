import tkinter
from tkinter import messagebox
from tkinter import *
import random
from PIL import ImageTk, Image
import words
import pygame

tab = Tk()
tab.title("HANGMAN GAME")
tab.geometry("1680x790")
width1= tab.winfo_screenwidth()
height1= tab.winfo_screenheight()
pygame.mixer.init()
bgimg= ImageTk.PhotoImage(Image.open("hang2.png"))
bg_label=Label(tab, image=bgimg)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)
pygame.mixer.music.load("welcome.mp3")
pygame.mixer.music.play(loops=0)
flist = []
undscr = []
count2 = 5
img = 2
word = ""

# Get letter and logic function
def get_letter():
    le = lett.get()
    lett.set("")
    global flist
    x = 0
    if (le == ""):
        nthenter()
    # print(flist)
    count = -1
    global count2
    for i in word:
        count += 1
        if (i == le):
            frg()
            flist[count] = le
            l3.config(text=flist)
            x += 1
    if (le != ""):
        if (x == 0):
            fwg()
            count2 -= 1
            l4.config(text="No. of tries left = " + str(count2 + 1))
            global img
            if (img == 2):
                l2.config(image=img2)
            elif (img == 3):
                l2.config(image=img3)
            elif (img == 4):
                l2.config(image=img4)
            elif (img == 5):
                l2.config(image=img5)
            elif (img == 6):
                l2.config(image=img6)
            elif (img == 7):
                l2.config(image=img7)
            img += 1
    if ('_' not in flist):
        wonmsg()
    elif (count2 == -1):
        los_msg()


lett = StringVar()

# nothing entered function
def nthenter():
    pygame.mixer.music.load("nthenter.mp3")
    pygame.mixer.music.play(loops=0)
    tkinter.messagebox.showerror("warning", "Nothing entered. Please enter any letter")

# for right guess function
def frg():
    l6.config(text="Wow! You guessed it right...")
    pygame.mixer.music.load("forrightguess.mp3")
    pygame.mixer.music.play(loops=0)

# For wrong guess function
def fwg():
    l6.config(text="Oops! Your guess is wrong...")
    if (count2 != 0):
        pygame.mixer.music.load("forwronguess.mp3")
        pygame.mixer.music.play(loops=0)

# Win message function
def wonmsg():
    global count2
    global img
    pygame.mixer.music.load("youwon.mp3")
    pygame.mixer.music.play(loops=0)
    tkinter.messagebox.showinfo("Result", "You Won")
    res = tkinter.messagebox.askquestion("Notification","Do you want to play again ?")
    if(res=="yes"):
        l3.config(text="")
        count2=5
        img=2
        flist.clear()
        l6.config(text="")
        main()
    else:
        tab.destroy()

#Loss message function
def los_msg():
    global count2
    global img
    pygame.mixer.music.load("youloose.mp3")
    pygame.mixer.music.play(loops=0)
    tkinter.messagebox.showinfo("Result", "You loose the word was " + word)
    res = tkinter.messagebox.askquestion("Notification", "Do you want to play again ?")
    if (res == "yes"):
        l3.config(text="")
        flist.clear()
        count2=5
        img=2
        l6.config(text="")
        main()
    else:
        tab.destroy()

# main function
def main():
    global word,flist,img1,img2,img3,img4,img5,img6,img7,l,l2,l3,l4,l5,l6
    undscr=[]
    word = random.choice(words.word_list)
    for a in word:
        flist += '_'
    for s in word:
        undscr += '_'
    print(word)

    img1 = ImageTk.PhotoImage(Image.open("h0.png").resize((400,350)))
    img2 = ImageTk.PhotoImage(Image.open("h1.png").resize((400,350)))
    img3 = ImageTk.PhotoImage(Image.open("h2.png").resize((400,350)))
    img4 = ImageTk.PhotoImage(Image.open("h3.png").resize((400,350)))
    img5 = ImageTk.PhotoImage(Image.open("h4.png").resize((400,350)))
    img6 = ImageTk.PhotoImage(Image.open("h5.png").resize((400,350)))
    img7 = ImageTk.PhotoImage(Image.open("h6.png").resize((400,350)))
    l = Label(tab, text="Enter a letter -:", font=("",30))
    l.place(x=600, y=453)
    l2 = Label( image=img1)
    l2.place(x=100, y=300)
    l3 = Label(tab, text=undscr, font=("",30))
    l3.place(x=600, y=650)
    l4 = Label(tab, text="No. of tries left = " + str(count2 + 1), font=("",30), fg="dark blue")
    l4.place(x=600, y=300)
    l6 = Label(tab, text="", font=("",20), bg="light blue",fg="dark blue")
    l6.place(x=600, y=550)
    entry = Entry(tab, textvariable=lett,font=("",18)).place(x=890, y=460)
    but = Button(tab, text="Submit", command=get_letter,font=("",18),activebackground="dark blue",activeforeground="white").place(x=1180, y=450)
main()
tab.mainloop()

