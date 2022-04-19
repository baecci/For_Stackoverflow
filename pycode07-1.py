'''''''''''''''''''''''''''''''''''''''''''''''''''
Program to choose your favorite animal and view pictures

'''''''''''''''''''''''''''''''''''''''''''''''''''
##error## can't print a animal picture ##

from tkinter import* 

#function declaration

def vote_animal():
    button1 = Button(window, text = "Picture", font = (5), fg = "black", command = show_animal)
    button1.place(x = xPos, y = yPos)

def show_animal():
    if var.get() == 1:
        photo = PhotoImage(file = "C:/picture/"+animalList[var.get()-1])
        label2.configure(image = photo)
        label2.pack()
        
    elif var.get() == 2:
        photo = PhotoImage(file = "C:/picture/"+animalList[var.get()-1])
        label2.configure(image = photo)
        label2.pack()
        
    else :
        photo = PhotoImage(file = "C:/picture/"+animalList[var.get()-1])
        label2.configure(image = photo)
        label2.pack()

#global variable declaration
        
animalList=["dog.gif", "cat.gif", "rabbit.gif"]
xPos, yPos = 270, 120

#main code

if __name__=="__main__":
    window = Tk()
    window.title("Vote for animal")
    window.geometry("600x500")

    label1 = Label(window, text = "Choose your favorite animal", font = (25), fg = "blue")
    label1.pack()

    var = IntVar()
    dogRB = Radiobutton(window, text = "Dog", variable = var, value = 1, command = vote_animal) 
    catRB = Radiobutton(window, text = "Cat", variable = var, value = 2, command = vote_animal)
    rabbitRB = Radiobutton(window, text = "Rabbit", variable = var, value = 3, command = vote_animal)

    dogRB.pack()
    catRB.pack()
    rabbitRB.pack()

    photo = PhotoImage(file = "C:/Users/qorld/Desktop/PythonWorkspace/picture/"+animalList[var.get()-1])
    label2 = Label(window, image = photo)
    
    window.mainloop()
    
