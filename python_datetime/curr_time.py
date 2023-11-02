from datetime import datetime
from datetime import date

# get current date in different formats
# format codes

today = date.today()
d1 = today.strftime("%d-%m-%Y")
print("d1 : ", d1)
d2 = today.strftime("%m-%d-%Y")
print("d2 : ", d2)
# Texual month, day , year
d3 = today.strftime("%B %d, %Y")
print("d3 : ", d3)
d4 = today.strftime("%b-%d-%Y")
print("d4 : ", d4)

now = datetime.now()
t1 = now.strftime("%d/%m/%Y %H:%M:%S")
print(t1)