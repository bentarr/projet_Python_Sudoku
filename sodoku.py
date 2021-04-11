from tkinter import *

monSudoku = Tk()

with open("sudoku1.txt") as file_in: #Ouverture d'un fichier et affichage d'un sudoku partiellement résolu
    sudokuUnsolved = []
    lines = []
    sudokus = file_in.read()
    separate_arrays = sudokus.split(";")
    array_without_break = separate_arrays[0].split("\n")
    while '' in array_without_break:
        array_without_break.remove('')
    for line in array_without_break:
        row = line.split(" ")
        sudokuUnsolved.append(row)

rows = [] #Mise en place de la matrice sur l'interface graphique
for i in range(len(sudokuUnsolved)):
    cols = []
    for j in range(len(sudokuUnsolved[i])):
        e = Entry(relief=GROOVE, bg="lightblue")
        e.grid(row=i, column=j, sticky=NSEW)
        e.insert(END, sudokuUnsolved[i][j])
        cols.append(e)
    rows.append(cols)

def VerifSolution() : #Fonction de vérification de la matrice depuis l'ouverture d'un fichier
    with open("sudoku1.txt") as file_in:
        sudokuSolved = []
        lines = []
        sudokus = file_in.read()
        separate_arrays = sudokus.split(";")
        array_without_break = separate_arrays[1].split("\n")
        while '' in array_without_break:
            array_without_break.remove('')
        for line in array_without_break:
            row = line.split(" ")
            sudokuSolved.append(row)
    check = 0
    for i in range(len(sudokuSolved)):
        for j in range(len(sudokuSolved[i])):
            if (str(sudokuSolved[i][j]) != rows[i][j].get()):
                check += check + 1
                rows[i][j].config(relief=GROOVE, bg="red")
            else:
                rows[i][j].config(relief=GROOVE, bg="green")
    if(check != 0):
       messagebox.showinfo("Résultat de la comparaison", "C'est perdu, essaye encore !")
    else:
        messagebox.showinfo("Résultat de la comparaison", "C'est gagné, félicitations !")    


monBouton = Button(monSudoku, text ="Vérifier le sudoku", command = lambda: VerifSolution())
monBouton.grid(row = 1, column=10 )
mainloop() 