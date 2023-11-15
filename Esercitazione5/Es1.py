import somme

n=input('Inserisci un numero: ')
x=int(n)
print('La somma dei primi ',x,' numeri naturali è : ', somme.somma(x))
y=int(input('inserisci un numero: '))
print('La somma delle prime ',y,' radici è : ', somme.radici(y))

j=int(input('inserisci un numero: '))
print('La somma e il prodotto dei primi ',j,' numeri sono: ', somme.sommaprodotto(j))
l=int(input('inserisci un numero: '))
p=int(input("inserisci un'altro numero"))
print('Il risultato è: ',somme.somman(l,p))
