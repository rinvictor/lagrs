#!/usr/bin/env python
import os, sys

def ishome(dir):
    if '~' in dir:
        home=os.path.expanduser('~') #home
        dir=home+dir.split("~")[1]
    return dir

def main():
    try:
        print("Se creará un enlace simbólico dst->src")
        print("Introduce la dirección de origen:")
        src=input()
        src=ishome(src)
        
        print("Introduce la dirección destino:")
        dst=input()
        dst=ishome(dst)
        #dst="/home/alumnos/vrincon/lagrs/practica02/mi_top.py"
        #src="/home/alumnos/vrincon/lagrs/practica02/mi_top02.py"
        os.symlink(src,dst)
        print("Enlace simbólico creado")
    except FileExistsError:
        sys.stderr.write("El enlace simbólico ya existe, bórralo para crear uno nuevo: rm "+ dst+"\n")
    except:
        print("Ha ocurrido un error")

if __name__=="__main__":
    main()
