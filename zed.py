import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()

root.geometry("1350x689+0+0")
root.attributes("-fullscreen", True)
root.title("Food Billing System")
root.configure(background='orange',padx = 5, pady = 5)

Values = [0,1,2,3,4,5,6,7,8,9,10]

foodsList = {'Footlong':30,'Halflong':15,'EggSandwich':15,'Burger':20,'VeggieBurger':25,
            'Hamburger':30,'Fries':15,'Palabok':40,'Spaghetti':40,'Carbonara':45}
foodsOM = dict()
foodVars = dict()

drinksList = {'Sprite':15,'Pepsi':10,'CokeZero':20,'MountainDew':15,'Royal':15,
              'CocaCola':15,'IcedTea':25,'HotCoffee':30,'ColdCoffee':30,'PineappleJuice':25}
drinksOM = dict()
drinkVars = dict()

def total():
    fullTotal = 0
    txtReceipt.config(state = NORMAL)
    txtReceipt.delete('1.0',END)
    txtReceipt.insert(END, "ITEM\t\t     COST\t          PIECES\t          TOTAL\n")
    txtReceipt.insert(END, "-"*89+"\n")
    for f in foodsList:
        itmTotal = foodsList[f] * foodVars[f].get()
        fullTotal += itmTotal
        if foodVars[f].get() > 0:
            txtReceipt.insert(END, "{0}\t\t     ₱{1}\t\t{2}\t₱{3}\n".format(f,foodsList[f], foodVars[f].get(), itmTotal))
    for d in drinksList:
        itmTotal = drinksList[d] * drinkVars[d].get()
        fullTotal += itmTotal
        if drinkVars[d].get() > 0:
            txtReceipt.insert(END, "{0}\t\t     ₱{1}\t\t{2}\t₱{3}\n".format(d,drinksList[d],drinkVars[d].get(), itmTotal))
    txtReceipt.insert(END, "-"*89+"\n")
    txtReceipt.insert(END, "FULL TOTAL:     ₱" + str(fullTotal))
    txtReceipt.config(state = DISABLED)

def iExit():
    qExit = tk.messagebox.askyesno("Zedric's Food System", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return

def reset():
    txtReceipt.config(state = NORMAL)
    txtReceipt.delete('1.0', END)
    txtReceipt.config(state = DISABLED)

    for f,d in zip(foodVars, drinkVars):
        foodVars[f].set(Values[0])
        drinkVars[d].set(Values[0])
        
Tops = Frame(root, bg = 'orange', bd = 13, pady = 5, relief = RIDGE)
Tops.pack(side = TOP, fill = X)

lblTitle=Label(Tops,font=('cooper black',35,'bold'),text="Zedric's Food System",
               bd=21,bg='black',fg='cornsilk',justify=CENTER)
lblTitle.pack(side = TOP, fill = X)

foodsFrame = Frame(root, bg = "orange", bd = 10, pady = 5, relief = RIDGE)
foodsFrame.pack(side = LEFT, fill = Y)

foodsLabel = Label(foodsFrame, text = 'Foods', font = ('cooper black',25,'bold')
                   ,width = 20)
foodsLabel.pack(side = TOP)

foodsNameFrame = Frame(foodsFrame, bg = 'gold', relief = SUNKEN,bd = 5)
foodsNameFrame.pack(side = LEFT, fill = BOTH, expand = TRUE)

foodsOMFrame = Frame(foodsFrame, bg = 'black',bd = 5)
foodsOMFrame.pack(side = RIGHT, fill = BOTH, expand = TRUE)

for f in foodsList:
    foodVars[f] = IntVar()
    foodName = Label(foodsNameFrame, text = f, font = ('cooper black', 14, 'bold'),width = 10, bg = 'orange')
    foodName.pack(expand = True, fill=X)
    foodsOM[f] = OptionMenu(foodsOMFrame, foodVars[f],*Values)
    foodsOM[f].config(font = ('cooper black',14,'bold'), bg = 'orange', activebackground ='gold')
    foodsOM[f].pack(expand = True)

drinksFrame = Frame(root, bg = "orange", bd = 10, pady = 5, relief = RIDGE)
drinksFrame.pack(side = LEFT, fill = Y)

drinksLabel = Label(drinksFrame, text = 'Drinks', font = ('cooper black',25,'bold')
                   ,width = 20)
drinksLabel.pack(side = TOP)

drinksNameFrame = Frame(drinksFrame, bg = 'gold', relief = SUNKEN,bd = 5)
drinksNameFrame.pack(side = LEFT, fill = BOTH, expand = TRUE)

drinksOMFrame = Frame(drinksFrame, bg = 'black',bd = 5)
drinksOMFrame.pack(side = RIGHT, fill = BOTH, expand = TRUE)

for d in drinksList:
    drinkVars[d] = IntVar()
    drinksName = Label(drinksNameFrame, text = d, font = ('cooper black', 14, 'bold'),width = 10, bg = 'orange')
    drinksName.pack(expand = True, fill=X)
    drinksOM[d] = OptionMenu(drinksOMFrame, drinkVars[d],*Values)
    drinksOM[d].config(font = ('cooper black',14,'bold'), bg = 'orange', activebackground ='gold')
    drinksOM[d].pack(expand = True)

receiptAndTotalFrame = Frame(root, bg = 'orange', bd = 10, pady = 5, relief = RIDGE)
receiptAndTotalFrame.pack(side = LEFT, fill = BOTH, expand = TRUE)

receiptFrame = Frame(receiptAndTotalFrame, bg = 'yellow', bd = 5, relief = SUNKEN)
receiptFrame.pack(side = TOP, fill = BOTH, expand = TRUE)

txtReceipt=Text(receiptFrame,width=52,height=21,bg='white',bd=4,font=('arial',12,'bold'),
                state = DISABLED)
txtReceipt.pack(side = BOTTOM)

buttonsFrame = Frame(receiptAndTotalFrame, bg = 'black', bd = 5)
buttonsFrame.pack(side = BOTTOM, fill = BOTH, expand = TRUE)

totalButton = Button(buttonsFrame, text = "Total", bg = 'orange',bd = 7 , font=('arial',14,'bold'),
                     activebackground = "yellow", height = 1, command = total)
totalButton.pack(side = LEFT, fill = BOTH, expand = TRUE)

resetButton = Button(buttonsFrame, text = "Reset", bg = 'orange',bd = 7 , font=('arial',14,'bold'),
                     activebackground = "yellow", height = 1, command = reset)
resetButton.pack(side = LEFT, fill = BOTH, expand = TRUE)
 
exitButton = Button(buttonsFrame, text = "Exit", bg = 'orange',bd = 7 , font=('arial',14,'bold'),
                     activebackground = "yellow", height = 1, command = lambda: iExit()).pack(side = RIGHT, fill = BOTH, expand = True)

root.mainloop()
