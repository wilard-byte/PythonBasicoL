peso = input("Cual es tu peso en Kg")
estatura = input("Cual es tu estatura en metros")


imc = round(float(peso)/float(estatura)**2,2)
if(imc<=18.5):
    print("Tu indice de masa corporal es",imc,"valor por debajo de lo normal")
elif(imc>=18.5 and imc<=24.9):
    print("Tu indice de masa corporal es",imc,"Tu indice es normal") 
elif(imc>=25.0 and imc>=29.9):
    print("Tu indice de masa corporal es",imc,"Tu indice esta por arriba de lo normal")
else:
    print("datos erroneos")
    

    
