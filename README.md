# "Indumentariaonline"
## Tienda de ropa

Aplicación funcional con Django, con 3 páginas.<br>
Dos de ellas enlazan entre sí, que son "index" y "contacto".

### Layout:
Esqueleto HTML presente en todas las páginas, contiene un header con un logo que al clickearlo lleva a **index**, y un footer con información de copyright.

### Index:
*http://localhost:8000/shop/*
Muestra una tabla con todos los productos disponibles, con un hipervínculo que lleva al **contacto**

### Contacto:
*http://localhost:8000/shop/contacto*
Muestra información de contacto y un hipervínculo que lleva al **index**

### Nueva remera:
*http://localhost:8000/shop/nueva-remera*
Presenta un formulario que al llenar correctamente añade una nueva remera a la base de datos local
