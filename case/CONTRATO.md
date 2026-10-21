# Contrato de entrega — C01

- Cliente: `cliente-337`
- Ejecución investigada: `RUN-C01-9012`
- Identidad: `arn:aws:iam::000000000000:role/lab-c01`
- Bucket autorizado: `lab-l2-c01-deliveries`
- Prefijo contratado: `clientes/cliente-337/daily/`
- Nombre de objeto: `delivery-c01.csv`
- SHA-256 del contenido: `b3ba0c8b0506b63cf698b474f9bff8242f16c2fa55c4debbb2f21baacc88722c`

## Procedimiento

1. Correlacionar logs por cliente y ejecución; los eventos históricos no describen necesariamente el estado actual.
2. Comparar el destino efectivo con este contrato y con `policy.json`, asignada a la identidad indicada.
3. Corregir localmente desvíos del destino contratado. No ampliar permisos ni modificar el contrato.
4. Aplicar la configuración al servicio afectado y validar clave, contenido y ejecución del recibo.
5. Si la configuración ya coincide y persiste el rechazo, escalar con identidad, acción, recurso e identificador del intento. No prometer tiempos sin evidencia.

En este simulador escribir de nuevo la misma clave reemplaza el mismo objeto; no añade registros ni genera cargos. En un sistema real se debe confirmar la seguridad de reprocesar.
