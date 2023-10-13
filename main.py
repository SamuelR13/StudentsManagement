import os 
import time
import random

def register():

    nombre=input("Cual es el nombre del Coder?\n")
    ingreso=input("Cuando ingresó el Coder?\n")
    edad=input("Que edad tiene el Coder?\n")
    grupo=input("A que grupo lo quieres registrar?\n")
    inasistencias =input("Cuantas insasistencias tiene el Coder?\n")
    participacion=input("Cuantas participaciones tiene el Coder?\n")
    monitor=input("Cuantas monitorias tiene el Coder?\n")
    talleres =input("Cuantos talleres tiene el Coder?\n ")
    colaboraciones=input("Cuantas colaboraciones tiene el Coder?\n")
    nota_nivelacion =input("Cual fue la nota de seguimiento?\n")

    coder ={"nombre":nombre,
    "ingreso":ingreso,
    "edad":edad,
    "grupo":grupo,
    "inasistencias":inasistencias,
    "participacion":participacion,
    "monitor":monitor,
    "talleres":talleres,
    "colaboraciones":colaboraciones,
    "nota_nivelacion":nota_nivelacion} 
    return coder

def find(group_A,group_B,group_C,):
    names_a = []
    names_b = []
    names_c = []
    
    for indice,coder in enumerate(group_A):

            
        for indice,coder in enumerate(group_B):

           
            for indice,coder in enumerate(group_C):






def list(group:list):
        os.system("clear")
        if not group:
            print("El grupo se encuentra vacío\n")
        else:
            print("nombre-ingreso-edad-grupo-inasistencias-participacion-monitor-talleres-colaboraciones-nota de nivelacion")
            for indice, coder in enumerate(group):
                print(indice,coder["nombre"],coder["ingreso"],coder["edad"],coder["grupo"],coder["inasistencias"],coder["participacion"],coder["monitor"],coder["talleres"],coder["colaboraciones"],coder["nota_nivelacion"],)

def generalList(group:list,group1:list,group2:list):
        os.system("clear")
        groups=(group,group1,group2)
        if not group and group1 and group2:
            print("Los grupos se encuentra vacíos\n")
        else:
            print("nombre-ingreso-edad-grupo-inasistencias-participacion-monitor-talleres-colaboraciones-nota de nivelacion")
            for i in range(3):
                for indice, coder in enumerate(groups[i]):
                    print(indice,coder["nombre"],coder["ingreso"],coder["edad"],coder["grupo"],coder["inasistencias"],coder["participacion"],coder["monitor"],coder["talleres"],coder["colaboraciones"],coder["nota_nivelacion"],)



def age(group_A:list,group_B:list,group_C:list):
    mayoresA=[]
    menoresA=[]
    mayoresB=[]
    menoresB=[]
    mayoresC=[]
    menoresC=[]
    for indice,coder in enumerate(group_A):
        if coder["edad"]>="18":
            mayoresA.append(indice)
        else:
            menoresA.append(indice)
        
    for indice,coder in enumerate(group_B):
        if coder["edad"]>="18":
            mayoresB.append(indice)
        else:
            menoresB.append(indice)      
    for indice,coder in enumerate(group_C):
        if coder["edad"]>="18":
            mayoresC.append(indice)
        else:
            menoresC.append(indice)
    return [mayoresA,menoresA,mayoresB,menoresB,mayoresC,menoresC]


def main():
    print("-----Bienvenido Trainer Riwi-----\n")
    group_A=[]
    group_B=[]
    group_C=[]
    while True:
        selection=input("Ingresa el numero de la opcion que deseas realizar\n1. Registrar Coder\n2. Eliminar Coders con inasistencias\n3. Lista de Coders\n4. Cambiar de Grupo a un Coder\n5. Mostrar Coders mayores y menores de edad\n6. Buscar Coders con el mismo nombre.\n7. Registrar Trainer\n8. Salir\n")
        if selection =="1":
            flag1= True
            while flag1:
                coder=register()
                if coder["grupo"]=="A" or coder["grupo"]=="a":
                    group_A.append(coder)
                elif coder["grupo"]=="B" or coder["grupo"]=="b":
                    group_B.append(coder)
                elif coder["grupo"]=="C" or coder["grupo"]=="c":
                    group_C.append(coder)
                else:
                    print("Oops!, tenemos un error agrando al Coder en el grupo que ingresaste")
                while True:
                    exit=input("Desea seguir agregando Coders?\n1. Si\n2. No\n")
                    if exit =="1":
                        break
                    elif exit =="2":
                        flag1=False
                        break
                    else:
                        print("Oops! Creo que esa opcion no existe")

        elif selection =="2":
            for indice,coder in enumerate(group_A):
                if coder["inasistencias"]>="15":
                    group_A.pop(indice)
                    print("Se eliminara a ",coder["nombre"], "del grupo A")
            for indice,coder in enumerate(group_B):
                if coder["inasistencias"]>="15":
                    group_B.pop(indice)
                    print("Se eliminara a ",coder["nombre"], "del grupo B")            
            for indice,coder in enumerate(group_C):
                if coder["inasistencias"]>="15":
                    group_C.pop(indice)
                    print("Se eliminara a ",coder["nombre"], "del grupo C")

        elif selection =="3":
            while True:
                lista=input("De cual grupo deseas ver la lista?\n1. A\n2. B\n3. C\n4. Todos los grupos\n")
                if lista == "1":
                    list(group_A)
                    break
                elif lista =="2":
                    list(group_B)
                    break
                elif lista=="3":
                    list(group_C)
                    break
                elif lista=="4":
                    generalList(group_A,group_B,group_C)
                    break
                else:
                    print("Oops! Creo que ese grupo no existe")    

        elif selection =="4":
            flag4=True
            while flag4:
                group=input("De que grupo es el Coder que quieres mover?\n1. A\n2. B\n3. C\n")
                if group == "1":
                    list(group_A)
                    index=int(input("Ingresa el indice del Coder que quieres mover"))
                    os.system("clear")
                    if index<0 or index>len(group_A):
                        print("El index no es valido")
                    else:
                        print("El Coder",group_A[index]["nombre"],"fue eliminado del Grupo A\n")
                        while True:
                            groupMove=input("A que grupo lo deseas mover?\n1. B\n2. C\n")
                            if groupMove=="1":
                                group_B.append(group_A[index])
                                group_A.pop(index)
                                print("El Coder",group_B[index]["nombre"],"fue agregadp al Grupo B\n")
                            elif groupMove=="2":
                                group_C.append(group_A[index])
                                group_A.pop(index)
                                print("El Coder",group_C[index]["nombre"],"fue agregadp al Grupo C\n")
                            else:
                                print("Oops! Creo que ese grupo no existe")

                elif group =="2":
                    list(group_B)
                    index=int(input("Ingresa el indice del Coder que quieres mover"))
                    os.system("clear")
                    if index<0 or index>len(group_B):
                        print("El index no es valido")
                    else:
                        print("El Coder",group_B[index]["nombre"],"fue eliminado del Grupo B\n")
                        while True:
                            groupMove=input("A que grupo lo deseas mover?\n1. A\n2. C\n")
                            if groupMove=="1":
                                group_A.append(group_B[index])
                                group_B.pop(index)
                                print("El Coder",group_A[index]["nombre"],"fue agregadO al Grupo A\n")
                            elif groupMove=="2":
                                group_C.append(group_B[index])
                                group_B.pop(index)
                                print("El Coder",group_C[index]["nombre"],"fue agregadp al Grupo C\n")
                            else:
                                print("Oops! Creo que ese grupo no existe")           
                elif group=="3":
                    list(group_C)
                    index=int(input("Ingresa el indice del Coder que quieres mover"))
                    os.system("clear")
                    if index<0 or index>len(group_B):
                        print("El index no es valido")
                    else:
                        print("El Coder",group_C[index]["nombre"],"fue eliminado del Grupo C\n")
                        while True:
                            groupMove=input("A que grupo lo deseas mover?\n1. A\n2. B\n")
                            if groupMove=="1":
                                group_A.append(group_C[index])
                                group_C.pop(index)
                                print("El Coder",group_A[index]["nombre"],"fue agregadp al Grupo A\n")
                            elif groupMove=="2":
                                group_B.append(group_C[index])
                                group_C.pop(index)
                                print("El Coder",group_B[index]["nombre"],"fue agregadp al Grupo B\n")
                            else:
                                print("Oops! Creo que ese grupo no existe")
                else:
                    print("Oops! Creo que ese grupo no existe")
        
        elif selection =="5":
            ages=age(group_A,group_B,group_C)
            print(ages)
            groupAge=input("De que grupo deseas ver las edades?\n1. A\n2. B\n3. C\n")
            if groupAge=="1":
                print("Del grupo A los mayores son: ")
                for i in range(len(ages[0])):
                    print(group_A[i]["edad"])
                print("Del grupo A los menores son: ")
                for i in range(len(ages[1])):
                    print(group_A[i]["edad"])                    
            elif groupAge=="2":
                print("Del grupo B los mayores son: ")
                for i in range(len(ages[2])):
                    print(group_B[i]["edad"])
                print("Del grupo B los menores son: ")
                for i in range(len(ages[3])):
                    print(group_B[i]["edad"])                
            elif groupAge=="3":
                print("Del grupo C los mayores son: ")
                for i in range(len(ages[4])):
                    print(group_C[i]["edad"])
                print("Del grupo C los menores son: ")
                for i in range(len(ages[5])):
                    print(group_C[i]["edad"])                
            else:
                print("Oops! Creo que ese grupo no existe")


        elif selection =="6":
            find()

        elif selection =="7":
            trainer=input("A que grupo deseas registrar el Trainer\n1. A\n2. B\n3. C\n")
            trainerName=input("Nombre del Trainer")
            if trainer=="1":
                group_A.append(trainerName)
            elif trainer=="2":
                group_B.append(trainerName)
            elif trainer=="3":
                group_C.append(trainerName)
            else:
                print("Oops! Creo que ese grupo no existe")
            

        elif selection == "8":
            print("Saliendo...")
            time.sleep(2)
            break    
        else:
            print("Seleccion no valida, intentemos de nuevo")
    

main()    


