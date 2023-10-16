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