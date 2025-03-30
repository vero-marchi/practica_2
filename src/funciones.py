## Importaciones para utilizar en las funciones
import random
import string
from datetime import datetime


"""
======================================================
FUNCION PARA VALIDAR USUARIO - EJERCICIO 4
======================================================
"""

def validate_user(username):
    """
    Valida un nombre de usuario con los siguientes criterios:
    - Al menos 5 caracteres.
    - Contiene al menos un número.
    - Contiene al menos una letra mayúscula.
    - Contine solo letras y números.
    
    Args: 
    Nombre de usuario a validar (str).
    
    Returns: 
    bool: True si se cumplen todos los criterios. False si no se cumple alguno de ellos

    """
    
    # Verificar si el usuario tiene menos de 5 caracteres y retorna falso
    if len(username) < 5:
        return False

    # Inicializo variables booleanas para verificar las condiciones
    has_number = False
    has_uppercase = False

    # Recorro con un for cada caractér de username
    for char in username:
        # Verifico si el caracter es un número
        if char.isdigit():
            has_number = True
        # Verifico si es una letra mayúscula
        elif char.isupper():
            has_uppercase = True
        # Verifico si el caracter no es ni una letra ni un número
        # char.isalpha() devuelve True si el carácter es una letra (A-Z, a-z)
        # Si no es una letra ni un número devuelve false
        elif not (char.isalpha() or char.isdigit()):
            return False

    # Retorno True o False verificando si se cumplen las condiciones
    return has_number and has_uppercase


"""
======================================================
FUNCIÓN PARA CLASIFICAR VELOCIDAD - EJERCICIO 5
======================================================
"""

def classify_reaction_time(reaction_time):
    """
    Dado un tiempo de reacción ingresado, los clasifica en las siguientes categorías:
    - Menos de 200 ms: Rápido
    - Entre 200 y 500 ms: Normal
    - Más de 500 ms: Lento
    
    Args: 
    Tiempo de reacción(int).
    
    Returns: 
    str: categoría correspondiente al tiempo de reacción.

    """    

    # Si el tiempo es menor a 200 lo calsifica en rápido
    if reaction_time < 200:
        return "Rápido"
    # Si el tiempo está entre 200 y 500 lo calsifica en normal
    elif 200 <= reaction_time <= 500:
        return "Normal"
    # Si no es menor a 200 ni está entre 200 a 500, entonces es mayor a 500
    # Si el tiempo es mayor a 500 clasifica en lento
    else:
        return "Lento"


    
"""
======================================================
FUNCIÓN PARA CONTAR PALABRAS CLAVE - EJERCICIO 6
======================================================
"""

def count_keywords(descriptions, keywords):
    """
    Cuenta las veces que se repita una palabra en una lista de descripciones (str).
    
    Args: 
    descriptions(list of str): lista de descripciones en las que se buscarán las palabras clave.
    Keyword(str): palabra clave qie se buscará en las descripciones.
    
    Returns: 
    int: cantidad de veces que la palabra clave se encuentra en la lista de descripciones.

    """   

    # Inicializo un diccionario clave-valor para llevar el conteo de menciones
    count = {keyword: 0 for keyword in keywords}
        
    # Recorro cada elemento de la lista
    for description in descriptions:
        # Separo las palabras
        words = description.lower().split()
        # Recorro la lista  de palabras clave a buscar
        for keyword in keywords:
            # Cuento las menciones exactas
            count[keyword] += words.count(keyword)

    # Retorno
    return count



"""
=============================================================
FUNCIÓN GENERADOR RANDOM DE CODIGO DE DESCUENTO -EJERCICIO 7
=============================================================
"""

def code_generator(username):
    """
    Genera un código de descuento aleatorio de 30 caracteres para un usuario.
    
    Este código se forma combinando el nombre de usuario (en mayúsculas), la fecha actual 
    y una cadena de 20 caracteres aleatorios.
  
    
    Args: 
    username(str): debe tener menos de 15 caracteres.
    
    Returns: 
    str: código de 30 caracteres conformado por nombre + fecha + caracteres aleatorios.
    None: si se ingresó un nombre de usuario mayor a 15 caracteres.

    """  

    # Verifico que el nombre de usuario no exceda los 15 caracteres
    if len(username) > 15:
        # Si excede los 15 caracteres imprimo mensaje de, sino avanzo al else
        print ('El nombre de usuario no puede exceder los 15 caracteres')
        return None
    else:
        # Genero la fecha actual
        date = datetime.today().strftime("%Y%m%d")
        
        # Definir los caracteres posibles
        valid_chars = string.ascii_uppercase + string.digits
        
        random_chars = ""

        # Generar la cadena de 20 caracteres aleatorios
        for i in range(20):
            random_chars += random.choice(valid_chars)

        # Concatenar el nombre del usuario, la fecha y los caracteres aleatorios
        discount_code = username.upper() + date + random_chars

        # Asegurarse de que el código tenga una longitud de 30 caracteres
        discount_code = discount_code[:30]

        return discount_code
        

