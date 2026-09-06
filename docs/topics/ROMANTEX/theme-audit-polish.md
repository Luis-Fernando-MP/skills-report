# Tema auditado (polish) — ROMANTEX

## Veredicto
**GO_con_cambios**

## Corrección sectorial (importante)
El planteamiento “Calzados Romantex + tallaje” era **incorrecto**: Romantex S.A.C. (RUC 20293975036) es especialista en **telas y revestimientos para decoración** (Lima), no calzado. El tema se reformuló a inventario de **metraje/rollos** y **fichas técnicas de producto**.

## Tema final
Digitalización del inventario (rollos/metraje residual) y estandarización de fichas técnicas mínimas de producto en Romantex S.A.C. — showroom/almacén Lima, línea de stock acotada (cortinas o tapicería).

## Descripción
PoC académico de un semestre: visibilidad de metros disponibles por variante (color, ancho, lote/rollo), ficha técnica mínima consultable y alertas de mínimo, sin implementar un ERP textil. El aporte se evalúa frente a gestión fragmentada (Excel/cuaderno), no como sustituto de Cuenti/Kaypi/Datatex.

## Problema identificado
**Hipótesis (pendiente_campo):** la promesa comercial de stock amplio y entrega inmediata puede degradarse si el metraje residual por rollo/variante no es consultable de forma única. No se afirma auditoría AS-IS interna. Romantex ya entrega fichas técnicas en contract (fuentes públicas); el PoC estandariza una **ficha operativa mínima interna** (código, color, ancho, metros residuales, ubicación), distinta del PDF de proveedor.

## Alcance
- **Incluye:** 1 sede (San Isidro o Surco); 1 familia de producto stock; 50–100 SKUs / rollos seed; modelo rollo→metros residuales; ficha mínima; altas/bajas; alertas; CSV.
- **Excluye:** calzado/tallaje; EDI; RFID; e-commerce; multi-almacén completo; PLM/ERP textil; BIM contract; normas Oeko-Tex como módulo completo.

## Tipo de sujeto
empresa

## Ficha de empresa (para init-project → company.md)
- **Identidad:** Romantex S.A.C., RUC 20293975036, San Isidro / Surco, Lima; retail telas y revestimientos; importador.
- **Historia:** actividades desde ~1995/1996; showroom y almacén con stock amplio; líneas residencial y contract.
- **Misión/visión/valores:** no publicados formalmente; narrativa de calidad, moda y servicio con diseñadores.
- **Oferta:** cortinas, tapicería, revestimientos, pasamanería; catálogo internacional; contract con fichas técnicas.
- **Fuentes:** romantex.com.pe/empresa; universidadperu.com (RUC).

## Tesis de valor (inversor)
Ahorro y riesgo evitado por menos sobrepromesa de metraje; no ROI SaaS en fase curso. Soft-veto: no vender “disrupción textil” sin baseline.

## MVP de arranque
**MVP 1:** catálogo seed + rollo/metros residuales + ficha mínima (5–7 campos) + alertas + CSV.  
**Criterio de éxito:** consulta de metros coherente; alerta ante umbral; ficha por código.  
**MVP 2 (después):** bitácora de ajustes / contraste conteo físico en muestra.

## Marco PICOCT (borrador)
- P: Personal showroom/almacén Romantex (Lima)
- I: Inventario digital rollo/metraje + ficha mínima
- C: Gestión fragmentada (Excel/cuaderno/hipótesis)
- O: Exactitud de disponibilidad y menos sobrepromesa
- C/T: Retail textil decoración Perú; curso 1 semestre

## Siguiente
`init-project` → `init-project-mvp` → `make-report` (alcance cap. 1)
