import os
import LogicModules.FileGetter
import LogicModules.FileNameChanger
import LogicModules.ScanFileSorter
import sys

file_getter = LogicModules.FileGetter.FileGetter()
file_name_changer = LogicModules.FileNameChanger.FileNameChanger()
scan_file_sorter = LogicModules.ScanFileSorter.ScanFileSorter()


if __name__ == "__main__":
    src = r"C:\Users\ASUS\Documents\Scan\2024_03_14"
    dst = r"C:\Users\ASUS\Documents\Scan\2024_03_14\Dest"
    file_getter.SetFilePath(src)
    file_name_changer.SetSourcePath(src)
    file_name_changer.SetSavePath(dst)

    file_getter.ShowAttributes()
    files = file_getter.GetFiles()

    scan_file_sorter.SetFiles(files)
    scan_file_sorter.SplitByOrder(False, True)
    scan_file_sorter.RenameAndRenumber()
    scan_file_sorter.ShowAttributes()
    src_files, dst_files = scan_file_sorter.GetResults()

    file_name_changer.SetSourceAndDestinationNames(src_files, dst_files)
    file_name_changer.ShowAttributes()
    file_name_changer.ChangeNames(True, False)
