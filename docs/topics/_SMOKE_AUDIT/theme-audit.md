# Auditoría de tema — _SMOKE_AUDIT

> SMOKE TEST 2026-09-06 — validación init-theme-audit.

## CONTEXTO
- dominio: retail / ferretería
- pais_region: LATAM (referente MX; curso Perú)
- fase_entregable: mvp
- restricciones: 1 semestre
- modo: una_alternativa
- tipo_sujeto: empresa
- empresa: Pulpos (referente público)

## Tema propuesto (entrada)
**Tema:** PoC de alertas de stock mínimo para ferretería pequeña
**Descripción:** MVP académico de catálogo + umbrales + alertas
**Problema identificado:** Quiebres por inventario a ojo
**Alcance:** 50–100 SKUs, sin POS

## Ficha de empresa (investigación)
**Identidad:** Pulpos — software de gestión/POS para comercios incl. ferreterías (México), sitio pulpos.com
**Reseña histórica (pública):** Plataforma cloud de gestión para PyME; línea ferreterías con inventario multi-SKU (fuentes de marketing público)
**Misión / visión / valores:** No publicada de forma clara en la página ferreterías; no inventar
**Oferta / sector relevante:** POS, inventario miles de SKUs, alertas de reposición, multi-sucursal
**Evidencia_empresa:** suficiente (sitio oficial de producto)
**Fuentes de empresa:** https://pulpos.com/ferreterias/

## Brainstorm
Acta: theme-audit-brainstorm.md — ángulos retenidos: alertas puras; alertas + lista de compra semanal

## Benchmarking (`benchmark-theme`)
**Casos (directo|proxy):** Pulpos (directo); Bodezy (directo); Nemi (directo LATAM hardware)
**Mini-matriz:**
| Capacidad | Pulpos | Bodezy | Nemi | Relevancia |
|-----------|--------|--------|------|------------|
| Inventario multi-SKU | presente | presente | presente | alta |
| Alertas reposición | presente | presente | parcial/desconocido | alta |
| Offline-first | desconocido | desconocido | presente | media |
| POS/cobro | presente | presente | presente | baja (fuera MVP) |
**Qué adaptar:** Umbral mínimo + lista reposición
**Diferenciador posible:** Solo alertas sin POS/CFDI para curso
**Evidencia:** suficiente — búsquedas usadas: 3/5

## Tema afinado (pre-polish)
**Tema:** Alertas de stock mínimo para ferretería pequeña (PoC)
**Descripción:** Catálogo acotado, umbrales y lista de reposición semanal
**Problema identificado:** Quiebres por falta de visibilidad de mínimos
**Alcance:** 1 tienda simulada, 50–100 SKUs, sin POS ni multi-sucursal

## Fuentes
- https://pulpos.com/ferreterias/
- https://bodezy.com/punto-de-venta-para-ferreterias/
- https://nemi.tech/
