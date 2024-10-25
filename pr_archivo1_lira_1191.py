#"r"- Leer 
#"a"- Anexar 
#"w"- Escribir 
#"x"- Crear

print(" ")#espacio
print("Lira Hernandez Dayana Yamileth 1191")
print(" ")#espacio

f = open("demostracion.txt", "r")#abre y lee el archivo y su contenido
print(f.read())
f.close()#cierra el archivo
print(" ")#espacio
