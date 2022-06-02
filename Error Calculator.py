import tkinter as tk

root= tk.Tk()
root.title("Error Calculator Beta")
canvas1 = tk.Canvas(root, width = 400, height = 400,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Error Calculator')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 55, window=label1)

label2 = tk.Label(root, text='A\n\n ΔA \n\n B\n\n ΔB')
label2.config(font=('helvetica', 10))
canvas1.create_window(120, 167, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 120, window=entry1)
entryd1 = tk.Entry (root) 
canvas1.create_window(200, 150, window=entryd1)
entry2 = tk.Entry (root) 
canvas1.create_window(200, 183, window=entry2)
entryd2 = tk.Entry (root) 
canvas1.create_window(200, 215, window=entryd2)

def plus ():
    try:
        label3.destroy()
    except:
        pass
    a  = float(entry1.get())
    da = float(entryd1.get())
    b  = float(entry2.get())
    db = float(entryd2.get())

    r= a+b
    e= da+db
    
    label3 = tk.Label(root, text='\t\t\t'+str(r)+' ± '+str(e) + '\t\t\t',font=('helvetica', 10))
    canvas1.create_window(175, 350, window=label3)

def minus ():
    try:
        label3.destroy()
    except:
        pass
    a  = float(entry1.get())
    da = float(entryd1.get())
    b  = float(entry2.get())
    db = float(entryd2.get())

    r= a-b
    e= da+db
    label3 = tk.Label(root, text='\t\t\t'+str(r)+' ± '+str(e) + '\t\t\t',font=('helvetica', 10))
    canvas1.create_window(175, 350, window=label3)

def multiply ():
    try:
        label3.destroy()
    except:
        pass
    a  = float(entry1.get())
    da = float(entryd1.get())
    b  = float(entry2.get())
    db = float(entryd2.get())

    r= a*b
    e= a*b*(da/a+db/b)
    label3 = tk.Label(root, text='\t\t\t'+str(r)+' ± '+str(e) + '\t\t\t',font=('helvetica', 10))
    canvas1.create_window(175, 350, window=label3)


def division ():
    try:
        label3.destroy()
    except:
        pass
    a  = float(entry1.get())
    da = float(entryd1.get())
    b  = float(entry2.get())
    db = float(entryd2.get())

    r= a/b
    e= a/b*(da/a+db/b)
    label3 = tk.Label(root, text='\t\t\t'+str(r)+' ± '+str(e) + '\t\t\t',font=('helvetica', 10))
    canvas1.create_window(175, 350, window=label3)
        
        
button1 = tk.Button(text=' \t+\t ', command=plus, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(125, 260, window=button1)
button2 = tk.Button(text=' \t-\t ', command=minus, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(275, 260, window=button2)
button3 = tk.Button(text=' \tx\t ', command=multiply, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(125, 300, window=button3)
button4 = tk.Button(text=' \t÷\t ', command=division, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(275, 300, window=button4)


root.mainloop()
