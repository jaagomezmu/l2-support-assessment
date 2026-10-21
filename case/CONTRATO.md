# Contrato de entrega — C05

- Cliente: `cliente-885`
- Ejecución investigada: `RUN-C05-2800`
- Identidad: `arn:aws:iam::000000000000:role/lab-c05`
- Bucket autorizado: `lab-l2-c05-deliveries`
- Prefijo contratado: `clientes/cliente-885/daily/`
- Nombre de objeto: `delivery-c05.csv`
- SHA-256 del contenido: `a9bda4def7f60e4e069aa79d52cb827dfafad65f1d3601db9cd51c4b19c8f388`

## Procedimiento

1. Correlacionar logs por cliente y ejecución; los eventos históricos no describen necesariamente el estado actual.
2. Comparar el destino efectivo con este contrato y con `policy.json`, asignada a la identidad indicada.
3. Corregir localmente desvíos del destino contratado. No ampliar permisos ni modificar el contrato.
4. Aplicar la configuración al servicio afectado y validar clave, contenido y ejecución del recibo.
5. Si la configuración ya coincide y persiste el rechazo, escalar con identidad, acción, recurso e identificador del intento. No prometer tiempos sin evidencia.

En este simulador escribir de nuevo la misma clave reemplaza el mismo objeto; no añade registros ni genera cargos. En un sistema real se debe confirmar la seguridad de reprocesar.
