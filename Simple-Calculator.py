import tkinter as tk

expression = ""

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("370x320") 

input_text = tk.StringVar()

input_field = tk.Entry(root, textvariable=input_text, font=('roboto', 25, 'bold'), bd=5, insertwidth=4, bg="powder blue", justify='right')
input_field.grid(columnspan=4, ipadx=8, ipady=15) 

buttons = [
    '7', '8', '9', '⨸',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        btn = tk.Button(root, text=button, padx=20, pady=15, bd=4, command=btn_equal)
    elif button == 'C':
        btn = tk.Button(root, text=button, padx=20, pady=15, bd=4, command=btn_clear)
    else:
        btn = tk.Button(root, text=button, padx=20, pady=15, bd=4, command=lambda item=button: btn_click(item))
    
    btn.grid(row=row_val, column=col_val)
    col_val = col_val+ 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
