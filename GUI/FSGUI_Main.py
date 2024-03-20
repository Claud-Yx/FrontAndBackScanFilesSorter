from FSGUI import *
import FSGUI_PathGetter as pg
import FSGUI_ImageViewer as iv

class MainGUI(tk.Tk):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.title("Front And Back Scan Files Sorter")
        self.geometry("640x400+100+100")
        self.resizable(False, False)

        # File Paths
        self.path_label_frame = tk.LabelFrame(self, text="Paths")
        self.path_label_frame.pack()
        self.pg_source = pg.PathGetterFrame(self.path_label_frame)
        self.pg_destination = pg.PathGetterFrame(self.path_label_frame)

        self.pg_source.SetFrameName("Source Path")
        self.pg_destination.SetFrameName("Destination Path")

        self.pg_source.pack(side="top", anchor='e')
        self.pg_destination.pack(side="top", anchor='e')


if __name__ == '__main__':
    window = MainGUI()

    window.mainloop()
