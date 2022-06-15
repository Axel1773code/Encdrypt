# encdrypt
Encriptar, desencritar y desencriptar por fuerza bruta
el uso es fácil.
para ejecutar el programa es necesario tener instalado Python.
algunas dependecias el cuál puedes instalar con el comando pip 

- cryptocode 
- argparse 
- string
- random

los modulos pueden ser instalados de la siguiente manera remplazando package por el nombre del paquete publicado en Pypi
pip package

Uso de EncDrypt

el uso de EncDrypt en fácil por lo comenzaremos clonando el repositorio. 
git clone https://github.com/Axel1773code/encdrypt.git
ya clonado el repositorio dirigete hacia la carpeta.

PEDIR AYUDA

python encdrypt.py --help

ENCRIPTAR UN TEXTO 

python encdrypt.py --encrypt archivo_texto.txt --password 123

al encriptar con EncDrypt es necesario pasarle un archivo de texto al encriptar o desencriptar 


DESENCRIPTAR UN TEXTO 

python encdrypt.py --decrypt archivo_texto.txt --password 123

si la contraseña es incorrecta es devuelto False 

DESENCRIPTAR TEXTOS POR FUERZA BRUTA

parametros de forcebrute:
ul = letters(letras)  u = letras mayúsculas(upper)   l = letras minúsculas(lower)   d = digitos(digits)    p = puntuaciones(punctuation)  spaces = espacios(space)

python encdrypt.py --decrypt archivo_texto.txt --forcebrute d --range1 1 --range2 4

sinceramente no recomiento los parametros de forcebrute por lo que esa cadena es editable y puedes pasarles parametros como 123_.,sdkcndro
por lo que podria quedar así:

python encdrypt.py --decrypt archivo_texto.txt --forcebrute 1234 --range1 1 --range2 4 

el anterior código tratara de hayar la contraseña de este texto encriptado 

range1 y range2 indican la diferencia entre ambos rangos es decir range1 y range2 tiene de diferencia 3 ya que al suma 1+3=4 y iguala el range2 
