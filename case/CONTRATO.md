# Contrato de entrega — C04

- Cliente: `cliente-748`
- Ejecución investigada: `RUN-C04-7919`
- Identidad: `arn:aws:iam::000000000000:role/lab-c04`
- Bucket autorizado: `lab-l2-c04-deliveries`
- Prefijo contratado: `clientes/cliente-748/daily/`
- Nombre de objeto: `delivery-c04.csv`
- SHA-256 del contenido: `bf29ba45a11e44ebd2e98c185faf3c0f72323cf1c0054a106e4754966cd501b1`

## Procedimiento

1. Correlacionar logs por cliente y ejecución; los eventos históricos no describen necesariamente el estado actual.
2. Comparar el destino efectivo con este contrato y con `policy.json`, asignada a la identidad indicada.
3. Corregir localmente desvíos del destino contratado. No ampliar permisos ni modificar el contrato.
4. Aplicar la configuración al servicio afectado y validar clave, contenido y ejecución del recibo.
5. Si la configuración ya coincide y persiste el rechazo, escalar con identidad, acción, recurso e identificador del intento. No prometer tiempos sin evidencia.

En este simulador escribir de nuevo la misma clave reemplaza el mismo objeto; no añade registros ni genera cargos. En un sistema real se debe confirmar la seguridad de reprocesar.
