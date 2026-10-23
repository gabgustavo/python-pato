import time
from datetime import datetime

# timestam (UTC)
# print(time.time())

fecha = datetime(2026, 10, 21)
fecha2 = datetime(2026, 10, 25)
print(fecha)

ahora = datetime.now()
print(ahora)

# strptime directives
# https://docs.python.org/3/library/datetime.html
fechaStr = datetime.strptime("2026-10-21 15:13:30", "%Y-%m-%d %H:%M:%S")
print(fechaStr)

# formatear una fecha
print(ahora.strftime("%d/%m/%Y %H:%M:%S"))

print(fecha > fecha2)
print(
    ahora.year,
    ahora.month,
    ahora.day,
    ahora.hour,
    ahora.minute,
    ahora.second,
)
