import tkinter as tk 
from tkinter.messagebox import showerror


#função para tratamento de erro, caso o usuario não insira um valor numerico valido.
def read_number(valor):
    try:
        return float(valor) 
    except ValueError:
        showerror(title="Erro!", message=f'Valor Inválido: {valor}', parent=root)
        return False
#função para limpar dados e preencher com os novos valores
def texto_set(entry, texto):
    entry.delete(0,tk.END)
    entry.insert(0,str(texto))

#função principal do programa, aqui é realizado toda a conversão da temperatura    
def converter():
    celsius_str = entry_celsius.get().strip()
    fahr_str = entry_fahr.get().strip()
    if celsius_str:
        temp_celsius = read_number(celsius_str)
        temp_fahr = (temp_celsius * 1.8) + 32
        texto_set(entry_fahr,temp_fahr)
        
    elif fahr_str:
        temp_fahr = read_number(fahr_str)
        temp_celsius = (temp_fahr -32) / 1.8
        texto_set(entry_celsius, temp_celsius)
       
#interface grafica
root = tk.Tk()
root.title("Conversor de Unidades")
root.geometry("300x70")

label_celsius = tk.Label(root, text = 'Celsius: ')
label_fahr = tk.Label(root, text="Fahrenheit: ")
entry_celsius = tk.Entry(root)
entry_fahr = tk.Entry(root)
button = tk.Button(root, text="Converter")

label_celsius.grid(row=0, column=0, sticky="w")
entry_celsius.grid(row=0, column= 1, sticky="we")
label_fahr.grid(row=1 , column=0 , sticky="w")
entry_fahr.grid(row=1, column=1, stick="we")
button.grid(row=2, column=0, columnspan=2)


#root.grid_columnconfigure(index=0, weight=0)
root.grid_columnconfigure(index=1, weight=1)

button['command'] = converter


root.mainloop()
