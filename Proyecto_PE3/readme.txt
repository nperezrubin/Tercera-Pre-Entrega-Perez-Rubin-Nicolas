Pre Entrega #3 - Nicolás Pérez Rubín
----------------------------------------------------------------------------------------------------------------------------------------------

Página de inicio: http://127.0.0.1:8000/AppGoldenCafe/padre/

La web contiene un nav con los siguientes botones: 
- Inicio (padre.html) --> Utilizada para heredar templates. Contiene un mensaje exclusivo de esta vista: "Usted se encuentra en nuestra página de inicio. Bienvenido!"
- Clientes (cliente.html - heredada de padre.html) --> Contiene valoraciones de 2 clientes
- Pedidos (pedido.html - heredada de padre.html) --> Contiene los dos cafés más pedidos
- Sucursales (sucursal.html - heredada de padre.html) --> Muestra las 2 sucursales actuales
- Formulario Cliente (cliente_form_2.html) --> Permite ingresar nuevos registros a la clase Cliente
- Formulario Pedido (pedido_form_2.html) --> Permite ingresar nuevos registros a la clase Pedido
- Formulario Sucursal (sucursal_form_2.html) --> Permite ingresar nuevos registros a la clase Sucursal
- Iniciar Sesión (aún no activa)
- Registrarse (aún no activa)

- Para buscar un cliente, pedido, o sucursal de la BD, se debe ingresar a las urls:
  - /AppGoldenCafe/busquedaCliente --> búsqueda por nombre
  - /AppGoldenCafe/busquedaPedido --> búsqueda por tipo_cafe
  - /AppGoldenCafe/busquedaSucursal --> búsqueda por barrio



-----------------------------------------------------------------------------------------------------------------------------------------------

Notas:

--> Abrir carpeta del proyecto con VSC

Consola-Terminal
entorno-virtual-p/Scripts/activate (para activar el entorno virtual)
python manage.py runserver (para correr el servidor y que se pueda ver la página en el URL que indica)


GIT BASH
en git Bash: (ir a la carpeta del proyecto, click derecho --> open git bash here)
- git status
- git add .
- git commit -m "comentario sobre el commit"
- ls
- git push (para llevarlo al repo) (luego hacer F5 en el repo y validar los cambios)


ADMIN
http://127.0.0.1:8000/admin/
superuser: nico_goldencafe
email: contacto@goldencafe.com
pass: goldencafe1234

