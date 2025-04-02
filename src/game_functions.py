
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
        str: player mvp de a ronda o none si no hay mvp.
    """
    
    #Inicialización de variables mvp y max_points
    mvp = None
    max_points = None
    
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
        
        
        points = calculate_points(stats_current)
        stats[player]['points'] += points
        
        # Comparación de puntaje para determinar mvp de la ronda
        if max_points is None or points > max_points:
            max_points = points
            mvp = player
            
    if mvp:
        stats[mvp]['MVP'] += 1

    return mvp
        

"""
=============================================================
FUNCIÓN DE ORDENAMIENTO
=============================================================
"""  

def sort_by_points(stats):
    """
    Ordena las estadísticas en orden decrecientes por puntos totales en primer lugar y kills en segundo lugar 
    usando sort()
    
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

    # Creo la lista
    sorted_stats = [(player, data) for player, data in stats.items()]
    
    # Uso el método sort() para ordenar la lista
    # La lista se ordena por points como primer criterio y kills como segundo criterio
    # reverse = True ordena de mayor a menor.
    sorted_stats.sort(key=lambda x: (x[1]['points'],x[1]['kills']), reverse=True)
    
    return sorted_stats
    

"""
=============================================================
FUNCIÓN DE VISUALIZACIÓN
=============================================================
"""

def print_ranking(round_number, stats, mvp=None):
    """
    Imprime el ranking de los jugadores según las estadísticas acumuladas.

    Args:
        round_number (int or str): número de la ronda actual (int), o 'Final' para el ranking acumulado final.
        stats (dict): diccionario con estadísticas acumuladas de todos los jugadores.
                      Las claves son los nombres de jugadores (str), y los valores incluyen:
                      'kills', 'assists', 'deaths', 'MVP', 'points' (todos int).
        mvp(str): mvp de la ronda.

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
    
    #Impresión del mvp de la ronda
    if mvp:
        print(f"MVP de la ronda: {mvp}")