import Functii
import PySimpleGUI as orice #in loc de PySimpleGUI, ,pot inlocui cu: orice!

label = orice.Text("Scrie o activitate:")
input_box = orice.InputText(tooltip="Scrie activitatea")
add_buton = orice.Button("Adauga")

fereastra = orice.Window("Lista mea de activitati", layout=[[label], [input_box, add_buton]]) #layout este un argument si asteapta o lista
#layout=[[label, input_box]]) le pune pe o singura linie
fereastra.read()
#print("Hello")
fereastra.close()