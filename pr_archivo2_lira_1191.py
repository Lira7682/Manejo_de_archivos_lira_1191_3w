print(" ")#espacio
print("Lira Hernandez Dayana Yamileth 1191 3W")
print(" ")#espacio

f = open("demostracion2.txt", "a")#abre el archivo y anexa el contenido
f.write("Now the file has more content!")
f.close()#cierra el archivo

f = open("demostracion2.txt", "r")#abre y lee el archivo y su contenido
print(f.read())

print(" ")#espacio