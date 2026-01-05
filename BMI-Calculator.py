def calc(weight_kg, height_m):
  return weight_kg / (height_m ** 2)

def conv(bmi_value):
  if bmi_value < 18.5:
    return "Underweight"
  elif 18.5 <= bmi_value < 25:
    return "Normal weight"
  elif 25 <= bmi_value < 30:
    return "Overweight"
  else:
    return "Obese"


import tkinter as tk

root = tk.Tk()
root.title("BMI Calculator")

def showBMI(event):
    w = float(weight.get())
    h = float(height.get())
    
    bmi_val = calc(w, h)
    status = conv(bmi_val)
    
    label.config(text=f"BMI: {round(bmi_val, 2)} - {status}")

root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Enter Weight (kg) then Height (m):").pack()

weight = tk.Entry(root)
weight.pack(padx=5, pady=5, fill="x")

height = tk.Entry(root)
height.pack(padx=5, pady=5, fill="x")

weight.bind("<Return>", showBMI)
height.bind("<Return>", showBMI)

label = tk.Label(root, text="Press Enter to Calculate")
label.pack(padx=5, pady=5, fill="x")

root.mainloop()
