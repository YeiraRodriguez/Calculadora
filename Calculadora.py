import tkinter as tk
from tkinter import ttk, messagebox

def calculadora(num1, num2, operador):
    resultado=0
    
    if operador=='+':
        resultado=num1 + num2
    elif operador=='-':
        resultado=num1-num2
    elif operador=='*':
        resultado=num1* num2
    elif operador=='/':
        if num2==0:
            messagebox.showerror(message="No es posible division por cero", title="ERROR")
        else:
            resultado=num1/num2
    else:        
            resultado=num1 ** num2
    
    return resultado

def click_calcular(label, num1, num2, operador, unidad, redondeo):
    if num1=='' or num2=='':
        messagebox.showerror(message="Inserte todos los valores", title="ERROR")
        res=0
    else:
        valor1=float(num1)
        valor2=float(num2)
        res=calculadora(valor1, valor2, operador)
        res=round(res, redondeo)

    label.configure(text='Resultado:' + str(res) + str(unidad))

    return res

def seleccion1(label, num1, num2, operador, unidad, redondeo):
    redondeo=1
    click_calcular(label, num1, num2, operador, unidad, redondeo)

def seleccion2(label, num1, num2, operador, unidad, redondeo):
    redondeo=2
    click_calcular(label, num1, num2, operador, unidad, redondeo)

def seleccion3(label, num1, num2, operador, unidad, redondeo):
    redondeo=3
    click_calcular(label, num1, num2, operador, unidad, redondeo)

def click_limpiar(entrada1, entrada2, combo_unidades, label_resultado):
    entrada1.delete(0, 'end')
    entrada2.delete(0, 'end')
    combo_unidades.delete(0, 'end')
    label_resultado.configure(text='Resultado:')      

def init_window():
    window=tk.Tk()
    window.title('Primera Aplicacion')
    window.geometry('550x250')

    label=tk.Label(window, text='Calculadora', font=('Arial bold', 15))
    label.grid(column=0, row=0)

    entrada1=tk.Entry(window, width=10)
    entrada2=tk.Entry(window, width=10)

    entrada1.grid(column=1, row=2)
    entrada2.grid(column=1, row=3)

    label_entrada1=tk.Label(window,text='Ingrese primer numero:', font=('Arial bold', 10))
    label_entrada1.grid(column=0, row=2)

    label_entrada2=tk.Label(window,text='Ingrese segundo numero:', font=('Arial bold', 10))
    label_entrada2.grid(column=0, row=3)  

    label_operador=tk.Label(window, text='Escoja un operador:', font=('Arial bold', 10))
    label_operador.grid(column=0, row=4)

    combo_operadores=ttk.Combobox(window, width = 7)
    combo_operadores['values']=['+','-','*','/','pow']
    combo_operadores.current(0)
    combo_operadores.grid(column=1, row=4)

    label_redondeo=tk.Label(window, text='Escoja cifra de redondeo (0 por defecto):', font=('Arial bold', 10))
    label_redondeo.grid(column=0, row=9)

    redondeo=0
    rad1 = tk.Radiobutton(window,text='Una', value=1, command=lambda: seleccion1(label_resultado, entrada1.get(), entrada2.get(), combo_operadores.get(), combo_unidades.get(), redondeo))
    rad1.grid(column=1, row=9)

    rad2 = tk.Radiobutton(window,text='Dos', value=2, command=lambda: seleccion2(label_resultado, entrada1.get(), entrada2.get(), combo_operadores.get(), combo_unidades.get(), redondeo))
    rad2.grid(column=2, row=9)

    rad3 = tk.Radiobutton(window,text='Tres', value=3, command=lambda: seleccion3(label_resultado, entrada1.get(), entrada2.get(), combo_operadores.get(), combo_unidades.get(), redondeo))
    rad3.grid(column=3, row=9)

    label_unidad=tk.Label(window, text='Escoja una unidad:', font=('Arial bold', 10))
    label_unidad.grid(column=0, row=5)

    combo_unidades=ttk.Combobox(window, width = 7)
    combo_unidades['values']=[' ','cm','m','mm','ft','in']
    combo_unidades.current(0)
    combo_unidades.grid(column=1, row=5)

    boton=tk.Button(window, command=lambda: click_calcular(label_resultado, entrada1.get(), entrada2.get(), combo_operadores.get(), combo_unidades.get(), redondeo), text='Calcular', bg="purple", fg="white")
    boton.grid(column=1, row=6)

    boton_limpiar=tk.Button(window, command=lambda: click_limpiar(entrada1, entrada2, combo_unidades, label_resultado), text='Limpiar', bg="blue", fg="white")
    boton_limpiar.grid(column=1, row=7)

    label_resultado=tk.Label(window, text='Resultado:', font=('Arial bold', 15))
    label_resultado.grid(column=1, row=8)

    window.mainloop()

def main():
    init_window()

main()