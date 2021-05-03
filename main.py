
import os
from datetime import date


"""
Se tienen los datos de 20 estudiantes almacenados en 
‘c:\notas\entrada.dat’. En el archivo, la estructura de 
cada registro para cada estudiante estudiante es:

Lea los datos de los estudiantes almacenados en ‘c:\notas\entrada.dat’, 
y genere el archivo ‘c:\notas\salida.dat’, donde para cada estudiante 
se consideran los siguientes datos:

Promedio almacena el promedio de las 2 mejores notas.
Estado puede tomar el valor «A» si el estudiante aprueba, o «R» si reprueba.
Un estudiante aprueba cuando el promedio es mayor o igual que 60 y el
numero de faltas es menor que el 40% del total de clases dictadas (definido con una constante NUM_CLASES).
Un estudiante reprueba en caso de no cumplir tal requisito de aprobación.
"""








PROMEDIO_APROBADO  = 60
NUM_CLASES = 0.40
"""

Campos permitidos en el archivo para que el programa
funcione de manera correcta:
archivo.csv -> contenido :
    matricula (9 caracteres),
    apellido (10 caracteres), 
    nota1 (entero), 
    nota2 (entero), 
    faltas (entero)


Salida del reporte 
los campos que saldran son los siguientes
matricula (9 caracteres), apellido (10 caracteres), promedio (entero), estado (tipo caracter).

"""


def main():
    ruta = input("Ingrese ruta del archivo:\n")
    if os.path.isfile(ruta):
        with open(ruta,'r') as f:
            if os.stat(ruta).st_size == 0:
                print("Error! ese archivo esta vacio")
            else:
                data = [_.rstrip('\n').split(",") for _ in f.readlines()][1::]
                new_data = list()
                for value in data:
                    promedio,asistencia = 0,0
                    promedio = int((int(value[2])+int(value[3]))/2)
                    asistencia = round((int(value[4])/40)*NUM_CLASES,2)
                    if promedio >= 60 and asistencia < NUM_CLASES:
                        new_data.append([value[0]+',',value[1]+',',str(promedio)+',','A\n'])
                    else:
                        new_data.append([value[0]+',',value[1]+',',str(promedio)+',','R\n'])
                with open('reporte_notas_'+date.today().strftime("%d_%m_%y")+'.csv',"w") as f:
                    f.write('matricula,apellido,promedio,estado\n')
                    for value in new_data:
                        f.write(value[0]+value[1]+value[2]+value[3])
    else:
        print("Error! ese archivo no existe, verifique la ruta ingresada")




if __name__ == "__main__":
    main()