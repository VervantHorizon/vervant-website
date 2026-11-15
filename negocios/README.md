# Vervant Local — Constructor interno

## Estado
Prototipo local, no publicado, no comercialmente validado. El objetivo es probar una oferta de catálogo/portafolio de cotizaciones para pequeños fabricantes y talleres. No contactar empresas ni publicar catálogos sin autorización expresa.

## Archivos
- `index.html`: página privada de explicación de la oferta.
- `constructor/index.html`: constructor en el navegador.
- El constructor genera un único archivo HTML autocontenido por negocio.

## Cómo probar
Desde la raíz del repositorio estático:
```bash
python3 -m http.server 8081
```
Abrir:
- `http://127.0.0.1:8081/negocios/`
- `http://127.0.0.1:8081/negocios/constructor/`

En el constructor:
1. Pulsa “Cargar ejemplo”.
2. Escribe un número de prueba propio, con código de país y solo dígitos.
3. Revisa el catálogo en la vista previa.
4. Descarga el HTML y ábrelo localmente para comprobarlo.
5. No uses datos ni fotografías de clientes reales en esta fase.

## Qué hace y qué no hace
- Funciona sin backend, cuenta, base de datos o librería externa.
- Procesa las fotos en el navegador y las optimiza a JPEG antes de incrustarlas.
- No sube ni guarda los datos en ningún sitio.
- Genera enlaces directos `wa.me` con mensaje prellenado para cada producto.
- No genera todavía QR. No anunciar esa característica hasta implementarla y probarla.
- No procesa pagos, órdenes, inventario, facturas fiscales o información privada.
- Requiere que el negocio autorice las fotografías, textos y el número comercial antes de publicar.

## Publicación
El repositorio está conectado a Render con despliegue automático en `main`. **No hacer push ni desplegar este prototipo sin autorización expresa.** La web pública actual está dirigida a desarrolladores del producto PDF API; no debe mezclarse la navegación de ambas ofertas sin decisión de marca.
