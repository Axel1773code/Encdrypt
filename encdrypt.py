import argparse
import cryptocode
import string
import random
parser = argparse.ArgumentParser()
parser.add_argument('--encrypt',help='encriptar texto')
parser.add_argument('--password',help='colocar la contraseña')
parser.add_argument('--decrypt',help='desencriptar texto pasando como parametro un archivo de texto')
parser.add_argument('--forcebrute',help='tratar de decifrar la contraseña del texto encriptado')
parser.add_argument('--range1',help='esto solo esta disponible para --forcebrute el cual indica el rango de combinaciones es decir 1-100 \nla cadena tendra entre 1 a 100 digitos \npara facilitar el trabajo al decifrar la contraseña si este parametro no se especifica por defecto es 1-9',type=int)
parser.add_argument('--range2',help='este es el argumento 2 el cual indica el rango 2',type=int)
args = parser.parse_args()
if args.encrypt and args.password:
  try:  
    file_encrypt = open(args.encrypt)
    print(cryptocode.encrypt(file_encrypt.read(),args.password))
    file_encrypt.close()
  except:
      print('Ha ocurrido un ERROR')
if args.decrypt and args.password:
    try:
        file_decrypt = open(args.decrypt)
        print(cryptocode.decrypt(file_decrypt.read(),args.password))
        file_decrypt.close()
    except:
         print('Ha ocurrido un ERROR')
if args.decrypt and args.forcebrute:
    ListCracker =  []
    #u = letras mayúsculas(upper)   l = letras minúsculas(lower)   d = digitos(digits)    p = puntuaciones(punctuation)  space = espacio(space)
    if args.forcebrute in 'ul':
      ListCracker += list(string.ascii_letters) 
    if args.forcebrute in 'd':
      ListCracker += list(string.digits)
    if args.forcebrute in 'p':
      ListCracker += list(string.punctuation)
    if args.forcebrute in 'l':
      ListCracker += list(string.ascii_lowercase)
    if args.forcebrute in 'u':
      ListCracker += list(string.ascii_uppercase)
    if args.forcebrute in 'space':
      ListCracker += ' '
    else:
       ListCracker += list(args.forcebrute)
    while True:
     try: 
       PassWordCracker = ''
       for i in range(args.range1,args.range2):
           PassWordCracker += random.choice(ListCracker)
       file_decrypt_force = open(args.decrypt)
       file_decrypt_forcebrute = file_decrypt_force.read()
       if cryptocode.decrypt(file_decrypt_forcebrute,PassWordCracker):
           print(f'Contraseña:{PassWordCracker}\nTexto(encriptado):{file_decrypt_forcebrute}\nTexto(desencriptado):{cryptocode.decrypt(file_decrypt_forcebrute,PassWordCracker)}')
           break
       else:
           print(f'Contraseña(error):{PassWordCracker}')
     except:
          print('Ha ocurrido un ERROR')