from utils.folder_visitor import visit_folders, restore_files

if __name__ == "__main__":
    mode = input("Enter mode (extract/restore): ").strip().lower()
    folder_path = input("Enter the folder path to visit: ")
    
    if(folder_path is ""):
        folder_path = "D:\\ImageData\\23년 1분기"
        
    if mode == "extract":
        visit_folders(folder_path)
    elif mode == "restore":
        dest_folder = input("Enter the folder path where the files are stored: ").strip()
        if not dest_folder:
            dest_folder = "D:\\DestFolder"
        restore_files(dest_folder, folder_path)
    else:
        print("Invalid mode. Please enter 'extract' or 'restore'.")