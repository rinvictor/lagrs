#!/usr/bin/env python3
# Víctor Rincón Yepes, vrincon

import subprocess,sys, re
from optparse import OptionParser

def exec(cmd):
    cmd_troceado=cmd.split()
    try:
        salida=subprocess.check_output(cmd_troceado)
    except subprocess.CalledProcessError:
        sys.stderr.write("La orden ha producido un error\n")
        raise SystemExit

    salida=salida.decode("utf-8") # De bytes a string

    return salida

def tofloat(s):
    f=float(s.replace(",","."))
    return f

def formato(salida, usuario, umbral, memoria):
    #una comprobación extra usando expresiones regulares
    patron = re.search(r'(?<=\+ )\w+', salida) #comprueba que en salida exista una palabra seguida de un + y luego un ' '
    if patron == None:
        print("Error: formato no esperado")

    salida_troc=salida.split("HORA+ ORDEN")[1]
    #dividir el lineas

    lineas=salida_troc.split("\n")
    i=0
    while i < len(lineas):
        if len(lineas[i].split()) == 14:

            if memoria:
                #Realizo la comprobación usando expresiones regulares
                regex=re.compile(".*0,0.*")
                m=regex.match(lineas[i].split()[10]) #memoria
                if m==None:
                    proc=lineas[i].split()[12]
                    pid=lineas[i].split()[1]
                    mem=lineas[i].split()[10]
                    user=lineas[i].split()[2]
                    uid=exec("id -u "+user)
                    uid=uid.split("\n")[0]
                    grupos=exec("id -Gn "+user)
                    grupos=grupos.split("\n")[0]
                    print(proc+" "+pid+" "+user+" "+uid+" "+grupos+" "+ mem)

            else:
                #Realizo la comprobación usando expresiones regulares
                regex=re.compile(".*0,0.*")
                m=regex.match(lineas[i].split()[9])

                fcpu=tofloat(lineas[i].split()[9]) #paso a float cpu de la salida
                if m==None:
                    if (usuario == lineas[i].split()[2] or usuario =="") and fcpu > umbral:
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
    usage="python3 mi_top02.py [options]"
    parser = OptionParser(usage)
    #mostrar solo los procesos de un usuario concreto
    parser.add_option("-u","--user", action="store",dest="usuario",
    help="filtrado de usuario", default="")

    #muestro los procesos mayores que un numero de CPU dado
    parser.add_option("-o", "--over", action="store", dest="umbral",
    type="float", help="filtrado por CPU dado", default=0.0)

    #ordeno por memoria en lugar de ordenar por cpu
    parser.add_option("-m", "--memory", action="store_true", dest="memoria",
    help="ordenar por eluso de memoria", default=False)

    options,args = parser.parse_args()

    if options.memoria:
        mandato="top -o %MEM -n 1"
    else:
        mandato="top -n 1"
    salida=exec(mandato)
    #print(salida)
    formato(salida, options.usuario, options.umbral, options.memoria)

if __name__ == "__main__":
    main()
