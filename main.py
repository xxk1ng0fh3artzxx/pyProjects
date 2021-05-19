from tkinter import *


root = Tk()
root.geometry('400x400')

class Chores: 

    def __init__(self,master):
        self.master=master
        master.title('House Chores')

def add_task():
        task = entry_task.get()
        if task!='':
            listbox_tasks.insert(END, task)
            entry_task.delete(0,END)
        else:
            pass


# Creating GUI
    ##Dropdown Boxes
clicked=StringVar()
clicked.set('Assign Chore')
drop_menu = OptionMenu(root, clicked, 'Preston', 'Micha', 'T\'Challa', 'Seppit')
drop_menu.pack()

frame_tasks=Frame(root)
frame_tasks.pack()

listbox_tasks= Listbox(root,height=3,width=50)
listbox_tasks.pack(side=LEFT)

scrollbar_tasks = Scrollbar(root)
scrollbar_tasks.pack(side=RIGHT, fill=Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = Entry(root, width=50)
entry_task.pack()

button_add_task = Button(root, text='Add Chore', width=48, command=add_task)
button_add_task.pack()

button_delete_task = Button(root, text='Delete Chore', width=48, command=add_task)
button_delete_task.pack()

button_load_task = Button(root, text='Load Chore', width=48, command=add_task)
button_load_task.pack()


button_assign_task = Button(root, text='Assign Chore', width=48, command=add_task)
button_assign_task.pack()

assign_menu = OptionMenu(root, clicked, 'Preston', 'Micha', 'T\'Challa', 'Seppit')
assign_menu.pack()

        

my_gui = Chores(root)
root.mainloop()
