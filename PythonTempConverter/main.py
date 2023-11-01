import tkinter as tk

window = tk.Tk()
window.geometry('600x350')

myLabel = tk.Label(window, text="Temperature Converter (°C to °F)", font="Calibri 24 bold")
myLabel.grid(row=0, column=0)

def convertCtoF():
    temp = float(entry.get())
    temp = temp * (9.0/5.0) + 32
    temp_val.set(str(temp) + "°F")

# Input box and Button to Convert
entry = tk.Entry(window)
button = tk.Button(window, text="Convert", command=convertCtoF)
entry.grid(row=1, column=0)
button.grid(row=2, column=0)

temp_val = tk.StringVar()
temp_val.set("---")
temp_label = tk.Label(window, text="--", font="Calibri 24 bold", textvariable=temp_val)
temp_label.grid(row=3, column=0)

window.mainloop()