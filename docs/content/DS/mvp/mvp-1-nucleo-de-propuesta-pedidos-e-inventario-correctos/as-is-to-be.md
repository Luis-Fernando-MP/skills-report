# AS-IS / TO-BE — MVP 1

Etiqueta global AS-IS: `hipótesis` / `pendiente_campo` (sin observación de campo en Komatsu).  
Confiabilidad TO-BE: **baja hasta Fase 0 / R1–R5**; el artefacto TO-BE materializa `ref: DT Prototype`.

## Leyenda

| Emoji | Significado |
|-------|-------------|
| 🟢 | Inicio |
| 🔵 | Actividad |
| 🔶 | Decisión |
| 🔴 | Fin |
| ⚠️ | Fricción |

## AS-IS (propuesta de trabajo)

Flujo crítico hipotético: demanda de parte → consulta de disponibilidad → promesa/pedido → riesgo de doble asignación. Artefactos posibles (no afirmados in-situ): NPS, WMS, Excel, correo, voz. `pendiente_campo`

```mermaid
flowchart TB
  subgraph laneOp ["Carril Operador pedidos"]
    direction TB
    a1(["🟢 1. Llega demanda de parte"])
    a2["🔵 2. Consulta disponibilidad"]
    a3{"🔶 3. Dato confiable ahora?"}
    a4["🔵 4. Promete / crea pedido"]
    a5(["🔴 5. Cliente/dealer notificado"])
  end
  subgraph laneInv ["Carril Inventario / centro partes"]
    direction TB
    b1["🔵 6. Revisa stock en sistema o soporte"]
    b2["⚠️ 7. Ajuste tardio o discrepancia"]
  end
  subgraph laneSis ["Carril Sistemas existentes"]
    direction TB
    c1["🔵 8. NPS y/o WMS u otro canal"]
  end
  a1 --> a2
  a2 --> c1
  c1 --> b1
  b1 --> a3
  a3 -->|"si"| a4
  a3 -->|"no / duda"| b2
  b2 -->|"⚠️ reconsulta"| a2
  a4 --> a5
```

**Paso a paso AS-IS**

1. **🟢 1.** Operador recibe demanda de parte.  
2. **🔵 2.** Busca disponibilidad (canal no observado).  
3. **🔵 8.** Puede abrir NPS/WMS u otro (`evidencia` de existencia pública; uso local `pendiente_campo`).  
4. **🔵 6.** Inventario interpreta stock.  
5. **🔶 3.** ¿Confía en el dato *ahora*?  
6. Si duda → **⚠️ 7** ajuste/discrepancia y vuelve a consultar.  
7. Si sí → **🔵 4** promete/crea pedido **sin invariante de reserva concurrente demostrado** (`hipótesis`).  
8. **🔴 5.** Notifica al solicitante.

**Fricciones ⚠️:** ventanas entre consulta y promesa; dos operadores pueden “ganar” el mismo stock; sin prueba de 0 oversell. `hipótesis`

## TO-BE (solo MVP 1)

Mismos carriles + artefacto `ReservarStockAlCrearPedido` (`ref: DT Prototype`). Sin ERP, sin multi-almacén global, sin reemplazo NPS/WMS.

```mermaid
flowchart TB
  subgraph laneOp2 ["Carril Operador pedidos"]
    direction TB
    t1(["🟢 1. Llega demanda de parte"])
    t2["🔵 2. POST /pedidos via coleccion"]
    t3{"🔶 3. HTTP 201?"}
    t4["🔵 4. Confirma pedido reservado"]
    t5["🔵 5. Comunica rechazo sin mutar"]
    t6(["🔴 6. Fin"])
  end
  subgraph lanePoC ["Carril PoC reserva"]
    direction TB
    p1["🔵 7. ReservarStockAlCrearPedido"]
    p2{"🔶 8. Stock alcanza bajo lock?"}
    p3["🔵 9. Commit pedido + reservado"]
    p4["🔵 10. Rollback total"]
  end
  subgraph laneInv2 ["Carril Inventario"]
    direction TB
    i1["🔵 11. Consulta GET inventario partNumber"]
  end
  subgraph laneSis2 ["Carril NPS/WMS"]
    direction TB
    s1["🔵 12. Fuera de alcance MVP1 - coexisten"]
  end
  t1 --> t2
  t2 --> p1
  p1 --> p2
  p2 -->|"si"| p3
  p2 -->|"no"| p4
  p3 --> t3
  p4 --> t3
  t3 -->|"201"| t4
  t3 -->|"4xx"| t5
  t4 --> t6
  t5 --> t6
  t4 -.-> i1
  s1 -.->|"no reemplazo"| p1
```

**Paso a paso TO-BE**

1. **🟢 1.** Demanda llega al operador.  
2. **🔵 2.** Ejecuta `POST /pedidos` (colección).  
3. **🔵 7–8.** PoC reserva bajo control de concurrencia.  
4. Si alcanza → **🔵 9** commit; si no → **🔵 10** rollback.  
5. **🔶 3.** ¿201?  
6. **🔵 4** confirma promesa con stock reservado **o** **🔵 5** comunica rechazo sin mutar.  
7. **🔴 6.** Fin.  
8. **🔵 11.** Inventario puede auditar `disponible`/`reservado`.  
9. **🔵 12.** NPS/WMS **no** se sustituyen en MVP 1 (`valida: R3`).

## Brecha AS-IS → TO-BE

| Brecha | Qué cambia en MVP 1 | Valida |
|--------|---------------------|--------|
| Promesa sin reserva atómica | `POST /pedidos` solo con reserva OK | `R2` |
| Dolor / prioridad no confirmados | Kickoff sponsor + tipificación | `R1` |
| Riesgo shadow IT vs NPS/WMS | Narrativa coexistencia + ADR | `R3` |
| Demo no usable sin explicación | Colección + demo muda | `R4` |
| Sin receptor empresarial | Sponsor nombrado + fecha | `R5` |

Fuera de esta brecha (MVP 2–3): Docker/k6 sistemático, ECS/AWS, extracción a microservicios.
