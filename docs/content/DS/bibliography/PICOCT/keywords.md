# Keywords PICOCT - DS

## Tabla de Keywords

| Componente | Keywords (EN) | Keywords (ES) |
|---|---|---|
| P | "spare parts", "service parts", "spare parts inventory", stockout, shortage, backorder, "peak demand", "spare parts order management", "inventory order management" | repuestos, "inventario de repuestos", desabastecimiento, "faltante de stock", "pico de demanda", "gestión de pedidos de repuestos", "administración de pedidos de inventario" |
| I | microservice*, "cloud-native architecture", containerization, "inventory allocation", "order fulfillment", "inventory reservation systems", "stock allocation policies", "overselling prevention", "consistent inventory updates" | microservicios, "arquitectura nativa en la nube", contenedorización, "asignación de inventario", "cumplimiento de pedidos", "sistemas de reserva de inventario", "políticas de asignación de stock", "prevención de sobreventa", "actualizaciones consistentes de inventario" |
| C | WMS, "warehouse management system", "legacy information system", "spreadsheet-based inventory management", "traditional inventory management", "decentralized inventory systems" | WMS, "sistema de gestión de almacenes", "sistema de información legado", "gestión de inventario basada en hojas de cálculo", "gestión de inventario tradicional", "sistemas de inventario descentralizados" |
| O | "inventory accuracy", "fill rate", "service level", "scalability of inventory systems", "microservices scalability", "cloud scalability", "response time", latency, overselling | "exactitud de inventario", "nivel de servicio", "escalabilidad de sistemas de inventario", "escalabilidad de microservicios", "escalabilidad en la nube", "tiempo de respuesta", latencia, sobreventa |
| Context | aftermarket, "after-sales", "spare parts aftermarket", "heavy equipment", "capital goods", manufacturing, OEM | posventa, "servicio postventa", "repuestos industriales", "equipo pesado", "bienes de capital", manufactura, OEM |

## Ecuaciones de búsqueda

### Scopus (English)

**Marco PICOCT (máxima precisión, menor recall)**
```text
TITLE-ABS-KEY ( "spare parts" OR "service parts" OR "spare parts inventory" OR stockout OR shortage OR backorder OR "peak demand" OR "spare parts order management" OR "inventory order management" ) AND TITLE-ABS-KEY ( microservice* OR "cloud-native architecture" OR containerization OR "inventory allocation" OR "order fulfillment" OR "inventory reservation systems" OR "stock allocation policies" OR "overselling prevention" OR "consistent inventory updates" ) AND TITLE-ABS-KEY ( WMS OR "warehouse management system" OR "legacy information system" OR "spreadsheet-based inventory management" OR "traditional inventory management" OR "decentralized inventory systems" ) AND TITLE-ABS-KEY ( "inventory accuracy" OR "fill rate" OR "service level" OR "scalability of inventory systems" OR "microservices scalability" OR "cloud scalability" OR "response time" OR latency OR overselling ) AND TITLE-ABS-KEY ( aftermarket OR "after-sales" OR "spare parts aftermarket" OR "heavy equipment" OR "capital goods" OR manufacturing OR OEM ) AND PUBYEAR > 2021 AND PUBYEAR < 2027 AND ( LIMIT-TO ( DOCTYPE , "ar" ) ) AND ( LIMIT-TO ( LANGUAGE , "English" ) )
```

**Marco PICOC (recall medio)**
```text
TITLE-ABS-KEY ( "spare parts" OR "service parts" OR "spare parts inventory" OR stockout OR shortage OR backorder OR "peak demand" OR "spare parts order management" OR "inventory order management" ) AND TITLE-ABS-KEY ( microservice* OR "cloud-native architecture" OR containerization OR "inventory allocation" OR "order fulfillment" OR "inventory reservation systems" OR "stock allocation policies" OR "overselling prevention" OR "consistent inventory updates" ) AND TITLE-ABS-KEY ( WMS OR "warehouse management system" OR "legacy information system" OR "spreadsheet-based inventory management" OR "traditional inventory management" OR "decentralized inventory systems" ) AND TITLE-ABS-KEY ( "inventory accuracy" OR "fill rate" OR "service level" OR "scalability of inventory systems" OR "microservices scalability" OR "cloud scalability" OR "response time" OR latency OR overselling ) AND TITLE-ABS-KEY ( aftermarket OR "after-sales" OR "spare parts aftermarket" OR "heavy equipment" OR "capital goods" OR manufacturing OR OEM ) AND PUBYEAR > 2021 AND PUBYEAR < 2027 AND ( LIMIT-TO ( DOCTYPE , "ar" ) ) AND ( LIMIT-TO ( LANGUAGE , "English" ) )
```
*Nota: La ecuación PICOC es idéntica a la PICOCT en este caso porque el componente 'Context' sigue siendo parte del marco PICOC y no se ha eliminado en esta relajación. Se consideraría una relajación si se eliminara Context o C (Comparison).*

**Marco PICO (mayor recall, menor precisión)**
```text
TITLE-ABS-KEY ( "spare parts" OR "service parts" OR "spare parts inventory" OR stockout OR shortage OR backorder OR "peak demand" OR "spare parts order management" OR "inventory order management" ) AND TITLE-ABS-KEY ( microservice* OR "cloud-native architecture" OR containerization OR "inventory allocation" OR "order fulfillment" OR "inventory reservation systems" OR "stock allocation policies" OR "overselling prevention" OR "consistent inventory updates" ) AND TITLE-ABS-KEY ( "inventory accuracy" OR "fill rate" OR "service level" OR "scalability of inventory systems" OR "microservices scalability" OR "cloud scalability" OR "response time" OR latency OR overselling ) AND PUBYEAR > 2021 AND PUBYEAR < 2027 AND ( LIMIT-TO ( DOCTYPE , "ar" ) ) AND ( LIMIT-TO ( LANGUAGE , "English" ) )
```

### Scopus (Español)

**Marco PICOCT (máxima precisión, menor recall)**
```text
TITLE-ABS-KEY ( repuestos OR "inventario de repuestos" OR desabastecimiento OR "faltante de stock" OR "pico de demanda" OR "gestión de pedidos de repuestos" OR "administración de pedidos de inventario" ) AND TITLE-ABS-KEY ( microservicios OR "arquitectura nativa en la nube" OR contenedorización OR "asignación de inventario" OR "cumplimiento de pedidos" OR "sistemas de reserva de inventario" OR "políticas de asignación de stock" OR "prevención de sobreventa" OR "actualizaciones consistentes de inventario" ) AND TITLE-ABS-KEY ( WMS OR "sistema de gestión de almacenes" OR "sistema de información legado" OR "gestión de inventario basada en hojas de cálculo" OR "gestión de inventario tradicional" OR "sistemas de inventario descentralizados" ) AND TITLE-ABS-KEY ( "exactitud de inventario" OR "nivel de servicio" OR "escalabilidad de sistemas de inventario" OR "escalabilidad de microservicios" OR "escalabilidad en la nube" OR "tiempo de respuesta" OR latencia OR sobreventa ) AND TITLE-ABS-KEY ( posventa OR "servicio postventa" OR "repuestos industriales" OR "equipo pesado" OR "bienes de capital" OR manufactura OR OEM ) AND PUBYEAR > 2021 AND PUBYEAR < 2027 AND ( LIMIT-TO ( DOCTYPE , "ar" ) ) AND ( LIMIT-TO ( LANGUAGE , "Spanish" ) )
```

**Marco PICOC (recall medio)**
```text
TITLE-ABS-KEY ( repuestos OR "inventario de repuestos" OR desabastecimiento OR "faltante de stock" OR "pico de demanda" OR "gestión de pedidos de repuestos" OR "administración de pedidos de inventario" ) AND TITLE-ABS-KEY ( microservicios OR "arquitectura nativa en la nube" OR contenedorización OR "asignación de inventario" OR "cumplimiento de pedidos" OR "sistemas de reserva de inventario" OR "políticas de asignación de stock" OR "prevención de sobreventa" OR "actualizaciones consistentes de inventario" ) AND TITLE-ABS-KEY ( WMS OR "sistema de gestión de almacenes" OR "sistema de información legado" OR "gestión de inventario basada en hojas de cálculo" OR "gestión de inventario tradicional" OR "sistemas de inventario descentralizados" ) AND TITLE-ABS-KEY ( "exactitud de inventario" OR "nivel de servicio" OR "escalabilidad de sistemas de inventario" OR "escalabilidad de microservicios" OR "escalabilidad en la nube" OR "tiempo de respuesta" OR latencia OR sobreventa ) AND TITLE-ABS-KEY ( posventa OR "servicio postventa" OR "repuestos industriales" OR "equipo pesado" OR "bienes de capital" OR manufactura OR OEM ) AND PUBYEAR > 2021 AND PUBYEAR < 2027 AND ( LIMIT-TO ( DOCTYPE , "ar" ) ) AND ( LIMIT-TO ( LANGUAGE , "Spanish" ) )
```
*Nota: La ecuación PICOC es idéntica a la PICOCT en este caso porque el componente 'Context' sigue siendo parte del marco PICOC y no se ha eliminado en esta relajación. Se consideraría una relajación si se eliminara Context o C (Comparison).*

**Marco PICO (mayor recall, menor precisión)**
```text
TITLE-ABS-KEY ( repuestos OR "inventario de repuestos" OR desabastecimiento OR "faltante de stock" OR "pico de demanda" OR "gestión de pedidos de repuestos" OR "administración de pedidos de inventario" ) AND TITLE-ABS-KEY ( microservicios OR "arquitectura nativa en la nube" OR contenedorización OR "asignación de inventario" OR "cumplimiento de pedidos" OR "sistemas de reserva de inventario" OR "políticas de asignación de stock" OR "prevención de sobreventa" OR "actualizaciones consistentes de inventario" ) AND TITLE-ABS-KEY ( "exactitud de inventario" OR "nivel de servicio" OR "escalabilidad de sistemas de inventario" OR "escalabilidad de microservicios" OR "escalabilidad en la nube" OR "tiempo de respuesta" OR latencia OR sobreventa ) AND PUBYEAR > 2021 AND PUBYEAR < 2027 AND ( LIMIT-TO ( DOCTYPE , "ar" ) ) AND ( LIMIT-TO ( LANGUAGE , "Spanish" ) )
```
