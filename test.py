import datetime
def calcular_horario(hora):
    """
    This function takes a time input and returns a string indicating whether it is in the morning,
    afternoon, evening, or late night.
    
    :param hora: The input parameter "hora" is expected to be a time object in the format of "HH:MM:SS"
    (hours, minutes, seconds) or a string that can be parsed into a time object
    :return: a string indicating the time of day based on the input time. The possible return values are
    "Madrugada" (dawn), "Mañana" (morning), "Tarde" (afternoon), or "Noche" (night).
    """
    hora_objeto = hora 
    if hora_objeto < datetime.time(6,0,0):
        return "Madrugada"
    elif hora_objeto < datetime.time(12,0,0):
        return "Mañana"
    elif hora_objeto < datetime.time(18,0,0):
        return "Tarde"
    else:
        return "Noche"