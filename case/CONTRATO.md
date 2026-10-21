# Contrato de entrega — C03

- Cliente: `cliente-611`
- Ejecución investigada: `RUN-C03-8774`
- Identidad: `arn:aws:iam::000000000000:role/lab-c03`
- Bucket autorizado: `lab-l2-c03-deliveries`
- Prefijo contratado: `clientes/cliente-611/daily/`
- Nombre de objeto: `delivery-c03.csv`
- SHA-256 del contenido: `e2a86306a8208c5404b423bc41cc8c7a941f47bdb77d159aac96bdb34632bc0d`

## Procedimiento

1. Correlacionar logs por cliente y ejecución; los eventos históricos no describen necesariamente el estado actual.
2. Comparar el destino efectivo con este contrato y con `policy.json`, asignada a la identidad indicada.
3. Corregir localmente desvíos del destino contratado. No ampliar permisos ni modificar el contrato.
4. Aplicar la configuración al servicio afectado y validar clave, contenido y ejecución del recibo.
5. Si la configuración ya coincide y persiste el rechazo, escalar con identidad, acción, recurso e identificador del intento. No prometer tiempos sin evidencia.

En este simulador escribir de nuevo la misma clave reemplaza el mismo objeto; no añade registros ni genera cargos. En un sistema real se debe confirmar la seguridad de reprocesar.
