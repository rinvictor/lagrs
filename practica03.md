Víctor Rincón Yepes, vrincon

# Práctica 3

### Práctica 3.1. FHS
- 2014.01. Ejercicio 2
Cuando se crea un usuario nuevo se copia en su home el
directorio /etc/skel. Si lo borras, seguirá existiendo en los usuarios ya
creados pero al crear un usuario nuevo tendrás un problema.

- 2014.01. Ejercicio 3: El SUID en un ejecutable hará que cuando lo ejecute
cualquier usuario, los permisos del proceso sean los del dueño del fichero
en vez de los de quien ejecuta. Para un script no tiene sentido ya que un 
script no se ejecuta, lo interpreta un intérprete (el cual si es ejecutable).
Que un intérprete tenga el bit SUID activado si que tiene consecuencias y muy
peligrosas. Su dueño es root, por lo que si tiene SUID, sea quien sea quien
ejecute el intérprete, tendrá siempre permisos de root.

- 2014.01. Ejercicio 4: Por convenio, lo renombramos para que acabe en d.
Para la configuración de puesta en marcha y parada habrá que crear el script
/etc/init.d/ups
Para que se ejecute y deje de ejecutar cuando deseemos, tenemos que crear
los ficheros que servirán de enlace simbólico al script en sus
correspondientes niveles. Iniciarlo: /etc/rc2.d y terminarlo: /etc/rc0.d y
/etc/rc6.d

- 2014.06. Ejercicio 1: Los ficheros pueden estar referenciados por distintos
enlaces, con distintos nombres. Estas "flechas" van en el sentido del nombre
al fichero, y no a la inversa, por lo que desde un fichero no podemos llegar
a sus nombres, solo podemos saber el número de referencias que existen al
fichero porque se almacena en el inodo.

- 2014.06. Ejercicio 2: El journal permite reparar inconsistencias causadas
por ejemplo un apagón durante la copia de un fichero. Básicamente, 
primero apunta lo que se va a hacer y luego lo hace, de forma que si el 
trabajo se queda a medias, se puede arreglar de cierta forma y no 
estropearse el sistema de ficheros.

- 2014.06. Ejercicio 3: El formato .tgz es general para Linux y el .deb es
específico para Debian. Si tenemos Debian o derivado de Debian deberíamos
usar el .deb, aunque el .tgz también funcionará pero tendremos que resolver
a mano las dependencias e incompatibilidades. Si tenemos otro Linux deberemos
usar el .tgz ya que el .deb no funcionará.

- 2015.01. Ejercicio 4: La secuencia #! indica que a continuación se indica
el path del ejecutable que sabe interpretar ese texto. Si no aparece esa
línea, se ejecutará el intérprete por omisión. Quizá tengamos suerte y lo
entienda o quizá no. Si el script no tiene permiso de ejecución dará error al
intentar ejecutarlo. Como opción alternativa se le puede pasar al intérprete
por stdin (esquivando la ejecución del fichero).

- 2015.06. Ejercicio 2: /dev/sda1 es una de las particiones de sda (SCSI disk a)
Si se deniega el acceso es probablemente porque no está montado.

- 2017.12. Ejercicio 1: VT-x es una tecnología propia del procesador Intel que permite la virtualización nativa.

- 2017.12. Ejercicio 2: La shell consulta los directorios indicados en PATH
por lo tanto encontrará el fichero y lo podrá ejecutar. Sin embargo, la
variable PATH es local a la shell, y cuando iniciemos un terminal nuevo no
estará "actualizada". Para que se actualice siempre, debemos incluir el
comando correspondiente en el script .bashrc que se ejecuta al iniciar un
terminal (export...).

- 2017.12. Ejercicio 3: /lib contiene librerías esenciales para los ejecutables
del sistema. /usr/lib contiene librerías para ejecutables de menor importancia.
/usr/local/lib contiene librerías de programas no estándar de la distribución.

- 2018.12. Ejercicio 3: Al salir y entrar se ejecuta un proceso nuevo y se
vuelven a leer esos ficheros. Utilizando la orden source obtenemos ese 
resultado sin tener que salir y entrar y así mantenemos el contexto de la
shell.

### Práctica 3.2. Recode
He creado tres ficheros y he copiado infrmación de páginas web.
Compruebo su codificación usando file <fichero>:

```
vrincon@f-l2108-pc09:~/lagrs/practica03/recode$ file texto1.txt 
texto1.txt: UTF-8 Unicode text, with very long lines
vrincon@f-l2108-pc09:~/lagrs/practica03/recode$ file texto2.txt 
texto2.txt: UTF-8 Unicode text
vrincon@f-l2108-pc09:~/lagrs/practica03/recode$ file texto3.txt 
texto3.txt: UTF-8 Unicode text, with very long lines
vrincon@f-l2108-pc09:~/lagrs/practica03/recode$
```

Para comprobar la codificación de mi máquina uso echo $LANG:
```
vrincon@f-l2108-pc09:~/lagrs/practica03/recode$ echo $LANG
es_ES.UTF-8
```

Ahora cambio la codificación de estos ficheros:

>recode utf-8..utf-16 <texto1.txt> texto1.utf-16.txt

>recode utf-8..utf-16 <texto2.txt> texto2.utf-16.txt

>recode utf-8..utf-16 <texto3.txt> texto3.utf-16.txt
 
### Práctica 3.3 netstat

Voy a usar netstat -tu para obtener infomación sobre TCP y UDP.
Conectándome por ssh y haciendo netstat -tu el resultado es:
```
Conexiones activas de Internet (servidores w/o)
Proto  Recib Enviad Dirección local         Dirección remota       Estado      
tcp        0    208 f-l2108-pc09.aulas.:ssh 213.37.33.174.dyn:41954 ESTABLECIDO
tcp        0      0 f-l2108-pc09.aulas.:ssh 213.37.33.174.dyn:41930 ESTABLECIDO
tcp        0      0 f-l2108-pc09.aula:57766 ldap-fue-2.aulas.e:ldap ESTABLECIDO
tcp        0      0 f-l2108-pc09.aula:46840 gitlab.etsit.urjc:https ESTABLECIDO
tcp        0      0 f-l2108-pc09.aula:57756 ldap-fue-2.aulas.e:ldap ESTABLECIDO
tcp        0      0 f-l2108-pc09.aulas.:791 nfsserver-fue-1.aul:nfs ESTABLECIDO
tcp       36      0 f-l2108-pc09.aula:57764 ldap-fue-2.aulas.e:ldap ESTABLECIDO
tcp        0      0 f-l2108-pc09.aula:57758 ldap-fue-2.aulas.e:ldap ESTABLECIDO
tcp        0      0 f-l2108-pc09.aula:57748 ldap-fue-2.aulas.e:ldap ESTABLECIDO
udp        0      0 localhost.localdo:60135 localhost.localdo:60135 ESTABLECIDO
```

En el laboratorio:

```
Conexiones activas de Internet (servidores w/o)
Proto  Recib Enviad Dirección local         Dirección remota       Estado      
tcp        0      0 f-l3203-pc02.aulas:8000 labs.etsit.urjc.e:57618 ESTABLECIDO
tcp        0      0 f-l3203-pc02.aula:45552 93.184.220.29:http      TIME_WAIT  
tcp       36      0 f-l3203-pc02.aula:34642 ldap-fue-2.aulas.e:ldap ESTABLECIDO
tcp        0      0 f-l3203-pc02.aula:34654 ldap-fue-2.aulas.e:ldap ESTABLECIDO
tcp        0      0 f-l3203-pc02.aula:33356 mad41s11-in-f3.1e1:http TIME_WAIT  
tcp       36      0 f-l3203-pc02.aula:34648 ldap-fue-2.aulas.e:ldap ESTABLECIDO
tcp        0      0 f-l3203-pc02.aula:51352 ec2-54-149-93-22.:https TIME_WAIT  
tcp        0      0 f-l3203-pc02.aulas:1019 nfsserver-fue-1.aul:nfs ESTABLECIDO
tcp        0      0 f-l3203-pc02.aula:33344 mad41s11-in-f3.1e1:http TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:37226 mad41s14-in-f10.1:https TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:32838 mad07s10-in-f4.1e:https TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:48324 102.115.120.34.bc:https TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:38616 104.21.78.7:https       TIME_WAIT  
tcp        0      0 f-l3203-pc02.aulas:8000 labs.etsit.urjc.e:57628 ESTABLECIDO
tcp        0      0 f-l3203-pc02.aula:48326 102.115.120.34.bc:https TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:33298 mad41s11-in-f3.1e1:http TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:49338 239.237.117.34.bc:https TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:34916 server-52-84-45-5:https TIME_WAIT  
tcp        0      0 f-l3203-pc02.aulas:5901 f-l3203-pc02.aula:54274 ESTABLECIDO
tcp        0      0 f-l3203-pc02.aula:40762 mad41s10-in-f3.1e:https TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:34656 ldap-fue-2.aulas.e:ldap ESTABLECIDO
tcp        0      0 f-l3203-pc02.aula:50378 edge-703.bunnyinf:https TIME_WAIT  
tcp       37      0 f-l3203-pc02.aula:34646 ldap-fue-2.aulas.e:ldap ESTABLECIDO
tcp        0      0 f-l3203-pc02.aula:49340 123.208.120.34.bc:https TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:32820 82.221.107.34.bc.g:http TIME_WAIT  
tcp        0      0 f-l3203-pc02.aulas:8000 labs.etsit.urjc.e:57620 ESTABLECIDO
tcp        0      0 f-l3203-pc02.aula:42432 a130-206-192-18.de:http TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:40760 mad41s10-in-f3.1e:https TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:42216 188.2.233.35.bc.g:https TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:38126 mad07s22-in-f16.1:https TIME_WAIT  
tcp        0      0 f-l3203-pc02.aulas:8000 labs.etsit.urjc.e:57638 ESTABLECIDO
tcp        0      0 f-l3203-pc02.aula:50382 edge-703.bunnyinf:https TIME_WAIT  
tcp        0      0 f-l3203-pc02.aulas:8000 labs.etsit.urjc.e:57622 ESTABLECIDO
tcp        0      0 f-l3203-pc02.aula:33338 mad41s11-in-f3.1e1:http TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:40068 104.18.31.182:http      TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:42218 188.2.233.35.bc.g:https TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:40766 mad41s10-in-f3.1e:https TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:53756 gitlab.etsit.urjc:https ESTABLECIDO
tcp        0      0 f-l3203-pc02.aula:45484 93.184.220.29:http      TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:34914 server-52-84-45-5:https TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:42398 a130-206-192-18.de:http TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:45396 aulavirtual.urjc.:https TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:33336 mad41s11-in-f3.1e1:http TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:33346 mad41s11-in-f3.1e1:http TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:35046 mad41s10-in-f8.1e:https TIME_WAIT  
tcp        0      0 f-l3203-pc02.aulas:8000 labs.etsit.urjc.e:57624 ESTABLECIDO
tcp        0      0 f-l3203-pc02.aula:32822 82.221.107.34.bc.g:http TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:49264 104.16.86.20:https      TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:56740 server-52-85-3-76:https TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:40764 mad41s10-in-f3.1e:https TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:50852 11.56.241.35.bc.g:https TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:35176 server-52-84-45-2:https TIME_WAIT  
tcp        0      0 f-l3203-pc02.aulas:8000 labs.etsit.urjc.e:57632 ESTABLECIDO
tcp        0      0 f-l3203-pc02.aula:56846 mad41s13-in-f10.1:https TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:46184 server-52-85-3-13:https TIME_WAIT  
tcp        0      0 f-l3203-pc02.aula:54274 f-l3203-pc02.aulas:5901 ESTABLECIDO
tcp6       0      0 f-l3203-pc02.aulas:1716 f-l3207-pc41.aula:57628 ESTABLECIDO
tcp6       0      0 f-l3203-pc02.aulas:1716 f-l3202-pc01.aula:33130 ESTABLECIDO
tcp6       0      0 f-l3203-pc02.aulas:1716 f-l3202-pc07.aula:45578 ESTABLECIDO
tcp6       0      0 f-l3203-pc02.aulas:1716 f-l3202-pc05.aula:34336 ESTABLECIDO
tcp6       0      0 f-l3203-pc02.aulas:1716 f-l3202-pc06.aula:59202 ESTABLECIDO
tcp6       0      0 f-l3203-pc02.aulas:1716 f-l3202-pc09.aula:35588 ESTABLECIDO
tcp6       0      0 f-l3203-pc02.aulas:1716 f-l3202-pc10.aula:46308 ESTABLECIDO
tcp6       0      0 f-l3203-pc02.aulas:1716 f-l3207-pc50.aula:54316 ESTABLECIDO
tcp6       0      0 f-l3203-pc02.aulas:1716 f-l3207-pc29.aula:38280 ESTABLECIDO
tcp6       0      0 f-l3203-pc02.aulas:1716 f-l3203-pc01.aula:33908 ESTABLECIDO
tcp6       0      0 f-l3203-pc02.aulas:1716 f-l3202-pc08.aula:38962 ESTABLECIDO
udp        0      0 localhost.localdo:49131 localhost.localdo:49131 ESTABLECIDO
```
En el primer caso aparece mi propia conexión ssh con esepuesto, en el segundo no aparece y, además, hay muchas másconexiones con otras máquinas y servicios.

### Práctica 3.4. tmux

Tal y como dice el enunciado, ejecuto en segundo plano tictacvrin (tras darle permisos con chmod +x)
Tras esto, hago tail -f /tmp/log.vrincon.txt, puedo ver como va la ejecución.

 - Copio en /tmp el script
 - Hago tmux
 - Ejecuto el script que había copiado previamente
 - Cierro el terminal(me da igual que me avise que hay un trabajo corriendo)
 - Vuelvo a conectarme por ssh
 - Hago tmux attach

¡Genial! Ahí sigue el trabajo

### Práctica 3.5. Túnel ssh inverso
En primer lugar descargo los dos scripts, romanserver.py y romanclient.py
>mkdir ~/bin, y los dejo ahí.

>chmod +x *

Pruebo los programas haciendo:
>./romanserver TCP 8000

>./romanclient localhost TCP 800 1

Me devuelve 1 en números romanos.

>Ahora inicio con vagrant up la máquina de vbox01 y hago vagrant ssh para acceder a ella.

>sudo apt install tmux, ya está instalado.

>Para abrir una ventana es la ctrl + b + "

>Para cambiar de una ventana a otra crtl +b + o

Ya tengo romanserver.py en la máquina de vagrant.

Para hacer el túnel inverso hago desde la máquina de Vagrant:
>ssh -R 9000:localhost:8000 vrincon@f-l3209-pc03.aulas.etsit.urjc.es

Dentro de la máquina de vagrant:
>./romanserver.py TCP 8000

Desde la máquina de la universidad:
>./romanclient.py localhost TCP 9000 2

### Práctica 3.6. Cron
No tenia en este ordenador ningún crontab.
Al hacer crontab -e (para editar una tabla) me dice que seleccione un editor, elijo nano.
Escribo en mi crontab:
> \* * * * * touch /tmp/test_cron_vrincon

Para comprobar que hace un touch cada minuto: 
>ls -l /tmp | grep test_cron_vrincon

Borro la entrada de la tabla.

He escrito escribe_log, (estoy usando mi ordenador personal por lo que no he seguido las especificaciones concretas de path)
>chmod +x escribe_log

Ejecuto escribe_log, funciona correctamente.
Ahora uso cron para que se ejecute cada minuto:
>\* * * * * /home/vrincon/Dropbox/temp_lagrs/practica03/escribe_log

¡Funciona!

Por último, modifico la entrada para que se ejecute de lunes a viernes a las 9:
>\* 9 * * 1-5 /home/vrincon/Dropbox/temp_lagrs/practica03/escribe_log

