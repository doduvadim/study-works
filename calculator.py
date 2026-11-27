import tkinter as tk

def click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(symbol))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")

root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")

# Поле ввода
entry = tk.Entry(root, font=("Arial", 20), justify="right", bd=10)
entry.pack(fill=tk.BOTH, padx=5, pady=5)

# Кнопки
buttons = [
    ["C", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", ""]
]

frame = tk.Frame(root)
frame.pack(expand=True, fill=tk.BOTH)

for row, row_buttons in enumerate(buttons):
    for col, text in enumerate(row_buttons):
        if not text:
            continue
        if text == "C":
            cmd = clear
        elif text == "=":
            cmd = calculate
        else:
            cmd = lambda t=text: click(t)
        
        tk.Button(
            frame, text=text, font=("Arial", 16),
            command=cmd
        ).grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

# Равномерное растягивание
for i in range(4):
    frame.columnconfigure(i, weight=1)
for i in range(5):
    frame.rowconfigure(i, weight=1)

root.mainloop()