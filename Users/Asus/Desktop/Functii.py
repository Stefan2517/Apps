FILEPATH = 'Activitati.txt' # in cazul in care ii schimb denumirea la .txt doar aici trebuie modificat..
#daca importez Functii si scriu dir(Functii) in Consola Python, FILEPATH va aparea acolo.

def get_activitati(filepath=FILEPATH):
    with open(filepath, 'r') as fisier_local:
        activitati_local = fisier_local.readlines()
    return activitati_local


def write_activitati(activitati_arg, filepath=FILEPATH):
    with open(filepath, 'w') as fisier_local:
        fisier_local.writelines(activitati_arg)

############## Code_experiments
'''
print(__name__) # cand rulez Functii pt aceasta linie de cod apare: __main__, iar daca rulez Lista de activitati apare: Functii!
print('1Hello from Functii1')
# prin aceste 2 linii de cod pot obs ca se ruleaza Functii inaintea fiserului Lista de activitati...

if __name__ == 'frvrvrv': #ruleaza si asa, de obicei se pune __main__!
    #am pus acest conditional ca liniile ce urmeaza sa nu fie executate si in celalat fisier, ci numai in Functii!
    print('Hello from Functii')
    print(get_activitati())
'''
###########

