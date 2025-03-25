# FUNCION PARA VALIDAR USUARIO

def validate_user(username):
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


# FUNCIÓN PARA CLASIFICAR VELOCIDAD

# Clasifica el tiempo de reacción en categorías
def classify_reaction_time(reaction_time):
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
    


# FUNCIÓN PARA CONTAR PALABRAS CLAVE

def count_keywords(descriptions, keywords):

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
