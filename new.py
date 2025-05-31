import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import Calendar
import csv
import os

FILENAME = "mood_history.csv"
MOODS = ["😊 Feliz", "😔 Triste", "😡 Enojado", "😴 Cansado", "😌 Relajado", "😕 Ansioso", "😍 Enamorado", "😎 Productivo"]

# Crear archivo CSV si no existe
if not os.path.exists(FILENAME):
    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Fecha", "Estado de ánimo"])

class MoodTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mood Tracker con Calendario")
        self.root.geometry("420x500")
        self.root.resizable(False, False)

        tk.Label(root, text="Selecciona una fecha:", font=("Helvetica", 12, "bold")).pack(pady=5)
        self.cal = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
        self.cal.pack(pady=10)

        tk.Label(root, text="Selecciona tu estado de ánimo:", font=("Helvetica", 12, "bold")).pack(pady=10)
        self.selected_mood = tk.StringVar()
        self.selected_mood.set(MOODS[0])
        mood_menu = ttk.Combobox(root, textvariable=self.selected_mood, values=MOODS, state="readonly", font=("Helvetica", 12))
        mood_menu.pack(pady=5)

        tk.Button(root, text="Guardar estado de ánimo", command=self.save_mood, bg="#26755F", fg="white", font=("Helvetica", 12, "bold")).pack(pady=15)
        tk.Button(root, text="Ver historial", command=self.show_history, font=("Helvetica", 12)).pack(pady=5)
        tk.Button(root, text="Exportar a CSV", command=self.export_csv, font=("Helvetica", 12)).pack(pady=5)

    def save_mood(self):
        date = self.cal.get_date()
        mood = self.selected_mood.get()
        with open(FILENAME, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, mood])
        messagebox.showinfo("Guardado", f"Estado '{mood}' para el {date} guardado con éxito.")

    def show_history(self):
        if not os.path.exists(FILENAME):
            messagebox.showwarning("Sin historial", "No hay datos guardados aún.")
            return

        history_win = tk.Toplevel(self.root)
        history_win.title("Historial")
        history_win.geometry("400x300")
        text_area = tk.Text(history_win, wrap="word")
        text_area.pack(fill="both", expand=True)

        with open(FILENAME, mode="r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                text_area.insert("end", f"{row[0]} - {row[1]}\n")

    def export_csv(self):
        if os.path.exists(FILENAME):
            messagebox.showinfo("Exportado", f"Historial guardado en '{FILENAME}'.")
        else:
            messagebox.showerror("Error", "No hay datos para expor.")

# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = MoodTrackerApp(root)
    root.mainloop()
