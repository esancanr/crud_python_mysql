from models.create_users import Users
from tkinter import messagebox, END


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
    for widget in [textBoxName, textBoxLastname, textBoxId, combo]:
      widget.delete(0, END)
  
  except ValueError as error:
    print('Error to save the data {}'.format(error))
