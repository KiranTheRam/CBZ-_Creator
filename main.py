import os
import zipfile

def zipdir(path, ziph):
    # Zip the files in a directory
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))

def create_cbz(manga_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for series in os.listdir(manga_dir):
        series_path = os.path.join(manga_dir, series)
        if os.path.isdir(series_path):
            series_output = os.path.join(output_dir, series)
            if not os.path.exists(series_output):
                os.makedirs(series_output)

            for chapter in os.listdir(series_path):
                chapter_path = os.path.join(series_path, chapter)
                if os.path.isdir(chapter_path):
                    cbz_filename = f"{chapter}.cbz"
                    cbz_path = os.path.join(series_output, cbz_filename)
                    with zipfile.ZipFile(cbz_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                        zipdir(chapter_path, zipf)

# User input for directories
manga_dir = input("Enter the path to your mangas folder: ")
output_dir = input("Enter the path to the manga_output folder: ")

create_cbz(manga_dir, output_dir)
