from FSGUI import *
import FSGUI_ImageViewer as iv


class ImageViewerWindow(tk.Toplevel):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        # Button Style
        self.ActivatedButtonStyle = Style()
        self.DeactivatedButtonStyle = Style()

        self.minsize(500, 600)
        self.maxsize(parent.winfo_screenwidth(), parent.winfo_screenheight())

        self.ActivatedButtonStyle.configure("Activated.TButton", background="blue")
        self.DeactivatedButtonStyle.configure("Deactivated.TButton")

        # frames
        self.button_frame = Frame(self)
        self.button_frame.pack(side="top", anchor="center")

        # ImageViewer
        self.image_viewer = iv.ImageViewer(self, padx=2, pady=2)
        self.image_viewer.pack(side="top", padx=10, pady=10, fill="both", expand=True)

        # buttons
        self.fitting_mode: FittingModeLiteral = "none"
        self.zoom_in_button = Button(self.button_frame, text="+", width=5)
        self.zoom_out_button = Button(self.button_frame, text="-", width=5)
        self.fit_width_button = Button(self.button_frame, text="↔", width=5, command=self._ActivateFitWidth_ButtonFunc)
        self.fit_height_button = Button(self.button_frame, text="↕", width=5, command=self._ActivateFitHeight_ButtonFunc)
        self.fit_screen_button = Button(self.button_frame, text="▣", width=5)
        self.original_size_button = Button(self.button_frame, text="100%", width=5)

        # Label
        self.magnification_rate = tk.StringVar(self.button_frame, value="None")
        self.magnification_rate_label = Label(self.button_frame, textvariable=self.magnification_rate)

        self.fit_width_button.pack(side='left', anchor='center')
        self.fit_height_button.pack(side='left', anchor='center')
        self.zoom_out_button.pack(side='left', anchor='center')
        self.magnification_rate_label.pack(side='left', anchor='center')
        self.zoom_in_button.pack(side='left', anchor='center')
        self.fit_screen_button.pack(side='left', anchor='center')
        self.original_size_button.pack(side='left', anchor='center')

        self.fitting_buttons = [
            self.fit_width_button,
            self.fit_height_button,
            self.fit_screen_button,
            self.original_size_button
        ]

    def ImageChange(self, image_path):
        self.image_viewer.SetImage(image_path)

    def _SwitchFittingMode(self, mode: FittingModeLiteral, button: Button):
        if self.fitting_mode != mode:
            self.fitting_mode = mode
            button.configure(style="Activated.TButton")
        else:
            self.fitting_mode = "none"
            button.configure(style="Deactivated.TButton")

    def _ActivateFitWidth_ButtonFunc(self):
        self._SwitchFittingMode("fit_width", self.fit_width_button)

    def _ActivateFitHeight_ButtonFunc(self):
        self._SwitchFittingMode("fit_height", self.fit_height_button)


if __name__ == '__main__':
    window = tk.Tk()
    window.title("main window")
    window.geometry("500x500")

    app = ImageViewerWindow(window)
    app.geometry("720x1080")
    app.title("top level")
    app.ImageChange(r"..\test\Image01.png")

    window.mainloop()
