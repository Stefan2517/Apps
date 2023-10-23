# ziua 7 in cadrul cursului

'''
while True:
    alegerile_utilizatorului = input('Alege din urmatoarele: Adauga, Prezinta, Editeaza, Finalizate sau Iesire')
    alegerile_utilizatorului =  alegerile_utilizatorului.strip()

    match alegerile_utilizatorului:
        case 'Adauga':
            activitate = input('Scrie o activitate!') + '\n'

            fisier = open('activitati.txt','r')
            activitati = fisier.readlines()
            fisier.close()

            activitati.append(activitate)

            fisier = open('activitati.txt', 'w')
            fisier.writelines(activitati)
            fisier.close()

        case 'Prezinta':
            fisier = open('activitati.txt', 'r')
            activitati = fisier.readlines()
            fisier.close()

            print(activitati)  #apare: ['tcyvubjnk\n', 'spal\n', 'citesc\n', 'lucrez\n'] deci trebuie sa scap de \n
            # ca la printare sa nu fie atatea spatii intre ele

#            noi_activitati = [] # deci de aici incepe rezolvarea eliminarea spatiilor

#            for item in activitati:
#                new_item = item.strip('\n') #strip elimina \n adica spatiile dintre rezultate
#                noi_activitati.append(new_item)
                                # pana aici!

            noi_activitati = [item.strip('\n') for item in activitati] # tot ce e comentat poate fi rezumat la linia asta de cod!
# e bine sa fie citit de la dreapta la stanga, se itereaza, se elimina spatiile si se salveaza in variabila apoi

            for index, actiune in enumerate(noi_activitati):
                K = f'{index +1}-{actiune}'
                print(K)
        case 'Editeaza':
            numar = int(input('Numarul activitatii de editat: '))
            numar = numar - 1
            activitate_noua = input("Scrie noua activitate: ")
            activitati[numar] = activitate_noua
        case 'Finalizate':
            numar = int(input('Numarul activitatii finalizate: '))
            activitati.pop(numar-1)
        case 'Iesire':
            break
        case _:
            print('Hei, ai introdus o comanda gresita!')

print('O zi buna!')
'''

################

'''
while True:
    alegerile_utilizatorului = input('Alege din urmatoarele: Adauga, Prezinta, Editeaza, Finalizate sau Iesire')
    alegerile_utilizatorului =  alegerile_utilizatorului.strip()

    match alegerile_utilizatorului:
        case 'Adauga':
            activitate = input('Scrie o activitate!') + '\n'

            fisier = open('activitati.txt','r')
            activitati = fisier.readlines()
            fisier.close()

            activitati.append(activitate)

            fisier = open('activitati.txt', 'w')
            fisier.writelines(activitati)
            fisier.close()

        case 'Prezinta':
            fisier = open('activitati.txt', 'r')
            activitati = fisier.readlines()
            fisier.close()

            for index, actiune in enumerate(activitati):
                actiune = actiune.strip('\n')   # sau modalitatea aceasta e mai scurta decat celelalte 2 de a elimina spatiile 
                K = f'{index +1}-{actiune}'
                print(K)
        case 'Editeaza':
            numar = int(input('Numarul activitatii de editat: '))
            numar = numar - 1
            activitate_noua = input("Scrie noua activitate: ")
            activitati[numar] = activitate_noua
        case 'Finalizate':
            numar = int(input('Numarul activitatii finalizate: '))
            activitati.pop(numar-1)
        case 'Iesire':
            break
        case _:
            print('Hei, ai introdus o comanda gresita!')

print('O zi buna!')
'''

################
'''
while True:
    alegerile_utilizatorului = input('Alege din urmatoarele: Adauga, Prezinta, Editeaza, Finalizate sau Iesire')
    alegerile_utilizatorului =  alegerile_utilizatorului.strip()

    match alegerile_utilizatorului:
        case 'Adauga':
            activitate = input('Scrie o activitate!') + '\n'

 # introduc managerul de context cu with, scap de linia cu close...
 # metoda e mai stabila deoarece in cazul celeilalte daca apar probleme in timpul rularii nu mai ajunge la close si va ramane un fisier deschis ce va incurca mai mult...

            with open('activitati.txt','r') as fisier:
                activitati = fisier.readlines()

            activitati.append(activitate)

 # introduc managerul de context cu with, scap de linia cu close...
            with open('activitati.txt', 'w') as fisier:
                fisier.writelines(activitati)

# introduc managerul de context cu with, scap de linia cu close...
        case 'Prezinta':
            with open('activitati.txt', 'r') as fisier:
                activitati = fisier.readlines()

            for index, actiune in enumerate(activitati):
                actiune = actiune.strip('\n')   # sau modalitatea aceasta e mai scurta decat celelalte 2 de a elimina spatiile
                K = f'{index +1}-{actiune}'
                print(K)

        case 'Editeaza':
            numar = int(input('Numarul activitatii de editat: '))
            numar = numar - 1

            with open('activitati.txt', 'r') as fisier:
                activitati = fisier.readlines()
            #print('Aici e ceea ce exista deja in activitati', activitati)

            activitate_noua = input("Scrie noua activitate: ")
            activitati[numar] = activitate_noua + '\n'
            #print('Aici e ceea ce va fi', activitati)

            with open('activitati.txt', 'w') as fisier:
                fisier.writelines(activitati)

        case 'Finalizate':
            numar = int(input('Numarul activitatii finalizate: '))

            with open('activitati.txt', 'r') as fisier:
                activitati = fisier.readlines()

            index = numar - 1
            activitate_tobe_remove = activitati[index].strip('\n') #strip elimina un ,,ENTER``
            activitati.pop(index)

            with open('activitati.txt', 'w') as fisier:
                fisier.writelines(activitati)

            mesaj = f'Activitatea {activitate_tobe_remove} a fost eliminata cu succes!'
            print(mesaj)

        case 'Iesire':
            break
        case _:
            print('Hei, ai introdus o comanda gresita!')

print('O zi buna!')

# daca pun ../ inaintea unei cai, atunci poate accesa un fisier dintr-un alt folder decat cel in care e fisierul din care se ruleaza
# with open('activitati.txt', 'r') as fisier: poate fi scris si # with open('activitati.txt') as fisier:
# with open are ca implicit read
'''
########## BONUS example aplicatie tip jurnal
'''
data = input('Introdu data de azi: ')
stare = input('Cum iti evaluezi azi starea de la 0 la 10? ')
descriere = input('Scrie cateva cuvinte descriptive ale zilei curente: \n')

with open(f'./Jurnal/{data}.txt', 'w') as fisier:
    # am folosit doar ./ si nu 2 puncte deoarece altfel nu-l gaseste. folderul Jurnal se afla impreuna cu aplicatia in acelasi folder!
    fisier.write(stare + 2*'\n')
    fisier.write(descriere)
'''
############
'''
while True:
    alegerile_utilizatorului = input('Alege din urmatoarele: Adauga, Prezinta, Editeaza, Finalizate sau Iesire')
    alegerile_utilizatorului =  alegerile_utilizatorului.strip()

# cu shift+Tab am scos identarea, si o pun cu Tab doar
    if 'Adauga' in alegerile_utilizatorului:
        activitate = alegerile_utilizatorului[7:]
#list slicing, elimin Adauga din raspunsul utilizatorul si memorez restul

        with open('activitati.txt','r') as fisier:
            activitati = fisier.readlines()

        activitati.append(activitate)

        with open('activitati.txt', 'w') as fisier:
            fisier.writelines(activitati)

    elif 'Prezinta' in alegerile_utilizatorului:
        with open('activitati.txt', 'r') as fisier:
            activitati = fisier.readlines()

        for index, actiune in enumerate(activitati):
            actiune = actiune.strip('\n')
            K = f'{index +1}-{actiune}'
            print(K)

    elif 'Editeaza' in alegerile_utilizatorului:
        numar = int(alegerile_utilizatorului[9:])
        print(numar)
        numar = numar - 1

        with open('activitati.txt', 'r') as fisier:
            activitati = fisier.readlines()

        activitate_noua = input("Scrie noua activitate: ")
        activitati[numar] = activitate_noua + '\n'

        with open('activitati.txt', 'w') as fisier:
            fisier.writelines(activitati)

    elif 'Finalizate' in alegerile_utilizatorului:
        numar = int(alegerile_utilizatorului[11:])

        with open('activitati.txt', 'r') as fisier:
            activitati = fisier.readlines()

        index = numar - 1
        activitate_tobe_remove = activitati[index].strip('\n')
        activitati.pop(index)

        with open('activitati.txt', 'w') as fisier:
            fisier.writelines(activitati)

        mesaj = f'Activitatea {activitate_tobe_remove} a fost eliminata cu succes!'
        print(mesaj)

    elif 'Iesire' in alegerile_utilizatorului:
        break

    else:
        print('Comanda nu e valida!')

print('O zi buna!')
'''
########### BONUS puterea unei parole
'''
parola = input('Tasteaza parola: ')
rezultat = []

if len(parola) >=8:
    rezultat.append(True)
else:
    rezultat.append(False)
# nu am facut cu elif-uri deoarece toate 3 conditiile sunt interdependente, de aceea folosesc lista rezultat

digit = False
for i in parola:
    if i.isdigit():
        digit = True
rezultat.append(digit)
# folosesc iteratia ca poate prin parola gasesc un numar printre caractere...
# la .isdigit() 45gbtrg = False, prin iteratie da True

majuscula = False
for i in parola:
    if i.isupper():
        majuscula = True
rezultat.append(majuscula)

#print(rezultat)
#print(all(rezultat)) # arata rezultatul final, nu toate 3...

if all(rezultat): # == True, am sters deoarece e setat implicit True!!!
    print('Parola puternica')
else:
    print('Parola vulnerabila')
'''
####### inlocuiesc list cu dict BONUS
'''
parola = input('Tasteaza parola: ')
rezultat = {}

if len(parola) >=8:
    rezultat['lungimea'] = (True)
else:
    rezultat['Lungimea'] = (False)

digit = False
for i in parola:
    if i.isdigit():
        digit = True
rezultat['Numere'] = (digit)

majuscula = False
for i in parola:
    if i.isupper():
        majuscula = True
rezultat['Majuscula'] = (majuscula)
print(rezultat)
print(rezultat.values())

if all(rezultat.values()): #am pus .values() deoarece acm e dict sa aiba acces la valorile cheilor, daca nu puneam era True pt toate
    print('Parola puternica')
else:
    print('Parola vulnerabila')
'''
#########
'''
while True:
    alegerile_utilizatorului = input('Alege din urmatoarele: Adauga, Prezinta, Editeaza, Finalizate sau Iesire')
    alegerile_utilizatorului =  alegerile_utilizatorului.strip()

    if alegerile_utilizatorului.startswith('Adauga'): # daca incepe cu Adauga...
        activitate = alegerile_utilizatorului[7:]

        with open('activitati.txt','r') as fisier:
            activitati = fisier.readlines()

        activitati.append(activitate + '\n')

        with open('activitati.txt', 'w') as fisier:
            fisier.writelines(activitati)

    elif alegerile_utilizatorului.startswith('Prezinta'):
        with open('activitati.txt', 'r') as fisier:
            activitati = fisier.readlines()

        for index, actiune in enumerate(activitati):
            actiune = actiune.strip('\n')
            K = f'{index +1}-{actiune}'
            print(K)

    elif alegerile_utilizatorului.startswith('Editeaza'):
        #am pus try si except pt a nu aparea eroarea la utilizator
        try:
            numar = int(alegerile_utilizatorului[9:])
            print(numar)
            numar = numar - 1

            with open('activitati.txt', 'r') as fisier:
                activitati = fisier.readlines()

            activitate_noua = input("Scrie noua activitate: ")
            activitati[numar] = activitate_noua + '\n'

            with open('activitati.txt', 'w') as fisier:
                fisier.writelines(activitati)
        except ValueError:
            print('Comanda ta nu e corecta! ')
            #continue # am obs ca merge si fara...
    elif alegerile_utilizatorului.startswith('Finalizate'):
        try:
            numar = int(alegerile_utilizatorului[11:])

            with open('activitati.txt', 'r') as fisier:
                activitati = fisier.readlines()

            index = numar - 1
            activitate_tobe_remove = activitati[index].strip('\n')
            activitati.pop(index)

            with open('activitati.txt', 'w') as fisier:
                fisier.writelines(activitati)

            mesaj = f'Activitatea {activitate_tobe_remove} a fost eliminata cu succes!'
            print(mesaj)
        except IndexError:
            print('Ai introdus un numar de activitate gresit! ')
            #continue #merge si fara...

    elif alegerile_utilizatorului.startswith('Iesire'):
        break

    else:
        print('Comanda nu e valida!')

print('O zi buna!')
'''
############ BONUS
'''
try:
    lungime = float(input('Tastati lungimea dreptunghiului: '))
    latime = float(input('Tastati latimea dreptunghiului: '))

    if lungime==latime:
        exit('Arata a patrat! ')

    aria = lungime*latime
    print(f'Dreptunghiul are aria {aria}')
except ValueError: # in cazul ca scrie unu si nu 1....
    print('Introdu te rog un numar! ')
'''
########### scot liniile de cod repetitive
'''
def get_activitati():
    with open('activitati.txt', 'r') as fisier_local:
        activitati_local = fisier_local.readlines()
    return activitati_local #returneaza valoarea

while True:
    alegerile_utilizatorului = input('Alege din urmatoarele: Adauga, Prezinta, Editeaza, Finalizate sau Iesire')
    alegerile_utilizatorului =  alegerile_utilizatorului.strip()

    if alegerile_utilizatorului.startswith('Adauga'): # daca incepe cu Adauga...
        activitate = alegerile_utilizatorului[7:]

        activitati = get_activitati()

        activitati.append(activitate + '\n')

        with open('activitati.txt', 'w') as fisier:
            fisier.writelines(activitati)

    elif alegerile_utilizatorului.startswith('Prezinta'):
        activitati = get_activitati()

        for index, actiune in enumerate(activitati):
            actiune = actiune.strip('\n')
            K = f'{index +1}-{actiune}'
            print(K)

    elif alegerile_utilizatorului.startswith('Editeaza'):
        #am pus try si except pt a nu aparea eroarea la utilizator
        try:
            numar = int(alegerile_utilizatorului[9:])
            print(numar)
            numar = numar - 1

            activitati = get_activitati()

            activitate_noua = input("Scrie noua activitate: ")
            activitati[numar] = activitate_noua + '\n'

            with open('activitati.txt', 'w') as fisier:
                fisier.writelines(activitati)
        except ValueError:
            print('Comanda ta nu e corecta! ')
            #continue # am obs ca merge si fara...
    elif alegerile_utilizatorului.startswith('Finalizate'):
        try:
            numar = int(alegerile_utilizatorului[11:])

            activitati = get_activitati()

            index = numar - 1
            activitate_tobe_remove = activitati[index].strip('\n')
            activitati.pop(index)

            with open('activitati.txt', 'w') as fisier:
                fisier.writelines(activitati)

            mesaj = f'Activitatea {activitate_tobe_remove} a fost eliminata cu succes!'
            print(mesaj)
        except IndexError:
            print('Ai introdus un numar de activitate gresit! ')
            #continue #merge si fara...

    elif alegerile_utilizatorului.startswith('Iesire'):
        break

    else:
        print('Comanda nu e valida!')

print('O zi buna!')
'''
######### exemplu functie/reteta (exemplul cu cafeaua din cafenea pe care o ceri/,,apelezi``)
'''
def lala():
    mesaj = 'Hello'
    print('Hey hey') #afiseaza asta chiar daca nu apelezi functia daca are: tralala = lala()
    mesaj_nou = mesaj.capitalize()
    return mesaj_nou

tralala = lala()
print(tralala)
#print(mesaj_nou) # da eroare deoarece variabila exista DOAR in cadrul functiei, cat NICI variabila mesaj..
'''
########## BONUS media temperaturilor
'''
def get_media():
    with open('data.txt', 'r') as file_local:  # fisierul data.txt e langa fisierul acesta
        data = file_local.readlines()

    valori = data[1:] #pt a exclude titlul: temperaturi din data.txt
    valori = [float(i) for i in valori] # pt a elimina \n

    media_local = sum(valori) / len(valori)
    return media_local

media = get_media()
print(media)
'''
# daca returneaza eroare cu NoneType e legat de return, poate nu era pus...
##################
'''
def get_activitati(filepath):
    with open(filepath, 'r') as fisier_local:
        activitati_local = fisier_local.readlines()
    return activitati_local
# filepath aici reprezinta parametrul functiei, cand scriem functia e vb de parametru, nu argument!

def write_activitati(filepath, activitati_arg):
    with open(filepath, 'w') as fisier_local:
        fisier_local.writelines(activitati_arg)
#n-am nevoie de return deoarece trebuie doar sa scrie, nu sa-mi dea cv inapoi

while True:
    alegerile_utilizatorului = input('Alege din urmatoarele: Adauga, Prezinta, Editeaza, Finalizate sau Iesire')
    alegerile_utilizatorului =  alegerile_utilizatorului.strip()

    if alegerile_utilizatorului.startswith('Adauga'): # daca incepe cu Adauga...
        activitate = alegerile_utilizatorului[7:]

        activitati = get_activitati(filepath='activitati.txt') #pot scrie si fara filepath=, doar valoarea lui..
        #'activitati.txt' reprezinta valoarea argumentului, cand se apeleaza o functie vb de argument!

        activitati.append(activitate + '\n')

        write_activitati(filepath='activitati.txt',activitati_arg=activitati)#se poate scrie si fara filepath= sau activitati_arg=

    elif alegerile_utilizatorului.startswith('Prezinta'):
        activitati = get_activitati('activitati.txt')

        for index, actiune in enumerate(activitati):
            actiune = actiune.strip('\n')
            K = f'{index +1}-{actiune}'
            print(K)

    elif alegerile_utilizatorului.startswith('Editeaza'):
        #am pus try si except pt a nu aparea eroarea la utilizator
        try:
            numar = int(alegerile_utilizatorului[9:])
            print(numar)
            numar = numar - 1

            activitati = get_activitati('activitati.txt')

            activitate_noua = input("Scrie noua activitate: ")
            activitati[numar] = activitate_noua + '\n'

            write_activitati('activitati.txt',activitati)
        except ValueError:
            print('Comanda ta nu e corecta! ')

    elif alegerile_utilizatorului.startswith('Finalizate'):
        try:
            numar = int(alegerile_utilizatorului[11:])

            activitati = get_activitati('activitati.txt')

            index = numar - 1
            activitate_tobe_remove = activitati[index].strip('\n')
            activitati.pop(index)

            write_activitati('activitati.txt', activitati)

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
############ BONUS
'''
feet_inches = input('Enter feet and inches: ')
def convert(feet_inches):
    parts = feet_inches.split(' ') #taie spatiul liber
    feet = float(parts[0]) #ia primul nr
    inches = float(parts[1]) #ia al doilea nr

    meters = feet * 0.3048 + inches * 0.0254
    return meters

result = convert(feet_inches)

if result < 1:
    print('Kid is too small.')
else:
    print('Kid can use the slide.')
'''