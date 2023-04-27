print("Bienvenido a nuestro proyecto, te recordamos que no somos profesionales, porfavor consulta un medico especializado.")
print("Porfavor ingrese 1 si es verdadero o 0 si es falso.")
contador=0

edad=input("Ingresa tu edad: ")
edad=int(edad)
print("Tienes ", edad, "años.")

if edad<=25:
    contador+=1

#empiezan preguntas

a=input("¿Consumes drogas?: ")
a=int(a)
if a==1:
    contador+=1
    a=input("¿Has consumido más de una vez? ")
    a=int(a)
    if a==1:
        contador+=1
        a=0
    a=input("¿Consumes más de una vez al mes? ")
    a=int(a)
    if a==1:
        contador+=1
        a=0
    a=input("¿Consumes alucinógenos? ")
    a=int(a)
    if a==1:
        contador+=1
        a=0
    a=input("¿Has consumido más de una vez? ")
    a=int(a)
    if a==1:
        contador+=1
        a=0
    a=input("¿Consumes más de una vez al mes? ")
    a=int(a)
    if a==1:
        contador+=1
        a=0
    a=input("¿Consumes alcohol o otras drogas de efecto retardante? ")
    a=int(a)
    if a==1:
        contador+=1
        a=0
    a=input("¿Consumes más de una vez a la semana? ")
    a=int(a)
    if a==1:
        contador+=1
        a=0
    a=input("¿Consumes frecuentemente? ")
    a=int(a)
    if a==1:
        contador+=1
        a=0
    
b=input("¿Alguien de tu línea sanguínea padece de alguna enfermedad mental?: ")
b=int(b)
if b==1:
    contador+=1
    b=input("¿Son más de una persona?: ")
    b=int(b)
    if b==1:
        contador+=1
        b=0
    b=input("¿Esta a menos de 3 generaciones arriba de ti?: ")
    b=int(b)
    if b==1:
        contador+=1
        b=0
    b=input("¿Padece alguna enfermedad mental de tipo trastorno como locura o alucinaciones?: ")
    b=int(b)
    if b==1:
        contador+=1
        b=0
    b=input("¿Padece de alguna enfermedad mental como alzheimer o esquizofrenia?: ")
    b=int(b)
    if b==1:
        contador+=1
        b=0



#resultados
print(contador, a)

if contador>22:
    print("error")
elif contador>=15:
    print("Ten cuidado, es probable que a largo plazo tengas un problema mental.")
elif contador>=10:
    print("Ten cuidado, es probable que a largo plazo tengas un problema mental.")
elif contador>=5:
    print("Ten cuidado, es probable que a largo plazo tengas un problema mental.")
else:
    print("Ten cuidado, es probable que a largo plazo tengas un problema mental.")