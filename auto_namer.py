import os

def rename_files_in_folder(folder_path, prefix="file"):
    files = sorted(os.listdir(folder_path))
    count = 1

    for filename in files:
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1]
            new_name = f"{prefix}_{count:03}{ext}"
            new_path = os.path.join(folder_path, new_name)

            os.rename(file_path, new_path)
            print(f"已重新命名：{filename} >> {new_name}")
            count += 1

if __name__ == "__main__":
    folder = input("請輸入資料夾路徑: ")
    prefix = input("請輸入重新命名的檔案名稱: ")
    rename_files_in_folder(folder, prefix)