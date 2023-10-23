# acest fisier reprezinta o continuare a celui anterior
'''
user_prompt = "Introdu activitatile:"
text = input(user_prompt) # ce e scris in user_prompt se salveaza in variabila text
print(text) # afisam variabila text
'''
import types

################

'''
user_prompt = "Introdu activitatile:"
activitate1 = input(user_prompt)
activitate2 = input(user_prompt)
activitate3 = input(user_prompt)

activitati = [activitate1, activitate2, activitate3, "Hello"]
print(activitati)

print(type(activitate1))
'''

################

'''
user_prompt = "Introdu activitatile:"
while 2>1: # 2>1 este intotdeauna valabil, deci poate fi inlocuita conditia cu True,
    # daca pun False nu executa comenzile
    activitate = input(user_prompt)
    print(activitate)
    print("Urmatoarea...")
'''

################

'''
user_prompt = "Introdu activitatile:"

activitati = []

while True:
    activitate = input(user_prompt)
    #activitate.append()  o sa dea eroare deoarece activitate e string nu lista
    print(activitate.capitalize()) # capitalize returneaza stringul ca avand majuscula prima litera
    activitati.append(activitate)
    print(activitati)
    print(activitate.title()) # title returneaza stringul ca fiecare cuvant sa fie cu majuscula

'''

################  BONUS

'''
parola = input("Introdu parola:")

while parola != "pass123":
    parola = input("Introdu parola:")

print("Parola e corecta!")
'''

################  BONUS

'''
x = 1

while x <= 6:
    print(x)
    x = x + 1
'''

# pentru a afla metodele in consola scriu de exemplu pt STRING: dir('str'), sau dir('oricelitere'), dir(int)
# tot in consola ca sa aflu cum functioneaza metodele: help(list.append), sau help([]) sau help(list),
# sau a = [1, 2, 3]
# dir(a)
# cand cauti append sau capitalize, ultimul nu are argument, primul are. Asa stii unde se cere...  ??????
# adica: append(self, object, /),  ?????????
# sau pentru functii: import builtins
# help(builtins)

################

'''
activitati = []

while True:
    alegerile_utilizatorului = input('Adauga, Prezinta sau Iesire')
    alegerile_utilizatorului =  alegerile_utilizatorului.strip()
    # strip() e o metoda ce elimina spatiile

    match alegerile_utilizatorului:
        case 'Adauga':
            activitate = input('Scrie o activitate!')
            activitati.append(activitate)
        case 'Prezinta' | 'Afiseaza':
            for actiune in activitati:
                actiune = actiune.title()
                # poti pune cate doresti doar sa pastrezi indentarea
                print(actiune)
        case 'Iesire':
            break
        case _: # "_" putea fi inlocuit de orice altcv, dar asa se utilizeaza deobicei
            print('Hei, ai introdus o comanda gresita!')

print('O zi buna!')
'''

################  BONUS

'''
for masa in 'mese':
    print(masa.capitalize())

print('Salut!')
'''

#sau alta varianta diferita:
'''
mese = ['fructe','pizza','salata']
for masa in mese:
    print(masa.capitalize())

print('Salut!')
'''

################  BONUS

'''
nume = ['ioan ionut', 'stefan mare', 'stefan mic']

for i in nume:
    print(i.title())
    # fiecare nume sa fie scris cu majuscula
'''

################

'''
activitati = []

while True:
    alegerile_utilizatorului = input('Adauga, Prezinta, Editeaza sau Iesire')
    alegerile_utilizatorului =  alegerile_utilizatorului.strip()

    match alegerile_utilizatorului:
        case 'Adauga':
            activitate = input('Scrie o activitate!')
            activitati.append(activitate)
        case 'Prezinta' | 'Afiseaza':
            for actiune in activitati:
                actiune = actiune.title()
                print(actiune)
        case 'Editeaza':
            numar = int(input('Numarul activitatii de editat: ')) #deoarece in paranteza avem ghilimele ia ca si string de aia am pus int in fata
            numar = numar - 1 # in programare incepe numararea de la 0, iar utilzatorul nu stie asta...
            activitate_noua = input("Scrie noua activitate: ")
            activitati[numar] = activitate_noua # prin [] se alege elementul din lista
        case 'Iesire':
            break
        case _:
            print('Hei, ai introdus o comanda gresita!')

print('O zi buna!')
'''

################

'''
a = input('scrie un numar')
b = int(a)
print(type(a))
print(type(b))
b = b*10
a = a*10
print(a,b) # a fiind string nu calculeaza un numar final fix, ci il multiplica de atatea ori!
c = float('10') # transformare din int in float
print(c)
d = str(1.23) # transformare din float in string
print(type(d))
'''

###

'''
lista_mea = ['a','b','c']
z = lista_mea[1] # elementele dintr-o lista se pot stoca in variabile
print(z)
print(type(z))
if z == 'b':
    print('Este adevarat!')

print(lista_mea.index('b'))
lista_mea.__setitem__(1, 'y') # metoda inlocuieste elementul cu index-ul 1 ca fiind y, nu b
print(lista_mea)
# sau o varianta mai simpla:
lista_mea[1] = 'x' # inlocuirea lui y cu x
print(lista_mea)

print(lista_mea.__getitem__(2))
# sau o varianta mai simpla pentru a obtine valoarea index-ului din lista:
print(lista_mea[2])
'''

################  BONUS

'''
filename = '1.Ana are mere.txt'
print(filename[1]) # astfel ne returneaza punctul deoarece acesta are index-ul 1
#filename[1] = '-'  # da eroare
info = ['Maria are pere', 'Maria are mere']
print(info[1]) # returneaza 'Maria are mere'
print(info)
k = filename.replace('.', '-') # inlocuieste punctele cu liniute
print(k)
print(filename.replace('.','-', 1)) # inlocuieste doar primul punct cu o liniuta
'''

################  BONUS

'''
nume_de_fisiere = ['1.Date.txt', '2.Rapoarte.txt', '3.Prezentari.txt']
# folosesc for pentru a schimba primul punct din fiecare denumire de fisier in liniuta
for i in nume_de_fisiere:
    i = i.replace('.','-',1)
#   file.rename(i)  # schimba denumirile fisierelor din folder
    print(i)
# rezulta ca sirurile de caractere sunt imuabile(nu se schimba), iar listele mutabile
# tuple este varianta ce ramane neschimbata a unei liste
G = ('1.Date.txt', '2.Rapoarte.txt', '3.Prezentari.txt') # tuple e cu paranteze rotunde
print(type(G)) # tuple nu se poate modifica/edita,sterge/adauga, ci doar afisa
'''

################

'''
activitati = []

while True:
    alegerile_utilizatorului = input('Adauga, Prezinta, Editeaza sau Iesire')
    alegerile_utilizatorului =  alegerile_utilizatorului.strip()

    match alegerile_utilizatorului:
        case 'Adauga':
            activitate = input('Scrie o activitate!')
            activitati.append(activitate)
        case 'Prezinta':
            for index, actiune in enumerate(activitati): # enumerate e o functie ce are acces la index-urile si valorile dintr-o lista, cea in paranteza
            #    print(index, '-' ,actiune) # pt index-uri putea fi utilizata si alta denumire de variabila
                K = f'{index}-;)-{actiune}' #fString-ul ofera posibilitatea sa dispara locurile libere de la varianta anterioara
                print(K)
        case 'Editeaza':
            numar = int(input('Numarul activitatii de editat: ')) #deoarece in paranteza avem ghilimele ia ca si string de aia am pus int in fata
            numar = numar - 1 # in programare incepe numararea de la 0, iar utilzatorul nu stie asta...
            activitate_noua = input("Scrie noua activitate: ")
            activitati[numar] = activitate_noua # prin [] se alege elementul din lista
        case 'Iesire':
            break
        case _: # _ se pune deobicei cand nu ai o denumire
            print('Hei, ai introdus o comanda gresita!')

print('O zi buna!')
'''

################

'''
lista_mea = ['a', 'b', 'c']
lista_mea.remove('b') # sterge un element dorit din lista, clear sterge tot, lista_mea.pop(1) sterge elementul si il returneaza 'b' in consola
print(lista_mea)
'''

################

'''
activitati = []

while True:
    alegerile_utilizatorului = input('Alege din urmatoarele: Adauga, Prezinta, Editeaza, Finalizate sau Iesire')
    alegerile_utilizatorului =  alegerile_utilizatorului.strip()

    match alegerile_utilizatorului:
        case 'Adauga':
            activitate = input('Scrie o activitate!')
            activitati.append(activitate)
        case 'Prezinta':
            for index, actiune in enumerate(activitati):
            #    print(index, '-' ,actiune)
                K = f'{index +1}-;)-{actiune}' # +1 ca sa nu apara de la 0 ci de la 1 la afisare
                print(K)
          # print('SALUTARE', index, actiune) #indexul are ca valoare ultimul index din bucla for, deci atentie la indentare
            print(f'Lungimea listei e de {index + 1} elemente') # aici ajuta exemplul anterior cu indentarea
            print(len(activitati)) # aceasta metoda functioneaza si fara bucla for
        case 'Editeaza':
            numar = int(input('Numarul activitatii de editat: '))
            numar = numar - 1
            activitate_noua = input("Scrie noua activitate: ")
            activitati[numar] = activitate_noua
        case 'Finalizate':
            numar = int(input('Numarul activitatii finalizate: '))
            activitati.pop(numar-1) # pun -1 deoarece la 'Prezinta' am pus +1
        case 'Iesire':
            break
        case _:
            print('Hei, ai introdus o comanda gresita!')

print('O zi buna!')
'''

################

'''
for i, j in enumerate('Ana are mere'): # i este pt index, iar j pt valori
    print(i,j)
'''

'''
x = enumerate(['a','b','c'])
print(x) # apare: <enumerate object at 0x0000021DF16E4280>
y = list(x) # il convertesc in lista
print(y) # apare: [(0, 'a'), (1, 'b'), (2, 'c')] adica o lista cu 3 tuple ce contin index+valoare/element
for i, item in [(0, 'a'), (1, 'b'), (2, 'c')]:
    print(i, item) # apare: 0 a / 1 b / 2 c

g = enumerate('Salut')
print(g) # apare: <enumerate object at 0x0000015C57A2BBC0>
print(list(g)) # apare: [(0, 'S'), (1, 'a'), (2, 'l'), (3, 'u'), (4, 't')]
p = str(g) # daca il convertim in string ar fi inutil deoarece apare: <enumerate object at 0x0000025F7FD4BBC0>
print(p)
'''

################  BONUS
#dir(list) cautam ce metode are lista in consola!!!
#help(list.sort) asa cautam ce face metoda

'''
lista_de_asteptare = ['Stefan', 'Carina', 'Ana', 'Ioan']
lista_de_asteptare.sort() # sorteaza elementele listei alfabetic

for index, element in enumerate(lista_de_asteptare):
    h = f'{index + 1 }.{element.capitalize()}'
    print(h)

l = 'Salutare'
o = l.replace('a', 'xyz')
print(o)

m = ['c','d','b']
m.sort()
print(m) # apare ['b', 'c', 'd'] adica alfabetic

n = ['c','d','b']
n.sort(reverse=True) # implicit e pe False de aia am specificat acm sa fie pe True
print(n) # apare ['d', 'c', 'b'], descrescator sau invers

litere = [('a','v', 'm'), ('e', 't', 'u')]
for one, two, three in litere:
    print(one, two, three) # apare a v m  /  e t u deci se poate for cu 2 tuple in lista, dar la enumerate doar 2 variabile pot fi
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
            activitati = fisier.readlines() #aici s-ar declara lista in mod automat
            fisier.close() #odata ce folosim open e de dorit sa punem close pt ca pot interveni erori la programe complexe

            activitati.append(activitate) #folosesc un fisier extern ca sa ramana salvate activitatile

            fisier = open('activitati.txt', 'w')
            fisier.writelines(activitati)
            fisier.close()

        case 'Prezinta':
            fisier = open('activitati.txt', 'r')
            activitati = fisier.readlines()
            fisier.close()
            for index, actiune in enumerate(activitati):
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
a = [1, 2, 3]
b = [10, 20, 30]
x = zip(a,b)
print(list(x)) # am convertit in lista si arata asa: [(1, 10), (2, 20), (3, 30)]
'''

################

'''
# cele 3 continuturi sunt puse separat fiecare in cele 3 fisiere

continuturi = ['Acesta este primul continut', 'Acesta este al doilea continut',
               'Acesta este al treilea continut'] # am dat un enter sa fie vizibil continutul listei

nume_fisiere = ['doc.txt', 'raport.txt', 'prezentare.txt']

for continut, nume_fisier in zip(continuturi, nume_fisiere):
    fisier = open(f'files/{nume_fisier}', 'w') #am creat variabila fisier prin care cream fisierele propriu zise cu numele lor
    fisier.write(continut) # apoi scriem continutul in acele fisiere create.
    # am creat manual un folder files, daca da eroarea: FileNotFoundError: [Errno 2] No such file or directory: '../files/doc.txt'
    # inseamna ca nu gaseste locatia si ce ar trebui, astfel pt a muta intr-un folder inainte celui prezent folosim ../
'''

################

'''
a = "Sunt o variabila ce " \
    "stocheaza date de " \
    "tipul String"
print(a)

# nu pot pune comentariul sau # chiar si spatii libere langa \ ca imi da eroare
# \ apare cand dau enter in cadrul continutului variabilei, ajuta cand nu poti afisa intreaga variabila
# pe orizontala ecranului, aceasta ramanand neschimbata daca ii dau print()
'''
