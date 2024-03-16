import os
import re
import shutil
import send2trash


class FileNameChanger:
    __save_path = ""
    __src_path = ""
    __src_names = []
    __dst_names = []

    def Reset(self):
        self.__save_path = ""
        self.__src_path = ""
        self.__src_names = []
        self.__dst_names = []

    def ShowAttributes(self):
        print("Save Path:", self.__save_path)
        print("Source Path:", self.__src_path)
        print("=== File Name Change List ===")
        for i in range(len(self.__src_names)):
            print(self.__src_names[i], "->", self.__dst_names[i])

    def SetSourceAndDestinationNames(self, src_names, dst_names):
        if not len(src_names) == len(dst_names):
            return False
        self.__src_names = src_names
        self.__dst_names = dst_names

    def SetSavePath(self, new_path):
        self.__save_path = os.path.normpath(new_path)

    def SetSourcePath(self, new_path):
        self.__src_path = os.path.normpath(new_path)

    @staticmethod
    def CheckPathValidation(path):
        return os.path.exists(path)

    @staticmethod
    def TryGetDestinationFileAltName(dst_path):
        base_name, file_ext = os.path.splitext(dst_path)
        unique_number = 0
        while os.path.exists(dst_path):
            dst_path = f"{base_name}({unique_number}){file_ext}"
            unique_number += 1
        return dst_path

    @staticmethod
    def TryRemoveDestinationFile(dst_path):
        if os.path.exists(dst_path):
            send2trash.send2trash(dst_path)

    def ChangeNames(self, preserve_original: bool, allow_destination_duplicate: bool):
        if not self.CheckPathValidation(self.__save_path):
            return f"Invalid Save Path: {self.__save_path}"

        for src_name, dst_name in zip(self.__src_names, self.__dst_names):
            src = os.path.join(self.__src_path, src_name)

            if not os.path.exists(src):
                return f"Source file does not exist: {src}"

            dst = os.path.join(self.__save_path, dst_name)

            if allow_destination_duplicate:
                dst = self.TryGetDestinationFileAltName(dst)
            else:
                self.TryRemoveDestinationFile(dst)

            shutil.copyfile(src, dst)

            if not preserve_original:
                send2trash.send2trash(src)


if __name__ == '__main__':
    a = FileNameChanger()

    a.SetSourcePath(r"C:\Users\ASUS\Documents\Scan\2024_03_13\Test")
    a.SetSavePath(r"C:\Users\ASUS\Documents\Scan\2024_03_13\Test\dst")

    src_names = ["img tmp.png"]
    dst_names = ["img tmp1.png"]

    a.SetSourceAndDestinationNames(src_names, dst_names)
    a.ShowAttributes()

    a.ChangeNames(True, True)
