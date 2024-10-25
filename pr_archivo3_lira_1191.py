print(" ")#espacio
f = open("demostracion3.txt", "w")#abre el archivo
f.write("Woops! I have deleted the content!")#mensaje que indica que borra 
f.close()#espacio

f = open("demostracion3.txt", "r")
print(f.read())
print(" ")#espacio