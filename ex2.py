""" AQUEST PROGRAMA INDICA QUIN ES MES GRAN O IGUAL """

NUM1 = int(input("Introdueix el primer valor "))
NUM2 = int(input("Intrpdueix el segon valor "))

if NUM1 > NUM2:
    print("El numero mes gran es", NUM1)
else:
    if NUM1 < NUM2:
        print("El numero mes gran es", NUM2)
    else:
        print("Els numeros son identics")
