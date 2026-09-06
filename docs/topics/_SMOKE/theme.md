# Temas propuestos — _SMOKE

> SMOKE TEST 2026-09-06 — validación init-theme (post brainstorm + benchmark).

## CONTEXTO
- dominio: logística / retail
- pais_region: Perú (Lima)
- fase_entregable: mvp
- restricciones: curso 1 semestre, equipo pequeño
- modo: N_alternativas

## Entrada
- Tópicos del usuario: rutas delivery bodegas; dashboard stock ferreterías; chatbot WhatsApp restaurantes
- Carpeta: _SMOKE
- Acta brainstorm: theme-brainstorm.md

## Alternativa 1
**Tema:** Rutas diarias acotadas para bodega de barrio (Lima)
**Descripción:** Planificación simple de entregas del día sin flota GPS ni app conductor.
**Problema identificado:** Rutas improvisadas elevan costo de combustible y retrasos.
**Alcance:** 1 bodega, pedidos del día, 2–3 rutas manuales + enlace a mapas.
**Tipo de sujeto:** dominio_sin_empresa
**Ficha de empresa (si aplica):** N/A — dominio sin org. ancla
**Benchmarking (`benchmark-theme`):** EasyRoutes / Routific (proxy e-commerce last-mile) — directo parcial; Routella (proxy WhatsApp tracking). Adaptar: lista de paradas del día sin Shopify. Diferenciador: UX para bodega no-Shopify en Lima. Evidencia: suficiente (proxies).
**Diferenciador propuesto:** Flujo manual→digital para bodega sin plataforma de delivery.

## Alternativa 2
**Tema:** Alertas de stock mínimo para ferretería pequeña
**Descripción:** Registro y alertas de quiebre en catálogo acotado.
**Problema identificado:** Inventario a ojo genera quiebres y compras de emergencia.
**Alcance:** 1 tienda, ~50–100 SKUs, altas/bajas, alertas de mínimo.
**Tipo de sujeto:** dominio_sin_empresa
**Ficha de empresa (si aplica):** N/A
**Benchmarking (`benchmark-theme`):** Pulpos, Bodezy, Nemi (directo ferretería LATAM, México). Adaptar: subset sin POS/CFDI. Diferenciador: solo alertas + catálogo mínimo para curso. Evidencia: suficiente.
**Diferenciador propuesto:** MVP solo inventario/alertas, no POS completo.

## Alternativa 3
**Tema:** Pedidos estructurados por WhatsApp para restaurante pequeño
**Descripción:** Menú fijo + confirmación humana sin NLP.
**Problema identificado:** Pedidos por chat libre generan errores en hora pico.
**Alcance:** Menú fijo, plantillas, confirmación; sin API Meta obligatoria en v1 (puede ser mock/flujo web→WhatsApp).
**Tipo de sujeto:** dominio_sin_empresa
**Ficha de empresa (si aplica):** N/A
**Benchmarking (`benchmark-theme`):** WATI / OrderViaChat / flujos API (proxy). Adaptar: evitar costo API en MVP de curso. Diferenciador: pedido estructurado offline-first o deep-link. Evidencia: suficiente (proxies).
**Diferenciador propuesto:** Estructura de pedido sin depender de BSP de pago.

## Fuentes del benchmarking
- https://pulpos.com/ferreterias/
- https://nemi.tech/
- https://bodezy.com/punto-de-venta-para-ferreterias/
- https://apps.shopify.com/easyroutes
- https://orderviachat.com/blog/whatsapp-business-vs-api-restaurant-guide
