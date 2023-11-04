import PySimpleGUI as sg
from zip_extractor import extract_archive

sg.theme("Black")

label1 = sg.Text("Selecteaza arhiva:")
input1 = sg.Input()
alege_buton1 = sg.FileBrowse("Alege", key="arhiva") #am pus FileBrowse, nu FilesBrowse!

label2 = sg.Text("Selecteaza destinatia:")
input2 = sg.Input()
alege_buton2 = sg.FolderBrowse("Alege", key="folder")

extract_button = sg.Button("Extrage")
output_label = sg.Text(key="output", text_color="green") #mesajul de dupa comprimare pt utilizator

fereastra = sg.Window("Archive Extractor",
                      layout=[[label1, input1, alege_buton1],
                              [label2, input2, alege_buton2],
                              [extract_button, output_label]])
while True:
    event, values = fereastra.read()
    print(event, values)
    archive_path = values["arhiva"]
    dest_dir = values["folder"]
    extract_archive(archive_path, dest_dir)
    fereastra["output"].update(value="Extragerea a fost terminata cu succes!")
fereastra.close()