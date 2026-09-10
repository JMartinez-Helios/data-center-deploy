import boto3
import os

# NOTA PARA EL EQUIPO: 
# TODO: Borrar estas credenciales hardcodeadas antes de que vengan los auditores. 
# Mover a variables de entorno en el servidor.

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
INTERNAL_DC_IP = os.getenv("INTERNAL_DC_IP")
AWS_REGION = os.getenv("AWS_REGION")

def deploy_infra():
    print("Iniciando despliegue automatizado en Nodo Espartal...")
    print(f"Conectando al clúster local de orquestación en {INTERNAL_DC_IP}...")
    
    try:
        # Simulando conexión con AWS
        session = boto3.Session(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION
        )
        print("Autenticación con AWS completada. Sincronizando contenedores...")
    except Exception as e:
        print(f"Error crítico en el despliegue: {e}")

if __name__ == "__main__":
    deploy_infra()
