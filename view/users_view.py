import tkinter
from tkinter import *
from tkinter import ttk

from database.connectionMySql import *
from controllers.save_user import saveRegistry

class formUsers:
 global base
 base = None
 global groupBox
 groupBox = None
 global textBoxId
 textBoxId = None
 global textBoxName
 textBoxName = None
 global textBoxLastname
 textBoxLastname = None
 global combo
 combo = None
 global tree
 tree = None

def form():
  global base, groupBox, textBoxId, textBoxName, textBoxLastname, combo, tree

  try:
    base = tkinter.Tk()
    base.geometry('1450x300')
    base.title('CRUD')

    '''GROUP BOX'''
    #Personal Data Box
    groupbox = LabelFrame(
        base, 
        text='Personal Data',
        padx=5,
        pady=5
    )
    groupbox.grid(row=0,column=0,padx=10,pady=10)

    '''LABELS'''
    #Label Id
    labelId=Label(
      groupbox, 
      text='ID',
      width=13,
      font=('arial',10)
      ).grid(row=0, column=0)
    textBoxId = Entry(groupbox)
    textBoxId.grid(row=0,column=1)
    #Label Name
    labelName=Label(
      groupbox, 
      text='Name',
      width=13,
      font=('arial',10)
      ).grid(row=1, column=0)
    textBoxName = Entry(groupbox)
    textBoxName.grid(row=1,column=1)
    #Label Last Name
    labelLastName=Label(
      groupbox, 
      text='Last Name',
      width=13,
      font=('arial',10)
      ).grid(row=2, column=0)
    textBoxLastname = Entry(groupbox)
    textBoxLastname.grid(row=2,column=1)
    #Label Gender
    labelGender=Label(
      groupbox, 
      text='Gender',
      width=13,
      font=('arial',10)
      ).grid(row=3, column=0)
    optionGender = tkinter.StringVar()
    combo = ttk.Combobox(
      groupbox,
      values=['Male', 'Female'],
      textvariable=optionGender
    )
    combo.grid(row=3,column=1)


    '''Buttons'''
    #Button Save Information on my data bases
    Button(groupbox, 
           text='Save',
           width=10,
           command=lambda: saveRegistry(
                  textBoxId,
                  textBoxName,
                  textBoxLastname,
                    combo
            )
        ).grid(row=4,column=0)
    #Button Modify Information on my data bases
    Button(groupbox, 
           text='Modify',
           width=10 
        ).grid(row=4,column=1)
    #Button Delete Information on my Data Bases
    Button(groupbox, 
           text='Delete',
           width=10 
        ).grid(row=4,column=3)
    
    '''GROUP BOX'''
    #Information Data Box
    groupBox = LabelFrame(
      base,
      text='Information',
      padx=5,
      pady=5
    )
    groupBox.grid(row=0,column=1,padx=5,pady=5)

    '''TREEVIEW'''
    columns = ("Id", "Nombres", "Apellidos", "Sexo")

    tree = ttk.Treeview(groupBox, columns=columns, show='headings')

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    tree.pack()

  except ValueError as error:
    print("Error to show the iu: {}".format(error))

form()