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
Nota histórica supersedida el 15-11-2026: el constructor y los ejemplos español/inglés ya están publicados en Render. El repositorio vervant-website despliega automáticamente los commits de main. Mantener ejemplos ficticios claramente identificados y no publicar material de clientes sin autorización.


## International English offer
- English landing: negocios/en/index.html; English catalog builder: negocios/en/builder/index.html.
- Remote-first service for customers worldwide. English delivery; quotes in USD unless otherwise agreed.
- First 3 international pilots: USD 199 one-time; expected standard price USD 299.
- Capability sheet: USD 99 standalone / USD 59 with catalog. Additional language adaptation from USD 149.
- English catalogs support business WhatsApp and/or email enquiry channels, depending on the contact methods the customer provides.
- The exported file contains a guided quote form for measurements/specifications, material/finish, quantity, location, target date and additional details. The visitor chooses WhatsApp or email where both are configured.
- Do not send international cold email into jurisdictions where consent is required unless the contact has a documented lawful basis. Observe opt-outs and retain source/date/role evidence.


## International English pages
- International overview: en/index.html
- Industry directory: en/industries/index.html
- Sector pages:
  - en/industries/furniture-makers/
  - en/industries/metal-fabrication-cnc/
  - en/industries/signage-print/
  - en/industries/packaging-print/
  - en/industries/commercial-interiors/
- English catalog builder: en/builder/index.html
- English capability sheet PDF builder: en/capability-sheet/index.html

## International quote intake
- The English catalog builder supports business WhatsApp, business enquiry email, or both.
- At least one valid channel is required before export.
- Guided enquiry fields include measurements/specifications, measurement unit (mm, cm, m, inches, feet), material/finish, quantity, location, target date and additional details.
- If only email is configured, the catalog opens a pre-addressed email with the enquiry details. If only WhatsApp is configured, it opens WhatsApp with the details. If both are configured, visitors can choose the channel.
- The form itself does not submit to a Vervant server or store entries.
- Do not use placeholder customer details in a real delivery. Only approved names, photos, descriptions, contact details and intellectual property may be published.

## International offer and geographic scope
- First 3 international pilots: USD 199 one-time; expected standard price USD 299.
- Capability sheet: USD 99 standalone / USD 59 with a catalog.
- Additional language adaptation starts at USD 149, after review.
- Service is remote-first. English delivery; USD pricing unless otherwise agreed in writing.
- Superseded 15 Nov 2026: the English landing, builder and sector pages are published at https://vervant-public-site.onrender.com/negocios/en/; the Render static site auto-deploys commits to main.
- Use country-specific outbound compliance rules. Current outbound pilot is limited to verified UK corporate subscribers at role-based company email addresses. See /home/will/Documentos/Vervant-Operations/international-go-to-market.md.

## Spanish sector pages
- /negocios/industrias/: directory.
- /negocios/industrias/carpinterias/: custom furniture and joinery.
- /negocios/industrias/fabricacion-metalica/: metal fabrication and CNC.
- /negocios/industrias/rotulacion-impresion/: signage and print.
The Spanish pages use the El Salvador pilot price. English sector pages retain the international price and currency.
