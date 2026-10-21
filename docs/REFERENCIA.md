# Referencia disponible para todos

## Docker

Ejecuta desde la raíz del repositorio. El entrevistador precarga las imágenes.

| Comando | Uso |
|---|---|
| `python3 tools/lab.py start` | Inicia los servicios con la imagen preparada |
| `docker compose ps -a` | Estado de los contenedores |
| `docker compose logs --no-color` | Logs de los servicios |
| `docker compose logs --no-color delivery` | Logs de un servicio |
| `docker compose exec -T delivery env` | Entorno efectivo del proceso |
| `docker compose restart delivery` | Reinicia el contenedor existente |
| `docker compose up -d --no-build --force-recreate delivery` | Recrea un servicio con su configuración actual |
| `python3 tools/lab.py capture` | Guarda logs, estado y recibo en evidence/ |
| `python3 tools/lab.py check` | Comprueba el recibo y el archivo simulado contra el contrato |
| `python3 tools/lab.py answers` | Revisa formato de respuestas, sin calificarlas |

Un proceso activo puede haber fallado al realizar su trabajo. Reiniciar un
contenedor existente no carga cambios en su configuración de entorno. La
recreación sí crea un contenedor con la configuración actual.

## Archivos y búsqueda

`pwd`, `ls`, `cat archivo`, `less archivo`, `grep -n 'texto' archivo` y
`rg -n 'texto'` permiten navegar y buscar. Usa el editor que prefieras.
Los logs incluyen eventos históricos: correlaciona cliente, run_id y hora.

## S3 e IAM en este laboratorio

Bucket es el contenedor lógico; key es la clave completa del objeto. El prefijo
es el comienzo de esa clave, no una carpeta con permisos independientes.
`s3:PutObject` identifica la acción de escribir un objeto. La política de
`case/policy.json` se aplica a la identidad indicada en el contrato.
`Resource` identifica los objetos autorizados mediante un ARN.

Un AccessDenied requiere comparar identidad, acción y recurso con la política.
En AWS real puede haber más políticas y otras causas; este ejercicio limita el
modelo a una única política Allow sin otras capas.

El procedimiento de la sesión está en `case/CONTRATO.md`. Corregir un destino
fuera del contrato no requiere ampliar permisos. Los reintentos con la misma
configuración no corrigen un rechazo determinista de permisos.

## Git

Sustituye los marcadores por los valores de tu sesión.

```sh
git clone --branch caso/Cxx <URL_REPOSITORIO> prueba-l2
cd prueba-l2
git switch -c entrega/Cxx
git status
git diff
git add RESPUESTAS.json evidence
git commit -m "Documenta diagnóstico y evidencia del incidente"
git add config.env RESPUESTAS.json evidence
git commit -m "Corrige destino y documenta validación"
git push -u origin entrega/Cxx
git rev-parse HEAD
git ls-remote origin refs/heads/entrega/Cxx
```

Guarda el diagnóstico en el primer commit **antes** de modificar la configuración.
Un commit local no publica cambios; compara el SHA local y el remoto tras el push.
No se pide pull request, rebase ni resolver conflictos.

## Referencias originales

- Docker Compose: https://docs.docker.com/reference/cli/docker/compose/
- Políticas S3: https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-policy-language-overview.html
- Git: https://git-scm.com/book/en/v2.html
