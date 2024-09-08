variables={}
variables_nombres=[]
macros={}
parametros_temporales=[]
macros_nombres=[]
syntax_correcta = True
safeExe = False
constantes=["size","myx","myy","mychips","myballoons","balloonshere","chipshere","roomforchips"]
comandos={
#Definimos los comandos que se pueden usar en el lenguaje, se hace asi para poder verificar si el comando es valido 
# y no queda como "EXEC1" y en minuscula porque no importa si es mayuscula o minuscula
"base":["exec","new"],
"new":["var","macro",],
"exec":["turntomy","turntothe","walk","jump","drop","pick","grab","letgo","pop","moves","nop","safeExe"],
"turntomy":["left","right","back"],
"turntothe":["north, south, east, or west"],
"moves":["forward", "right", "left","backwards"],
"numeros":["0","1","2","3","4","5","6","7","8","9"],
"acciones":["walk","jump","drop","pick","grab","letgo","pop"],# Aquellos que se pueden usar en todo momento
"if":["if","then","else","fi","(",")"], # Aquellos que se pueden usar en un if
"do":["do","od","(",")"], # Aquellos que se pueden usar en un do
"rep":["rep","times","(",")"], # Aquellos que se pueden usar en un rep
"var":["new","var","="], # Aquellos que se pueden usar en una variable
"macro":["new","macro","(",")","{"], # Aquellos que se pueden usar en un macro
"condiciones":["isblocked?","isfacing?","zero?","not"], # Condiciones
"condiciones_valores":{
    "isBlocked?":["front","left","right","back"],
    "isfacing?":["north","south","east","west"],
    "not":["isblocked?","isfacing?","zero?"]}
}    
