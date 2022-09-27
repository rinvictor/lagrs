#!/usr/bin/env python3
# Víctor Rincón Yepes, vrincon

import subprocess,sys,os
import vrincon_mod
'''
def exec(cmd):
    cmd_troceado=cmd.split()
    try:
        salida=subprocess.check_output(cmd_troceado)
    except subprocess.CalledProcessError:
        sys.stderr.write("La orden ha producido un error\n")
        raise SystemExit

    salida=salida.decode("utf-8") # De bytes a string

    return salida
'''
'''
def formato(salida):
    salida_troc=salida.split("HORA+ ORDEN")[1]
    #dividir el lineas

    lineas=salida_troc.split("\n")
    i=0
    while i < len(lineas):
        if len(lineas[i].split()) == 14:
            if lineas[i].split() [9] != "0,0":
                proc=lineas[i].split()[12]
                pid=lineas[i].split()[1]
                cpu=lineas[i].split()[9]
                user=lineas[i].split()[2]
                uid=vrincon_exec.exec("id -u "+user)
                uid=uid.split("\n")[0]
                grupos=vrincon_exec.exec("id -Gn "+user)
                grupos=grupos.split("\n")[0]
                print(proc+" "+pid+" "+user+" "+uid+" "+grupos+" "+ cpu)     
        i+=1  
'''

def main(): 
    lib_path = "/lagrs/lib" 
    full_path = os.environ['HOME'] + lib_path
    file1 = "/vrincon_mod.py"
    #comprobamos que PYTHONPATH existe
    if not "PYTHONPATH" in os.environ:
        raise SystemExit("Error: PYTHONPATH no existe")
    #comprobamos que el modulo esté en el PYTHONPATH
    found = False
    for path in os.environ['PYTHONPATH'].split(os.pathsep):
        if path == full_path:
            found = True
    if not found:
        raise SystemExit("Error: El path del módulo no está en PYTHONPATH")
    else:
        #compruebo que los archivos estén en los directorios
        if (not os.path.exists(full_path + file1)):
            raise SystemExit("Error: Faltan uno o más archivos")
    

    mandato="top -n 1"
    salida=vrincon_mod.exec(mandato)
    #print(salida)
    vrincon_mod.formato(salida)

if __name__ == "__main__":
    main()
