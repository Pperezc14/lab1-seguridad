#Pablo Pérez

import requests 

abc  = "abcdefghijklmnopqrstuvwxyz "
def CesarCifr(mensaje,n): #Funcion Cesar , recibe el mendasaje a cifrar y en n , este es la clave de cesar , en nuestro caso es 7 y 15 
    cifrado =""
    for l in mensaje: #Como el abc esta en mayuscula, el mensaje recibido se transforma en mayuscula
            if l in abc:
                i = abc.find(l)
                i += n
                if i >=27 :
                    i -= 27
                cifrado += abc[i]

            else:
                    cifrado + l 
            
    return cifrado

def CesarDes(cifrado,n):
    mensaje =""
    for l in cifrado:
        if l in abc:
                e = abc.find(l)
                e -=n
                if e<0:
                    e+=27
                  
                mensaje += abc[e]
        else:
                mensaje+ l
    return mensaje


def get_desp(char):
    return (ord(char.upper())-65)


def vigenereCif(mensaje,clave):
    cifrado = ""
    for i in range(0,len(mensaje)):
        des = get_desp(clave[i % len(clave)]) #Desplazamiento de la clave
        cifrado+=(CesarCifr(mensaje[i],des)) #Usamos Cesar
    return cifrado

def vigenereDescif(mensaje,clave):
    cifrado = ""
    for i in range(0,len(mensaje)):
        des = get_desp(clave[i % len(clave)]) #Desplazamiento de la clave
        cifrado+=(CesarDes(mensaje[i],des)) #Usamos Cesar
    return cifrado


def main():
    run = True
    while (run):
        print(" 1) Cifrar y descifrar")
        print(" 2) Salir")
        opcion = int(input("Indique su opción : "))
        print("-------------------------------------------------------------")
        if (opcion == 1):
            print("Desafio n°1")
            mensajeE = input("Ingrese el mensaje / Escribir en minuscula \n :")
            cesar1 = CesarCifr(mensajeE,7)
            vigenere1 = vigenereCif(cesar1,"cvqnoteshrwnszhhksorbqcoas")
            mensaje= CesarCifr(vigenere1,15)
            print(mensaje)
            headers = {
            'Content-Type': 'text/plain',
            }

            data = '{"msg":"cifrado(mensaje)"}'

            response = requests.post('http://finis.malba.cl/SendMsg', headers=headers, data=data)
        
            cesar2 = CesarDes(mensaje,15)
            vigenere2 = vigenereDescif(cesar2,"cvqnoteshrwnszhhksorbqcoas")
            mensajeF = CesarDes(vigenere2,7)
            print(mensajeF)

        else:
            print("Saliendo")
            run = False

main()


