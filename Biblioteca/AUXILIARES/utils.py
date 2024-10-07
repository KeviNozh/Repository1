from datetime import datetime, timedelta

def calcular_multa(fecha_prestamo, fecha_devolucion):
    dias_retraso = (fecha_devolucion - fecha_prestamo).days
    if dias_retraso > 0:
        return dias_retraso * 2
    return 0

def dias_prestamo(fecha_prestamo):
    hoy = datetime.now().date()
    return (hoy - fecha_prestamo).days
