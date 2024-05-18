from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("test_treeview")

tree = Treeview(root, columns=("cities"))

tree.heading("#0", text="state")
tree.heading("#1", text="city")

tree.insert("", index=END, text="GD", values="shenzhen")
tree.insert("", index=END, text="Shaanxi", values="xian")

for item in tree.get_children():
    print(item)
    if item == "I001":
        tree.delete(item)

tree.pack()

root.mainloop()



