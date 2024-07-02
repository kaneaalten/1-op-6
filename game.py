import tkinter as tk
from tkinter import messagebox
import random

class MainApp:
    def __init__(self, master):
        # Hoofd venster instellingen
        self.master = master
        self.master.title("Hoofdscherm")
        self.master.geometry("400x300")
        
        self.create_widgets()

    def create_widgets(self):
        # Welkomstlabel
        self.label = tk.Label(self.master, text="Welkom bij de Applicatie!")
        self.label.pack(pady=20)
        
        # Knop om het getallen raden spel te starten
        self.play_button = tk.Button(self.master, text="Start 1 op 6 Spel", command=self.open_getallen_raden)
        self.play_button.pack(pady=10)
        
        # Knop om de applicatie te sluiten
        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.quit)
        self.quit_button.pack(pady=10)
    
    def open_getallen_raden(self):
        # Open een nieuw venster voor het getallen raden spel
        getallen_raden_window = tk.Toplevel(self.master)
        GetallenRadenApp(getallen_raden_window)

class GetallenRadenApp:
    def __init__(self, master):
        # Venster instellingen voor het getallen raden spel
        self.master = master
        self.master.title("1 op 6 Spel")
        self.master.geometry("400x300")
        
        # Willekeurig doelgetal tussen 1 en 6
        self.target_number = random.randint(1, 6)
        self.create_widgets()

    def create_widgets(self):
        # Instructielabel
        self.label = tk.Label(self.master, text="Raad het getal tussen 1 en 6")
        self.label.pack(pady=20)
        
        # Invoerveld voor de gok
        self.entry = tk.Entry(self.master)
        self.entry.pack(pady=10)
        
        # Knop om de gok te controleren
        self.guess_button = tk.Button(self.master, text="Gok!", command=self.check_guess)
        self.guess_button.pack(pady=10)
        
        # Label om resultaten te tonen
        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack(pady=20)
        
    def check_guess(self):
        try:
            # Haal de gok van de gebruiker op en controleer of deze tussen 1 en 6 ligt
            guess = int(self.entry.get())
            if guess < 1 or guess > 6:
                raise ValueError("Getal moet tussen 1 en 6 zijn")
            
            # Geef feedback op basis van de gok
            if guess < self.target_number:
                self.result_label.config(text="Te laag! Probeer opnieuw.")
            elif guess > self.target_number:
                self.result_label.config(text="Te hoog! Probeer opnieuw.")
            else:
                self.result_label.config(text="Gefeliciteerd! Je hebt het juiste getal geraden.")
                self.reset_game()
        except ValueError as e:
            # Toon foutmelding bij ongeldige invoer
            messagebox.showerror("Ongeldige invoer", str(e))
    
    def reset_game(self):
        # Reset het spel met een nieuw doelgetal
        self.target_number = random.randint(1, 6)
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    # Start de hoofdapplicatie
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
