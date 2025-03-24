
# FUNCION PARA VALIDAD USUARIO

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