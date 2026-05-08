from models.users_model import Users
from tkinter import messagebox
from tkinter import END


def saveRegistry( textBoxId, textBoxName, textBoxLastname, combo):

  try:
    name = textBoxName.get()
    lastname = textBoxLastname.get()
    gender = combo.get()

    if not name or not lastname or not gender:
      messagebox.showinfo('Importante:', 'Please complete all fields')
      return
    
    Users.createUsers(name, lastname, gender)
    messagebox.showinfo('information:','The data was sent')

    #Clean the widgets
    textBoxId.delete(0, END)
    combo.delete(0, END)
    textBoxName.delete(0, END)
    textBoxLastname.delete(0, END)
  
  except ValueError as error:
    print('Error to save the data {}'.format(error))
