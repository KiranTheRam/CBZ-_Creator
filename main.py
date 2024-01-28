# <CBZ_Creator. Script to create CBZ files out of loose images>
# Copyright (C) <2024> <Kiran Ramjisingh>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
