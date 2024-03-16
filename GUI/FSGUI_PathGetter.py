import tkinter

from FSGUI import *


class PathGetterFrame(Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.path = tk.StringVar(self, value="Path Here", name="path")

        self.path_label = tk.Text(self)
        self.path_label.configure(
            relief="solid",
            pady=2,
            padx=2,
            width=30,
            height=0
        )
        self.path_label.insert(0.0, self.path.get())

        #         (
        #     textvariable=self.path,
        #     relief="solid",
        #     borderwidth=2,
        #     padding=2,
        # )
        self.path_label.pack(side="left", anchor="w")

        self.path_getter_button = Button(self)
        self.path_getter_button.pack(side="left", anchor="e")


if __name__ == '__main__':
    window = tk.Tk()
    window.geometry("600x300")

    pg_frame = PathGetterFrame(window)
    pg_frame.pack()

    window.mainloop()



