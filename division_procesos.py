import config

def procesar_if(instrucciones, actual): 
    string = ""
    i = actual
    centinela = False

    while i < len(instrucciones):

        if type(instrucciones[i]) == str:
            string += instrucciones[i]
        
        if string.lower() == "then":
            i+=1
            numero=procesar_then(instrucciones,i)
            string=""
        elif string.lower() == "else":
            numero = procesar_else(instrucciones, i + 1)
            string=""
        elif string.lower() == "not":
            numero = procesar_not(instrucciones, i + 1)
            centinela = True
        elif string == "(":
            numero = procesar_condicional(instrucciones, i)
            centinela = True
        elif string == ")":
            string = ""
            i += 1
            continue
        if centinela:
            string = ""
            if numero != False:
                i = numero
            centinela = False
        if string.lower() == "fi;":
            return i  
        elif i < len(instrucciones) and instrucciones[i] == ")":
            i += 1
            continue 
        i += 1                    

    for j in range(i, len(instrucciones)):
        if type(instrucciones[j]) == str and instrucciones[j].lower() == "fi":
            return j
        elif type(instrucciones[j]) ==list:
            procesar_if(instrucciones[j], 0)
        
    
    config.syntax_correcta=False
    return False

         
def procesar_then(instrucciones, actual):
    if type(instrucciones[actual])==list:
        return procesar_EXEC(instrucciones[actual], 0)
def procesar_else(instrucciones, actual):
    return procesar_EXEC(instrucciones, actual)
    
def procesar_condicional(instrucciones, actual):
    string = ""
    i = actual
    centinela = False
    numero=0
    if instrucciones[i] == "(":
        i+=1
        while i < len(instrucciones) and not centinela:
            if type(instrucciones[i]) == str:
                string += instrucciones[i]
            if len(string) >= 9:
                if string.lower() == "isblocked?":
                    numero= procesar_isBlocked(instrucciones, i+1)
                    centinela = True
                if string.lower() == "isfacing?":
                    numero = procesar_isFacing(instrucciones, i+1)
                    centinela = True
            elif len(string) >= 4:
                if string.lower() == "zero?":
                    numero = procesar_zero(instrucciones, i+1)
                    centinela = True
            elif len(string) >= 3:
                if string.lower() == "not":
                    numero = procesar_not(instrucciones, i)
                    centinela = True     
            i += 1
        if numero!=False:
            return numero
    return False
def procesar_isBlocked(instrucciones, actual):
    string=""
    i=actual
    centinela=False
    if instrucciones[i]=="(":
        i+=1
        while i < len(instrucciones):
            while instrucciones[i]!=")" and not centinela:
                if instrucciones[i]!="_":
                    string+=instrucciones[i]
                if i == len(instrucciones)-1:
                    centinela=True
                i+=1
            if string.lower() in config.comandos["condiciones_valores"]["isBlocked?"]:
                return i+1
            else:
                config.syntax_correcta=False
                return False
    config.syntax_correcta=False
    return False
       
def procesar_isFacing(instrucciones, actual):
    string = ""
    i = actual
    centinela = False
    if instrucciones[i]=="(":
        i+=1
        while i < len(instrucciones):
            while instrucciones[i]!=")" and not centinela:
                if instrucciones[i]!="_":
                    string+=instrucciones[i]
                if i == len(instrucciones)-1:
                    centinela=True
                i+=1
            if string.lower() in config.comandos["condiciones_valores"]["isfacing?"]:
                return i+1
            else:
                config.syntax_correcta=False    
                return False
    config.syntax_correcta=False
    return False
        
def procesar_zero(instrucciones, actual):
    string = ""
    i = actual
    centinela = False
    if instrucciones[i]=="(":
        i+=1
        while i < len(instrucciones):
            while instrucciones[i]!=")" and not centinela:
                if instrucciones[i]!="_":
                    string+=instrucciones[i]
                if i == len(instrucciones)-1:
                    centinela=True
                i+=1
            if string.lower() in config.constantes:
                return i
            elif string.lower().isdigit() and not instrucciones[i].isdigit():
                return i
            else:
                config.syntax_correcta=False
                return False
    config.syntax_correcta=False
    return False
def procesar_not(instrucciones, actual):
    return procesar_condicional(instrucciones, actual)

def procesar_EXEC(instrucciones, actual):
    string = ""
    i = actual
    centinela = False
    numero = 0
    contador_instrucciones = 0
    while i < len(instrucciones) and not centinela:
        if type(instrucciones[i]) == list:
            instrucciones=instrucciones[i]
            centinela=True
        i+=1
    i=0
    centinela=False
    while i < len(instrucciones) or not centinela:
        if type(instrucciones[i]) == str:
            string += instrucciones[i]
        if string.lower() in config.macros_nombres:
            numero = procesar_macro_creado(instrucciones, i+1, string)
            if numero == False:
                config.syntax_correcta=False
                return False
            i=numero
            string=""
            contador_instrucciones+=1
        if len(string) >= 9:
            if string.lower() == "turntothe" and instrucciones[i+1] == "(":
                contador_instrucciones+=1
                numero = procesar_turnToThe(instrucciones, i)
                if numero == False:
                    config.syntax_correcta=False
                    return False
                i=numero
                string=""
        elif len(string) >= 7:
            if string.lower() == "turntomy" and instrucciones[i+1] == "(":
                contador_instrucciones+=1
                numero = procesar_turnToMy(instrucciones, i+1)
                if numero == False:
                    config.syntax_correcta=False
                    return False
                i=numero
                string=""
            elif string.lower() == "safeexe" and instrucciones[i+1] == "(":
                contador_instrucciones+=1
                numero = procesar_safeExe(instrucciones, i+1)
                if numero == False:
                    config.syntax_correcta=False
                    return False
                i=numero
                string=""
                
        elif len(string) >= 5:
            if string.lower() == "letgo" and instrucciones[i+1] == "(":
                contador_instrucciones+=1
                numero = procesar_accion(instrucciones, i)
                if numero == False:
                    config.syntax_correcta=False
                    return False
                i=numero
                string=""
            elif string.lower() == "moves" and instrucciones[i+1] == "(":
                contador_instrucciones+=1
                numero = procesar_moves(instrucciones, i+1)
                if numero == False:
                    config.syntax_correcta=False    
                    return False
                i=numero
                string=""

        elif len(string) >= 4:
            if string.lower() in ["walk","jump","drop", "pick" ,"grab"] and instrucciones[i+1] == "(":
                contador_instrucciones+=1
                numero = procesar_accion(instrucciones, i)
                if numero == False:
                    config.syntax_correcta=False
                    return False
                i=numero
                string=""
        elif len(string) >= 3:
            if string.lower() == "rep":
                contador_instrucciones+=1
                numero = procesar_rep(instrucciones, i+1)
                if numero == False:
                    config.syntax_correcta=False
                    return False
                i=numero
                string=""
            if string.lower() == "pop" and instrucciones[i+1] == "(":
                contador_instrucciones+=1
                numero = procesar_accion(instrucciones, i)
                if numero == False:
                    config.syntax_correcta=False
                    return False
                string=""
                i=numero
            elif string.lower() == "nop":
                contador_instrucciones+=1
                numero = procesar_nop(instrucciones, i)
                if numero == False:
                    config.syntax_correcta=False
                    return False
        elif len(string) >= 2:
            if string.lower() == "if":
                contador_instrucciones+=1
                numero = procesar_if(instrucciones, i+1)
                if numero == False:
                    config.syntax_correcta=False
                    return False
                i=numero
                string="" 
            elif string.lower() == "do":
                contador_instrucciones+=1
                numero = procesar_do(instrucciones, i+1)
                if numero == False:
                    config.syntax_correcta=False
                    return False
                i=numero-1
                string=""
        
        i += 1  
        if centinela==True:
            config.syntax_correcta=False
            return False
        if i == len(instrucciones) and contador_instrucciones == 0:
            config.syntax_correcta=False
            return False
        elif i == len(instrucciones) and contador_instrucciones > 0:
            return i
    return numero
def procesar_macro_creado(instrucciones, actual,string):
    if instrucciones[actual] == "(":
        """
        {"nombre": nombre,              ej: foo
        "parametros": param,            ej: a,b      ej: ""
        "bloque": bloque_codigo})       ej: [Esta guardado]
        """
        pos = actual
        cantidad_parametros = 0
        cantidad = 0
        proceso = False
        while pos < len(instrucciones) and not proceso:
            if instrucciones[pos] == ",":
                cantidad_parametros += 1
            if instrucciones[pos] == ")":
                proceso = True
            else:
                pos += 1
        
        parametros_macro = config.macros[string].get("parametros","")
        
        if parametros_macro == "":
            parametros_macro = 0
        else:
            cantidad = parametros_macro.count(",")
        
        if cantidad != cantidad_parametros:
            config.syntax_correcta=False
            return False
            
        if instrucciones[pos] != ")":
            config.syntax_correcta=False
            return False
        pos += 1
        if pos >= len(instrucciones):
            config.syntax_correcta=False
            return False
        if instrucciones[pos] != ";":
            config.syntax_correcta=False
            return False
        elif instrucciones[pos] != ";" and len(instrucciones) == pos:
            config.syntax_correcta=False
            return False
        
    return pos
        
def procesar_do(instrucciones, actual):
    if instrucciones[actual] == "(":
        actual=procesar_condicional(instrucciones, actual)
        actual+=1
        if type(instrucciones[actual])==list:
            procesar_EXEC(instrucciones[actual], 0)
        string_od=""
        actual+=1
        while string_od!="od;" and type(instrucciones[actual])==str:
            string_od+=instrucciones[actual]
            actual+=1
        if string_od.lower()=="od;":
            return actual
        else:
            config.syntax_correcta=False
            return False
    config.syntax_correcta=False
    return False
        
        

def procesar_NEW(instrucciones, actual):
    string = ""
    i = actual
    centinela = False
    numero = 0
    while i < len(instrucciones) and not centinela:
        if type(instrucciones[i]) == list:
            config.syntax_correcta=False
            return False
        elif type(instrucciones[i]) == str:
            string += instrucciones[i]
        if len(string) >= 5:
            if string.lower() == "macro":
                numero = procesar_NEW_MACRO(instrucciones, i)
                centinela = True
            else:
                config.syntax_correcta=False
                return False
        elif len(string) >= 3:
            if string.lower() == "var":
                numero = procesar_NEW_VAR(instrucciones, i)
                centinela = True
            # NO SE ALGUIEN ARREGLE ESTO AAAAAAAAAAAAAA
            elif string.lower() == "mac" or string.lower() == "macr":
                i+=1
                continue
            else:
                config.syntax_correcta=False
                return False
        i += 1
    return numero 
   
def procesar_NEW_VAR(instrucciones, actual):
    # Inicialización de variables
    nombre = ""
    valor = ""
    igual = 0
    i = actual + 1
    centinela = False
    string_temporal = ""
    string = "" 
    igual_encontrado = False    
    while i < len(instrucciones) and not centinela and "exec" not in string_temporal.lower() and "new" not in string_temporal.lower():
        # Verifica si hay espacios, si los hay, se salta a la siguiente letra
        # Verifica si el elemento actual de las instrucciones es un igual
        string_temporal += instrucciones[i]
        if instrucciones[i] == "=":
            igual_encontrado = True
            # Guarda la posición del igual
            igual = i
            for j in range(actual + 1, i):
                # Añade el nombre de la variable si no es un espacio
                if instrucciones[j] != "_":
                    nombre += instrucciones[j]
        # Si se ha encontrado un igual, se añade el valor de la variable
        if igual != 0:
            string += instrucciones[i]
        # Si lo que sigue es otro comando, se termina
        if "new" in string.lower():
            centinela = True
            i -= 3
        elif "exec" in string.lower():
            centinela = True
            i -= 4
        i += 1
    
    # Check if the equal sign was not found
    if not igual_encontrado:
        config.syntax_correcta=False
        return False
    #Se añade el valor de la variable
    for j in range(igual+1,i):
        if instrucciones[j]!="_":
            valor+=instrucciones[j]
    #Se añade la variable a la lista de variables
    config.variables[nombre]=valor
    config.variables_nombres.append(nombre)
    i-=1
    return i

def procesar_NEW_MACRO(instrucciones, actual):
    nombre = ""
    param = ""
    bloque_codigo = ""
    pos = actual+1
    string=""
    contador_para_parentesis=actual+1
    contador_parentesis=0
    while contador_para_parentesis < len(instrucciones) and ("new" not in string.lower() or "exec" not in string.lower()) :
        if type(instrucciones[contador_para_parentesis])==list:
            break
        string+=instrucciones[contador_para_parentesis]
        if instrucciones[contador_para_parentesis]=="(":
            contador_parentesis+=1
        if instrucciones[contador_para_parentesis]==")":
            contador_parentesis-=1
        contador_para_parentesis+=1
    if contador_parentesis % 2 != 0:
        config.syntax_correcta=False
        return False
    
    in_bloque = False
    in_param = False
    procesado = False

    pos_param = 0
    
    while pos < len(instrucciones) and not procesado:
        if instrucciones[pos] == "(" and not in_bloque:
            nombre = "".join(instrucciones[actual+1:pos])
            config.macros_nombres.append(nombre)
            config.macros[nombre] = {}
            pos_param = pos+1
            in_param = True
        if instrucciones[pos] == ")" and in_param:
            param = "".join(instrucciones[pos_param:pos])
            config.macros[nombre]["parametros"] = param
            config.parametros_temporales=param.split(",")
            pos_bloque = pos+1
            in_param = False
            in_bloque = True
        if in_bloque:
            bloque_codigo = instrucciones[pos_bloque]
            numero=procesar_EXEC(instrucciones,pos_bloque) #numero es como pos
            if numero==False:
                config.syntax_correcta=False
                return False
            procesado = True
        pos += 1
    if not procesado:
        config.syntax_correcta=False
        return False
    config.macros_nombres.append(nombre)
    config.macros[nombre] = {"parametros": param, #Si no tiene parametros queda como ""
                             "bloque": bloque_codigo}
    return pos
    

def procesar_turnToMy(instrucciones, actual):
    if instrucciones[actual] == "(":
        # Quitar el (
        actual += 1
        string = ""
        
        while actual < len(instrucciones) and instrucciones[actual] != ")":
            if instrucciones[actual] != "_":
                string += instrucciones[actual]
            actual += 1
        
        # Si se sale del ciclo y no se encuentra el paréntesis de cierre
        if actual >= len(instrucciones) or instrucciones[actual] != ")":
            config.syntax_correcta=False
            return False
        
        # Quitar el )
        actual += 1
        
        if string.lower() in config.comandos["turntomy"] and instrucciones[actual] == ";":
            return actual
        elif string.lower() in config.variables_nombres and instrucciones[actual] == ";":
            if config.variables[string.lower()] in config.comandos["turntomy"]:
                return actual
        else:
            config.syntax_correcta=False
            return False
    else:
        config.syntax_correcta=False
        return False
def procesar_turnToThe(instrucciones, actual):  
    if instrucciones[actual] == "(":
        # Quitar el (
        actual += 1
        string = ""
        
        while actual < len(instrucciones) and instrucciones[actual] != ")":
            if instrucciones[actual] != "_":
                string += instrucciones[actual]
            actual += 1
        
        # Si se sale del ciclo y no se encuentra el paréntesis de cierre
        if actual >= len(instrucciones) or instrucciones[actual] != ")":
            config.syntax_correcta=False
            return False
        
        # Quitar el )
        actual += 1
        
        if string.lower() in config.comandos["turntothe"] and instrucciones[actual] == ";":
            return actual
        elif string.lower() in config.variables_nombres and instrucciones[actual] == ";":
            if config.variables[string.lower()] in config.comandos["turntothe"]:
                return actual
        else:
            config.syntax_correcta=False
            return False
    else:
        config.syntax_correcta=False
        return False

def procesar_accion(instrucciones, actual):
    i = actual
    encontrado=False
    while i < len(instrucciones) and not encontrado:
        if instrucciones[i] == "(":
            i += 1
            numeros = ""
            string = ""
            while instrucciones[i] != ")":
                if instrucciones[i].isdigit():
                    numeros += instrucciones[i]
                else:
                    string += instrucciones[i]
                i += 1
            if i < len(instrucciones) and instrucciones[i] == ")":
                if len(numeros) > 0:
                    encontrado=True
                elif len(string) > 0:
                    if string.lower() in config.constantes:
                        encontrado=True 
                    elif string.lower() in config.variables_nombres or string.lower() in config.parametros_temporales:
                        encontrado=True
                    else:
                        config.syntax_correcta=False
                        return False
                else:
                    config.syntax_correcta=False
                    return False
            else:
                config.syntax_correcta=False
                return False
        i += 1
    if i == len(instrucciones) or instrucciones[i] != ";":
        config.syntax_correcta=False
        return False
    return i
def procesar_moves(instrucciones, actual):
    i=actual
    if instrucciones[i]=="(":
        i+=1
        string=""
        contador_strings=0
        contador_comas=0
        parentesis=False
        while i < len(instrucciones):
            if instrucciones[i]==")":
                parentesis=True
            if instrucciones[i]==";" and contador_strings==contador_strings and parentesis and len(string)==0:
                return i  
            if string in config.comandos["moves"]:
                contador_strings+=1
                string=""
            if instrucciones[i]==",":
                contador_comas+=1
                i+=1
            if instrucciones[i]!="_" and parentesis==False:
                string+=instrucciones[i]  
            i+=1
        config.syntax_correcta=False
        return False                
def procesar_nop(instrucciones, actual):
    for i in range(actual, len(instrucciones)):
        if instrucciones[i] == ";":
            return i
    config.syntax_correcta=False
    return False
def procesar_safeExe(instrucciones, actual):
    string=""
    i=actual
    centinela=False 
    modificador=False
    while i < len(instrucciones) and not centinela:
        if instrucciones[i]=="(":
            if modificador==False:
                i+=1
                modificador=True
            if string.lower() =="walk" or string.lower()=="jump" or string.lower()=="drop" or string.lower()=="pick" or string.lower()=="grab" or string.lower()=="pop" or string.lower()=="letgo" :
                i=procesar_accion(instrucciones,i)
        if instrucciones[i]==")":
            centinela=True
        string+=instrucciones[i]
        i+=1
    if i < len(instrucciones) and instrucciones[i]==";":
        return i
    else:
        config.syntax_correcta=False
        return False
    return i
            
def procesar_rep(instrucciones, actual):
    string = ""
  
    i = actual
    centinela = False
    error_en_rep = False
    while i < len(instrucciones) and not centinela:
        if type(instrucciones[i]) == list:
            centinela = True
        if type(instrucciones[i]) == str:
            string += instrucciones[i]
        if string.isdigit() and not(instrucciones[i+1].isdigit()):
            centinela = True
        elif string.lower() in config.constantes:
            centinela = True
        elif string.lower() == "times":
            centinela = True
        elif "times" in string.lower():
            error_en_rep = True
        i += 1
    string_constante = ""
    if error_en_rep == False:
        while i < len(instrucciones) and string_constante.lower() != "times":
            string_constante += instrucciones[i]
            i += 1
    else:
        return False

    if i < len(instrucciones) and type(instrucciones[i]) == list:
        procesar_EXEC(instrucciones, i-1)
    return i+1