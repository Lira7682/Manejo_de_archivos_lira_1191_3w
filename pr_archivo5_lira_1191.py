print(" ")#espacio
print("Lira Hernandez Dayana Yamileth 1191")
print(" ")#espacio
#Comprueba si el archivo existe y luego elimínalo
import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")#indica que el archivo ya no existe
print(" ")#espacio