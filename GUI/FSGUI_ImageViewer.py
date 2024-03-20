import tkinter

from FSGUI import *
from PIL import Image, ImageTk


class FSImage:
    kMinMagnificationRate: Final[float] = 25.0
    kMaxMagnificationRate: Final[float] = 300.0
    kZoomStep: Final[float] = 25.0

    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.original_size: Final[tuple[int, int]] = self.image.size

        min_rate = self.kMinMagnificationRate / 100
        max_rate = self.kMaxMagnificationRate / 100

        self.kMinSize: Final[tuple[int, int]] = (int(self.image.width * min_rate), int(self.image.height * min_rate))
        self.kMaxSize: Final[tuple[int, int]] = (int(self.image.width * max_rate), int(self.image.height * max_rate))

        self.ratio: Final[float] = self.image.width / self.image.height
        self.magnification_rate = 100.0

    def SetSize(self, width=0, height=0, size_policy: Literal["fit_width", "fit_height", "none"] = "none"):
        if size_policy == "none":
            width = self.image.width if width == 0 else width
            width = clamp(width, self.kMinSize[0], self.kMaxSize[0])
            height = self.image.height if height == 0 else height
            height = clamp(height, self.kMinSize[1], self.kMaxSize[1])

        elif size_policy == "fit_width":
            width = self.image.width if width == 0 else width
            width = clamp(width, self.kMinSize[0], self.kMaxSize[0])
            height = int(width / self.ratio)

        elif size_policy == "fit_height":
            height = self.image.height if height == 0 else height
            height = clamp(height, self.kMinSize[1], self.kMaxSize[1])
            width = int(height * self.ratio)

        print(width, height)
        self.image = self.image.resize((width, height))
        print(self.image.size)

    def Zoom(self, value, adjustment_type: Literal["offset", "absolute"] = "offset"):
        if adjustment_type == "offset":
            self.magnification_rate += value

        elif adjustment_type == "absolute":
            self.magnification_rate = value

        new_size = self.original_size * (self.magnification_rate / 100)
        self.image = self.image.resize(new_size)


class ImageViewer(tk.Frame):
    image: FSImage
    photo: ImageTk.PhotoImage

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.pack_propagate(False)
        self.configure(relief="solid", borderwidth=5)

        self.image = None
        self.photo = None

        self.image_canvas = tk.Label(self)
        self.image_canvas.pack_propagate(False)
        self.image_canvas.pack(fill="both", expand=True)

    def RefreshImage(self):
        self.photo = ImageTk.PhotoImage(self.image.image, master=self)
        self.image_canvas.configure(image=self.photo)

    def SetImage(self, image_path):
        self.image = FSImage(image_path)
        self.RefreshImage()

    def SetImageSize(self, width=0, height=0, size_policy: FittingModeLiteral = "none"):
        self.image.SetSize(width, height, size_policy)
        self.RefreshImage()


# 사용 예
if __name__ == "__main__":
    image_path = r"..\test\Image01.png"  # 이미지 파일 경로

    window = tk.Tk()
    iv = ImageViewer(window, width=600, height=600)
    iv.SetImage(image_path)
    iv.pack(fill="both", expand=True)

    window.mainloop()
