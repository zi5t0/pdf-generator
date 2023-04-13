
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
Para probar el funcionamiento del microservicio simplemente podemos hacer una llamada a la URL donde se levante FLASK llamando por POST y pasándole como datos un JSON con el siguiente formato
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
