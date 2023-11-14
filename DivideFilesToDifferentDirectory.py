import os
import shutil


def move_files_to_parts(source_folder, destination_folder, batch_size=1000):
    file_list = sorted(os.listdir(source_folder))

    for i in range(0, len(file_list), batch_size):
        batch = file_list[i : i + batch_size]
        part_number = i // batch_size + 1
        part_folder = os.path.join(destination_folder, f"part-{part_number}")

        os.makedirs(part_folder, exist_ok=True)

        for file_name in batch:
            source_path = os.path.join(source_folder, file_name)
            destination_path = os.path.join(part_folder, file_name)

            shutil.move(source_path, destination_path)
            print(f"Moved: {source_path} to {destination_path}")


if __name__ == "__main__":
    source_folder = r"C:\Users\heroi\OneDrive\Desktop\desktop4\projects\github\tv-logos\tv-logos\countries\all-countries"
    destination_folder = r"C:\Users\heroi\OneDrive\Desktop\desktop4\projects\github\tv-logos\tv-logos\countries\all-countries"

    move_files_to_parts(source_folder, destination_folder)
