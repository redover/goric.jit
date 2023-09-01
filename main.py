import tkinter as tk
from datetime import datetime


def send_click(event=None):
    entered_text = text_entry.get()
    if entered_text:  # Verifica che il campo non sia vuoto
        current_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        label.config(text=f"Hai inserito il pettorale: {entered_text} a {current_time}")
        text_entry.delete(0, tk.END)  # Svuota il campo


def export_click():
    print("Ancora non puoi esportare")


def open_file():
    print("Apre un file")


def show_help():
    print("Mostra aiuto")


# Crea la finestra principale
root = tk.Tk()
root.title("goric.jit")

# Setta i colori per un tema scuro
root.configure(bg="#2e2e2e")

# Crea una barra dei menu
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Exit", command=root.quit)

viewmenu = tk.Menu(menubar, tearoff=0)
# Aggiungi elementi al menu "View" qui

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help", command=show_help)

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="View", menu=viewmenu)
menubar.add_cascade(label="Help", menu=helpmenu)

# Mostra la barra dei menu
root.config(menu=menubar)

# Creazione dei widget
label = tk.Label(root, text="Ciao goditi un togo", bg="#2e2e2e", fg="#ffffff")
label.grid(row=0, column=0, columnspan=2, pady=10)
text_entry = tk.Entry(
    root, width=10, bg="#555555", fg="#ffffff", insertbackground="white"
)
text_entry.grid(row=1, column=0, pady=10, padx=10)
text_entry.bind("<Return>", send_click)
send_button = tk.Button(
    root, text="Invia", command=send_click, bg="#555555", fg="#ffffff"
)
send_button.grid(row=1, column=1, pady=10)
export_button = tk.Button(
    root, text="Export", command=export_click, bg="#555555", fg="#ffffff"
)
export_button.grid(row=2, column=0, pady=10)

root.mainloop()
