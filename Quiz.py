import tkinter as tk
print("How many questions?")
n = int(input())

q = []
a = []
for i in range(n):
    print("Question", i)
    q.append(input())
    print("Answer to Question", i)
    a.append(input())
root = tk.Tk()
root.title("Quiz")
score = 0
current_i = 0  
label = tk.Label(root, text=q[0]) 
label.pack(padx=5, pady=5, fill="x")
answer = tk.Entry(root)
answer.pack(padx=5, pady=5, fill="x")

def check(event):
    global current_i, score
    user = answer.get()
    if user == a[current_i]:
        score += 1
    answer.delete(0, tk.END)
    current_i += 1
    if current_i < n:
        label.config(text=q[current_i])
    else:
        label.config(text=f"Final Score: {score}")
        answer.pack_forget()

answer.bind("<Return>", check)
root.mainloop()
