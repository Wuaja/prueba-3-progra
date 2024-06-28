import json

def agregar_categoria(nombre:str):
    with open("biblioteca.json",mode='r') as LECTURA_JSON:
        LEER_JSON = json.load(LECTURA_JSON)
        nueva_categoria = {
            "categoriaID": len(LEER_JSON["categoria"])+1,
            "nombre" : nombre
        }
    LEER_JSON["categoria"].append(nueva_categoria)

    with open("biblioteca.json", mose= "w") as ESCRITURA_JSON:
        json.dump(LEER_JSON,ESCRITURA_JSON,indent=4)

def editar_categoria(Buscar_ID:int):
    with open("biblioteca.json",mode='r') as LECTURA_JSON:
     LEER_JSON =json.load(LECTURA_JSON)
    contador = 0
    for i in LEER_JSON["categoria"]:
        if i ["categoriaID"] == Buscar_ID:
            print(1)
            break    
        contador = contador+1
    LEER_JSON["categoria"][contador]["nombre"]= input("ingrese un nuevo nombre para la categoria: ")
    with open("biblioteca.json", mode="w" ) as ESCRITURA_JSON:
        json.dump(LEER_JSON, ESCRITURA_JSON, indent=4)

def eliminar_cat(eliminarCATE:int):
    with open("biblioteca.json", mode="r") as LECTURA_JSON:
        LEER_JSON=json.load(LECTURA_JSON)
        contador = 0
        for i in LEER_JSON["categoria"]:
            if i ["categoriaID"] == eliminarCATE:
                print (1)
                break
        contador = contador+1
        del LEER_JSON["categoriaID"][contador]
    with open("biblioteca.json", mode="w") as ESCRITURA_JSON:
        json.dump(LEER_JSON,LECTURA_JSON, indent=4)
    
def Buscar_CAT():
    with open("biblioteca.json", mode="r") as LECTURA_JSON:
     LEER_JSON =json.load(LECTURA_JSON)
     for i in LEER_JSON["categoria"]:
        print(1)