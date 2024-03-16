import os.path


class ScanFileSorter:
    __original_files = []
    __result_files = []
    __front_pages = []
    __back_pages = []
    __sorted_whole_pages = []

    def Reset(self):
        self.__original_files = []
        self.__result_files = []
        self.__front_pages = []
        self.__back_pages = []
        self.__sorted_whole_pages = []

    def ShowAttributes(self):
        print(f"Original Files: {self.__original_files}")
        print(f"Front Files: {self.__front_pages}")
        print(f"Back Files: {self.__back_pages}")
        print(f"Sorted Whole Files: {self.__sorted_whole_pages}")
        print(f"Result Files: {self.__result_files}")

    def SetFiles(self, files):
        if len(files) % 2 != 0:
            print("Error: File count must be even.")
            return False
        self.Reset()
        self.__original_files = files
        return True

    def RenameAndRenumber(self, new_name="", after_number="", start_num=0, zero_padding=0):
        if zero_padding == 0:
            zero_padding = len(str(len(self.__sorted_whole_pages)))

        # 확장자를 분리하고 새로운 이름을 생성
        self.__result_files = [
            f"{new_name}{i:0{zero_padding}}{after_number}{ext}"
            for i, filename in enumerate(self.__sorted_whole_pages, start=start_num)
            for _, ext in [os.path.splitext(filename)]
        ]

    def SplitByOrder(self, front_reverse: bool, back_reverse: bool):
        half_index = len(self.__original_files) // 2
        self.__front_pages = sorted(self.__original_files[:half_index], reverse=front_reverse)
        self.__back_pages = sorted(self.__original_files[half_index:], reverse=back_reverse)

        # self.__sorted_whole_pages에 front와 back pages를 번갈아 가면서 추가
        self.__sorted_whole_pages = [item for pair in zip(self.__front_pages, self.__back_pages) for item in pair]

    def GetResults(self):
        return self.__sorted_whole_pages, self.__result_files

    # def SetFiles(self, files):
    #     if len(files) % 2 == 1:
    #         return False
    #     self.Reset()
    #     self.__original_files = files
    #     return True
    #
    # def RenameAndRenumber(self, new_name, after_number="", start_num=0, zero_padding=0):
    #     new_whole_page = [os.path.splitext(e) for e in self.__sorted_whole_pages]
    #
    #     if zero_padding == 0:
    #         zero_padding = len(str(len(self.__sorted_whole_pages)))
    #
    #     new_whole_page = [f"{new_name}{i:0{zero_padding}}{after_number}{e[1]}" for i, e in
    #                       enumerate(new_whole_page, start=start_num)]
    #     new_whole_page.sort()
    #     self.__result_files = new_whole_page
    #
    # def SplitByOrder(self, front_reverse: bool, back_reverse: bool):
    #     half_index = len(self.__original_files) // 2
    #     self.__front_pages = self.__original_files[:half_index]
    #     self.__back_pages = self.__original_files[half_index:]
    #
    #     self.__front_pages.sort()
    #     self.__back_pages.sort()
    #
    #     if front_reverse:
    #         self.__front_pages.reverse()
    #
    #     if back_reverse:
    #         self.__back_pages.reverse()
    #
    #     self.__sorted_whole_pages = [e for T in zip(self.__front_pages, self.__back_pages) for e in T]
    #
    # def GetResults(self):
    #     return self.__sorted_whole_pages, self.__result_files


if __name__ == '__main__':
    a = ScanFileSorter()

    files = ["a1.png", "a2.png", "a3.png", "a4.png", "a5.png", "a6.png"]

    a.SetFiles(files)
    a.SplitByOrder(False, True)
    a.RenameAndRenumber("NewFile(", ")", 0, 3)
    a.ShowAttributes()
