from io import open
import time
import re
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from tkinter import * 


#-------------------Functions-------------------------------------------------------------
def askNumber():
    ''' 
    This function request for the user to enter a txt file.
    Then reads that file and tells us the number of animals in the file
    '''
    file = filedialog.askopenfilename(title= "Open")
    corral=set()
    with open(file, "r") as f:
        for line in f:
            corral.add(int(line))
        messagebox.showinfo(file,f'The number of animals in this stockyard is: {len(corral)}')

def animalRelease():
    '''
    This function compares two livestock lots in a .txt file and tells us the number of animals in both lots.
    Then we can create a file by subtracting the animals from the first in the second file.
    '''
    file = filedialog.askopenfilename(title= "Open")
    release=set()
    with open(file, "r") as f:
        for line in f:
            release.add(int(line))
        
        messagebox.showinfo(file,f'The number of animals released is: {len(release)}')
        
        messagebox.showinfo(file,'Now you have to enter the stockyard to compare')
        stockFile = filedialog.askopenfilename(title= "Open")
        
        stockyardSet=set()
        
        with open(stockFile, "r") as f:
            for line in f:
                stockyardSet.add(int(line))
            
            messagebox.showinfo(file, f'The number of animals in this stockyard is: {len(stockyardSet)}')

        final_set = release & stockyardSet
        messagebox.showinfo('Released', f"The number of animals to be released that were in this stockyard is: {final_set}\n And the quantity of animals is: {len(final_set)}")
        
        Label(miFrame, text=final_set, fg="green").grid(row=2, column=0, sticky="w", padx=3, pady=3)

        question1 = messagebox.askquestion('New File', 'Do you want to create a new file with the animals released?')
        if question1 == 'yes':
            animales_quedan = stockyardSet - release
            animales_quedan = str(animales_quedan)
            pattern = re.findall(r'\d{8,}', animales_quedan)
        
            archivo = open(stockFile,"w")
            for line in pattern:
                archivo.write(line + '\n')
            
        else:
            salir_aplicacion()

def lotsCompare():
    file = filedialog.askopenfilename(title= "Open")
    release=set()
    with open(file, "r") as f:
        for line in f:
            release.add(int(line))
        
        messagebox.showinfo(file,f'The number of animals in stockyard 1 is: {len(release)}')
        
        stockFile = filedialog.askopenfilename(title= "Open")
        
        stockyardSet=set()
        
        with open(stockFile, "r") as f:
            for line in f:
                stockyardSet.add(int(line))
            
            messagebox.showinfo(file, f'The number of animals in stockyard 2 is: {len(stockyardSet)}')

        final_set = release & stockyardSet
        messagebox.showinfo('Released', f"The number of animals in both stockyards is: {final_set}\n And the quantity of animals is: {len(final_set)}")
        
        Label(miFrame, text=final_set, fg="green").grid(row=2, column=0, sticky="w", padx=3, pady=3)
        # Variable para que salga en el entry
        global animales
        animales.set(len(final_set))
        Entry(miFrame, textvariable=animales).grid(row=2, column=1)

def salir_aplicacion():
    '''
    This function enable the user to get out the application
    '''
    salir = messagebox.askquestion("Exit", "¿Do you want to exit the application?")
    if salir == "yes":
        root.destroy()

#---------------------------------------------------------------------------------------------
# Root creation and configuration
root = Tk()

root.title('Caravanas')
root.resizable(1,1)
root.iconbitmap('caravana.ico')
root.config(background="chocolate1")

barMenu=Menu(root)
root.config(menu=barMenu)

#-------------------------------------------------------------------------------------------------------
# Frame cration and configuration
miFrame=Frame()
miFrame.pack()
miFrame.config(bg="chocolate1", width=650, height=650)

#----------------------------------------------------------
# Variable global
animales = StringVar()


#----------------------------------------------------------------------------------------------
# First menu bar
optionIndex=Menu(barMenu, tearoff=0)

barMenu.add_cascade(label="Index", menu=optionIndex)

optionIndex.add_command(label="Ask number", command=askNumber)
optionIndex.add_separator()
optionIndex.add_command(label="Salir", command=salir_aplicacion)

#--------------------------------------------------------------------------------------------------------
# Menu New animal release
optionRelease=Menu(barMenu, tearoff=0)
barMenu.add_cascade(label="Release", menu=optionRelease)

optionRelease.add_command(label="File release", command=animalRelease)
optionRelease.add_separator()
optionRelease.add_command(label="File compare", command=lotsCompare)

#---------------------------------------------------------------------------------------------------------
# Labels for the enter the File name
fileName = StringVar()

Label(miFrame, text="File name", fg="green").grid(row=0, column=0, sticky="w")
cuadroTexto1=Entry(miFrame, textvariable=fileName).grid(row=0, column=1)

root.mainloop()