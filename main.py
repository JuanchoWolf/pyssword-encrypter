from appmodule import *

def menu()->int:
    print(f"""
    {'='*40}
    \t\tMENU
    {'='*40}
    \t1) - Crear Contraseña.
    \t2) - Leer Contraseña.
    \t3) - Sair.
    {'='*40}
    """)

    opc = ""
    flag = False

    while not opc.isdigit() or (int(opc) < 1 or int(opc) > 3):

        if flag:
            print("Error, Nro Invalido Cargue Nuevamente...")

        else:
            flag = True
        opc = input("Opcion: ")

    return int(opc)


def mod1(mk: int):
    pssw = ""
    flag_pssw = False

    while not flag_pssw:
        pssw = input("Contraseña a guardar: ")

        key = input(f"\n\n{pssw} , esta de acuerdo? [S|N] ")

        if key in "sSyY":
            flag_pssw = True
    
    tpl = converter_fused(mk, pssw)

    dir = get_rute()
    name_file = input("Ingrese el nombre del Archivo: ")
    dir += f"\\{name_file}.ecy"
    fileO = abrir_archivo(dir, "wb")

    salvar_archivo(fileO, tpl)
    fileO.close()
    return


def mod2(mk: int):
    dir = get_rute()
    fileO = abrir_archivo(dir, "rb")

    reg_pwws = leer_archivo(fileO)
    fileO.close()

    pwws = desconvert_fused(mk, reg_pwws)

    if isinstance(pwws, str):
        print(f"\nSu clave Guardada es: {pwws}")

    else:
        print(f"\nLas claves maestras ingresadas no coinciden con las del archivo...")
    return 


def app()->None:
    while True:
        opc = menu()
        
        if opc == 1:
            masterkey = value_of_mk()
            mod1(masterkey)
            
        elif opc == 2:
            masterkey = value_of_mk()
            mod2(masterkey)

        else:
            exit('Done!')
    

if __name__ == '__main__':
    app()
