#!/usr/bin/env python3
# Víctor Rincón Yepes, vrincon

import subprocess,sys

def exec(cmd):
    cmd_troceado=cmd.split()
    try:
        salida=subprocess.check_output(cmd_troceado)
    except subprocess.CalledProcessError:
        sys.stderr.write("La orden ha producido un error\n")
        raise SystemExit

    salida=salida.decode("utf-8") # De bytes a string

    return salida


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
                uid=exec("id -u "+user)
                uid=uid.split("\n")[0]
                grupos=exec("id -Gn "+user)
                grupos=grupos.split("\n")[0]
                print(proc+" "+pid+" "+user+" "+uid+" "+grupos+" "+ cpu)     
        i+=1  


def main():
    mandato="top -n 1"
    salida=exec(mandato)
    #print(salida)
    formato(salida)

if __name__ == "__main__":
    main()
