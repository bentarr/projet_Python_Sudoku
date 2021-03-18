from tkinter import * #import de l'interface graphique

monSudoku = Tk()

a = [[6,3,2,5,4,8,1,9,7], #initialisation de la matrice
    [8,7,9,6,1,3,5,2,4],
    [5,4,1,9,2,7,3,6,8],
    [2,5,4,3,7,6,8,1,9],
    [3,6,8,2,9,1,7,4,5],
    [1,9,7,8,5,4,2,3,6],
    [4,8,3,7,6,2,9,5,1],
    [7,1,5,4,3,9,6,8,2],
    [9,2,6,1,8,5,4,7,3]]

rows = [] #Mise en place de la matrice sur l'interface graphique
for i in range(len(a)):
    cols = []
    for j in range(len(a[i])):
        e = Entry(relief=GROOVE)
        e.grid(row=i, column=j, sticky=NSEW)
        e.insert(END, a[i][j])
        cols.append(e)
    rows.append(cols)

monBouton = Button(monSudoku, text ="Click ME")
monBouton.pack()


monSudoku.mainloop()