import importar as imp 
import division_procesos as dp
import config
print("---------Bienvenido al programa de ejecucion de comandos del robot---------\n")
print("---------Asegurese que el archivo se encuentre en la carpeta de archivos---------\n")
archivo=input("Ingrese el nombre del archivo con extension: ")
ola=imp.importar_archivo(archivo)

#Aqui se separan las instrucciones haciendolas de esta estructura
"""
instrucciones = ["E","X","E","C",["C","O","M","A","N","D","O"], "N","E","W",["C","O","M","A","N","D","O"]]
Cada comando se separa en una lista, si se encuentra una llave se hace una lista dentro de la lista
Se hace letra por letra porque los espacios no se tienen en cuenta
"""
#TODO: PODER HACER QUE      
def separar_instrucciones(instrucciones, inicio=0, cantidadllaves=0):
    instrucciones_separadas = [] # Lista donde se guardaran las instrucciones
    i = inicio # Posicion donde se encuentra
    while i < len(instrucciones): # Mientras no se haya llegado al final del programa
        if instrucciones[i] == "{": # Si se encuentra una llave se hace una subinstruccion
            subinstruccion, fin = separar_instrucciones(instrucciones, i + 1, cantidadllaves + 1) # Se hace una subinstruccion con la posicion siguiente en adelante
            instrucciones_separadas.append(subinstruccion) # Se guarda la subinstruccion
            i = fin # Se cambia la posicion a la del final de la subinstruccion para que no se repita
        elif instrucciones[i] == "}": #Es un caso base para saber cuando se cierra una llave y cuando la funcion tiene que devolverse
            return instrucciones_separadas, i
        else:# Si no es una llave se guarda la letra
            if instrucciones[i] != " " and instrucciones[i] != "\n" and instrucciones[i] != "\t": # Si no es un espacio se guarda
                instrucciones_separadas.append(instrucciones[i])
             # Se guarda un guion bajo para saber que es un espacio
        i += 1 #Se le suma 1 😲
    return instrucciones_separadas, i            
# Y ya :)
            
def divisor_procesos(instrucciones,string, i):
    #Se encarga de dividir los comandos y procesarlos de acuerdo a lo que se necesite
    numero=0
    if string.lower()=="exec":
        numero=dp.procesar_EXEC(instrucciones,i)
        if numero==False:
            return False
        else:
            numero=i
        string=""
    if string.lower()=="new":
        numero=dp.procesar_NEW(instrucciones,i)
        string=""
        
    return numero
    
def main():
    # Se encarga de recorrer la cadena y procesarla     
    instrucciones = separar_instrucciones(ola)[0]
    # Arma un string vacío para poder concatenar las letras
    string = ""
    i = 0
    contador_espacios = 0
    while i < len(instrucciones):
        # Verifica si el string actual es un comando base
        if string.lower() in config.comandos["base"]:
            # Llama a la función divisor_procesos con las instrucciones, el string y el índice ajustado
            numero = divisor_procesos(instrucciones, string, i)
            string = ""
            # Si la función retorna False, termina el programa con False
            if numero == False:
                config.syntax_correcta=False
                return False
            else:
                # Ajusta el índice para continuar después del comando procesado
                i = numero + 1
        else:
            if len(string) >= 5:
                config.syntax_correcta=False
                return False
        if i == len(instrucciones):
            return True 
        if type(instrucciones[i]) == str:
            if instrucciones[i] != "_":
                # Concatenar la letra al string
                string += instrucciones[i]
        # Incrementa el índice para la siguiente iteración
        i += 1
    # Si se ha recorrido toda la cadena de instrucciones
     
    
    
      
if __name__ == "__main__":
    retorno=main()
    if retorno==False or config.syntax_correcta==False:
        print("---------Error en el programa (No)---------")
    else:
        print("---------Programa ejecutado correctamente (Si)---------")