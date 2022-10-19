# Filename: PasswordGen.py
# Created Date: 10/15/2022
# Author: Clint Kline
# Purpose: generate a password and store it along with the name of the website the account is for and a username in a txt file. 
# creds = credentials
# texbox = entry = textbox

# !!! IMPORTS >>---------------------------------------------------------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk
import tkinter as tk
import random
import string
from tkinter.filedialog import askopenfilename, asksaveasfile
import sv_ttk


# ??? PROGRAM >>-------------------------------------------------------------------------------------------------------------------------------------------------


# !!! FUNCTIONS >>---------------------------------------------------------------------------------------------------------------------------------

# --------------------------------

def createNew(): # function: purpose: create a new file to store creds in
    dialog = Tk() # variable: type:<class 'tkinter.Tk'>: createa a file dialog object
    dialog.withdraw()  # hides the weird tiny tkinter window
    dialog.attributes('-topmost', 1) # make sure the dialog window pops up in front of everything else
    files = [('All Files', '*.*'),  # variable: type:list: determines which filetypes the file can be saved as
            #  ('Python Files', '*.py'), # python? maybe??
            ('Text Document', '*.txt')] # definitely text files, actually only text files. 
    textfile = asksaveasfile(filetypes = files, defaultextension = '.txt') # variable: type:<class '_io.TextIOWrapper'>: show the file dialog and return the path of the selected folder
    textfile = textfile.name # overwrite the 'textfile' variable so it contains only the name of the _io.TextIOWrapper object
    filepathLabel2 = tk.Label(master=fileframe, text=textfile, wraplength=350) # variable: type:tkinter.label: 
    filepathLabel2.grid(row = 3, column = 0, padx = (40, 0), pady = 2) # positions the filepath label
    global FilePath # instantiates a global variable to store text from the filepath label
    FilePath = filepathLabel2.cget('text') # variable: type:_tkinter.Tcl_Obj: stores the text from the filepath label in the filepath
    
# --------------------------------

def chooseExisting(): # function: purpose: choose an existing file to store creds in
    dialog = Tk() # variable: type:<class 'tkinter.Tk'>: creates a file dialog object
    dialog.withdraw()  # hides the little tkinter window
    dialog.attributes('-topmost', 1) # make sure the dialog window pops up in front of everything else
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    filepathLabel2 = tk.Label(master=fileframe, text=filename, wraplength=350) # variable: type:tkinter.label: creates a label object to display the chosen file
    filepathLabel2.grid(row = 3, column = 0, padx = (40, 0), pady = 2) # positions the filepath label
    global FilePath # instantiates a global variable to store text from the filepath label
    FilePath = filepathLabel2.cget('text') # variable: type:_tkinter.Tcl_Obj: stores the text from the filepath label

# --------------------------------

def generatePwd(): # function: purpose: generate a secure password
    pwd = ''.join(random.choice(string.ascii_letters + string.punctuation + string.digits) for _ in range(12)) # variable: type:String: creates a variable to store the generated password
    return pwd # returns the password to the calling script
    
# --------------------------------

def getweb(): # function: purpose: read the website label, store it in a variable and return the value to the calling script
    webDirect = webentry.get() # variable: type:StringVar: stores the website text in a variable
    webvar.set("") # clears the webvar variable 
    return webDirect # returns the value of the webDirect variable to the calling script
    
# --------------------------------

def getun(): # function: purpose: read the text in the UN textbox, store its value in a variable and return the value to the calling script
    unDirect = unentry.get() # variable: type:StringVar: stores the UN text in a variable
    unvar.set("") # clears the unvar variable
    return unDirect # returns the value of the unDirect variable to the calling script

# --------------------------------

def getpwd(): # function: purpose: read the pwd label, store its value in a variable and return the value to the calling script
    pwdDirect = pwdentry.cget('text') # variable: type:_tkinter.Tcl_Obj: stores the text from the password label 
    pwdvar.set("") # clears the pwdvar variable
    return pwdDirect # returns the value of the pwdDirect variable to the calling script

# --------------------------------

def submit():      
    webDirect = getweb() # variable: type:StringVar: calls the getweb function and stores the returned value
    unDirect = getun() # variable: type:StringVar: calls the getun function and stores the returned value
    pwdDirect = getpwd() # variable: type:StringVar: calls the getpwd function and stores the returned value
    entryContent = [webDirect, unDirect, pwdDirect] # variable: type:list: consolidates the above variables into a single list variable
    
    file1 = open(str(FilePath), "a")  # variable: type:<class '_io.TextIOWrapper'>: open the selected file in append mode
    
    file1.write('\nAccount: ' + entryContent[0]) # writes the account text to the selected text file
    file1.write('\nUN: ' + entryContent[1]) # writes the username text 
    file1.write('\nPW: ' + entryContent[2]) # writes the password text
    file1.write('\n----------------------------------------------') # writes a divider after each set of submitted credentials
    file1.close() # close the file after writing

# !!! WINDOW >>---------------------------------------------------------------------------------------------------------------------------------

# window = ThemedTk(theme="sun-valley-dark")
window = tk.Tk() # variable: type:tkinter.Tk: create a Tk window object
window.geometry("460x400")
window.title(" *** Clint's Password Manager ***") # determines what the titlebar of the window says
window.resizable(width=False, height=False) # disable the resizability function of the window vertically and horizontally
# window['bg']='black' # determines the color of the window background

# !!! FRAMES >>---------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------

# file frame
fileframe = tk.Frame(master=window) # variable: type:tkinter.frame: creates a frame object, in this case for the file selection section of the window
fileframe.grid(row = 0, column = 0, sticky = W, pady = 2) # position the frame, in this case using a grid
filelabel = tk.Label(master=fileframe, text="\nChoose a file to save credentials to: ", padx=20).grid(row = 1, column = 0, sticky = W, padx = (100, 0), pady = 2) # determines what the label says

# buttons
buttonframe = tk.Frame(master=window) # variable: type:tkinter.frame: creates a frame for the file selection buttons
ttk.Button(master=fileframe, text="Create New", command=lambda: createNew()).grid(row = 2, column = 0, sticky = 'W', pady = 10, padx = (110, 0)) # creates a button object for the createNew function
ttk.Button(master=fileframe, text="Choose Existing", command=lambda: chooseExisting()).grid(row = 2, column = 0, sticky = 'W', padx = (210, 0)) # creates a button object for the chooseExisting function

# filepath label
pathvar = StringVar() # variable: type:StringVar: creates the variable that will store the text that will populate the filepath label
filepathLabel = tk.Label(master=fileframe) # variable: type:tkinter.label: creates a label that will display the path that the user will select from the file dialog
filepathLabel.grid(row = 3, column = 0, padx = (30, 0), pady = 2) # determines the position of the filepath label on the grid

# --------------------------------------------------------------------------------------------------------------------------------

# website frame
webframe = tk.Frame(master=window) # variable: type:tkinter.frame: creates a frame for the account website name portion of the window
webframe.grid(row = 4, column = 0, sticky = W, pady = 2) # position the webframe
weblabel = tk.Label(master=webframe, text="Enter the name of the website you wish to create an account for: ").grid(row = 5, column = 0, sticky = W, padx = (26, 0), pady = 2) # determines what the webframe label says
webvar = StringVar() # variable: type:StringVar: creates a varibale that will store the text entered by the user in the website textbox
webentry = tk.Entry(master=webframe, textvariable = webvar, text = '', width = 62) # variable: type:tikinter.Entry: creates a textbox for users to enter the name of the website that the account belongs to
webentry.grid(row = 6, column = 0, sticky = W, padx = (30, 0), pady = 2) # determines the position of the entry

# --------------------------------------------------------------------------------------------------------------------------------

# username frame
unframe = tk.Frame(master=window) # variable: type:tkinter.frame: creates a frame for the username portion of the window
unframe.grid(row = 7, column = 0, sticky = W, pady = 2) # positions the UN webframe
unlabel = tk.Label(master=unframe, text="\nEnter the username of the account you wish to save: ").grid(row = 8, column = 0, sticky = W, padx = (26, 0), pady = 2) # determines what the UN label says
unvar = StringVar() # variable: type:StringVar: creates a variable that will store the username entered by the user
unentry = tk.Entry(master=unframe, textvariable = unvar, text = '', width = 62) # variable: type:tkinter.Entry: creates a textbar for user to enter the username for the relevant account
unentry.grid(row = 9, column = 0, padx = (30, 0), pady = 2) # positions the UN entry

# --------------------------------------------------------------------------------------------------------------------------------

# password frame
pwdframe = tk.Frame(master=window) # variable: type:tkinter.frame: creates a frame for the password portion of the window
pwdframe.grid(row = 10, column = 0, sticky = W, pady = 2) # positions the password webframe
pwdlabel = tk.Label(master=pwdframe, text="\nGenerated Password: ").grid(row = 11, column = 0, sticky = W, padx = (150, 0), pady = 2) # determines what the password label says
pwdvar = StringVar() # variable: type:StringVar: creates a variable that will be used to store and display the password generated by the program
pwdentry = tk.Label(master=pwdframe, text=generatePwd()) # variaable: type:tkinter.Label: creates a variableto contain the password
pwdentry.grid(row = 12, column = 0, padx = (150, 0), pady = 2) # positions the password

# --------------------------------------------------------------------------------------------------------------------------------

#  Submit button frame
submitframe = tk.Frame(master=window) # variable: type:tkinter.frame: creates a fram for the submit button
submitframe.grid(row = 13, column = 0, sticky = W, pady = 2) # positions the submit button
ttk.Button(master=submitframe, text="Save", command=lambda: [submit(), window.destroy()]).grid(row = 14, column = 0, sticky = 'NSEW', padx = (190, 0), pady = (20, 50)) # creates a button to submit the completed form and close the tkinter window

# --------------------------------------------------------------------------------------------------------------------------------

sv_ttk.set_theme("dark")

window.mainloop() # mainloop runs the program