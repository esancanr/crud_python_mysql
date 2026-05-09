from tkinter import messagebox, END

from models.delete_user import deleteUser
from models.update_tree_view import updateTreeView


def deleteRegistry(textBoxId, tree, textBoxName, textBoxLastname, combo):

  try:
    userId = textBoxId.get()

    if not userId:
      messagebox.showinfo('Importante:', 'Please complete all fields')
      return
    
    deleteUser(userId)
    messagebox.showinfo('information:','The data was updated')

    updateTreeView(tree)

    #Clean the widgets
    for widget in [textBoxName, textBoxLastname, textBoxId, combo]:
      widget.delete(0, END)
  
  except ValueError as error:
    print('Error to delete the data {}'.format(error))
