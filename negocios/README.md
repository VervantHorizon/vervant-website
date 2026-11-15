# Vervant Local — catálogo de cotización

## Oferta comercial piloto
Catálogo móvil hecho por Vervant para fabricantes y negocios que cotizan productos o trabajos a medida.

- Precio piloto: USD 149 pago único para los tres primeros proyectos.
- Precio regular previsto: USD 249.
- Alcance: hasta 12 fichas, categorías, búsqueda, fotografías optimizadas, solicitud guiada a WhatsApp y una ronda de cambios.
- Complemento: ficha de capacidades de una página en PDF por USD 49 con el catálogo.
- Entrega: HTML autónomo listo para publicarse en el alojamiento del cliente o en un servicio de alojamiento elegido por separado.
- No incluye dominio, alojamiento de pago, tienda, pagos, inventario, integraciones privadas ni mensualidad de mantenimiento.

## Estado técnico
- index.html: oferta comercial y landing page en español.
- constructor/index.html: constructor español. La exportación genera un catálogo autónomo con búsqueda, filtros por categoría y formulario guiado de cotización que prepara un mensaje contextual para WhatsApp.
- en/index.html y en/builder/index.html: landing y constructor en inglés.
- capability-sheet/index.html y en/capability-sheet/index.html: generador de ficha de capacidades A4 en español e inglés.
- El HTML generado no requiere backend, cuenta ni base de datos.
- Las imágenes se optimizan en el navegador y se incrustan en el archivo.
- Los campos del formulario de cotización no se guardan; el usuario decide abrir el mensaje preparado en WhatsApp.

## Cómo probar
Desde la raíz del repositorio estático:
    python3 -m http.server 8081
Abrir:
- http://127.0.0.1:8081/negocios/
- http://127.0.0.1:8081/negocios/constructor/

En el constructor:
1. Pulsa Cargar ejemplo.
2. Introduce un WhatsApp de prueba propio (solo dígitos y código de país).
3. Descarga el HTML.
4. Abre el HTML descargado y prueba búsqueda, filtros y formulario de WhatsApp. No envíes mensajes de prueba a números ajenos.
5. Sustituye el ejemplo por contenido y fotografías autorizadas antes de entregar a un cliente.

## Privacidad y límites
- No se transmiten productos o fotografías al servidor del constructor.
- El mensaje solo se entrega a WhatsApp cuando la persona pulsa el botón de envío del formulario.
- No procesa pagos, pedidos, inventario, facturación fiscal ni agenda.
- No garantiza ventas, tráfico, posicionamiento, leads ni SLA.
- No usar información privada ni publicar datos, imágenes, marcas o testimonios sin autorización expresa.

## Publicación
El constructor y sus ejemplos siguen en desarrollo local. No hacer push ni desplegar el sitio comercial sin autorización expresa.
