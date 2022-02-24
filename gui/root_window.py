from . import tk
from .top_frame import TopFrame

class RootWindow(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        
        self.title("Smart Key")
        self.geometry('600x400')
        
        self.frm_main = TopFrame(self)
        self.frm_main.pack()