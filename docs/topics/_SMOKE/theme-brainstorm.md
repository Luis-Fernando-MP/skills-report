# Brainstorm de temas — _SMOKE

> SMOKE TEST 2026-09-06 — validación de flujo init-theme. Borrar carpeta cuando no haga falta.

## CONTEXTO
- dominio: logística / retail
- pais_region: Perú (Lima)
- fase_entregable: mvp
- restricciones: curso 1 semestre, equipo pequeño
- modo: N_alternativas

## Entrada (tópicos)
1. App de rutas de delivery para bodegas en Lima
2. Dashboard de stock para ferreterías pequeñas
3. Chatbot de pedidos WhatsApp para restaurantes

## Acta (brainstorm-theme)

### Modo
N_alternativas

### Lente problema/usuario
1. Rutas delivery bodegas — rutas improvisadas, costo combustible, reclamos; sufren dueño/repartidor y cliente de barrio.
2. Dashboard stock ferreterías — quiebres y sobrestock; sufren dueño y cliente que no encuentra el ítem.
3. Chatbot WhatsApp restaurantes — mensajes repetidos y errores en hora pico; sufren encargado y cliente.

### Lente viabilidad de curso
1. Rutas — parcial: MVP = 1 bodega, asignación manual + mapas; riesgo routing/app móvil.
2. Stock — sí, más manejable: 50–100 SKUs, alertas de mínimo.
3. Chatbot — parcial: menú fijo + confirmación humana; riesgo API Meta.

### Lente oportunidad/ángulo
1. Nicho 1–2 distritos, no competir con Rappi.
2. Alertas de reorden, no ERP multi-sucursal.
3. Catálogo fijo + recojo, no NLP ni pasarela pagos.

### Síntesis
#### Candidata 1
- Tema: Rutas diarias acotadas para bodega de barrio (Lima)
- Descripción: Planificación simple de entregas del día sin flota GPS
- Problema: Rutas improvisadas elevan costo y retrasos
- Alcance: 1 bodega, lista de pedidos, 2–3 rutas manuales + enlace mapas
- tipo_sujeto tentativo: dominio_sin_empresa
- empresa nombrada: ninguna

#### Candidata 2
- Tema: Alertas de stock mínimo para ferretería pequeña
- Descripción: Registro y alertas de quiebre en catálogo acotado
- Problema: Inventario a ojo genera quiebres y compras de emergencia
- Alcance: 1 tienda, ~50–100 SKUs, altas/bajas, alertas
- tipo_sujeto tentativo: dominio_sin_empresa
- empresa nombrada: ninguna

#### Candidata 3
- Tema: Pedidos estructurados por WhatsApp para restaurante pequeño
- Descripción: Flujo de menú fijo y confirmación sin NLP
- Problema: Pedidos por chat libre generan errores y demora
- Alcance: Menú fijo, plantillas, confirmación humana
- tipo_sujeto tentativo: dominio_sin_empresa
- empresa nombrada: ninguna

### Descartados / no perseguir
- Optimizador de tráfico metropolitano; ERP ferretero completo; chatbot conversacional avanzado + pagos.

### Notas
Smoke: 3 lentes en paralelo OK. Sin empresas inventadas.
