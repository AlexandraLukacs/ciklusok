## eljárásaink tesztelése
import eljaras

#Tesztesetek
print("1. teszteset: Pozitív számok")
eljaras.hanyados(3, 5)
print("2. teszteset: Negatív számok")
eljaras.hanyados(-5, -2)
print("3. teszteset: Tört számok - nem jó teszteset, mert egész számot")
eljaras.hanyados(-5.2, -2.2)
print("4. teszteset: Nincs paraméter")
eljaras.hanyados() # adtunk alapértelmezett
print("5. teszteset: A számláló 0, a=0")
eljaras.hanyados(0, -5)
print("5. teszteset: A nevező 0, b=0")
eljaras.hanyados(-5, 0)