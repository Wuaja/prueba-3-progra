import json
import funciones
import os
import datetime

def menu():
    print("**************************")
    print("*      MUNDO LIBRO       *")
    print("**************************")
    print()
    print("[1] - mantenedor de categorias")
    print("[2] - reportes")
    print("[3] - salir")
    global opc

    opc =int(input("ingrese la opción que desea: "))

    if opc == 1:
        

         print("**************************")
         print("*  MANTENEDOR CATEGORIAS *")
         print("**************************")
         print()
         print("[1] - Agrgar categoria")
         print("[2] - Editar categoria")
         print("[3] - Eliminar categoria")
         print("[4] - Buscar categoria")
         print("[5] - Volver")
         opc2 = int(input("Ingrese la opcion que desea: "))
         if opc2 == 1:   
            categoria_nueva=input("ingrese el nombre de la nueva categoria")
            funciones.agregar_categoria(nombre=categoria_nueva)
            print("Cambio realizado con exito")
         if opc2 == 2:
            funciones.editar_categoria(int(input("Ingrese el dato que desea editar: ")))
            print("Nombre editado con exito")
         if opc2 == 3:
             funciones.eliminar_cat(int(input("Ingrese la ID a eliminar: ")))
             print("Categoria eliminada con exito")
         if opc2 == 4:
             funciones.Buscar_CAT()

         else:
             print("Volviendo al menu anterior")
             print()
             menu()
    if opc == 2:
         print()
         print("**************************")
         print("*        REPORTES        *")
         print("**************************")
         print()

    if opc == 3:
        print("Adios")
        print()

menu()