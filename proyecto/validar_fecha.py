from datetime import datetime

def validar_fecha(fecha_str):
    """
    Verifica si una fecha en formato texto es válida.

    :param fecha_str: Fecha como string en formato 'YYYY-MM-DD'.
    :return: True si la fecha es válida, False en caso contrario.
    """
    try:
        datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False