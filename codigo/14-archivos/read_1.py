archivo = open("archivo.txt", "r")

contenidos = archivo.read()
archivo.close()  # Ya se almacenaron los contenidos del archivo

print(contenidos)