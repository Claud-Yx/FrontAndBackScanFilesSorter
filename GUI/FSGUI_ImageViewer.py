from FSGUI import *
from PIL import Image, ImageTk


# 이미지 뷰어 클래스
class ImageViewer(tk.Tk):
    def __init__(self, image_path):
        super().__init__()
        self.title('Image Viewer')

        # 이미지 로드
        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(self.image)

        # 이미지를 표시할 레이블 위젯
        self.label = tk.Label(self, image=self.photo)
        self.label.pack()


# 사용 예
if __name__ == "__main__":
    image_path = r"C:\Users\ASUS\Documents\Scan\2024_03_14\IMG_0001.png"  # 이미지 파일 경로
    app = ImageViewer(image_path)
    app.mainloop()
