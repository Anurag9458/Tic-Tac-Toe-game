from tkinter import *
from tkinter import messagebox
import random
root=Tk()

root.title("This is Tic Tac Toe")
count=0
clk=True
winner=None
mode=None
flat=0
cb=0
xa=" "
xb=" "


def click(button):

    global count,clk,winner,mode,flat,cb,bx,bo,xa,xb


    #vs friend mode     
    if mode=="f":
        

        if button["text"]=="X":
            xa="X"
            xb="O"
            bx.config(bg="red")
            bx.config(state="disabled")
            bo.config(state="disabled")
            messagebox.showinfo("Tic Tac Toe",f"Player 1- {xa} // Player 2- {xb} \n Player 1's Turn")

        elif button["text"]=="O":
            xb="X"
            xa="O"
            bo.config(bg="red")
            bx.config(state="disabled")
            bo.config(state="disabled")
            messagebox.showinfo("Tic Tac Toe",f"Player 1- {xa} // Player 2- {xb} \n Player 1's Turn")
        
        if xa == " " and button["text"]!="Reset":
            messagebox.showerror("Tic Tac Toe","Please choose X or O first")
        else:    
            if button["text"]=="Reset"  :
                reset()
            elif button["text"]==" " and clk==True :
                button["text"]=xa
                count =count + 1
                clk=False
            elif button["text"]==" " and clk==False :
                button["text"]=xb
                count = count + 1
                clk=True
            elif button["text"]!="Vs AI" and button["text"]!="Vs Friend" and count!=0:
                messagebox.showerror("Tic Tac Toe","Already selected choose another")
        
        

    # vs ai mode
    elif mode=="ai":
        
        list=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
        
        
        for i in range(0,9):
            if list[i]==button:
                cb=i


        cb=cb+1

        if button["text"]=="Reset":
            reset()
        elif button["text"]==" ":
            button["text"]=xb
            flat=1
            count =count + 1
        else:
            if button["text"]!="Vs AI" and button["text"]!="Vs Friend": 
                flat=0
                messagebox.showerror("Tic Tac Toe","Already selected choose another")
        
        
        


        check_if_win()
        if count==9:
            messagebox.showinfo("Tic Tac Toe",f"It's a Tiee")
        

        
        if cb==1 and flat==1:
            
            

            c=count
            l=[b2,b4]
            if winner!="X" and winner!="O":
                c=count
                while c==count and c!=9 :
                    ran=random.choice(l)
                    if ran["text"]==" ":
                        ran["text"]=xa
                        count=count+1

                    else:
                        if winner!="X" and winner!="O":
                            c=count
                        while c==count and c!=9:
                            ran=random.choice(list)
                            if ran["text"]==" ":
                                ran["text"]=xa
                                count=count+1 

        if cb==2 and flat==1:
            c=count
            l=[b3,b6]
            if winner!="X" and winner!="O":
                c=count
                while c==count and c!=9:
                    ran=random.choice(l)
                    if ran["text"]==" ":
                        ran["text"]=xa
                        count=count+1

                    else:
                        if winner!="X" and winner!="O":
                            c=count
                        while c==count and c!=9:
                            ran=random.choice(list)
                            if ran["text"]==" ":
                                ran["text"]=xa
                                count=count+1 

        if cb==3 and flat==1:
            c=count
            l=[b2,b6]
            if winner!="X" and winner!="O":
                c=count
                while c==count and c!=9 :
                    ran=random.choice(l)
                    if ran["text"]==" ":
                        ran["text"]=xa
                        count=count+1

                    else:
                        if winner!="X" and winner!="O":
                            c=count
                        while c==count and c!=9:
                            ran=random.choice(list)
                            if ran["text"]==" ":
                                ran["text"]=xa
                                count=count+1 

        if cb==4 and flat==1:
            c=count
            l=[b1,b7]
            if winner!="X" and winner!="O":
                c=count
                while c==count and c!=9:
                    ran=random.choice(l)
                    if ran["text"]==" ":
                        ran["text"]=xa
                        count=count+1

                    else:
                        if winner!="X" and winner!="O":
                            c=count
                        while c==count and c!=9:
                            ran=random.choice(list)
                            if ran["text"]==" ":
                                ran["text"]=xa
                                count=count+1 

        
        if cb==6 and flat==1:
            c=count
            l=[b8,b9]
            if winner!="X" and winner!="O":
                c=count
                while c==count and c!=9:
                    ran=random.choice(l)
                    if ran["text"]==" ":
                        ran["text"]=xa
                        count=count+1

                    else:
                        if winner!="X" and winner!="O":
                            c=count
                        while c==count and c!=9:
                            ran=random.choice(list)
                            if ran["text"]==" ":
                                ran["text"]=xa
                                count=count+1 

        if cb==7 and flat==1:
            c=count
            l=[b8,b4]
            if winner!="X" and winner!="O":
                c=count
                while c==count and c!=9:
                    ran=random.choice(l)
                    if ran["text"]==" ":
                        ran["text"]=xa
                        count=count+1 
            
                    else:
                        if winner!="X" and winner!="O":
                            c=count
                        while c==count and c!=9:
                            ran=random.choice(list)
                            if ran["text"]==" ":
                                ran["text"]=xa
                                count=count+1

        if cb==8 and flat==1:
            c=count
            l=[b7,b9]
            if winner!="X" and winner!="O":
                c=count
                while c==count and c!=9:
                    ran=random.choice(l)
                    if ran["text"]==" ":
                        ran["text"]=xa
                        count=count+1 
            
                    else:
                        if winner!="X" and winner!="O":
                            c=count
                        while c==count and c!=9:
                            ran=random.choice(list)
                            if ran["text"]==" ":
                                ran["text"]=xa
                                count=count+1
        if cb==9 and flat==1:
            c=count
            l=[b6,b8]
            if winner!="X" and winner!="O":
                c=count
                while c==count and c!=9:
                    ran=random.choice(l)
                    if ran["text"]==" ":
                        ran["text"]=xa
                        count=count+1 
            
                    else:
                        if winner!="X" and winner!="O":
                            c=count
                        while c==count and c!=9:
                            ran=random.choice(list)
                            if ran["text"]==" ":
                                ran["text"]=xa
                                count=count+1

        


        
        
    
    if button["text"]=="Reset":
        b02.config(bg="red")
        reset()



    if button["text"]=="Vs AI":
        reset()
        l=[bx,bo]
        bchose=random.choice(l)
        bchose.config(bg="red")
        xa=bchose["text"]
        messagebox.showinfo("tic tac toe",f"Computer has choosen  {xa}")
        
        if xa=="X":
            xb="O"
        else:
            xb="X"
        
        messagebox.showinfo("Tic Tac Toe",f"Computer- {xa} // User- {xb} \n  Compuetr's Turn")
        b0.config(bg="yellow")
        b5.config(text=xa)
        b0.config(state=DISABLED)
        bx.config(state=DISABLED)
        bo.config(state=DISABLED)
        count=count+1
        mode="ai"
        
    elif button["text"]=="Vs Friend":
        reset()
        b01.config(bg="pink")
        b01.config(state=DISABLED)
        mode="f"
        messagebox.showinfo("Tic Tac Toe",f" player 1 choose X or O")

    if mode !="f" and mode !="ai" and button["text"]!="Reset":
         reset()
         messagebox.showinfo("Tic Tac Toe ","Please select mode first")


    
    
    check_if_win()
    if winner=="X" or winner=="O":
        messagebox.showinfo("Tic Tac Toe",f"{winner} is Winner Congratulationssss")
        reset()
    elif count == 9:
        messagebox.showinfo("Tic Tac Toe","It's a Tieeee ")
        reset()
        


    
    

def check_if_win():
    global winner,count
    if b1["text"]==b2["text"]==b3["text"]!=" ":
        winner=b1["text"]
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
    elif b4["text"]==b5["text"]==b6["text"]!=" ":
        winner=b4["text"]
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
    elif b7["text"]==b8["text"]==b9["text"]!=" ":
        winner=b7["text"]
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
    elif b1["text"]==b4["text"]==b7["text"]!=" ":
        winner=b1["text"]
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
    elif b2["text"]==b5["text"]==b8["text"]!=" ":
        winner=b2["text"]
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
    elif b3["text"]==b6["text"]==b9["text"]!=" ":
        winner=b3["text"]
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
    elif b1["text"]==b5["text"]==b9["text"]!=" ":
        winner=b1["text"]
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
    elif b3["text"]==b5["text"]==b7["text"]!=" ":
        winner=b3["text"]
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
    
   
    
    








def reset():
    global b0,b01,b02,b1,b2,b3,b4,b5,b6,b7,b8,b9,bx,bo
    global count,clk,winner,mode,flat,cb,xa,xb
    count=0
    clk=True
    winner=None
    mode=None
    flat=0
    cb=0
    xa=" "
    xb=" "
    bch=Button(text="Choose",font=("arial",30),height=1,width=7,bg="white")
    bx=Button(text="X",font=("arial",30),command=lambda :click(bx),height=1,width=7,bg="white")
    bo=Button(text="O",font=("arial",30),command=lambda :click(bo),height=1,width=7,bg="white")
    b0=Button(text="Vs AI",font=("arial",30),command=lambda :click(b0),height=1,width=7,bg="white")
    b01=Button(text="Vs Friend",font=("arial",30),command=lambda :click(b01),height=1,width=7,bg="white")
    b02=Button(text="Reset",font=("arial",30),command=lambda :click(b02),height=1,width=7,bg="white")
    b1=Button(text=" ",font=("arial",40),command=lambda :click(b1),height=3,width=7,bg="white")
    b2=Button(text=" ",font=("arial",40),command=lambda :click(b2),height=3,width=7,bg="white")
    b3=Button(text=" ",font=("arial",40),command=lambda :click(b3),height=3,width=7,bg="white")
    b4=Button(text=" ",font=("arial",40),command=lambda :click(b4),height=3,width=7,bg="white")
    b5=Button(text=" ",font=("arial",40),command=lambda :click(b5),height=3,width=7,bg="white")
    b6=Button(text=" ",font=("arial",40),command=lambda :click(b6),height=3,width=7,bg="white")
    b7=Button(text=" ",font=("arial",40),command=lambda :click(b7),height=3,width=7,bg="white")
    b8=Button(text=" ",font=("arial",40),command=lambda :click(b8),height=3,width=7,bg="white")
    b9=Button(text=" ",font=("arial",40),command=lambda :click(b9),height=3,width=7,bg="white")
    b0.grid(row=0,column=0)
    b01.grid(row=1,column=0)
    b02.grid(row=2,column=0)
    b1.grid(row=0,column=1)
    b2.grid(row=0,column=2)
    b3.grid(row=0,column=3)
    b4.grid(row=1,column=1)
    b5.grid(row=1,column=2)
    b6.grid(row=1,column=3)
    b7.grid(row=2,column=1)
    b8.grid(row=2,column=2)
    b9.grid(row=2,column=3)
    bch.grid(row=3,column=0)
    bx.grid(row=3,column=1,columnspan=2)
    bo.grid(row=3,column=2,columnspan=2)
    bch.config(state="disabled")
    

reset()

root.geometry("850x750")
root.config(bg="gray")
root.resizable(width=False,height=False)

root.mainloop()
