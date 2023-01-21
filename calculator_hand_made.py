#------------------------------------------------------------------------------------------------------------------------------------
import tkinter as tk





index_dat = -2
index_operator = -1
font_number = 15

str_ing = ""


                      
def func_appnd(a):
    global index_dat
    global index_operator
    global var_str
    global str_ing
    if len(str_ing) == 32:
        var_str.set('nmitvan bish az 31 karaktar vared kard')
        return
    
    
    if a == "." and index_dat < index_operator :
        str_ing = str_ing + '.'
        var_str.set(str_ing)
        index_dat = len(str_ing)
        
        
    
    
    
    try:
        if a in ['+', '-', '/', '*'] and str_ing[-1] in ['+', '-', '/', '*']:
            j = 0
            for i in str_ing:
                j += 1
            j -= 1
            a = ''
            for i in range(int(j)):
                
                a += str_ing[i]
                
            str_ing = a
            var_str.set(str_ing)
            index_operator = len(str_ing)
            
        if a in ["(",")","7","8","9",'4',"5","6","1",'2',"3",'0','+', '-', '/', '*',]:
            str_ing = str_ing + a
            var_str.set(str_ing)
    except IndexError:
        var_str.set('number vared knid')

    
    
    
    
    
    
    
def func_delet(*args):
    global var_str
    global str_ing ,index_dat, index_operator
    
    j = 0
    for i in str_ing:
        j += 1
    j -= 1
    a = ''
    for i in range(int(j)):
        
        a += str_ing[i]    
    str_ing = a
    var_str.set(str_ing)
    
    len_str = len (str_ing)
    
    for i in str_ing[::-1]:
        if i in ['+', '-', '/', '*']:
            list_op = str_ing[::-1].index(i)
            index_operator = len_str - list_op
    if index_dat > len_str and '.' in str_ing:
        list_dot = str_ing[::-1].index('.')
        index_dat = len_str - list_dot
    if str_ing == '':
        index_dat,index_operator = -2 , -1
    
    
def natije(*args):
    global str_ing
    global var_str
    if str_ing == '':
        var_str.set('number vared knid')
    else:
        number = str(eval(str_ing))
        var_str.set(number)
        str_ing = number
    index_operator = -1
    index_dat = -2
    
    
def func_ful_delet():
    global var_str
    global str_ing
    str_ing = ""
    var_str.set(str_ing)
    index_operator = -1
    index_dat = -2
    
    
list_str = [["(", lambda: func_appnd('(')], [")", lambda: func_appnd(")")],\
    ["\U000025C0", lambda: func_delet()], ["\U00002797", lambda: func_appnd("/")],\
        ["7", lambda: func_appnd('7')], ["8",lambda: func_appnd("8")], ["9", lambda: func_appnd("9")],\
            ["\U00002716", lambda: func_appnd("*")], ["4", lambda: func_appnd('4')], ["5", lambda: func_appnd('5')],\
                ["6", lambda: func_appnd('6')], ["\U00002796", lambda: func_appnd("-")], ["1", lambda: func_appnd('1')],\
                    [ "2" ,lambda: func_appnd('2')],[ "3" ,lambda: func_appnd("3")], ["\U00002795" ,lambda: func_appnd('+')],\
                        ["." ,lambda: func_appnd(".")],[ "0" ,lambda: func_appnd('0')],["\U000023EA" ,\
                            lambda: func_ful_delet()],[ "=" ,lambda: natije()]]

windo = tk.Tk()

var_str = tk.StringVar()
windo.geometry("369x479")
windo.configure(background = '#D0DEED')
lbl_1 = tk.Label(text="................................."*8+'...',bd=50,font=('Jokerman', 1))
lbl_0 = tk.Label(text="      "*8+'    ',bg="#CADCEF",bd=40,font=('Jokerman', 16))
lbl_0.grid(row=1,column=0,columnspan=4,sticky='we')
lbl_1.grid(row=0,column=0,columnspan=4)
lbl_2 = tk.Label(textvariable=var_str,relief='raised',justify='right',bd=4,bg="#CADCEF",font=('Jokerman', font_number))
lbl_2.grid(row=1,columnspan=4,)


    
l = -1
for i,j in list_str :
    
    l = l + 1
    a = "#BBC3CC"
    if i in ["\U00002797", "\U00002716", "\U00002796", "\U00002795", "="]:
        a = '#5093CD'
    if i in ["\U000025C0", "\U000023EA"]:
        a = '#796363' 
    if i == "\U000025C0":
        windo.bind('<Button-3>', func_delet)
    if i == "=":
        windo.bind('<Return>', natije)



# -----------------------------
    tk.Button(master=windo,background=a, height=1,width=5,bd=4,relief=tk.RIDGE, text=i, font=('Jokerman', 16),command=j,).grid(sticky='we',row= ( 2 + l // 4),padx=1, pady=4, column= l % 4)

def bind_0_9(a):
    func_appnd(a.char)
def bind_natije(a):
    natije(a.char)

for a in ["(",")","7","8","9",'4',"5","6","1",'2',"3",'0','+', '-', '/', '*','.']:
    windo.bind(a, bind_0_9)
windo.bind('=', bind_natije)

tk.mainloop()

# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


