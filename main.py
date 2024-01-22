import requests

def send_whatsapp_template_message(token, phone_number, template_name, language_code):
    url = 'https://graph.facebook.com/v18.0/213714565158727/messages'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    body = {
        'messaging_product': 'whatsapp',
        'to': phone_number,
        'type': 'template',
        'template': {
            'name': template_name,
            'language': {
                'code': language_code
            }
        }
    }
    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()  # Manejo de errores
        return response.json()
    except requests.exceptions.RequestException as e:
        return f'Error: {e}'

# Uso de la función con una plantilla
access_token = 'EAADr2Bfvo30BO3bD5Em0g79E3lUeNjnSS9fPV5ulStPJwDp09EiwXqwid3h7sHJGm6B36JI4QRg2lN0KglTcgvdQNyNHWgKpxzcIZCY3wu8CEZCH7U0YpTn75SjiCj02jOZBsTmlHRZCDhinWC2u56DtxPijq0Ckbo4KxP0l0vzLfVYTbkjyhdHU17a1UIZBIBhGhjWQT9WCxnY67ugZDZD'
recipient_number = '573115839595'
template_name = 'defualt'
language_code = 'es'

response = send_whatsapp_template_message(access_token, recipient_number, template_name, language_code)
print(response)