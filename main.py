import tkinter as tk
from datetime import datetime

def send_click(event=None):
    entered_text = text_entry.get()
    if entered_text:  # Verifica che il campo non sia vuoto
        current_time = datetime.now().strftime('%H:%M:%S.%f')[:-3]  # Ora con millisecondi
        label.config(text=f"Hai inserito il pettorale: {entered_text} a {current_time}")
        text_entry.delete(0, tk.END)  # Svuota il campo

def export_click():
    print("Ancora non puoi esportare")

# Variabili comode
pady_variable = 10
padx_variable = 10

# Crea la finestra principale
root = tk.Tk()
root.title("goric.jit")

# Etichetta di verifica aggiunta pettorale
label = tk.Label(root, text="Ciao goditi un togo")
label.grid(row=0, column=0, columnspan=2, pady=pady_variable)

# Campo di inserimento
text_entry = tk.Entry(root, width=10)
# text_entry.pack(pady=10)
text_entry.grid(row=1, column=0, pady=pady_variable, padx=padx_variable)
text_entry.bind('<Return>', send_click)

# Tasto invia
send_button = tk.Button(root, text="Invia", command=send_click)
# send_button.pack(pady=10)
send_button.grid(row=1, column=1, pady=pady_variable)

# Tasto export
export_button = tk.Button(root, text="Export", command=export_click)
# export_button.pack(pady=10)
export_button.grid(row=2, column=0, pady=pady_variable)


root.mainloop()
