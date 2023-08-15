import subprocess

while True:
    # Ejecuta el comando 'netsh' en Windows para obtener la información de las redes Wi-Fi
    comando_perfiles = "netsh wlan show profiles"
    resultado_perfiles = subprocess.run(comando_perfiles, capture_output=True, text=True)

    # Obtén la salida del comando
    salida_perfiles = resultado_perfiles.stdout

    # Imprime la lista de perfiles de redes Wi-Fi y las contraseñas
    print("Redes Wi-Fi conectadas:")
    for linea_perfiles in salida_perfiles.splitlines():
        if "Perfil de todos los usuarios" in linea_perfiles:
            # Extrae el nombre del perfil de red Wi-Fi
            perfil = linea_perfiles.split(":")[1].strip()

            # Ejecuta el comando para obtener la información detallada del perfil
            comando_informacion = f"netsh wlan show profile name=\"{perfil}\" key=clear"
            resultado_informacion = subprocess.run(comando_informacion, capture_output=True, text=True)

            # Obtén la salida del comando de información del perfil
            salida_informacion = resultado_informacion.stdout

            # Busca la línea que contiene la contraseña
            for linea_informacion in salida_informacion.splitlines():
                if "Contenido de la clave" in linea_informacion:
                    # Extrae la contraseña
                    clave = linea_informacion.split(":")[1].strip()
                    print(f"Perfil: {perfil}")
                    print(f"Contraseña: {clave}")
                    break

    opcion = input("¿Desea salir? (s/n): ")
    if opcion.lower() == 's':
        break
