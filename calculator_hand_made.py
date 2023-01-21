

import tkinter as tk



windo = tk.Tk()

var_str = tk.StringVar()
windo.geometry("369x479")
windo.configure(background = '#D0DEED')
lbl_1 = tk.Label(text="................................."*8+'...',bd=50,font=('Bauhaus 93', 1))
lbl_0 = tk.Label(text="      "*8+'    ',bg="#CADCEF",bd=40,font=('Bauhaus 93', 16))
lbl_0.grid(row=1,column=0,columnspan=4,sticky='we')
lbl_1.grid(row=0,column=0,columnspan=4)
lbl_2 = tk.Label(textvariable=var_str,justify='right',bd=40,bg="#CADCEF",font=('Bauhaus 93', 16))
lbl_2.grid(row=1,columnspan=4,)





# -----------------------------
tk.Button(master=windo, height=1,width=5,bd=4,relief=tk.RIDGE, font=('Bauhaus 93', 16),)

tk.mainloop()
