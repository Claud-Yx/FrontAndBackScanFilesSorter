import os
import re

debug = False


# if __name__ == "__main__":
#     debug = True

class FileGetter:
    __file_path = ""
    __file_extension = ""
    __re_included_file_name = re.compile('')
    __match_case = True
    result_file_paths = []

    def Reset(self):
        self.__file_path = ""
        self.__file_extension = ""
        self.__re_included_file_name = re.compile('')
        self.__match_case = True
        self.result_file_paths = []

    def ShowAttributes(self):
        print("File Path:", self.__file_path)
        print("File Extension:", self.__file_extension)
        print("Included File Name:", self.__re_included_file_name.pattern)
        print("Match Case:", self.__match_case)

    def SetFileExtension(self, ext=""):
        self.__file_extension = f".{ext.lstrip('.')}" if ext else ""

    def SetFilePath(self, path: str):
        # 경로 정규화
        self.__file_path = os.path.normpath(path)

    def SetIncludedFileName(self, included_name: str, in_match_case=True, in_match_whole_word=False):
        self.__match_case = in_match_case
        flags = 0 if in_match_case else re.IGNORECASE
        if in_match_whole_word:
            pattern = r'\b' + re.escape(included_name) + r'\b'
        else:
            pattern = re.escape(included_name)
        self.__re_included_file_name = re.compile(pattern, flags)

    def GetFilePath(self):
        return self.__file_path

    def GetFiles(self):
        if not os.path.exists(self.__file_path):
            return []

        files = [file for file in os.listdir(self.__file_path) if os.path.isfile(os.path.join(self.__file_path, file))]
        files.sort()

        filtered_files = []
        for file in files:
            name, ext = os.path.splitext(file)
            if self.__file_extension and ext != self.__file_extension:
                continue
            if self.__re_included_file_name.search(name):
                filtered_files.append(file)

        return filtered_files


if __name__ == "__main__":
    a = FileGetter()

    print("Test 1 ===================================================================================================>")
    a.SetFilePath("a\\b\\c/d/e\\f/g")
    a.SetIncludedFileName("")
    a.SetIncludedFileName("IMG", True, False)
    a.SetFileExtension(".jpg")
    a.SetFileExtension("")
    a.SetFileExtension("png")
    a.ShowAttributes()

    print("Test 2 ===================================================================================================>")
    a.Reset()
    a.SetFilePath(r"C:\Users\ASUS\Documents\Scan\2024_03_13")
    a.SetFileExtension(".jpg")
    a.SetIncludedFileName("")
    b = a.GetFiles()
    print(b)

    print("Test 3 ===================================================================================================>")
    a.Reset()
    a.SetFilePath(r"C:\Users\ASUS\Documents\Scan\2024_03_13\Test")
    a.SetIncludedFileName("IMG", True, False)
    a.ShowAttributes()
    b = a.GetFiles()
    print(b)

    print("Test 4 ===================================================================================================>")
    a.Reset()
    a.SetFilePath(r"C:\Users\ASUS\Documents\Scan\2024_03_13\Test")
    a.SetIncludedFileName("IMG", False, False)
    a.ShowAttributes()
    b = a.GetFiles()
    print(b)

    print("Test 5 ===================================================================================================>")
    a.Reset()
    a.SetFilePath(r"C:\Users\ASUS\Documents\Scan\2024_03_13\Test")
    a.SetIncludedFileName("IMG", False, True)
    a.ShowAttributes()
    b = a.GetFiles()
    print(b)

    print("Test 6 ===================================================================================================>")
    a.Reset()
    a.SetFilePath(r"C:\Users\ASUS\Documents\Scan\2024_03_13\Test")
    a.SetFileExtension("jpg")
    a.ShowAttributes()
    b = a.GetFiles()
    print(b)

    print("Test 6 ===================================================================================================>")
    a.Reset()
    a.SetFilePath(r"C:\Users\ASUS\Documents\Scan\2024_03_13\Test")
    a.SetIncludedFileName("IMG", True, False)
    a.SetFileExtension("png")
    a.ShowAttributes()
    b = a.GetFiles()
    print(b)
