# Flujos AS-IS / TO-BE - Confiabilidad de Inventario PT

## AS-IS
```mermaid
flowchart TD
  comercial[Comercial] --> consultaStock["Consulta disponibilidad WhatsApp o llamada"]
  consultaStock --> almacenero[Almacenero]
  almacenero --> revisaStock["Revisa stock fisico o cuaderno"]
  revisaStock --> informaComercial["Informa a Comercial oral"]
  informaComercial --> comercialConfirma["Comercial confirma a cliente"]
  revisaStock -->|"Friccion: lento, errores, dato desactualizado"| inconsistencia["Inconsistencia fisico vs declarado"]
  inconsistencia --> perdidaVenta["Perdida de venta por incertidumbre"]
```
Etiqueta global: `hipótesis` (supuesto de trabajo hasta Fase 0)

## TO-BE (MVP 1)
```mermaid
flowchart TD
  comercial[Comercial] --> consultaSheets["Consulta hoja de calculo Google Sheets"]
  consultaSheets --> maestroVariantes["Maestro de variantes"]
  consultaSheets --> stockUbicaciones["Stock por ubicacion cierre de turno"]
  maestroVariantes --> comercialConfirma["Comercial confirma a cliente"]
  stockUbicaciones --> comercialConfirma
  almacenero[Almacenero] --> registroMovimientos["Registro entrada salida traslado ajuste"]
  registroMovimientos --> stockUbicaciones
  registroMovimientos -->|"Cierre de turno"| actualizaStock["Stock actualizado al cierre"]
```
`ref: DT Prototype` · `confiabilidad: baja hasta Fase 0`

## Brecha AS-IS → TO-BE

- Qué cambia: fuente única en Sheets (maestro + saldos + bitácora) y registro de movimientos al cierre de turno por almacenero.
- Qué se deja igual: roles comercial/almacenero; consulta sigue siendo humana (sin POS ni tiempo real).
- Qué valida el salto: `valida: R1, R2, R3`
