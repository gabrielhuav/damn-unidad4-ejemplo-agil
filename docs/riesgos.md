# Riesgos y respuestas

| Riesgo | Evidencia temprana | Respuesta |
|---|---|---|
| Sensor ausente o permiso denegado | Prueba en dispositivo real al inicio | Referencia manual y explicación en UI |
| Diferente soporte KMP/Flutter por destino | Prototipo pequeño con adaptador | Delimitar plataformas y documentar alternativa |
| API o red no disponible | Timeout y prueba de modo avión | Borrador local y reintento idempotente |
| Acceso a reportes ajenos | Prueba con dos identidades ficticias | Autorización en servidor y reglas de nube |
| Cambio de alcance | Historias añadidas durante Sprint | Conversar impacto y reordenar backlog |

La matriz se revisa en cada Sprint y no sustituye las pruebas.
