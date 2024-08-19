import requests
import json

# URL del endpoint de autenticación para obtener el token
token_url = "https://sso-sso-project.apps.desplakur3.desintra.banesco.com/auth/realms/realm-api-qa/protocol/openid-connect/token"

# Credenciales proporcionadas por Banesco
client_id = "1b328428"  # Reemplaza con tu Client ID
client_secret = "209d0798893f3d98c2f1e1a34a55b73b"  # Reemplaza con tu Client Secret

# Datos necesarios para la solicitud del token
token_data = {
    "grant_type": "client_credentials"
}

# Encabezados de la solicitud
token_headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Solicitud POST para obtener el token de acceso
response = requests.post(token_url, data=token_data, auth=(client_id, client_secret), headers=token_headers)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    # Extrae el token de acceso del cuerpo de la respuesta
    token = response.json()["access_token"]
    print("Token de acceso obtenido:", token)
    
    # URL de la API de Banesco
    api_url = "https://sid-validador-consulta-de-transacciones-api-qa-production.apps.desplakur3.desintra.banesco.com/transactions/financial-account/transactions"
    
    # Datos para la solicitud a la API
    payload = {
        "dataRequest": {
            "device": {
                "type": "Notebook",
                "description": "LENOVO",
                "ipAddress": "181.225.47.130"
            },
            "securityAuth": {
                "sessionId": ""
            },
            "transaction": {
                "referenceNumber": "",
                "amount": 0.00,
                "accountId": "01340950160002538514",
                "startDt": "2024-01-26",
                "endDt": "2024-01-26",
                "phoneNum": "",
                "bankId": ""
            }
        }
    }
    
    # Encabezados de la solicitud a la API
    api_headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # Solicitud POST a la API
    api_response = requests.post(api_url, headers=api_headers, data=json.dumps(payload))
    
    # Verifica si la solicitud fue exitosa
    if api_response.status_code == 200:
        # Muestra la respuesta de la API
        print("Respuesta de la API:", api_response.json())
    else:
        print("Error en la solicitud a la API:", api_response.status_code, api_response.text)
else:
    print("Error al obtener el token de acceso:", response.status_code, response.text)
