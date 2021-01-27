import tkinter as tk 
from tkinter.messagebox import showerror


#milhas para kilometros
def read_number(valor):
    try:
        return float(valor) 
    except ValueError:
        showerror(title="Erro!", message=f'Valor Inválido: {valor}', parent=root)
        return False

def texto_set(entrada, texto):
    entrada.delete(0,tk.END)
    entrada.insert(0,str(texto))
 
def converter():
    km_str = entry_km.get().strip()
    milhas_str = entry_milhas.get().strip()
    if km_str:
        dist_km = read_number(km_str)
        dist_milhas = (dist_km / 1.609344) 
        texto_set(entry_milhas,f'{dist_milhas:.2f}')
        
    elif milhas_str:
        dist_milhas = read_number(milhas_str)
        dist_km = (dist_milhas * 1.609344) 
        texto_set(entry_km,f'{dist_km:.2f}' )
       

root = tk.Tk()
root.title("Conversor")
root.geometry("300x70")

label_km = tk.Label(root, text = 'Quilómetros: ')
label_milhas = tk.Label(root, text="Milhas: ")
entry_km = tk.Entry(root)
entry_milhas = tk.Entry(root)
button = tk.Button(root, text="Converter")

label_km.grid(row=0, column=0, sticky="w")
entry_km.grid(row=0, column= 1, sticky="we")
label_milhas.grid(row=1 , column=0 , sticky="w")
entry_milhas.grid(row=1, column=1, stick="we")
button.grid(row=2, column=0, columnspan=2)


#root.grid_columnconfigure(index=0, weight=0)
root.grid_columnconfigure(index=1, weight=1)

button['command'] = converter


root.mainloop()
