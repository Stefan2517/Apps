import zipfile
import pathlib

def make_archive(filepaths, destination_director):
    #with zipfile.ZipFile(destination_director + "/" + "compressed.zip", "w") as archive: sau folosesc pathlib!
    dest_path = pathlib.Path(destination_director, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath) #pt ca la crearea folderului compresat sa nu apara calea fisierelor initiale
            archive.write(filepath, arcname=filepath.name) #pt a extrage denumirea fisierului

if __name__ == "__main__":
    make_archive(filepaths=["Functii.py", "data.txt"], destination_director="dest")