from pathlib import Path
import shutil
import os
import winreg


# GET WINDOWS FOLDER PATHS

def folder(name):
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
    )

    value, _ = winreg.QueryValueEx(key, name)
    winreg.CloseKey(key)

    return Path(os.path.expandvars(value))


D = folder("{374DE290-123F-4565-9164-39C4925E467B}")  # Downloads
P = folder("My Pictures")                              # Pictures
M = folder("My Music")                                 # Music
V = folder("My Video")                                 # Videos
DOC = folder("Personal")                               # Documents


# CREATE ORGANIZER FOLDERS

folders = [
    D / "Apps",
    D / "Archives",
    D / "Other",

    P / "Images",
    P / "GIF",

    DOC / "PDF",
    DOC / "PowerPoint",
    DOC / "Text",
    DOC / "Word",
    DOC / "Other"
]

for folder_path in folders:
    folder_path.mkdir(parents=True, exist_ok=True)


# FILE TYPES

IMAGE = {
    ".jpg", ".jpeg", ".png", ".webp",
    ".bmp", ".tif", ".tiff", ".ico", ".svg"
}

AUDIO = {
    ".mp3", ".wav", ".flac", ".aac",
    ".m4a", ".ogg", ".wma", ".opus"
}

VIDEO = {
    ".mp4", ".mkv", ".avi", ".mov",
    ".wmv", ".webm", ".flv", ".m4v"
}

PDF = {
    ".pdf"
}

PPT = {
    ".ppt", ".pptx", ".pps",
    ".ppsx", ".pot", ".potx", ".odp"
}

WORD = {
    ".doc", ".docx", ".docm",
    ".odt", ".rtf"
}

TEXT = {
    ".txt", ".md", ".csv",
    ".log", ".json", ".xml"
}

ARCHIVE = {
    ".zip", ".rar", ".7z",
    ".tar", ".gz", ".bz2",
    ".xz", ".iso"
}

APP = {
    ".exe", ".msi", ".msix",
    ".appx", ".apk", ".deb",
    ".rpm", ".dmg"
}


# MOVE FILE SAFELY

def move_file(file, destination):
    new_file = destination / file.name
    number = 1

    # Avoid overwriting files
    while new_file.exists():
        new_file = destination / f"{file.stem} ({number}){file.suffix}"
        number += 1

    shutil.move(str(file), str(new_file))

    print(f"{file.name} -> {new_file}")



# ORGANIZE PICTURES

for file in list(P.iterdir()):

    if not file.is_file():
        continue

    extension = file.suffix.lower()

    if extension in IMAGE:
        move_file(file, P / "Images")

    elif extension == ".gif":
        move_file(file, P / "GIF")



# ORGANIZE DOWNLOADS


for file in list(D.iterdir()):

    # Ignore folders
    if not file.is_file():
        continue

    extension = file.suffix.lower()

    if extension in IMAGE:
        move_file(file, P / "Images")

    elif extension == ".gif":
        move_file(file, P / "GIF")

    elif extension in AUDIO:
        move_file(file, M)

    elif extension in VIDEO:
        move_file(file, V)

    elif extension in ARCHIVE:
        move_file(file, D / "Archives")

    elif extension in APP:
        move_file(file, D / "Apps")

    else:
        move_file(file, D / "Other")



# ORGANIZE DOCUMENTS


for file in list(DOC.iterdir()):

    if not file.is_file():
        continue

    extension = file.suffix.lower()

    if extension in PDF:
        move_file(file, DOC / "PDF")

    elif extension in PPT:
        move_file(file, DOC / "PowerPoint")

    elif extension in WORD:
        move_file(file, DOC / "Word")

    elif extension in TEXT:
        move_file(file, DOC / "Text")

    else:
        move_file(file, DOC / "Other")


# FINISHED

print("\nFiles organized successfully.")
input("Press Enter to close...")
