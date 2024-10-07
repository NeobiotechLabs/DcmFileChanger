import os
import shutil

def check_scans_and_ct_data(folder_path):
    scans_exist = False
    ct_data_exist = False

    for entry in os.listdir(folder_path):
        entry_path = os.path.join(folder_path, entry)
        if os.path.isdir(entry_path):
            if entry == "Scans":
                scans_exist = True
            dcm_count = sum(1 for f in os.listdir(entry_path) if f.endswith('.dcm'))
            if dcm_count >= 100:
                ct_data_exist = True

    return scans_exist, ct_data_exist

def copy_dcm_files(src_folder, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    parent_dir_name = os.path.basename(os.path.dirname(src_folder))

    for subdir in ['Lower', 'Upper']:
        subdir_path = os.path.join(src_folder, subdir)
        if os.path.exists(subdir_path):
            for file_name in os.listdir(subdir_path):
                if file_name.endswith('.dcm'):
                    src_file = os.path.join(subdir_path, file_name)
                    new_file_name = f"{parent_dir_name}_Scans_{subdir}_{file_name}"
                    dest_file = os.path.join(dest_folder, new_file_name)
                    shutil.copy2(src_file, dest_file)
                    print(f"Copied {src_file} to {dest_file}")
                    
def visit_folders(folder_path):
    def perform_action(entry_path):        
        scans_exist, ct_data_exist = check_scans_and_ct_data(entry_path)
        print(f"Scans exist: {scans_exist}, CT data exist: {ct_data_exist}")
        
        if scans_exist:
            dest_folder = "D:\\DestFolder"  # Change this to your desired destination folder
            copy_dcm_files(os.path.join(entry_path, "Scans"), dest_folder)
        
        pass  # Placeholder for additional actions

    for entry in os.listdir(folder_path):
        entry_path = os.path.join(folder_path, entry)
        if os.path.isdir(entry_path):
            print(f"Visiting folder: {entry_path}")
            perform_action(entry_path)

def restore_files(src_folder, base_folder):
    for file_name in os.listdir(src_folder):
        if not file_name.endswith('.dcm'):
            parts = file_name.split('_')
            if len(parts) >= 4:
                original_file_name = parts[-1]
                subdir = parts[-2]
                scans_folder = parts[-3]
                parent_dir_name = '_'.join(parts[:-3])
                dest_folder = os.path.join(base_folder, parent_dir_name, scans_folder, subdir)
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                src_file = os.path.join(src_folder, file_name)
                dest_file = os.path.join(dest_folder, original_file_name)
                shutil.copy2(src_file, dest_file)
                print(f"Restored {src_file} to {dest_file}")