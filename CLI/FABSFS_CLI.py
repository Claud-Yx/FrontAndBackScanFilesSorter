import os
import LogicModules.FileGetter
import LogicModules.FileNameChanger
import LogicModules.ScanFileSorter
import sys

file_getter = LogicModules.FileGetter.FileGetter()
file_name_changer = LogicModules.FileNameChanger.FileNameChanger()
scan_file_sorter = LogicModules.ScanFileSorter.ScanFileSorter()
running = True

# params
src_dir_path = ""
dst_dir_path = ""
ext = ""
included_name = ""
match_case = True
match_whole_word = False
new_name = ""
new_name_end = ""
start_number = 0
zero_padding = 0
split_policy = "order"
split_policy_values = []


def Reset():
    global src_dir_path
    global dst_dir_path
    global ext
    global included_name
    global match_case
    global match_whole_word
    global new_name
    global new_name_end
    global start_number
    global zero_padding
    global split_policy
    global split_policy_values

    src_dir_path = ""
    dst_dir_path = ""
    ext = ""
    included_name = ""
    match_case = True
    match_whole_word = False
    new_name = ""
    new_name_end = ""
    start_number = 0
    zero_padding = 0
    split_policy = "order"
    split_policy_values = []

    file_getter.Reset()
    file_name_changer.Reset()
    scan_file_sorter.Reset()


def str_to_bool(str):
    if str == "True" or str == "true" or str == "1" or str == "t" or str == "T":
        return True
    else:
        return False


def DecodeOrder(orders):
    global src_dir_path
    global dst_dir_path
    global ext
    global included_name
    global match_case
    global match_whole_word
    global new_name
    global new_name_end
    global start_number
    global zero_padding
    global split_policy
    global split_policy_values

    order_cnt = len(orders)
    order = orders[0]

    # /!
    if order == '/!' or order == '/exit':
        global running
        running = False

    # /?
    elif order == "/?" or order == "/help":
        OutputHelp()

    # /reset
    elif order == "/reset":
        Reset()
        print("All Reset !!!")

    # /src_dir
    elif order == "/src_dir":
        if order_cnt == 2:
            src_dir_path = order[1]
        else:
            src_dir_path = ""
        src_str = src_dir_path if src_dir_path else os.path.curdir
        print(f"Source Directory Path: {src_str}")

    # /dst_dir
    elif order == "/dst_dir":
        if order_cnt == 2:
            dst_dir_path = order[1]
        else:
            dst_dir_path = ""
        dst_str = dst_dir_path if src_dir_path else os.path.curdir
        print(f"Destination Directory Path: {dst_str}")

    # /info
    elif order == "/info":
        OutputInfo()

    # /ext
    elif order == "ext":
        if order_cnt == 2:
            ext = order[1]
        else:
            ext = ""
        ext_str = ext if ext else "ALL"
        print(f"File Extension: {ext_str}")

    # /included_name
    elif order == "/included_name":
        if order_cnt == 2:
            included_name = order[1]
        else:
            included_name = ""
        print(f"File Included Name: {included_name}")

    # /match_case
    elif order == "/match_case":
        if order_cnt == 2:
            match_case = str_to_bool(order[1])
        print(f"Check Match Case: {match_case}")

    # /match_whole_word
    elif order == "/match_whole_word":
        if order_cnt == 2:
            match_whole_word = str_to_bool(order[1])
        print(f"Check Match Whole Word: {match_whole_word}")

    # /nf_new_name
    elif order == "/nf_new_name":
        if order_cnt == 2:
            new_name = order[1]
        else:
            new_name = ""
        print(f"Name Format - New Name: {new_name}")

    # /nf_new_name_end
    elif order == "/nf_new_name_end":
        if order_cnt == 2:
            new_name_end = order[1]
        else:
            new_name_end = ""
        print(f"Name Format - New Name End: {new_name_end}")

    # /nf_start_number
    elif order == "/nf_start_number":
        if order_cnt == 2:
            if order[1].isdigit():
                start_number = int(order[1])
            else:
                start_number = 0
        else:
            start_number = 0
        print(f"Name Format - Start Number: {start_number}")

    # /nf_zero_padding
    elif order == "/nf_zero_padding":
        if order_cnt == 2:
            if order[1].isdigit():
                zero_padding = int(order[1])
            else:
                zero_padding = 0
        else:
            zero_padding = 0
        print(f"Name Format - Zero Padding: {zero_padding}")

    # /split_policy
    elif order == "/split_policy":
        if order_cnt >= 2:
            if order[1] == "order" and order_cnt == 4:
                split_policy = order[1]
                split_policy_values = order[2:]
            else:
                split_policy = "order"
        else:
            split_policy = "order"
        print(f"Split Policy: {split_policy}")
        print(f"└Values: {split_policy_values}")

    # /execute
    elif order == "/execute":
        if order_cnt == 3:
            preserve_original = str_to_bool(order[1])
            allow_destination_duplicate = str_to_bool(order[2])
            print(f"Are you sure? [preserve_original: {preserve_original} | allow_destination_duplicate: {allow_destination_duplicate}] (y/n)")
            ans = input()
            if ans == 'y' or 'yes':
                execute(preserve_original, allow_destination_duplicate)
                print("Processing !!!")
            else:
                print("Canceled !!!")



def OutputInfo():
    print("<========================================= Information =========================================>")
    src_str = src_dir_path if src_dir_path else os.path.abspath(os.path.curdir)
    print(f"Source Directory Path: {src_str}")

    dst_str = dst_dir_path if src_dir_path else os.path.abspath(os.path.curdir)
    print(f"Destination Directory Path: {dst_str}")

    ext_str = ext if ext else "ALL"
    print(f"File Extension: {ext_str}")

    print(f"File Included Name: {included_name}")
    print(f"Check Match Case: {match_case}")
    print(f"Check Match Whole Word: {match_whole_word}")
    print("Name Format")
    print(f"└New Name: {new_name}")
    print(f"└New Name End: {new_name_end}")
    print(f"└Start Number: {start_number}")
    print(f"└Zero Padding: {zero_padding}")
    print(f"Split Policy: {split_policy}")
    print(f"└Values: {split_policy_values}")


def OutputHelp():
    help = r'''
    <=== Common ===>
    /reset: Reset all parameters
    /src_dir ([src_dir_path]=""): Set the source file directory path[Default: Current Path]
    /dst_dir ([dst_dir_path]=""): Set the destination file directory path[Default: Current Path]
    /info: Show parameters
    
    <=== FileGetter ===>
    /ext ([extension]=""): Set the files extension[default: ALL]
    /included_name ([included_name=""]): Set the included name for regex[Default: None]
    /match_case [match_case=True]: bool
    /match_whole_word [match_whole_word=False]: bool 
    
    <=== ScanFileSorter ===>
    nf: Name Format
    /nf_new_name ([new_name=""])
    /nf_new_name_end ([new_name_end=""])
    /nf_start_number ([start_number=0])
    /nf_zero_padding ([zero_padding=0])
        
    /split_policy [by] [Values...]: [default: order]
        by
        - 'order': just sorted order
            Values
            - front_reverse: bool
            - back_reverse: bool
    
    <=== FileNameChanger ===>
    /execute [preserve_original: bool] [allow_destination_duplicate: bool]: Execute name change.
    '''
    print(help)


def execute(preserve_original: bool, allow_destination_duplicate: bool):
    pass


print("===== Front And Back Scan Files Sorter (help: /? | end: /!) =====")
while running:
    print("===>", end='')

    order_input = sys.stdin.readline().rstrip()
    order_split = order_input.split()

    if len(order_split) >= 1:
        DecodeOrder(order_split)
