# Brainstorm de auditoría — ROMANTEX

## CONTEXTO
- dominio: retail textil / decoración de interiores
- pais_region: Perú (Lima)
- fase_entregable: mvp
- restricciones: curso 1 semestre, PoC académico
- modo: una_alternativa
- tipo_sujeto: empresa
- empresa: Romantex S.A.C.

## Corrección de tema (obligatoria)
El usuario propuso “Calzados Romantex” + tallaje. **Romantex S.A.C. existe** (RUC 20293975036) pero opera en **telas y revestimientos para decoración**, no calzado. Se reformula el problema a **inventario de rollos/metraje + estandarización de fichas técnicas** (equivalente funcional a “tallaje” en calzado).

## Tema de entrada (corregido)
Digitalización del inventario y estandarización de fichas técnicas de producto (metraje, color, lote/variante) en Romantex S.A.C.

## Acta (brainstorm-theme)

### Modo
una_alternativa

### Lente problema/usuario
- Dolor: stock de miles de metros de telas/revestimientos; variantes por color, ancho, catálogo vs showroom; riesgo de promesa de entrega inmediata sin visibilidad fina del rollo/metraje.
- Quién: personal de almacén/showroom y diseñadores que atienden residencial/contract.
- Por qué importa: Romantex destaca almacén con miles de metros para entrega rápida; sin ficha/stock digital coherente, esa promesa se degrada.

### Lente viabilidad de curso
- Ángulo viable: catálogo acotado de SKUs (familia cortinas/tapicería), stock en metros, ficha técnica mínima (código, color, ancho, metros disponibles, ubicación), alertas de mínimo.
- No perseguir: ERP textil completo, PLM, RFID multi-almacén, e-commerce.

### Lente oportunidad/ángulo
- Giro: capa delgada de inventario + fichas para showroom/almacén Lima, no clonar PolyPM/Datatex.
- No perseguir: fabricación textil, tintorería, contract BIM.

### Síntesis — Ángulos
#### 1
- Tema: Inventario digital de metraje + fichas técnicas mínimas (Romantex)
- Problema: Visibilidad incompleta de rollos/variantes vs promesa de entrega inmediata
- Alcance: 1 almacén/showroom simulado; 50–150 SKUs; metros + ficha (color, ancho, lote); alertas de mínimo
- tipo_sujeto: empresa — Romantex S.A.C.

#### 2
- Variante: + lista de reposición / pedido a catálogo importado (sin EDI)
- Alcance: mismo núcleo + export CSV de faltantes

### Descartados / no perseguir
- Calzado/tallaje (sector incorrecto para esta RUC).
- ERP textil enterprise (PolyPM/Datatex) completo.

### Notas
Corrección sectorial documentada; empresa real con web y RUC.
