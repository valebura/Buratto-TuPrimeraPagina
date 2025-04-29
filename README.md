💈 Barbería Manager
Este es un sistema web desarrollado en Django orientado a la gestión de una barbería. Permite registrar y administrar profesionales, cortes de pelo y clientes, junto con funcionalidades de autenticación de usuarios y edición de perfil.

✂️ Funcionalidades principales

🔐 Usuarios
- Registro de usuario (/registro)
- Login (/login)
- Logout
- Edición de perfil con fecha de nacimiento y avatar (/editar_perfil)
- Visualización de perfil (/ver_perfil)
Algunas acciones (como crear, editar o eliminar registros) solo están disponibles para usuarios autenticados.

👨‍🔧 Profesionales
- Crear profesional: /profesionales/crear
- Listar profesionales: /profesionales/
- Ver detalle de profesional: /profesionales/<id>
- Modificar profesional: /profesionales/<id>/modificar
- Eliminar profesional: /profesionales/<id>/eliminar

Cada profesional tiene:
- Nombre y apellido
- Años de experiencia
- Avatar (imagen)
- Fecha de ingreso

💇‍♂️ Cortes de pelo
- Crear corte: /cortes_pelo/crear
- Listar cortes: /cortes_pelo/
- Ver detalle del corte: /cortes_pelo/<id>
- Modificar corte: /cortes_pelo/<id>/modificar
- Eliminar corte: /cortes_pelo/<id>/eliminar

Cada corte incluye:
- Nombre del corte
- Precio
- Tiempo estimado (en minutos)

👥 Clientes
- Crear cliente: /clientes/crear
- Listar clientes: /clientes/
- Ver detalle del cliente: /clientes/<id>
- Modificar cliente: /clientes/<id>/modificar
- Eliminar cliente: /clientes/<id>/eliminar

Cada cliente posee:
- Nombre y apellido
- Email de contacto

📂 Estructura del proyecto
- home/: Contiene toda la lógica relacionada con profesionales, cortes de pelo y clientes.
- usuarios/: Gestión de login, registro, perfil y edición del usuario.
- templates/: Vistas HTML (no incluidas en este repo, pero se espera su presencia).
- media/: Carpeta donde se guardan los archivos subidos (como avatares e imágenes de profesionales).