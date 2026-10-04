def image():
    import os
    import shutil
    path = r"C:/Users/shirm/OneDrive/Pictures/Pictures and PDF/"
    file_name = os.listdir(path)
    folder_names = ['Image files', 'GIF files', 'Other files', 'PDF files']

    for loop in range(0,4):
        if not os.path.exists(path + folder_names[loop]):
            os.makedirs(path + folder_names[loop])

    for file in file_name:
        if file.lower().endswith(".jpg") and not os.path.exists(path + "Image files/" + file):
            shutil.move(path + file, path + "Image files/" + file)
        elif file.lower().endswith(".png") and not os.path.exists(path + "Image files/" + file):
            shutil.move(path + file, path + "Image files/" + file)
        elif file.lower().endswith(".jpeg") and not os.path.exists(path + "Image files/" + file):
            shutil.move(path + file, path + "Image files/" + file)
        elif file.lower().endswith(".gif") and not os.path.exists(path + "GIF files/" + file):
            shutil.move(path + file, path + "GIF files/" + file)
        elif file.lower().endswith(".pdf") and not os.path.exists(path + "PDF files/" + file):
            shutil.move(path + file, path + "PDF files/" + file)
        elif os.path.isfile(path + file) and not os.path.exists(path + "Other files/" + file):
            shutil.move(path + file, path + "Other files/" + file)
def download():
    import os
    import shutil
    path = r"C:/Users/shirm/Downloads/"
    file_name = os.listdir(path)
    folder_names = ['EXE files','Documents', 'Archives', 'Videos','Audio']

    for loop in range(0,5):
        if not os.path.exists(path + folder_names[loop]):
            os.makedirs(path + folder_names[loop])

    for file in file_name:
        if file.lower().endswith(".exe") and not os.path.exists(path + "EXE files/" + file):
            shutil.move(path + file, path + "EXE files/" + file)
        elif file.lower().endswith(".docx") and not os.path.exists(path + "Documents/" + file):
            shutil.move(path + file, path + "Documents/" + file)
        elif file.lower().endswith(".pptx") and not os.path.exists(path + "Documents/" + file):
            shutil.move(path + file, path + "Documents/" + file)
        elif file.lower().endswith(".xlsx") and not os.path.exists(path + "Documents/" + file):
            shutil.move(path + file, path + "Documents/" + file)
        elif file.lower().endswith(".zip") and not os.path.exists(path + "Archives/" + file):
            shutil.move(path + file, path + "Archives/" + file)
        elif file.lower().endswith(".rar") and not os.path.exists(path + "Archives/" + file):
            shutil.move(path + file, path + "Archives/" + file)
        elif file.lower().endswith(".7z") and not os.path.exists(path + "Archives/" + file):
            shutil.move(path + file, path + "Archives/" + file)
        elif file.lower().endswith(".mp4") and not os.path.exists(path + "Videos/" + file):
            shutil.move(path + file, path + "Videos/" + file)
        elif file.lower().endswith(".mkv") and not os.path.exists(path + "Videos/" + file):
            shutil.move(path + file, path + "Videos/" + file)
        elif file.lower().endswith(".mp3") and not os.path.exists(path + "Audio/" + file):
            shutil.move(path + file, path + "Audio/" + file)
        elif file.lower().endswith(".wav") and not os.path.exists(path + "Audio/" + file):
            shutil.move(path + file, path + "Audio/" + file)
download()
image()
