import os

def importar_archivo(archivo:str):
    string_retorno=""
    path=os.getcwd()
    print(path)
    archivo = open(path + "/archivo/" + archivo, "r")
    for linea in archivo:
        string_retorno+=linea.strip()
    archivo.close()
    
    return string_retorno
if __name__ == "__main__":
    importar_archivo("archivo.txt")