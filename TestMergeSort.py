from timeit import default_timer as timer #funzione per misurare tempo di esecuzione
from decimal import * #funzione per limitare il numero di decimali nei valori
import random #funzione per ottenere vettori randomizzati
limit = 25
index = 0

getcontext().prec = 4 #limite cifre significative decimali

def MergeSort(A, index, end, time): #end è l'ultimo elemento, index il primo, A il vettore
    if index < end:
        q = int((index + end)/2)
        MergeSort(A, index, q, time)
        final = Decimal(timer())
        if final - time > limit:  #verifica la condizione di uscita*
            return
        MergeSort(A, q+1, end, time)
        Merge(A, index, q, end)
        final = Decimal(timer())
        if final - time > limit: #verifica la condizione di uscita *
            return
#* il controllo temporale viene fatto quando arriva al primo caso base e prima di ogni suddivisione del sottovettore dx.
#Di conseguenza viene perso molto tempo di esecuzione per verificare la condizione di uscita, ma ciò garantisce che
## l'esecuzione termini non appena (o poco dopo) venga raggiunto il limite.


def Merge(A, index, q, end):
    n1 = q - index + 1          #dimensione L
    n2 = end - q                #dimensione R
    #creo due sottoarray L e R
    L = []
    R = []
    for i in range(n1):
        L.append(A[index+i])
    for j in range(n2):
        R.append(A[q+j+1])
    i = 0
    j = 0
    k = index
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k +=1
    if i < n1:
        A[k:end+1] = L[i:n1] #inserisco gli ultimi elementi di L in A
    if j < n2:
        A[k:end+1] = R[j:n2] #inserisco gli ultimi elementi di R in A

#######################################################################
# test con vettore già ordinato
def YetSortedMergeSort():
    start = Decimal(timer())
    N = 10
    records = {}
    while True:
        vector = list(range(N))  # best Vector for MergeSort
        reStart = Decimal(timer())
        MergeSort(vector, index, N-1, reStart)
        end = Decimal(timer())
        executionTime = end - start
        sortTime = end - reStart
        records[N] = sortTime
        if executionTime > limit:
            return records
        N *= 10

##################################################################
# test con vettore ordinato al contrario
def ReversedMergeSort():
    start = Decimal(timer())
    N = 10
    records = {}
    while True:
        vector = list(range(N))
        vector.reverse()         # worst Vector for MergeSort
        reStart = Decimal(timer())
        MergeSort(vector, index, N-1, reStart)
        end = Decimal(timer())
        sortTime = end - reStart
        executionTime = end - start
        records[N] = sortTime
        if executionTime > limit:
            return records
        N *= 10

####################################################################
#test con vettore randomizzato
def RndVector(N):
    A = list(range(N))
    random.shuffle(A)
    return A

def RNDMergeSort():
    start = Decimal(timer())
    N = 10
    records = {}
    while True:
        vector = RndVector(N)  # random Vector for MergeSort
        reStart = Decimal(timer())
        MergeSort(vector, index, N-1, reStart)
        end = Decimal(timer())
        sortTime = end - reStart
        executionTime = end - start
        records[N] = sortTime
        if executionTime > limit:
            return records
        N *= 10

####################################################################
num = range(4) #TEST DI 5 PROVE
#TEST YET SORTED LIST
avgTime = [] #tempo medio calcolato
numTime = [] #numero di ripetizioni (utili per avgTime)
Nmax = 0     #Dimensione massima raggiunta nei test ( se 1 = 10, 2 = 100 ...)
for i in num:
    yetSortedRecords = YetSortedMergeSort()
    print(yetSortedRecords)
    if i==0:                                      #se è il primo test
        Nmax = len(yetSortedRecords) - 1          #inizializzo Nmax con la lunghezza del vettore
        for j in range(Nmax):
            avgTime.append(0)
            numTime.append(0)
    if Nmax < len(yetSortedRecords) - 1 :         #se un test calcola per una dimensione maggiore
        diff = len(yetSortedRecords) - Nmax - 1
        for k in range(diff):
            avgTime.append(0)
            numTime.append(0)
        Nmax += diff                              #aggiungo i nuovi valori
    for l in range(len(yetSortedRecords)-1):      #calcolo la somma totale dei tempi per dimensione
        avgTime[l] += yetSortedRecords[10**(l+1)]
        numTime[l] += 1
    yetSortedN = 10**(len(yetSortedRecords)-1) #non sono sicuro dell'ultima tempistica, potrebbe essere terminata prima
    yetSortedTime = yetSortedRecords.get(yetSortedN)
    print("Merge Sort ha impiegato", yetSortedTime, "secondi per ordinare un vettore di", yetSortedN,
                  "elementi già ordinato.")
for i in range(Nmax):                             #calcolo la media per dimensione
    avgTime[i] /= numTime[i]
print(":> Tempi medi registrati con vettore ordinato: ", avgTime)

#TEST REVERSED LIST
avgTime = [] #ri-inizializzo il tempo medio calcolato
numTime = [] #ri-inizializzo il numero di ripetizioni (utili per avgTime)
Nmax = 0     #ri-inizializzo il la dimensione massima raggiunta nei test ( se 1 = 10, 2 = 100 ...)
for i in num:
    reversedRecords = ReversedMergeSort()
    print(reversedRecords)
    if i==0:                                      #se è il primo test
        Nmax = len(reversedRecords) - 1          #inizializzo Nmax con la lunghezza del vettore
        for j in range(Nmax):
            avgTime.append(0)
            numTime.append(0)
    if Nmax < len(reversedRecords) - 1 :         #se un test calcola per una dimensione maggiore
        diff = len(reversedRecords) - Nmax - 1
        for k in range(diff):
            avgTime.append(0)
            numTime.append(0)
        Nmax += diff                              #aggiungo i nuovi valori
    for l in range(len(reversedRecords)-1):      #calcolo la somma totale dei tempi per dimensione
        avgTime[l] += reversedRecords[10**(l+1)]
        numTime[l] += 1
    reversedN = 10 ** (len(reversedRecords) - 1)
    reversedTime = reversedRecords.get(reversedN)
    print("Merge Sort ha impiegato", reversedTime, "secondi per ordinare un vettore di", reversedN,
          "elementi ordinati al contrario.")
for i in range(Nmax):                             #calcolo la media per dimensione
    avgTime[i] /= numTime[i]
print(":> Tempi medi registrati con vettore ordinato al contrario: ", avgTime)



#TEST RANDOM CASE
avgTime = [] #ri-inizializzo il tempo medio calcolato
numTime = [] #ri-inizializzo il numero di ripetizioni (utili per avgTime)
Nmax = 0     #ri-inizializzo il la dimensione massima raggiunta nei test ( se 1 = 10, 2 = 100 ...)
for i in num:
    rndRecords = RNDMergeSort()
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
    print("Merge Sort ha impiegato", rndTime, "secondi per ordinare un vettore di", rndN,
          "elementi casuali.")
for i in range(Nmax):                             #calcolo la media per dimensione
    avgTime[i] /= numTime[i]
print(":> Tempi medi registrati con vettore casuale: ", avgTime)





