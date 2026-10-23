from datetime import datetime, timedelta


fecha1 = datetime(2026, 1, 20) + timedelta(weeks=1, minutes=10)
fecha2 = datetime(2026, 3, 21)

delta = fecha2 - fecha1
print(delta)
print('dias', delta.days)
print('segundos', delta.seconds)
print('microseconds', delta.microseconds)
print('total_seconds', delta.total_seconds)
