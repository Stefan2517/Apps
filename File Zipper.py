import PySimpleGUI as sg

label1 = sg.Text("Selecteaza fisiere pentru compresie:")
input1 = sg.Input()
alege_buton1 = sg.FilesBrowse("Alege")

label2 = sg.Text("Selecteaza destinatia:")
input2 = sg.Input()
alege_buton2 = sg.FolderBrowse("Alege")

compress_button = sg.Button("Comprima")

fereastra = sg.Window("File Zipper",
                      layout=[[label1, input1, alege_buton1],
                              [label2, input2, alege_buton2],
                              [compress_button]])

fereastra.read()
fereastra.close()

