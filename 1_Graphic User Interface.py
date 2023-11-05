import Functii
import PySimpleGUI as orice #in loc de PySimpleGUI, ,pot inlocui cu: orice!
import time
import os

#pt a putea face exe din acest program si sa ne asiguram ca va exista Activitati.txt, altfel e un bug!
if not os.path.exists("Activitati.txt"):
    with open("Activitati.txt", "w") as file:
        pass

#orice.theme("DarkPurple2") # le gasesti pe net temele
orice.theme("Black")

ceas = orice.Text("", key="ceas")
label = orice.Text("Scrie o activitate:")
input_box = orice.InputText(tooltip="Scrie activitatea", key='todo')
#add_buton = orice.Button("Adauga", size=10) #merge si fara a zice dimensiunea
add_buton = orice.Button(size=10, image_source="add.png", mouseover_colors="LightBlue2", #cand pui mouse-ul pe buton
                         tooltip="Adauga activitatea", key="Adauga") #tooltip e un mesaj pt utilizator

list_box = orice.Listbox(values=Functii.get_activitati(), key="activitati",
                         enable_events=True, size=[45, 10]) #45 reprezinta 45 de caractere pe o linie, si sunt 10 linii afisate
#go to Implementation pe ListBox si pot personaliza de acolo
edit_button = orice.Button("Editeaza")
complete_button = orice.Button(size=10, image_source="complete.png", mouseover_colors="LightBlue2",
                         tooltip="Activitate finalizata", key="Finalizate")

exit_button = orice.Button("Iesire")

fereastra = orice.Window("Lista mea de activitati",
                         layout=[[ceas],
                                 [label],
                                 [input_box, add_buton],
                                 [list_box, edit_button, complete_button],
                                 [exit_button]],
                         font=('Helvetica', 15)) #layout este un argument si asteapta o lista
#layout=[[label, input_box]]) le pune pe o singura linie

while True:
    event, values = fereastra.read(timeout=200) # se repeta la fiecare 200 milisecunde
    fereastra["ceas"].update(value=time.strftime('%d - %b - %Y, %H:%M:%S'))
#    print(1, event)
#    print(2, values)
#    print(3, values['activitati'])
    match event:
        case "Adauga":
            todos = Functii.get_activitati()
            new_activitate = values["todo"] + "\n"
            todos.append(new_activitate)
            Functii.write_activitati(todos)
            fereastra["activitati"].update(values=todos)

        case "Editeaza":
            try:
                todo_to_edit = values["activitati"][0]
                new_todo = values['todo']

                activitati = Functii.get_activitati()
                index = activitati.index(todo_to_edit)
                activitati[index] = new_todo
                Functii.write_activitati(activitati)
                fereastra["activitati"].update(values=activitati) # sa se schimbe in timp real ce am editat in fereastra utilizatorului
            except IndexError:
                orice.popup("Te rog întâi selectează o activitate!", font=("Helvetica", 15))

        case "Finalizate":
            try:
                todo_to_complete = values["activitati"][0]
                activitati= Functii.get_activitati()
                activitati.remove(todo_to_complete)
                Functii.write_activitati(activitati)
                fereastra["activitati"].update(values=activitati)
                fereastra["todo"].update(value="") # empty string sa nu apara nmk in ,,bara"
            except IndexError:
                orice.popup("Te rog întâi selectează o activitate!", font=("Helvetica", 15))

        case "Iesire":
            break

        case 'activitati':  # sa apara ce am selectat in casuta de editat
            fereastra['todo'].update(value=values['activitati'][0])

        case orice.WIN_CLOSED:
            #exit() # ne scoate din program si nu mai ruleaza nmk dupa, nici Bye nu e afisat! (experiment)
            break
#print('Bye')
fereastra.close()