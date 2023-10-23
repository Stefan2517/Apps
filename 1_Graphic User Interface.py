import Functii
import PySimpleGUI as orice #in loc de PySimpleGUI, ,pot inlocui cu: orice!

label = orice.Text("Scrie o activitate:")
input_box = orice.InputText(tooltip="Scrie activitatea", key='todo')
add_buton = orice.Button("Adauga")
list_box = orice.Listbox(values=Functii.get_activitati(), key="activitati",
                         enable_events=True, size=[45, 10])
edit_button = orice.Button("Editeaza")


fereastra = orice.Window("Lista mea de activitati",
                         layout=[[label], [input_box, add_buton], [list_box, edit_button]],
                         font=('Helvetica', 15)) #layout este un argument si asteapta o lista
#layout=[[label, input_box]]) le pune pe o singura linie

while True:
    event, values = fereastra.read()
    print(1, event)
    print(2, values)
    print(3, values['activitati'])
    match event:
        case "Adauga":
            todos = Functii.get_activitati()
            new_activitate = values["todo"] + "\n"
            todos.append(new_activitate)
            Functii.write_activitati(todos)
            fereastra["activitati"].update(values=todos)

        case "Editeaza":
            todo_to_edit = values["activitati"][0]
            new_todo = values['todo']

            activitati = Functii.get_activitati()
            index = activitati.index(todo_to_edit)
            activitati[index] = new_todo
            Functii.write_activitati(activitati)
            fereastra["activitati"].update(values=activitati) # sa se schimbe in timp real ce am editat in fereastra utilizatorului
        case 'activitati':  # sa apara ce am selectat in casuta de editat
            fereastra['todo'].update(value=values['activitati'][0])

        case orice.WIN_CLOSED:
            break

fereastra.close()