from timeit import default_timer as timer
from decimal import *
import random
limit = 25

getcontext().prec = 4

def InsertionSort(A, time):
    for j in range(1,len(A)):
        i = j - 1
        key = A[j]
        while i >= 0 and key < A[i]:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
        end = Decimal(timer())
        if(end - time) > limit:
            return

def RndVector(N):
    A = list(range(N))
    random.shuffle(A)
    return A


def BestInsertionSort():
    start = Decimal(timer())
    N = 1
    records={} #dizionario la cui chiave è N e il valore è il tempo di esecuzione
    while (True):
        N *= 10
        vector = list(range(N))  # best Vector for InsertionSort
        reStart = Decimal(timer())
        InsertionSort(vector, reStart)
        end = Decimal(timer())
        executionTime = end - start
        sortTime = end - reStart
        records[N]=sortTime
        if executionTime > limit:
            return records

def WorstInsertionSort():
    start = Decimal(timer())
    N = 1
    records={}
    while (True):
        N *= 10
        vector = list(range(N))
        vector.reverse()         # worst Vector for InsertionSort
        reStart = Decimal(timer())
        InsertionSort(vector, reStart)
        end = Decimal(timer())
        sortTime = end - reStart
        executionTime = end - start
        records[N]=sortTime
        if executionTime > limit:
            return records

def RNDInsertionSort():
    start = Decimal(timer())
    N = 1
    records={}
    while (True):
        N *= 10
        vector = RndVector(N)  # random Vector for InsertionSort
        reStart = Decimal(timer())
        InsertionSort(vector, reStart)
        end = Decimal(timer())
        sortTime = end - reStart
        executionTime = end - start
        records[N]=sortTime
        if executionTime > limit:
            return records

################################################################################
num = range(4) #TEST DI 5 PROVE
#TEST BEST CASE
avgTime = [] #tempo medio calcolato
numTime = [] #numero di ripetizioni (utili per avgTime)
Nmax = 0     #Dimensione massima raggiunta nei test ( se 1 = 10, 2 = 100 ...)
for i in num:
    bestRecords = BestInsertionSort()
    print(bestRecords)
    if i==0:                                      #se è il primo test
        Nmax = len(bestRecords) - 1          #inizializzo Nmax con la lunghezza del vettore
        for j in range(Nmax):
            avgTime.append(0)
            numTime.append(0)
    if Nmax < len(bestRecords) - 1 :         #se un test calcola per una dimensione maggiore
        diff = len(bestRecords) - Nmax - 1
        for k in range(diff):
            avgTime.append(0)
            numTime.append(0)
        Nmax += diff                              #aggiungo i nuovi valori
    for l in range(len(bestRecords)-1):      #calcolo la somma totale dei tempi per dimensione
        avgTime[l] += bestRecords[10**(l+1)]
        numTime[l] += 1
    bestN = 10 ** (len(bestRecords) - 1)  # non sono sicuro dell'ultima tempistica, potrebbe essere terminata prima
    bestTime = bestRecords.get(bestN)
    print("Insertion Sort ha impiegato", bestTime, "secondi per ordinare un vettore di", bestN,
          "elementi nel caso migliore.")
for i in range(Nmax):                             #calcolo la media per dimensione
    avgTime[i] /= numTime[i]
print(":> Tempi medi registrati con vettore ordinato: ", avgTime)


#TEST WORST CASE
avgTime = [] #ri-inizializzo il tempo medio calcolato
numTime = [] #ri-inizializzo il numero di ripetizioni (utili per avgTime)
Nmax = 0     #ri-inizializzo il la dimensione massima raggiunta nei test ( se 1 = 10, 2 = 100 ...)
for i in num:
    worstRecords = WorstInsertionSort()
    print(worstRecords)
    if i==0:                                      #se è il primo test
        Nmax = len(worstRecords) - 1          #inizializzo Nmax con la lunghezza del vettore
        for j in range(Nmax):
            avgTime.append(0)
            numTime.append(0)
    if Nmax < len(worstRecords) - 1 :         #se un test calcola per una dimensione maggiore
        diff = len(worstRecords) - Nmax - 1
        for k in range(diff):
            avgTime.append(0)
            numTime.append(0)
        Nmax += diff                              #aggiungo i nuovi valori
    for l in range(len(worstRecords)-1):      #calcolo la somma totale dei tempi per dimensione
        avgTime[l] += worstRecords[10**(l+1)]
        numTime[l] += 1
    worstN = 10 ** (len(worstRecords) - 1)
    worstTime = worstRecords.get(worstN)
    print("Insertion Sort ha impiegato", worstTime, "secondi per ordinare un vettore di", worstN,
          "elementi nel caso peggiore.")
for i in range(Nmax):                             #calcolo la media per dimensione
    avgTime[i] /= numTime[i]
print(":> Tempi medi registrati con vettore ordinato al contrario: ", avgTime)


#TEST RANDOM CASE
avgTime = [] #ri-inizializzo il tempo medio calcolato
numTime = [] #ri-inizializzo il numero di ripetizioni (utili per avgTime)
Nmax = 0     #ri-inizializzo il la dimensione massima raggiunta nei test ( se 1 = 10, 2 = 100 ...)
for i in num:
    rndRecords = RNDInsertionSort()
    print(rndRecords)
    if i==0:                                      #se è il primo test
        Nmax = len(rndRecords) - 1          #inizializzo Nmax con la lunghezza del vettore
        for j in range(Nmax):
            avgTime.append(0)
            numTime.append(0)
    if Nmax < len(rndRecords) - 1 :         #se un test calcola per una dimensione maggiore
        diff = len(rndRecords) - Nmax - 1
        for k in range(diff):
            avgTime.append(0)
            numTime.append(0)
        Nmax += diff                              #aggiungo i nuovi valori
    for l in range(len(rndRecords)-1):      #calcolo la somma totale dei tempi per dimensione
        avgTime[l] += rndRecords[10**(l+1)]
        numTime[l] += 1
    rndN = 10 ** (len(rndRecords) - 1)
    rndTime = rndRecords.get(rndN)
    print("Insertion Sort ha impiegato", rndTime, "secondi per ordinare un vettore di", rndN,
          "elementi casuali.")
for i in range(Nmax):                             #calcolo la media per dimensione
    avgTime[i] /= numTime[i]
print(":> Tempi medi registrati con vettore ordinato al contrario: ", avgTime)




