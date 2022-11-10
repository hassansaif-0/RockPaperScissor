from tkinter import *
from PIL import Image,ImageTk
from random import randint



root=Tk()
root.title("RockPaperScissor")
root.configure(background="Red")

def updatepromp(val):
    promp['text']=val

def updateplayerscore():
    score=int(playerscore['text'])
    score=score+1
    playerscore['text']=str(score)

def updatecompscore():
    score=int(compscore['text'])
    score=score+1
    compscore['text']=str(score)

def winner(player,comp):
    if player==comp:
        updatepromp("Game Tie")
    elif player=="rock":
        if comp=="paper":
            updatepromp("Computer Won")
            updatecompscore()
        else:
            updatepromp("You Won")
            updateplayerscore()
    elif player=="paper":
        if comp=="scissor":
            updatepromp("Computer Won")
            updatecompscore()
        else:
            updatepromp("You Won")
            updateplayerscore()
    elif player=="scissor":
        if comp=="rock":
            updatepromp("Computer Won")
            updatecompscore()
        else:
            updatepromp("You Won")
            updateplayerscore()




"""Loading the images for our canvas"""
rock_img_player=ImageTk.PhotoImage(Image.open("rock_player.png"))
paper_img_payer=ImageTk.PhotoImage(Image.open("paper_player.png"))
scissor_img_player=ImageTk.PhotoImage(Image.open("scissor_player.png"))
rock_img_comp=ImageTk.PhotoImage(Image.open("rock_comp.png"))
paper_img_comp=ImageTk.PhotoImage(Image.open("paper_comp.png"))
scissor_img_comp=ImageTk.PhotoImage(Image.open("scissor_comp.png"))

#Putting the labels for identity

userinfo=Label(root,font=60,text="Player")
compinfo=Label(root,font=60,text="Computer")



userinfo.grid(row=0,column=1)
compinfo.grid(row=0,column=3)


#prompts




#Setting images on canvas
userlabel=Label(root,image=scissor_img_player,bg="Red")
complabel=Label(root,image=scissor_img_comp,bg="Red")



userlabel.grid(row=1,column=0)
complabel.grid(row=1,column=4)




"""Update Function"""

def stateupdate(state):
    choice = ["rock", "paper", "scissor"]

    compchoice = choice[randint(0, 2)]

    if compchoice == "rock":
        complabel.configure(image=rock_img_comp)
    elif compchoice == "paper":
        complabel.configure(image=paper_img_comp)
    elif compchoice == "scissor":
        complabel.configure(image=scissor_img_comp)

    if state=="rock":
        userlabel.configure(image=rock_img_player)
    elif state=="paper":
        userlabel.configure(image=paper_img_payer)
    elif state=="scissor":
        userlabel.configure(image=scissor_img_player)
    winner(state,compchoice)

"""Computer Selections"""



#setting up score
playerscore=Label(root,text=0,font=150,bg="Red",fg="white")
compscore=Label(root,text=0,font=150,bg="Red",fg="white")

playerscore.grid(row=1,column=1)
compscore.grid(row=1,column=3)


#Setting Up Buttons

rock=Button(root,width=30,height=3,text="ROCK",bg="Blue",fg="White",command=lambda:stateupdate("rock"))
paper=Button(root,width=30,height=3,text="PAPER",bg="Orange",fg="White",command=lambda:stateupdate("paper"))
scissor=Button(root,width=30,height=3,text="SCISSOR",bg="Green",fg="White",command=lambda:stateupdate("scissor"))

rock.grid(rows=2,column=1)
paper.grid(row=2,column=2)
scissor.grid(row=2,column=3)

#prompts
promp=Label(root,font=50,text="Lets start")
promp.grid(row=5,column=2)






#Setting the entry point
root.mainloop()