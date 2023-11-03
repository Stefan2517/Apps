import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Selecteaza fisiere pentru compresie:")
input1 = sg.Input()
alege_buton1 = sg.FilesBrowse("Alege", key="fisiere")

label2 = sg.Text("Selecteaza destinatia:")
input2 = sg.Input()
alege_buton2 = sg.FolderBrowse("Alege", key="folder")

compress_button = sg.Button("Comprima")
output_label = sg.Text(key="output", text_color="yellow") #mesajul de dupa comprimare pt utilizator

fereastra = sg.Window("File Zipper",
                      layout=[[label1, input1, alege_buton1],
                              [label2, input2, alege_buton2],
                              [compress_button, output_label]])

while True:
    event, valori = fereastra.read()
    print(event, valori)
    calea_spre_fisiere = valori["fisiere"].split(";")
    folder = valori["folder"]
    make_archive(calea_spre_fisiere, folder)
    fereastra["output"].update(value="Compresia a fost incheiata cu succes!") #mesaj cu statusul pt utilizator

fereastra.close()

