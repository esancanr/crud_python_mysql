from tkinter import messagebox, END

from models.modify_user import modifyUser
from models.update_tree_view import updateTreeView


def modifyRegistry(textBoxId, textBoxName, textBoxLastname, combo, tree):

  try:
    userId = textBoxId.get()
    name = textBoxName.get()
    lastname = textBoxLastname.get()
    gender = combo.get()

    if not userId or not name or not lastname or not gender:
      messagebox.showinfo('Importante:', 'Please complete all fields')
      return
    
    modifyUser(userId, name, lastname, gender)
    messagebox.showinfo('information:','The data was updated')

    updateTreeView(tree)

    #Clean the widgets
    for widget in [textBoxName, textBoxLastname, textBoxId, combo]:
      widget.delete(0, END)
  
  except ValueError as error:
    print('Error to save the data {}'.format(error))
