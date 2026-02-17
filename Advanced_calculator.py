import tkinter as tk
import math

class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("420x560")
        self.root.resizable(False, False)

        self.expression = ""

        self.display = tk.Entry(
            root,
            font=("Arial", 20),
            bd=10,
            relief=tk.RIDGE,
            justify="right"
        )
        self.display.pack(fill="both", padx=10, pady=10, ipady=10)

        self.create_buttons()

    def add_to_expression(self, value):
        self.expression += value
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

    def backspace(self):
        self.expression = self.expression[:-1]
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def calculate(self):
        try:
            expr = self.expression
            expr = expr.replace("^", "**")
            result = eval(expr, {"__builtins__": None}, math.__dict__)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
            self.expression = str(result)
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
            self.expression = ""

    def create_buttons(self):
        btn_frame = tk.Frame(self.root)
        btn_frame.pack()

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("C", 1, 4),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("⌫", 2, 4),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), ("(", 3, 4),
            ("0", 4, 0), (".", 4, 1), ("%", 4, 2), ("+", 4, 3), (")", 4, 4),
            ("sin", 5, 0), ("cos", 5, 1), ("tan", 5, 2), ("√", 5, 3), ("^", 5, 4),
            ("log", 6, 0), ("ln", 6, 1), ("π", 6, 2), ("e", 6, 3), ("=", 6, 4)
        ]

        for (text, row, col) in buttons:
            if text == "=":
                btn = tk.Button(
                    btn_frame, text=text, width=7, height=2,
                    font=("Arial", 12), bg="#4CAF50", fg="white",
                    command=self.calculate
                )
            elif text == "C":
                btn = tk.Button(
                    btn_frame, text=text, width=7, height=2,
                    font=("Arial", 12), bg="#f44336", fg="white",
                    command=self.clear
                )
            elif text == "⌫":
                btn = tk.Button(
                    btn_frame, text=text, width=7, height=2,
                    font=("Arial", 12),
                    command=self.backspace
                )
            elif text == "√":
                btn = tk.Button(
                    btn_frame, text=text, width=7, height=2,
                    font=("Arial", 12),
                    command=lambda: self.add_to_expression("sqrt(")
                )
            elif text == "π":
                btn = tk.Button(
                    btn_frame, text=text, width=7, height=2,
                    font=("Arial", 12),
                    command=lambda: self.add_to_expression("pi")
                )
            elif text == "ln":
                btn = tk.Button(
                    btn_frame, text=text, width=7, height=2,
                    font=("Arial", 12),
                    command=lambda: self.add_to_expression("log(")
                )
            elif text in ["sin", "cos", "tan", "log"]:
                btn = tk.Button(
                    btn_frame, text=text, width=7, height=2,
                    font=("Arial", 12),
                    command=lambda t=text: self.add_to_expression(t + "(")
                )
            else:
                btn = tk.Button(
                    btn_frame, text=text, width=7, height=2,
                    font=("Arial", 12),
                    command=lambda t=text: self.add_to_expression(t)
                )

            btn.grid(row=row, column=col, padx=4, pady=4)

if __name__ == "__main__":
    root = tk.Tk()
    AdvancedCalculator(root)
    root.mainloop()
