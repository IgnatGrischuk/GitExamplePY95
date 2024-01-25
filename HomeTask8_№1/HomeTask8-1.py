import os
import shutil


def get_os_name():
    return os.name


def get_current_directory():
    return os.getcwd()


def sort_files_by_extension(folder_path):
    files = [f for f in os.listdir(folder_path) if
             os.path.isfile(os.path.join(folder_path, f))]
    sorted_files = {}

    for file in files:
        file_extension = file.split('.')[-1]
        if file_extension not in sorted_files:
            sorted_files[file_extension] = [file]
        else:
            sorted_files[file_extension].append(file)

    return sorted_files


def move_files_to_folders(folder_path, sorted_files):
    for extension, files in sorted_files.items():
        destination_folder = os.path.join(folder_path, extension)
        os.makedirs(destination_folder, exist_ok=True)

        for file in files:
            source_path = os.path.join(folder_path, file)
            destination_path = os.path.join(destination_folder, file)

            shutil.move(source_path, destination_path)


def rename_file(file_path, new_name):
    try:
        directory, old_name = os.path.split(file_path)
        new_path = os.path.join(directory, new_name)
        os.rename(file_path, new_path)
        print(f"Файл {old_name} был переименован в {new_name}")
    except Exception as e:
        print(f"Ошибка при переименовании файла {file_path}: {e}")


def main():
    folder_path = get_current_directory()

    print("Имя вашей ОС:", get_os_name())
    print("Путь до текущей папки:", folder_path)

    sorted_files = sort_files_by_extension(folder_path)
    move_files_to_folders(folder_path, sorted_files)

    for extension, files in sorted_files.items():
        total_size = 0
        for file in files:
            file_path = os.path.join(folder_path, extension, file)
            total_size += os.path.getsize(file_path)

        print(
            f"В папке с {extension} файлами перемещено {len(files)} файлов, "
            f"их суммарный размер - {total_size / (1024 ** 3):.2f} гигабайт")

    if 'txt' in sorted_files:
        file_to_rename = sorted_files['txt'][0]
        new_name = 'some_' + file_to_rename
        rename_file(os.path.join(folder_path, 'txt', file_to_rename), new_name)


if __name__ == "__main__":
    main()
