import tkinter as tk

class BasicCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expression = ""

        # Display
        self.display = tk.Entry(
            root,
            font=("Arial", 18),
            bd=8,
            relief=tk.RIDGE,
            justify="right"
        )
        self.display.pack(fill="both", padx=10, pady=10, ipady=10)

        # Buttons
        self.create_buttons()

    def press(self, value):
        self.expression += str(value)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

    def calculate(self):
        try:
            result = eval(self.expression)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
            self.expression = str(result)
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
            self.expression = ""

    def create_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack()

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0)
        ]

        for (text, row, col) in buttons:
            if text == "=":
                btn = tk.Button(
                    frame, text=text, width=5, height=2,
                    font=("Arial", 14),
                    command=self.calculate
                )
            elif text == "C":
                btn = tk.Button(
                    frame, text=text, width=22, height=2,
                    font=("Arial", 14), bg="#f44336", fg="white",
                    command=self.clear
                )
                btn.grid(row=row, column=col, columnspan=4, pady=5)
                continue
            else:
                btn = tk.Button(
                    frame, text=text, width=5, height=2,
                    font=("Arial", 14),
                    command=lambda t=text: self.press(t)
                )

            btn.grid(row=row, column=col, padx=4, pady=4)

if __name__ == "__main__":
    root = tk.Tk()
    BasicCalculator(root)
    root.mainloop()
