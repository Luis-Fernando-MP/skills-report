# Auditoría de tema — ROMANTEX

## CONTEXTO
- dominio: retail textil / decoración
- pais_region: Perú (Lima)
- fase_entregable: mvp
- restricciones: curso 1 semestre
- modo: una_alternativa
- tipo_sujeto: empresa
- empresa: Romantex S.A.C. (RUC 20293975036)

## Tema propuesto (entrada original del usuario)
**Tema:** Digitalización del inventario y estandarización de tallaje en Calzados Romantex S.A.C.  
**Corrección:** Romantex no es calzado; es especialista en telas y revestimientos. Tema afinado abajo.

## Ficha de empresa (investigación)

**Identidad:** Romantex S.A.C. — RUC 20293975036; sociedad anónima cerrada; Lima, Perú; domicilio público Av. Paz Soldán 185, San Isidro (también showroom Av. El Polo 376, Surco). Sector: venta al por menor de tapices, alfombras y cubrimientos para paredes/pisos; importador.  
**Reseña histórica (pública):** Inicio de actividades registrado el 01/10/1995 (SUNAT vía directorios); sitio corporativo indica creación/apertura de showroom en **1996** como especialista en telas para decoración, revestimientos y accesorios importados (residencial y contract).  
**Misión / visión / valores:** No hay bloque formal “misión/visión/valores” en la página Empresa; narrativa de calidad, moda, servicio integral con diseñadores y mejora continua.  
**Oferta / sector relevante:** Telas (cortinas, tapicería, exteriores, cubrecamas), revestimientos, pasamanería; stock en showroom; pedidos por catálogo de firmas internacionales; línea Contract (hoteles, restaurantes, áreas públicas) con fichas técnicas y normas (p. ej. Oeko-Tex 100 mencionadas en contract). Almacén con miles de metros para entrega inmediata.  
**Evidencia_empresa:** suficiente  
**Fuentes de empresa:**
- https://www.romantex.com.pe/empresa
- https://www.romantex.com.pe/linea-residencial-1
- https://www.romantex.com.pe/contract
- https://www.universidadperu.com/empresas/romantex.php (RUC / datos públicos)

## Brainstorm
Acta: theme-audit-brainstorm.md — ángulo retenido: inventario de metraje + fichas técnicas mínimas; variante CSV reposición.

## Benchmarking (`benchmark-theme`)

**Casos (directo|proxy):**
1. **PolyPM** — ERP/PLM textil con inventario a nivel rollo (ancho, shade, yardaje) — https://polypm.com/erp-inventory-software-for-textile-manufacturing/ — (proxy fabricante; no retail showroom)
   - fortaleza: trazabilidad roll-level
   - hueco: sobredimensionado para PyME showroom / curso
2. **Datatex NOW Inventory** — lotes, rollos, multi-unidad (m/kg) — https://datatex.com/portfolio-items/inventory/ — (proxy)
   - fortaleza: multi-UoM textil
   - hueco: suite enterprise

**Mini-matriz:**
| Eje | PolyPM | Datatex | Relevancia PoC |
|-----|--------|---------|----------------|
| Stock por rollo/metraje | presente | presente | alta |
| Variantes color/lote | presente | presente | alta |
| Ficha técnica / QC | presente | parcial | media |
| Escala enterprise | presente | presente | baja (evitar) |

**Qué adaptar:** unidades en metros + atributos color/ancho; ficha mínima; alertas de mínimo.  
**Diferenciador posible:** PoC showroom/almacén Lima, catálogo acotado, sin ERP textil completo.  
**Evidencia:** suficiente — búsquedas usadas: 3/5

## Tema afinado (pre-polish)

**Tema:** Digitalización del inventario y estandarización de fichas técnicas de producto (metraje, color, lote) en Romantex S.A.C.  
**Descripción:** PoC académico para visibilidad de stock en metros y fichas técnicas mínimas alineadas al catálogo showroom/almacén, sin reemplazar un ERP textil.  
**Problema identificado:** La promesa de stock amplio y entrega inmediata exige coherencia entre variantes (color, ancho, metraje) y fichas; la gestión no digital o fragmentada eleva riesgo de quiebre/sobrepromesa.  
**Alcance:** MVP 1 — catálogo 50–150 SKUs; stock en metros; ficha (código, descripción, color, ancho, metros, ubicación); altas/bajas; alertas de mínimo; export CSV. Fuera: EDI proveedores, RFID, e-commerce, contract BIM, calzado.

## Fuentes
- https://www.romantex.com.pe/empresa
- https://polypm.com/erp-inventory-software-for-textile-manufacturing/
- https://datatex.com/portfolio-items/inventory/
