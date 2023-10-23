'''
def get_activitati(filepath='activitati.txt'): #acm e implicita calea/argumentul si in apelarea functiei
    with open(filepath, 'r') as fisier_local:
        activitati_local = fisier_local.readlines()
    return activitati_local


def write_activitati(activitati_arg, filepath='activitati.txt'):#activitati_arg am pus inaintea celuilat pt a elimina eroarea, parametrul ce nu are nmk implicit setat se pune primul!
    with open(filepath, 'w') as fisier_local:
        fisier_local.writelines(activitati_arg)

while True:
    alegerile_utilizatorului = input('Alege din urmatoarele: Adauga, Prezinta, Editeaza, Finalizate sau Iesire')
    alegerile_utilizatorului =  alegerile_utilizatorului.strip()

    if alegerile_utilizatorului.startswith('Adauga'): # daca incepe cu Adauga...
        activitate = alegerile_utilizatorului[7:]

        activitati = get_activitati()

        activitati.append(activitate + '\n')

        write_activitati(filepath='activitati.txt',activitati_arg=activitati) #daca le declar nu e nevoie sa le scriu in ordinea lor

    elif alegerile_utilizatorului.startswith('Prezinta'):
        activitati = get_activitati()

        for index, actiune in enumerate(activitati):
            actiune = actiune.strip('\n')
            K = f'{index +1}-{actiune}'
            print(K)

    elif alegerile_utilizatorului.startswith('Editeaza'):
        try:
            numar = int(alegerile_utilizatorului[9:])
            print(numar)
            numar = numar - 1

            activitati = get_activitati()

            activitate_noua = input("Scrie noua activitate: ")
            activitati[numar] = activitate_noua + '\n'

            write_activitati(activitati,'activitati.txt')
        except ValueError:
            print('Comanda ta nu e corecta! ')

    elif alegerile_utilizatorului.startswith('Finalizate'):
        try:
            numar = int(alegerile_utilizatorului[11:])

            activitati = get_activitati()

            index = numar - 1
            activitate_tobe_remove = activitati[index].strip('\n')
            activitati.pop(index)

            write_activitati(activitati)# nu e obligatoriu sa pun filepath sau valoarea acestuia deoarece e implicita!..

            mesaj = f'Activitatea {activitate_tobe_remove} a fost eliminata cu succes!'
            print(mesaj)
        except IndexError:
            print('Ai introdus un numar de activitate gresit! ')

    elif alegerile_utilizatorului.startswith('Iesire'):
        break

    else:
        print('Comanda nu e valida!')

print('O zi buna!')
'''
########### BONUS metoda de afisare in loc de '''  '''
'''
text = "Principiul productivitatii:\n\
fadvavdavhahh. \
ajdkjdhjdshjednjwekd.\
"
print(text)
'''
################ BONUS
'''
feet_inches = input('Enter feet and inches: ')

def parse(feet_inches):
    parts = feet_inches.split(' ')
    feet = float(parts[0])
    inches = float(parts[1])
    return {'feet':feet,'inches':inches}
# astfel valorile astea pot fi utilizate oriunde in program nu raman locale in functie ca in versiunea anterioara a acestui exemplu!

def convert(feet,inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

par3 = parse(feet_inches)

result = convert(par3['feet'], par3['inches'])

print(f"{par3['feet']} feet and {par3['inches']} is equal to {result}")

if result < 1:
    print('Kid is too small.')
else:
    print('Kid can use the slide.')
'''
#########
'''
#from Functii import get_activitati, write_activitati
import Functii # e mai ok metoda asta decat sa scrii toate functiile ca mai in sus daca sunt multe..
import time

acum = time.strftime('%d - %b - %Y, %H:%M:%S')
print('Acum este: ',acum)

while True:
    alegerile_utilizatorului = input('Alege din urmatoarele: Adauga, Prezinta, Editeaza, Finalizate sau Iesire')
    alegerile_utilizatorului =  alegerile_utilizatorului.strip()

    if alegerile_utilizatorului.startswith('Adauga'):
        activitate = alegerile_utilizatorului[7:]

        activitati = Functii.get_activitati() #cu import Functii trebuie scris la fiecare get sau write in fata

        activitati.append(activitate + '\n')

        Functii.write_activitati(filepath='activitati.txt',activitati_arg=activitati)

    elif alegerile_utilizatorului.startswith('Prezinta'):
        activitati = Functii.get_activitati()

        for index, actiune in enumerate(activitati):
            actiune = actiune.strip('\n')
            K = f'{index +1}-{actiune}'
            print(K)

    elif alegerile_utilizatorului.startswith('Editeaza'):
        try:
            numar = int(alegerile_utilizatorului[9:])
            print(numar)
            numar = numar - 1

            activitati = Functii.get_activitati()

            activitate_noua = input("Scrie noua activitate: ")
            activitati[numar] = activitate_noua + '\n'

            Functii.write_activitati(activitati,'activitati.txt')
        except ValueError:
            print('Comanda ta nu e corecta! ')

    elif alegerile_utilizatorului.startswith('Finalizate'):
        try:
            numar = int(alegerile_utilizatorului[11:])

            activitati = Functii.get_activitati()

            index = numar - 1
            activitate_tobe_remove = activitati[index].strip('\n')
            activitati.pop(index)

            Functii.write_activitati(activitati)

            mesaj = f'Activitatea {activitate_tobe_remove} a fost eliminata cu succes!'
            print(mesaj)
        except IndexError:
            print('Ai introdus un numar de activitate gresit! ')

    elif alegerile_utilizatorului.startswith('Iesire'):
        break

    else:
        print('Comanda nu e valida!')

print('O zi buna!')
'''
############ BONUS 1
### ofera continuturile fisierelor:
'''
import glob

fisierele_mele = glob.glob("Jurnal/*.txt") # *.txt inseamna toate fisierele de tip .txt din folder-ul Jurnal

for filepath in fisierele_mele:
    with open(filepath, 'r') as file:
        print(file.read().upper()) # sa fie cu litere mari toate.
'''
#### BONUS 2, fisiere csv, in fisierele csv toate elementele ar fi de dorit sa aibe ghilimele: "element","element"
'''
import csv

with open('weather.csv','r') as file: # weather.csv se afla langa acest fisier in acelasi folder
    data = list(csv.reader(file))
print(data)
# astfel afiseaza o lista cu liste..
'''
#######
'''
import csv

with open('weather.csv','r') as file:
    data = list(csv.reader(file))

oras = input("Scrie orasul: ")

for row in data:
    print(row)
'''
#astfel afiseaza listele una sub alta
'''
import csv

with open('weather.csv','r') as file:
    data = list(csv.reader(file))

oras = input("Scrie orasul: ")

for row in data[1:]:
    if row[0] == oras:
        print(row[1])
# iti da doar temperatura orasului tastat..
'''
##### BONUS 3, SHUTIL = SHELL UTILITIES, copiaza, muta, creaza zip, etc..
'''
import shutil

shutil.make_archive('abc','zip', 'Jurnal') # tot ce e in Jurnal va fi facut zip cu numele abc
'''

#### BONUS 4, cauta direct in browser cuvantul tastat
'''
import webbrowser

user_term = input('Tasteaza un cuvant prentru cautare: ').replace(' ','+') # inlocuieste space cu +, merge si fara asta cautarea!..
webbrowser.open('https://www.google.com/search?q=' + user_term)
'''
###### BONUS
import json

with open("intrebari.json", "r") as file:
    content = file.read()
    #print(content) # afiseaza continutul din json
    #experiment = file.readlines()
#print(experiment) # imi apare doar: []

data = json.loads(content)
#print(data) #afiseaza continutul din json pe o singura linie

for question in data:
    print(question["intrebare_text"])
    for index, alternativ in enumerate(question["alternative"]):
        print(index + 1, "-", alternativ)
    user_choice = int(input('Scrie raspunsul tau: ')) #atentie la indentare!
    question["user_choice"] = user_choice

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["raspuns_corect"]:
        score = score + 1
        result = "Raspuns_corect"
    else:
        result = "Raspuns_gresit"
    mesaj = f"{index + 1} {result} - Raspunsul tau: {question['user_choice']}, " \
            f"Raspuns corect: {question['raspuns_corect']}"
    print(mesaj)
print(score, "/", len(data))
