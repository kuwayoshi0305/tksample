import tkinter as tk
from tkcode import CodeEditor
from tkinter import ttk
import os

root  = tk.Tk()
root.title('Planarian Player v.1.0.0')


text = CodeEditor(root, language="yaml",undo=True)
text.grid(rowspan=3,row=0, column=0)

currentpath = os.path.dirname(os.path.abspath(__file__))
inputPath = os.path.join(currentpath, "../", "input" ,"GUI_opt_input.yaml")
with open(inputPath, 'r') as f:
    inputText = f.read()
text.content = inputText


column = ('ID', 'API', 'Status')
tree = ttk.Treeview(root, columns=column)
# 列の設定
tree.column('#0',width=0, stretch='no')
tree.column('ID', anchor='center', width=80)
tree.column('API',anchor='w', width=100)
tree.column('Status', anchor='center', width=80)
# 列の見出し設定
tree.heading('#0',text='')
tree.heading('ID', text='',anchor='center')
tree.heading('API', text='API', anchor='w')
tree.heading('Status',text='Status', anchor='center')
# レコードの追加
tree.insert(parent='', index='end', iid=0 ,values=(1, 'Propeller',"Finished"), tags="green")
tree.insert(parent='', index='end', iid=1 ,values=(2,'Loft', "Running"), tags="red")
tree.insert(parent='', index='end', iid=2, values=(3,'Patch', "Waiting"), tags="gray")
tree.insert(parent='', index='end', iid=3, values=(4,'Periodic', "Waiting"), tags="gray")

tree.tag_configure("red", foreground='red')
tree.tag_configure("green", background='green')
tree.tag_configure("gray", foreground='gray')

# ウィジェットの配置
tree.grid(columnspan=2,row=0, column=1)

lbl_3 = tk.Label(text='Running time[s]:')
lbl_3.grid(row=1, column=1)


lbl_4 = tk.Label(text='0.0')
lbl_4.grid(row=1, column=2)

button = tk.Button(text="Play",width=10,height=5)
button.grid(columnspan=2,row=2, column=1)

root.mainloop()