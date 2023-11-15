def somma(n):
    risultato=0
    for i in range(n+1):
        risultato=risultato+i
    return risultato
def radici(n):
    risultato=0
    for i in range(n+1):
        risultato=risultato+i**(0.5)
    return risultato
def sommaprodotto(n):
    somma=0
    for i in range(n+1):
        somma=somma+i
    prodotto=1
    for i in range(1,n+1):
        prodotto=prodotto*i
    return somma,prodotto
def somman(n,a=1):
    risultato=0
    for i in range (n+1):
        risultato=risultato+i**(a)
    return risultato

        
