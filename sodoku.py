from tkinter import * #import de l'interface graphique
from tkinter import messagebox

monSudoku = Tk()

matriceUnsolved = [[0,0,0,2,0,0,4,0,0,],
                  [0,0,7,0,0,3,0,1,2,],
                  [0,2,1,4,0,0,0,6,3,],
                  [7,0,0,0,0,0,8,5,1,],
                  [8,0,4,0,0,0,3,0,6,],
                  [1,3,2,0,0,0,0,0,4,],
                  [5,1,0,0,0,4,2,9,0,],
                  [6,4,0,9,0,0,1,0,0,],
                  [0,0,9,0,0,5,0,0,1,]]
rows = [] #Mise en place de la matrice sur l'interface graphique
for i in range(len(matriceUnsolved)):
    cols = []
    for j in range(len(matriceUnsolved[i])):
        e = Entry(relief=GROOVE)
        e.grid(row=i, column=j, sticky=NSEW)
        e.insert(END, matriceUnsolved[i][j])
        cols.append(e)
    rows.append(cols)

def VerifSolution() : #Fonction de vérification de la matrice
    matriceSolved = [[3,6,5,2,7,1,4,8,9,],
                    [4,8,7,6,9,3,5,1,2,],
                    [9,2,1,4,5,8,7,6,3,],
                    [7,9,6,3,4,2,8,5,1,],
                    [8,5,4,7,1,9,3,2,6,],
                    [1,3,2,5,8,6,9,7,4,],
                    [5,1,3,8,6,4,2,9,7,],
                    [6,4,8,9,2,7,1,3,5,],
                    [2,7,9,1,3,5,6,4,8,]]
    check = 0
    for i in range(len(matriceSolved)):
        for j in range(len(matriceSolved[i])):
            if (str(matriceSolved[i][j]) != str(rows[i][j].get())):
                check += check + 1
    print(check)
    if(check != 0):
        messagebox.showinfo("Résultat de la comparaison", "C'est perdu, essaye encore !")
    else:
        messagebox.showinfo("Résultat de la comparaison", "C'est gagné, félicitations !")       


monBouton = Button(monSudoku, text ="Vérifier le sudoku", command = lambda: VerifSolution())
monBouton.grid(row = 1, column=10 )


monSudoku.mainloop()