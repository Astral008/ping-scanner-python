


# es importarte usar with para manejar los archivos, ya que esto garantiza que se cierren correctamente incluso si ocurre un error durante la lectura o escritura.
lista_ips=[]
def red_archivo():
    try :
        with open("hosts.txt","r") as archivo:
            for linea in archivo:
                print(linea.strip())
                lista_ips.append(linea.strip())
                print(f" IP encontradas y agregadas : {lista_ips} ")
    except FileNotFoundError:
        print("El archivo no se encontró.")


red_archivo()
