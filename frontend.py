from Tkinter import*
import backend

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    entry_1.delete(0,END)
    entry_1.insert(END,selected_tuple[1])
    entry_2.delete(0,END)
    entry_2.insert(END,selected_tuple[2])
    entry_3.delete(0,END)
    entry_3.insert(END,selected_tuple[3])
    entry_4.delete(0,END)
    entry_4.insert(END,selected_tuple[4])
#    return("selected_tuple")

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.inser(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
#    print(selected_tuple()[0],selected_tuple[1],selected_tuple[2],selected_tuple[3],selected_tuple[4])


root=Tk()
root.wm_title("BookStore")

label_1=Label(root, text="Title")
label_1.grid(row=0,column=0, sticky=E)

label_2=Label(root, text="Author")
label_2.grid(row=0,column=2, sticky=E)

label_3=Label(root, text="Year")
label_3.grid(row=1,column=0, sticky=E)

label_4=Label(root, text="ISBN")
label_4.grid(row=1,column=2, sticky=E)

title_text=StringVar()
entry_1=Entry(root, textvariable=title_text)
entry_1.grid(row=0, column=1)

author_text=StringVar()
entry_2=Entry(root, textvariable=author_text)
entry_2.grid(row=0, column=3)

year_text=StringVar()
entry_3=Entry(root, textvariable=year_text)
entry_3.grid(row=1, column=1)

isbn_text=StringVar()
entry_4=Entry(root, textvariable=isbn_text)
entry_4.grid(row=1, column=3)

list1=Listbox(root, height=6, width=35)
list1.grid(row=2,column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(root)
sb1.grid(row=2, column=2, rowspan=6)

list1.config(yscrollcommand=sb1.set)
sb1.config(command=list1.yview)

# sb2=Scrollbar(root)
# sb2.grid(row=7, column=1, columnspan=2)

# list1.config(xscrollcommand=sb2.set)
# sb2.config(command=list1.xview)

list1.bind("<<ListboxSelect>>",get_selected_row)
button_1=Button(root, text="View all", width=12, command=view_command)
button_1.grid(row=2, column=3)

button_2=Button(root, text="Search entry", width=12, command=search_command)
button_2.grid(row=3, column=3)

button_3=Button(root, text="Add entry", width=12, command=add_command)
button_3.grid(row=4, column=3)

button_4=Button(root, text="Update", width=12, command=update_command)
button_4.grid(row=5, column=3)

button_5=Button(root, text="Delete", width=12, command=delete_command)
button_5.grid(row=6, column=3)

button_6=Button(root, text="Close", width=12, comman=root.destroy)
button_6.grid(row=7, column=3)

root.mainloop()
