from models.show_users import showUsers

def updateTreeView(tree):
    try:
     tree.delete(*tree.get_children())
     data = showUsers()
     for row in showUsers():
        tree.insert('', 'end', values=row)
    except ValueError as error:
       print('Error to update the treeview {}'.format(error))