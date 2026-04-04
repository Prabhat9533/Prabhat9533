import tkinter as tk
from tkinter import colorchooser

class ColorCombiner:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Color Combiner")
        self.root.geometry("400x300")

        self.color1 = None
        self.color2 = None

        # Label to display combined color
        self.result_label = tk.Label(root, text="combined color", font=("Arial", 14))
        self.result_label.pack(pady=20)

        # Frame for buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)

        # make a add sign between first and second  colors options and make it in red color
        add_label = tk.Label(button_frame, text="+", font=("Arial", 14), fg="red")
        add_label.pack(side=tk.LEFT, padx=10)


        # Button to select first color (make this red)
        self.select_color1_btn = tk.Button(button_frame, text="Select Color 1", bg="orange", command=self.select_color1)
        self.select_color1_btn.pack(side=tk.LEFT, padx=10)

        
        # Button to select second color (blue)
        self.select_color2_btn = tk.Button(button_frame, text="Select Color 2", bg="white", command=self.select_color2)
        self.select_color2_btn.pack(side=tk.LEFT, padx=10)

        # Button to combine colors (blue)
        self.combine_btn = tk.Button(button_frame, text="Combine Colors", bg="green", command=self.combine_colors)
        self.combine_btn.pack(side=tk.LEFT, padx=10)

    def select_color1(self):
        color = colorchooser.askcolor(title="Choose Color 1")
        if color[1]:
            self.color1 = color[1]
            self.select_color1_btn.config(bg=self.color1)

    def select_color2(self):
        color = colorchooser.askcolor(title="Choose Color 2")
        if color[1]:
            self.color2 = color[1]
            self.select_color2_btn.config(bg=self.color2)

    def combine_colors(self):
        if self.color1 and self.color2:
            # Simple combination: average the RGB values
            r1, g1, b1 = self.hex_to_rgb(self.color1)
            r2, g2, b2 = self.hex_to_rgb(self.color2)
            r = (r1 + r2) // 2
            g = (g1 + g2) // 2
            b = (b1 + b2) // 2
            combined_color = self.rgb_to_hex((r, g, b))
            self.result_label.config(bg=combined_color, text="Combined Color")
        else:
            self.result_label.config(text="Please select both colors")

    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def rgb_to_hex(self, rgb):
        return '#%02x%02x%02x' % rgb

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorCombiner(root)
    root.mainloop()