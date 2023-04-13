
# Project Setup

## Quick setup (BETA)
Para levantar el entorno rápidamente ejecutar script flask_up.sh

## Manual setup 
- Crear entorno virtual python o instalar paquetes en máquina local
```bash
python3 -m venv venv
```
- Entrar al entorno
```bash
source ./venv/bin/activate
```
- Instalar dependencias
```bash
pip install -r requirements.txt
```
- Iniciar servidor (DEV)
Ejecutar en la terminal estando en el entorno virtual el comando: 
```bash
flask run --host 0.0.0.0 --port 5000
```

# Test the API
## POSTMAN
Para probar el funcionamiento del microservicio abrimos POSTMAN, hacemos una llamada a la URL:PUERTO donde esté Flask llamando por POST y pasándole como datos un JSON con el siguiente formato
```json
{
  "html_filepath": "0001/invoice.html",
  "css_filepath":  "0001/invoice.css",
  "pdf_filename":  "resultado_final.pdf",
  "data": {
    "invoice_number": "27272772",
    "first_name": "Tommy Nabou"
  }
}
```

## MANUAL
En una terminal ejecutamos el siguiente comando:
```bash
curl --location '127.0.0.1:5000/' \
--header 'Content-Type: application/json' \
--data '{
  "html_filepath": "0001/invoice.html",
  "css_filepath":  "0001/invoice.css",
  "pdf_filename":  "resultado_final.pdf",
  "data": {
    "invoice_number": "27272772",
    "first_name": "Tommy Nabou"
  }
}'
```

# EXPECTED BEHAVIOR
Si se ha generado el PDF correctamente la llamada a la API deberá devolver un String con la ruta donde se ha generado el fichero PDF.
Ejemplo:
```json
outputs/resultado_final.pdf
```
Si ha habido algún error al geenrar el PDF o recibir los datos la API devolverá un error 500 con el siguiente texto: 
```json
Fail generating PDF file
```

