
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
        if char.isupper():
            has_uppercase = True
        # Verifico si el caracter no es ni una letra ni un número
        # char.isalnum() devuelve True si el carácter es una letra (A-Z, a-z) o un número (0-9).
        # Si hubiere caracteres especiales, espacio, símbolos, etc, devuelve false
        if not char.isalnum():
            return False

    # Verifica si se cumplen todas las condiciones
    if has_number and has_uppercase:
        return True
    return False


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
