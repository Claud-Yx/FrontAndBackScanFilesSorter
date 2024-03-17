import tkinter
import tkinter.filedialog

from FSGUI import *


class PathGetterFrame(Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # Frame Name Label
        self.frame_name_label = tk.Label(self)
        self.frame_name = tk.StringVar(
            master=self,
            value="Frame Name"
        )
        self.frame_name_label.configure(
            textvariable=self.frame_name
        )
        self.frame_name_label.pack(side="left")

        # Path Label(Text)
        self.path = tk.StringVar(self, value="Path Here", name="path")
        self.path_label = tk.Text(self)
        self.path_label.configure(
            state="disabled",
            relief="groove",
            pady=2,
            padx=2,
            wrap="none",
            width=40,
            height=0
        )
        self._ChangePath("Path Here")
        self.path_label.pack(side="left")

        # Path Getter Button(Button)
        self.path_getter_button = Button(
            self,
            text="...",
            width=2,
            command=self._GetPath_ButtonFunc)
        self.path_getter_button.pack(side="left")

    def _ChangePath(self, text):
        self.path.set(text)
        self.path_label.configure(state="normal")
        self.path_label.delete(1.0, "end")
        self.path_label.insert(1.0, self.path.get())
        self.path_label.configure(state="disabled")

    def _GetPath_ButtonFunc(self):
        path = tkinter.filedialog.askdirectory(
            parent=self.path_getter_button,
            initialdir='./'
        )
        self._ChangePath(path)

    def SetFrameName(self, text):
        self.frame_name.set(text)

    def GetPath(self):
        return self.path.get()


if __name__ == '__main__':
    window = tk.Tk()
    window.geometry("600x300")

    pg_frame1 = PathGetterFrame(window)
    pg_frame2 = PathGetterFrame(window)
    pg_frame1.pack()
    pg_frame2.pack()

    pg_frame1.SetFrameName("Hello")
    pg_frame2.SetFrameName("Hi")

    window.mainloop()
