#simple
a = 33
b = 200

if b > a:
    print(b,"es mayor que ",a)

# Doble
y = 200
z = 300

if y > z:
    print(y," es mayor ",z)
else:
    print(y,"no es mayor que",z)

#Multiple
c = 200
d = 207
if c > d:
    print(c,"es mayor que",d)
elif c < d:
    print(c,"es menor que",d)
else:
    print(c,"es igual que",d)

#Condiciones enlazadas
x = 28

if x > 10:
    print("Por encima de diez,")
    if x > 20:
        print("y tambien por encima de 20!")
    else:
        print("pero no por encima de 20.")

#parametros end
print("Estudiar los sábados", end=' ')
print("es genial")

#print("Estudiar los sabados")
#print("es genial"

#parametros sep
print("Daniela","Luis","Carlos","Camila")#Agrega un espacio por defecto
print("Daniela","Luis","Carlos","Camila",sep="")#Quita el espacio
print("Daniela","Luis","Carlos","Camila",sep=",")#Agrega una coma

#parametros end y sep
print("Daniela","Luis","Carlos","Camila",sep="_",end="_Curso_python")#implementacion de end y sep
