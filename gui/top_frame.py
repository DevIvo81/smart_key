from . import tk

class TopFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        self.columnconfigure((0, 1, 2, 3), weight=1)
        self.columnconfigure(4, weight=6)
        
        self.lbl_welcome = tk.Label(self, 
                                    text='Dobro došli',
                                    font = ('Segoe UI', 16))
        self.lbl_welcome.grid(row=0, column=0, columnspan=5)
        
        self.button_pozvoni = tk.Button(self, text='Pozvoni', font = ('Segoe UI', 16))
        self.button_pozvoni.grid(row=1, column=0, sticky='nsew')
        
        self.button_otkljucaj = tk.Button(self, text='Otkljucaj', font = ('Segoe UI', 16))
        self.button_otkljucaj.grid(row=1, column=4, sticky='nsew')