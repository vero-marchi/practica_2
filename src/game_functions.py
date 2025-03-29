
"""
=============================================================
FUNCIÓN AUXILIAR
=============================================================
"""

def get_player_stats(player_data):
    """
    Obtiene las estadísticas de un jugador, asegurando valores por defecto para claves faltantes.

    Args:
        player_data (dict): diccionario con las estadísticas de un jugador.
    
    Returns:
        dict: diccionario con las estadísticas completas, incluyendo valores por defecto:
              'kills', 'assists', 'deaths' (int).
    """
    return {
        'kills': player_data.get('kills', 0),
        'assists': player_data.get('assists', 0),
        'deaths': player_data.get('deaths', 0)
    }


"""
=============================================================
FUNCIONES DE CÁLCULO
=============================================================
"""

def calculate_points(player_data):
    """
    Calcula los puntos de cada jugador para cada ronda, según cada acción.

    Args:
        player_data(dict): diccionario con las estadísticas de un jugador en la ronda.
        
    Returns:
        int: Puntos calculados según la fórmula:
            * 3 puntos por kill.
            * 1 punto por asistencia.
            * -1 punto por muerte.
    
    """
    stats = get_player_stats(player_data)
    return stats['kills'] * 3 + stats['assists'] * 1 - stats['deaths'] * 1


def update_stats(round_data, stats):
    """
    Actualiza el diccionario de estadísticas acumuladas con los datos de la ronda actual.

    Args:
        round_data (dict): diccionario donde cada clave es el nombre de un jugador (str), 
                           y cada valor es otro diccionario con estadísticas de la ronda:
                          'kills', 'assists', 'deaths' (int).
        stats (dict): diccionario con estadísticas acumuladas de todos los jugadores. 
                      Las claves son nombres de jugadores (str), y los valores incluyen:
                     'kills', 'assists', 'deaths', 'MVP', 'points' (todos int).

    Returns:
        None: modifica el diccionario stats, acumulando las estadísticas de la ronda.
    """
    # Itero por cada jugador de la ronda y calculo el puntaje basado en las acciones.
    for player in round_data:
        # Se contempla la posibilidad de que algún jugador no participe en la ronda
        if player not in stats:
            stats[player] = {'kills': 0, 'assists':0, 'deaths':0, 'MVP':0, 'points':0}
        
        # Llama a get_player_stats para obtener estadísticas con valores por defecto
        # Evita error del programa en caso de que alguna acción esté vacía
        stats_current = get_player_stats(round_data[player])
        
        stats[player]['kills'] += stats_current['kills']
        stats[player]['assists'] += stats_current['assists']
        stats[player]['deaths'] += stats_current['deaths']
        stats[player]['points'] += calculate_points(stats_current)

"""
=============================================================
FUNCIONES DE ANÁLISIS Y ORDENAMIENTO
=============================================================
"""

def find_mvp(round_data):
    """
    Busca el jugador con mayor puntaje de la ronda.
    
    Args:
        round_data(dict): diccionario donde cada clave es el nombre de un jugador (str), 
                          y cada valor es otro diccionario con sus estadísticas ('kills', 
                          'assists', 'deaths').
    
    Returns:
        str: nombre del jugador con mayor puntaje en la ronda.
        Devuelve None si no se encuentra un mvp
    """
    # Inicializo las variables
    max_points = 0
    mvp = None
    
    for player in round_data:
        points = calculate_points(round_data[player])
        if points > max_points:
            max_points = points
            mvp = player
    return mvp
    

def sort_by_points(stats):
    """
    Ordena las estadísticas en orden decrecientes según los puntos totales.
    
    Args:
        stats (dict): diccionario con estadísticas acumuladas de todos los jugadores. 
                      Las claves son nombres de jugadores (str), y los valores incluyen:
                      'kills', 'assists', 'deaths', 'MVP', 'points' (todos int).
    
    Returns:
        list: Lista de tuplas, donde cada tupla contiene:
          - Nombre del jugador (str).
          - Diccionario con sus estadísticas acumuladas.
          Las tuplas están ordenadas según la clave 'points' en orden descendente.

    """

    # Inicializo la lista
    sorted_stats = []
    for player, data in stats.items():
        sorted_stats.append((player,data))
    
    # range(len(sorted_stats) - i - 1): Ajusta el número de comparaciones necesarias a medida que el algoritmo avanza
    for i in range(len(sorted_stats)):
        for j in range(len(sorted_stats) -i -1):
            if sorted_stats[j][1]['points'] < sorted_stats[j + 1][1]['points']:
                temp = sorted_stats[j]
                sorted_stats[j] = sorted_stats[j + 1]
                sorted_stats[j + 1] = temp
                # Si los puntos son iguales, desempatar por kills en orden descendente
            elif sorted_stats[j][1]['points'] == sorted_stats[j + 1][1]['points']:
                if sorted_stats[j][1]['kills'] < sorted_stats[j + 1][1]['kills']:
                    # Intercambiar las posiciones
                    temp = sorted_stats[j]
                    sorted_stats[j] = sorted_stats[j + 1]
                    sorted_stats[j + 1] = temp
    return sorted_stats


"""
=============================================================
FUNCIÓN DE VISUALIZACIÓN
=============================================================
"""

def print_ranking(round_number, stats):
    """
    Imprime el ranking de los jugadores según las estadísticas acumuladas.

    Args:
        round_number (int or str): número de la ronda actual (int), o 'Final' para el ranking acumulado final.
        stats (dict): diccionario con estadísticas acumuladas de todos los jugadores.
                      Las claves son los nombres de jugadores (str), y los valores incluyen:
                      'kills', 'assists', 'deaths', 'MVP', 'points' (todos int).

    Returns:
        None: no retorna ningún valor. Imprime el ranking en formato de tabla.
        
    """
   
    sorted_stats = sort_by_points(stats)
    
    print("player    kills    assists    deaths    MVP    points")
    print("-"*54)
    
    for player, data in sorted_stats:
        print(f"{player:8} {data['kills']:8} {data['assists']:8} {data['deaths']:8} "
                  f"{data['MVP']:8} {data['points']:8}")
    print("-"*54)