def hanyados(a: int =1,b: int =1):
    if b == 0 :
        print("0-val nem lehet osztani!")
    else:
        osszeg:  float= a / b 
        print(f"{a} / {b} = {osszeg: .2f}")