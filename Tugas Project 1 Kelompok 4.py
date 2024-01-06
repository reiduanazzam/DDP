import tkinter as tk

def calculate():
    x = float(entry_bil1.get())
    y = float(entry_bil2.get())
    
    if operator.get() == "+":
        result.set(x + y)
    elif operator.get() == "-":
        result.set(x - y)
    elif operator.get() == ":":
        result.set(x / y)
    else:
        result.set(x * y)

# Create the main window
app = tk.Tk()
app.title("Kalkulator Tkinter")

# Define variables
entry_bil1 = tk.Entry(app)
entry_bil2 = tk.Entry(app)
operator = tk.StringVar()
result = tk.StringVar()

# Set up the UI
tk.Label(app, text="Bilangan 1:").grid(row=0, column=0)
entry_bil1.grid(row=0, column=1)

tk.Label(app, text="Bilangan 2:").grid(row=1, column=0)
entry_bil2.grid(row=1, column=1)

tk.Label(app, text="Pilih Operasi Aritmatika:").grid(row=2, column=0)
tk.Radiobutton(app, text="+", variable=operator, value="+").grid(row=2, column=1)
tk.Radiobutton(app, text="-", variable=operator, value="-").grid(row=2, column=2)
tk.Radiobutton(app, text=":", variable=operator, value=":").grid(row=2, column=3)
tk.Radiobutton(app, text="x", variable=operator, value="x").grid(row=2, column=4)

tk.Button(app, text="Hitung", command=calculate).grid(row=3, column=1)

tk.Label(app, text="Hasil Penjumlahan:").grid(row=4, column=0)
tk.Label(app, textvariable=result).grid(row=4, column=1)

# Start the main loop
app.mainloop()