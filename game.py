import tkinter as tk

class MainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Hoofdscherm")
        self.master.geometry("400x300")
        
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Welkom bij de Applicatie!")
        self.label.pack(pady=20)
        
        self.play_button = tk.Button(self.master, text="Start Getallen Raden")
        self.play_button.pack(pady=10)
        
        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.quit)
        self.quit_button.pack(pady=10)



if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()