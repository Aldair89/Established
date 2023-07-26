import psutil
#debes instalar el modulo psutil para que funcione
# Obtener las conexiones de red activas
conexiones = psutil.net_connections()

# Mostrar las conexiones de red
print("Conexiones de red activas:")
for conexion in conexiones:
    if conexion.status == 'ESTABLISHED':  # Filtrar conexiones establecidas
        print(f"Local Address: {conexion.laddr.ip}:{conexion.laddr.port} "
              f"-> Remote Address: {conexion.raddr.ip}:{conexion.raddr.port}")
