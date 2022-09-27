#!/usr/bin/env python3
import os
from datetime import datetime, timedelta
import time
import sys

def recorrer(dir,intervalo):
    files=[]

    if type(intervalo) != int:
        sys.stderr.write("Error!, No se acepta un intervalo no entero\n")
        status="No se acepta un intervalo no entero"
        return files, status

    if '~' in dir:
        home=os.path.expanduser('~') #home
        dir=home+dir.split("~")[1]
        
    try:
        contenido = os.listdir(dir)
    except:
        sys.stderr.write("Error!, No existe el directorio\n")
        status="No existe el directorio"
        return files,status


    else:
        try: 
            for nombredirectorio, dirs, ficheros in os.walk(dir):
                for nombrefichero in ficheros:

                    fecha_modif = os.path.getmtime(nombredirectorio+'/'+nombrefichero)
                    fecha_actual = time.time()
                    fecha_actual=datetime.fromtimestamp(fecha_actual)
                    fecha_modif=datetime.fromtimestamp(fecha_modif)
                    #quiero los ficheros cuya fecha de modificación sea posterior a:
                    fecha_umbral=(fecha_actual - timedelta(days=intervalo))

                    if (fecha_modif > fecha_umbral):
                        files.append(nombredirectorio+'/'+nombrefichero)
                        status = "ok"
        except:
            sys.stderr.write("Error!, No se puede acceder a ese directorio\n") #problemas de permisos
            files=[]
            status="No se puede acceder a ese directorio"

    return files, status


def main():
    f=recorrer("/home/vrincon/Dropbox/temp_lagrs", 8)
    print("---")
    f2=recorrer("~/lagrs", 70)

    print(f)
    print(f2)

if __name__ == "__main__":
    main()
