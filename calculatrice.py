import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculatrice")
        self.root.geometry("400x600")

        # Style for ttk widgets
        self.style = ttk.Style()
        self.style.configure("TButton", font=('Arial', 18), padding=10)
        self.style.configure("TEntry", font=('Arial', 24), padding=10)

        # Entry field for displaying the calculations
        self.entry = ttk.Entry(root, width=16, font=('Arial', 24), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

        # Button labels
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '←',
            '1', '2', '3', '-', '(',
            '0', '.', '=', '+', ')'
        ]

        # Create buttons in a grid
        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            ttk.Button(root, text=button, command=action).grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

        # Make the grid cells responsive
        for i in range(5):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        # Handle button click events
        if char == 'C':
            self.entry.delete(0, tk.END)
        elif char == '←':
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current_text[:-1])
        elif char == '=':
            try:
                expression = self.entry.get()
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Erreur")
        else:
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text + str(char))

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
