import os
import shutil

downloads_folder = os.path.expanduser('~') + '/Downloads/'

file_extensions = {
    'txt': 'TextFiles',
    'pdf': 'PDFs',
    'jpg': 'Images',
    'png': 'Images',
    'zip': 'Archives',
    'exe': 'Executables',
}

for folder_name in file_extensions.values():
    folder_path = os.path.join(downloads_folder, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

for filename in os.listdir(downloads_folder):
    if os.path.isfile(os.path.join(downloads_folder, filename)):
        file_ext = filename.split('.')[-1].lower()
        if file_ext in file_extensions:
            dest_folder = os.path.join(downloads_folder, file_extensions[file_ext])
            shutil.move(os.path.join(downloads_folder, filename), os.path.join(dest_folder, filename))
