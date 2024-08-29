from datetime import date

mi_fecha = date(1999, 2, 3)
print(mi_fecha)

from datetime import date

hoy = date.today()
print(hoy)

from datetime import datetime

ahora = datetime.now()
minutos = datetime.now().minute

print(minutos)
print(ahora)