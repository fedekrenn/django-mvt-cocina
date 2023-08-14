# 👨‍🍳 Recetas de cocina

Web desarrollada en Django con patron MVT

## 📄 Descripción

Esta web permite a los usuarios consultar y crear recetas de cocina, cociner@s y restaurantes. Los conceptos que se tratan son:

- Herencia HTML
- Clases en modelos
- Formularios de ingreso de datos en todas las clases
- Relaciones entre clases
- Formulario de búsqueda de recetas por su nombre

## 🔧 Instalación

Para instalar el proyecto se debe clonar el repositorio 
```
git clone https://github.com/fedekrenn/Krenn-Federico-Comision-43865.git
```

## Uso

1 - Para utilizar el proyecto se debe ejecutar el siguiente comando en la carpeta del proyecto
```
python manage.py runserver
```

2 - Luego se debe ingresar al localhost en el puerto 8000
<br><br>
`http://127.0.0.1:8000/misitio` o `http://localhost:8000/misitio`

3 - Para ingresar al administrador se debe ingresar a la siguiente dirección
```
http://localhost:8000/admin
```
<br>

4 - La pantalla principal de la web muestra la bienvenida y un input de búsqueda por nombre de receta, el 
cual permite buscar recetas por su nombre. Si se ingresa un nombre de receta que no existe, se mostrará un mensaje de error.

<br>

![primero](https://github.com/fedekrenn/Tercera-pre-entrega-Krenn/assets/90353038/aeb7b656-2505-496c-a9f0-3db80177190f)

<br><br>

5 - En cada una de las 3 secciones que representan Clases (Recetas, Cocineros y Restaurantes) se podrá consultar una tabla con los 
registros cargados en la base de datos y clickeando el botón de call to action se abrirá un modal para la carga de datos la cual, 
si es correcta, redirigirá a una page de confirmación y se podrá ver la nueva entrada

<br>

![segundo](https://github.com/fedekrenn/Tercera-pre-entrega-Krenn/assets/90353038/96b0922a-f55f-45b3-aee5-a773e24476a1)

<br><br>

6 - En la ruta `/admin` se puede hacer CRUD mediante el panel que provee Django, existe un superuser cargado con user: "admin" y pass "admin"

<br>

![tercero](https://github.com/fedekrenn/Tercera-pre-entrega-Krenn/assets/90353038/4dfb2aea-2356-4eb0-be21-9067c18986e6)

<br>


## 🙋‍♂️ Hola, Soy Federico Krenn
:nerd_face: Desarrollador web
<br>
👨‍🎓 Realizando la Tecnicatura en Desarrollo Web en ISPC y Tecnicatura en Software Libre en la UNL
<br>
📫 Conectemos en Linkedin: https://www.linkedin.com/in/fkrenn/
