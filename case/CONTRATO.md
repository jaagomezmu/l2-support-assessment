# Contrato de entrega — C02

- Cliente: `cliente-474`
- Ejecución investigada: `RUN-C02-3485`
- Identidad: `arn:aws:iam::000000000000:role/lab-c02`
- Bucket autorizado: `lab-l2-c02-deliveries`
- Prefijo contratado: `clientes/cliente-474/daily/`
- Nombre de objeto: `delivery-c02.csv`
- SHA-256 del contenido: `6058fff8a331a7b23c5eaca78569fe29ef8da278a2f0da48118c425a7136a143`

## Procedimiento

1. Correlacionar logs por cliente y ejecución; los eventos históricos no describen necesariamente el estado actual.
2. Comparar el destino efectivo con este contrato y con `policy.json`, asignada a la identidad indicada.
3. Corregir localmente desvíos del destino contratado. No ampliar permisos ni modificar el contrato.
4. Aplicar la configuración al servicio afectado y validar clave, contenido y ejecución del recibo.
5. Si la configuración ya coincide y persiste el rechazo, escalar con identidad, acción, recurso e identificador del intento. No prometer tiempos sin evidencia.

En este simulador escribir de nuevo la misma clave reemplaza el mismo objeto; no añade registros ni genera cargos. En un sistema real se debe confirmar la seguridad de reprocesar.
