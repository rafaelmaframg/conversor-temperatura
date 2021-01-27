import tkinter as tk 
from tkinter.messagebox import showerror


#função para limpar dados e preencher com os novos valores
def texto_set(entry, texto):
    entry.delete(0,tk.END)
    entry.insert(0,str(texto))
    
def convert_to_fahr(*args):
    global trace_fahr
    varfahr.trace_remove("write", trace_fahr)
    celsius_str = entry_celsius.get().strip()
    try:
        temp_celsius = float(celsius_str)
        temp_fahr = (temp_celsius * 1.8) + 32
        texto = f'{temp_fahr:.2f}'
    except:
        texto ="Invalido"
    texto_set(entry_fahr,texto)
    trace_fahr = varfahr.trace('w',convert_to_celsius)

def convert_to_celsius(*args):
    global trace_celsius
    varcelsius.trace_remove('write', trace_celsius)
    fahr_str = entry_fahr.get().strip()
    try:
        temp_fahr = float(fahr_str)
        temp_celsius = (temp_fahr -32) / 1.8
        texto = temp_celsius
    except:
        texto="INVALIDO"
    texto_set(entry_celsius, texto)
    trace_celsius = varcelsius.trace('w', convert_to_fahr)
    
#interface grafica
root = tk.Tk()
root.title("Conversor de Unidades")
root.geometry("300x70")

label_celsius = tk.Label(root, text = 'Celsius: ')
label_fahr = tk.Label(root, text="Fahrenheit: ")
entry_celsius = tk.Entry(root)
entry_fahr = tk.Entry(root)


label_celsius.grid(row=0, column=0, sticky="w")
entry_celsius.grid(row=0, column= 1, sticky="we")
label_fahr.grid(row=1 , column=0 , sticky="w")
entry_fahr.grid(row=1, column=1, stick="we")


#root.grid_columnconfigure(index=0, weight=0)
root.grid_columnconfigure(index=1, weight=1)

varcelsius = tk.StringVar()
varfahr= tk.StringVar()
entry_celsius['textvariable'] = varcelsius
entry_fahr['textvariable'] = varfahr
trace_celsius = varcelsius.trace('w', convert_to_fahr)
trace_fahr = varfahr.trace('w', convert_to_celsius)

root.mainloop()
