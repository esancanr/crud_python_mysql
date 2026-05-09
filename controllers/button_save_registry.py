from tkinter import messagebox, END

from models.create_users import createUsers
from models.update_tree_view import updateTreeView


def saveRegistry(textBoxId, textBoxName, textBoxLastname, combo, tree):

  try:
    name = textBoxName.get()
    lastname = textBoxLastname.get()
    gender = combo.get()

    if not name or not lastname or not gender:
      messagebox.showinfo('Importante:', 'Please complete all fields')
      return
    
    createUsers(name, lastname, gender)
    messagebox.showinfo('information:','The data was sent')

    updateTreeView(tree)

    #Clean the widgets
    for widget in [textBoxName, textBoxLastname, textBoxId, combo]:
      widget.delete(0, END)
  
  except ValueError as error:
    print('Error to save the data {}'.format(error))
