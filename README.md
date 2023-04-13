
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
