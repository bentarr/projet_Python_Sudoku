from tkinter import *

test = Tk()

sudoku1 = open("sudoku1.txt", "r")
str1 = sudoku1.read()
x = str1.split(",")


rows = [] #Mise en place de la matrice sur l'interface graphique
for i in range(len(x)):
    j = 0
    cols = []
    while j < 9:
        e = Entry(relief=GROOVE, bg="lightblue")
        e.grid(row=i, column=j, sticky=NSEW)
        e.insert(END, x[i][j])
        cols.append(e)
rows.append(cols)

print(rows)
        

mainloop() 