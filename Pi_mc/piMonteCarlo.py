import random
import csv

aproximaciones = []

for experimento in range(30):
    punto_circulo= 0
    punto_cuadrado= 0
    for i in range(10000):
            
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        punto= x**2 + y**2
        punto_cuadrado+=1

        if punto <= 1:
            punto_circulo+=1
            
        
        pi = 4*(punto_circulo / punto_cuadrado)

    print("Estimacion de PI: " , pi)
    aproximaciones.append(pi)
    

archivo_Coord= "Lista_coordenadas.csv"
with open( archivo_Coord,mode='w', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Iteracion", "Aproximacion"])

    for i in range(len(aproximaciones)):
        escritor.writerow([i+1, aproximaciones[i]])
print(f"Archivo,'{archivo_Coord}',creado correctamente.")

