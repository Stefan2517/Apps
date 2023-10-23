import Functii
import PySimpleGUI as orice #in loc de PySimpleGUI, ,pot inlocui cu: orice!

label = orice.Text("Scrie o activitate:")
input_box = orice.InputText(tooltip="Scrie activitatea", key='todo')
add_buton = orice.Button("Adauga")

fereastra = orice.Window("Lista mea de activitati",
                         layout=[[label], [input_box, add_buton]],
                         font=('Helvetica', 15)) #layout este un argument si asteapta o lista
#layout=[[label, input_box]]) le pune pe o singura linie

while True:
    event, values = fereastra.read()
    print(event)
    print(values)
    match event:
        case "Adauga":
            todos = Functii.get_activitati()
            new_activitate = values["todo"] + "\n"
            todos.append(new_activitate)
            Functii.write_activitati(todos)

        case orice.WIN_CLOSED:
            break

fereastra.close()