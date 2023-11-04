import zipfile

def extract_archive(archive_path, dest_dir):
    with zipfile.ZipFile(archive_path,"r") as archive1:
        archive1.extractall(dest_dir)

if __name__=="__main__":
    extract_archive(r"C:\Users\Asus\Desktop\Udemy\dest\compressed.zip",
                    r"C:\Users\Asus\Desktop") #am pus r deoarece aveam urmatoarea eroare:
#SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 0-

# aici am testat programul cu liniile de cod de la linia 7