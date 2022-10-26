
def value_of_mk()->int:
    from math import log
    # get masterkey
    masterkey = ""
    flag_masterkey = False

    while not flag_masterkey:
        masterkey = input("Contraseña Maestra: ")

        key = input(f"\n\n{masterkey} , esta de acuerdo? [S|N] ")

        if key in "sSyY":
            flag_masterkey = True

    # get masterpin
    masterpin = ""
    flag_masterpin = False

    while not flag_masterpin:
        masterpin = input("Pin Maestro: ")

        key = input(f"\n\n{masterpin} , esta de acuerdo? [S|N] ")

        if key in "sSyY":
            flag_masterpin = True
            masterpin = int(masterpin)

    # get encripted
    mastercount = 0
    for i in range(len(masterkey)):
        #   ord() | chr()
        xrf = ord(masterkey[i])
        xrf *= masterpin
        mastercount += xrf

    # put unic value (len-8)
    yrf = log(mastercount, masterpin)
    yrf *= 10000000

    return round(yrf)


def leer_archivo(file)-> tuple:
    from pickle import load
    tple = load(file)

    return tuple(tple)


def abrir_archivo(dir_file: str, mode: str):
    from os.path import exists

    # format directory and file result
    if dir_file[-1] == '\\':
        dir_file += "case.ecy"
    
    elif dir_file[-4:] != ".ecy":
        dir_file += ".ecy"


    # posibiliti open specific file for read or write
    if exists(dir_file) or mode[0] == "w":
        file = open(dir_file, mode)

    return file


def get_rute()-> str:
    from os.path import exists
    dir = 0
    while True:
        dir = input("Ingrese la Ruta del archivo ecy: ")
        if exists(dir):
            return dir
        else:
            print("Direccion Invalida...")


def salvar_archivo(file, obj):
    from pickle import dump
    dump(obj, file)

    return


def converter_fused(clave: int, registro: str)->tuple:
    volm = []
    for i in range(len(registro)):
        xor = ord(registro[i])
        xor *= clave
        volm.append(xor)

    return tuple(volm)


def desconvert_fused(clave: int, registro: str)->str|int:
    pssw = ""
    for i in range(len(registro)):
        yor = registro[i] / clave
        
        if str(yor)[-2:] != ".0":
            return -1

        else:
            yxr = chr(int(yor))
            pssw += yxr

    return pssw