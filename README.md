# CBZ-_Creator
Converts manga stored as raw images into CBZ files

This project provides a Python script that automates the organization and conversion of manga chapters into CBZ (Comic Book Zip) files. The script is designed to traverse a specified directory containing manga series, compress each chapter into its own CBZ file, and then store these files in an organized output directory. This utility is perfect for manga enthusiasts who want to manage their digital manga collection efficiently.

## How It Works

The script scans the specified "mangas" directory, identifies individual manga series and their respective chapters, and compresses each chapter into a CBZ file. The generated CBZ files are then placed in a corresponding series folder within the "manga_output" directory.

## Directory Structure Requirement

For the script to function correctly, your manga must be organized in the following hierarchy:

```
mangas/
├── [Manga Series Name]/
│   ├── Chapter 1/
│   │   ├── page1.jpg
│   │   ├── page2.jpg
│   │   └── ...
│   ├── Chapter 2/
│   └── ...
├── [Another Manga Series Name]/
│   ├── Chapter 1/
│   ├── Chapter 2/
│   └── ...
└── ...
```
## Guidelines:
- Top-Level Folder: Name this folder 'mangas' (or another name of your choice; you will specify this when running the script).
- Manga Series Folders: Each series should have its own folder within the 'mangas' directory, named after the series (e.g., 'Naruto', 'One Piece').
- Chapter Folders: Within each series folder, create individual folders for each chapter, labeled as 'Chapter 1', 'Chapter 2', etc.
- Image Files: Place the image files (pages of the manga) inside the respective chapter folders. These images can be in formats like JPG, PNG, etc.

## Usage Instructions

- Clone/download the repository.
- Ensure Python is installed on your system.
- Navigate to the script directory in your terminal or command prompt.
- Run the script and follow the prompts to enter the path of your 'mangas' folder and the desired output directory for the CBZ files.

## Contributing

Contributions to improve the script or add new features are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.

The GNU GPL v3.0 is a copyleft license that requires anyone who distributes your code or a derivative work to make the source available under the same terms, and also provides an express grant of patent rights from contributors to users.
