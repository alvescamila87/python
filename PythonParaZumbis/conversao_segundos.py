d = int(input("Dias: "))
h = int(input("Horas: "))
m = int(input("Minutos: "))
s = int(input("Segundos: "))

total = d*24*60*60 + h*60*60 + m*60 + s
print(f"""
      Dias: {d}", 
      Horas: {h}",
      Minutos: {m}", 
      Segundos: {s}",
      são um total de: {total} segundos.
""")