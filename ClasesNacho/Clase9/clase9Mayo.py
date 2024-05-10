
listaApps = ["facebook", "instagram", "whastapp", "camara", "google"]

app = "whastapp"

if app in listaApps:
    print("Está instalada")
else:
    print("No está instalada, añadiendo a apps")
    listaApps.append(app)

print(listaApps)