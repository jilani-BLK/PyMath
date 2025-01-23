import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("360x600")
app.title("Calculatrice")

display = ctk.CTkEntry(app, 
                       width=340, 
                       height=50, 
                       font=("Arial", 24), 
                       justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

def add_to_display(text):
    current = display.get()
    display.delete(0, "end")
    display.insert(0, current + text)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for text, row, col in buttons:
    button = ctk.CTkButton(app, 
                           text=text, 
                           width=80, 
                           height=60, 
                           font=("Arial", 18),
                           command=lambda t=text: add_to_display(t) if t not in ["C", "="] else None)
    button.grid(row=row, column=col, padx=5, pady=5)

app.mainloop()