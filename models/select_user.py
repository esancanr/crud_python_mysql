from tkinter import END

def selectRegistry(event, tree, textBoxId, textBoxName, textBoxLastname, combo):
 try:
  selectItem = tree.focus()
  if selectItem:
   #GET THE VALUES FROM COLUMN
   values = tree.item(selectItem)['values']
   #SET THE VALUES ON THE WIHTGETS ENTRY
   fields = [
    (textBoxId, values[0]),
    (textBoxName, values[1]),
    (textBoxLastname, values[2])
    ]
   for textbox, value in fields:
        textbox.delete(0, END)
        textbox.insert(0, value)

   combo.set(values[3])
 except ValueError as error:
   print('Error to select registry {}'.format(error))