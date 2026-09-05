# Auditoría de tema — ITD

## CONTEXTO
- dominio: transformación digital / inventario y catálogo con tallaje en manufactura de calzado (PYME)
- pais_region: Perú (Trujillo / norte del país); mercados locales y tiendas de provincias
- fase_entregable: diagnostico
- restricciones: proyecto académico acotado; MVP sin ERP/POS/contabilidad/e-commerce completos; no inventar hechos de empresa
- modo: una_alternativa
- empresa: Calzados Romantex S.A.C. (familiar; calzado de cuero; sede Trujillo; +20 años; talleres propios y tercerizados en El Porvenir — según perfil del proyecto)

## Tema propuesto (entrada)
**Tema:** Digitalización del inventario y estandarización de tallaje en Calzados Romantex S.A.C.

**Descripción:** Romantex enfrenta el desafío de integrar y optimizar digitalmente la gestión de productos, inventario, ventas y atención al cliente, por la amplitud del catálogo y la diversidad de clientes. Aunque cuenta con presencia digital y tienda virtual, hay oportunidad de fortalecer la integración entre inventario físico, información de productos, ventas y atención comercial. La variedad de atributos de producto (en el tema: tallaje y variantes de calzado) exige información actualizada y centralizada para evitar inconsistencias, mejorar disponibilidad y facilitar la decisión de compra.

**Problema identificado:** Dificultad para conocer el stock en tiempo real, responder con rapidez a consultas, gestionar pedidos con eficiencia y aprovechar datos de ventas para identificar tendencias. El reto de transformación digital es integrar canales y sistemas de información para una gestión basada en datos, mejorar la experiencia del cliente, optimizar el control de inventarios y fortalecer la toma de decisiones comerciales.

**Alcance:** MVP acotado — sistema de inventario digital con fichas técnicas de tallaje estandarizadas. Contabilidad y e-commerce como fases futuras.

## Benchmarking
**Casos (directo|proxy):**
1. **INVY (Perú)** — POS + inventario en la nube para tiendas de calzado: stock por talla/color/modelo, alertas, rotación por talla, multi-sucursal — https://www.invyperu.com/tienda-de-calzado-punto-de-venta — (**directo**)
2. **iSiore GO (Perú)** — ERP para fábricas de calzado: modelos/tallas/colores, OP, BOM, inventarios multipunto, kárdex — https://www.isiorego.com/blog/erp/erp-para-fabricas-de-calzado-en-peru/ — (**directo**)
3. **Uphance (internacional)** — inventario/wholesale footwear con matriz de tallas y disponibilidad por variante — https://www.uphance.com/footwear-inventory-system/ — (**directo** en dominio; **proxy** geográfico/escala)
4. **ISO 19407:2023** — tablas de conversión entre sistemas de tallaje (Mondopoint, EUR, UK, US) — https://standards.iteh.ai/catalog/standards/iso/ac8767eb-dc46-4cec-bd13-a041c0268a09/iso-19407-2023 — (**proxy** normativo)

**Qué adaptar:** matriz modelo × color × talla con stock independiente; consulta casi en tiempo real para atención comercial; multipunto mínimo (taller propio / tercerizado / almacén); importación masiva de catálogo; equivalencias de tallaje solo como marco en fichas (ISO 19407), no como implementación completa.

**Diferenciador posible:**
1. Ficha técnica de tallaje como maestro del catálogo (medidas, horma/última, equivalencias, notas de ajuste) ligada al SKU variante.
2. Inventario “fábrica ligera” sin ERP: PT por variante + ubicación, sin BOM ni facturación en el MVP.
3. Protocolo de gobierno de datos (quién corrige tallaje/stock) documentado para el informe de TD.

**Evidencia:** suficiente (4/5 búsquedas)

## Tema afinado (pre-polish)
*(Ajustes mínimos tras benchmark; sin inventar hechos de empresa. Se alinea el alcance al hueco vs POS/ERP comerciales y se precisa el objeto “calzado/tallaje”; el texto de entrada que aludía a atributos tipo tela se interpreta en el marco del tema de calzado declarado.)*

**Tema:** Digitalización del inventario por variante y estandarización de fichas técnicas de tallaje en Calzados Romantex S.A.C.

**Descripción:** Propuesta de transformación digital acotada para una PYME de calzado en Trujillo: centralizar información de producto terminado e inventario físico con una matriz modelo × color × talla, y vincular cada variante a fichas técnicas de tallaje estandarizadas, de modo que ventas y atención comercial consulten stock e información consistente sin depender de un ERP o POS completo.

**Problema identificado:** Desalineación entre inventario físico, datos de producto/tallaje y atención comercial: stock poco confiable en tiempo real por variante, respuestas lentas a consultas de disponibilidad/ajuste, y limitaciones para usar datos de ventas en decisiones — en un contexto de catálogo amplio y canales digitales aún poco integrados al inventario.

**Alcance:** Diagnóstico + diseño de MVP: inventario digital de producto terminado por variante y ubicación (taller propio / tercerizado / almacén comercial) + fichas técnicas de tallaje estandarizadas (equivalencias y criterios de ajuste). Fuera de alcance en esta fase: contabilidad, facturación SUNAT, BOM/MRP, e-commerce y POS completo.

## Fuentes
- INVY — https://www.invyperu.com/tienda-de-calzado-punto-de-venta
- iSiore GO — https://www.isiorego.com/blog/erp/erp-para-fabricas-de-calzado-en-peru/
- Uphance — https://www.uphance.com/footwear-inventory-system/
- ISO 19407:2023 — https://standards.iteh.ai/catalog/standards/iso/ac8767eb-dc46-4cec-bd13-a041c0268a09/iso-19407-2023
- Perfil del proyecto: `docs/content/ITD/profile.md`
