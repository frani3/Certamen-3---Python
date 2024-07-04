from os import system
from random import randint
system("cls")



menu="""
1. Registrar pedido
2. Listar los todos los pedidos
3. Imprimir hoja de ruta
4. Buscar un pedido por ID
5. Salir del programa
"""

comunas=["CONCEPCION", "CHIGUAYANTE", "TALCAHUANO",
"HUALPEN", "SAN PEDRO"]
pedidos=[]

def registrar_pedido(comunas, pedidos):
    while True:
        nombre=input("Ingresar nombre del cliente: ").upper()
        if len(nombre)>3 and nombre.isalpha():
            break
        else:
            print("Nombre no válido.")
    while True:
        apellido=input("Ingrese apellido del cliente: ").upper()
        if len(apellido)>3 and apellido.isalpha():
            break
        else:
            print("Apellido no válido")
    while True:
        comuna=input("Ingrese comuna: ").upper()
        if comuna in comunas:
            break
        else:
            print("Comuna no válida. ")
    while True:
        direccion=input("Ingresar dirección: ").upper()
        if len(direccion)>3:
            break
        else:
            print("Dirección no válida. ")
    while True:
        disp_6=input("Ingrese cantidad de dispensador de 6 litros: ")
        if disp_6.isnumeric():
            disp_6=int(disp_6)
            if disp_6>=0:
                break
            else:
                print("Opción no válida")
        else:
            print("Debe ser númerico.")
    while True:
        disp_10=input("Ingrese cantidad de dispensador de 10 litros: ")
        if disp_10.isnumeric():
            disp_10=int(disp_10)
            if disp_10>=0:
                break
            else:
                print("Opción no válida")
        else:
            print("Debe ser númerico.")
    while True:
        disp_20=input("Ingrese cantidad de dispensador de 20 litros: ")
        if disp_20.isnumeric():
            disp_20=int(disp_20)
            if disp_20>=0:
                break
            else:
                print("Opción no válida")
        else:
            print("Debe ser númerico.")
    id=randint(100000,999999)
    nom_ape=nombre+" "+apellido
    detalle=[id, nom_ape, direccion, comuna, disp_6, disp_10, disp_20]
    pedidos.append(detalle)
    print("Pedido ingresado!")
    input("Ingrese enter para continuar...")

def listar_pedidos(pedidos):
    print("ID pedido      Cliente            Dirección      Sector      Disp.6lts      Disp.10lts      Disp.20lts")
    for persona in pedidos:
        print(f"{persona[0]}      {persona[1]}      {persona[2]}      {persona[3]}          {persona[4]}                {persona[5]}                 {persona[6]}")
    input("Ingrese enter para continuar...")

def hoja_ruta(pedidos):
    com=input("Ingrese sector para imprimir hora de ruta: ").upper()
    print("ID pedido      Cliente            Dirección      Sector      Disp.6lts      Disp.10lts      Disp.20lts")
    f=open("hoja_ruta.csv","w")
    f.write("ID pedido      Cliente            Dirección      Sector      Disp.6lts      Disp.10lts      Disp.20lts\n")
    for persona in pedidos:
        if persona[3]==com:
            print(f"{persona[0]}      {persona[1]}      {persona[2]}      {persona[3]}          {persona[4]}                {persona[5]}                 {persona[6]}")
            f.write(f"{persona[0]}      {persona[1]}      {persona[2]}      {persona[3]}          {persona[4]}                {persona[5]}                 {persona[6]}\n")
    input("Ingrese enter para continuar...")
    f.close()

def buscar_id(pedidos):
    while True:
        id_b=input("Ingrese ID a buscar: ")
        if id_b.isnumeric():
            id_b=int(id_b)
            break
        else:
            print("ID no válido.")
    print("ID pedido      Cliente            Dirección      Sector      Disp.6lts      Disp.10lts      Disp.20lts")
    for persona in pedidos:
        if persona[0]==id_b:
            print(f"{persona[0]}      {persona[1]}      {persona[2]}      {persona[3]}          {persona[4]}                {persona[5]}                 {persona[6]}")
    input("Ingrese enter para continuar...")

while True:
    system("cls")
    print("-------Bienvenido a CleanWasser------")
    print(menu)
    op=input("Seleccione una opción: ")
    if op=="1":
        print("-------Registrar Pedido------")
        registrar_pedido(comunas, pedidos)
    elif op=="2":
        listar_pedidos(pedidos)
    elif op=="3":
        hoja_ruta(pedidos)
    elif op=="4":
        buscar_id(pedidos)
    elif op=="5":
        break
    else:
        print("Opción no válida.")

