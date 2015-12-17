"""Aquest programa fa pim pam pum utilitza (3 number) """



NUMBER1 = int(input("Introdueix un valor"))
NUMBER2 = int(input("Introdueix un altre valor"))

if NUMBER2 > NUMBER1:
    NUMBER3 = NUMBER1
    NUMBER1 = NUMBER2
    NUMBER2 = NUMBER3
if NUMBER1%NUMBER2 == 0:
    print("El nombre", NUMBER2, "es multiple de", NUMBER1)
else:
    print("El nombre", NUMBER2, "NO es multiple de", NUMBER1)
