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
access_token = 'EAADr2Bfvo30BO74iuBBg3fqiJTEYH6bg45T1DhNTpLtKZCywpZBi0vEMui1HOEmkESBfa3MW0I5dIh0ox3ZCC4ic7c8wGkqrIVQGFE5mZCXAOvODmGgB7RS3MRA4mTgfiqZBVSQpScRfB6mSZCjpwSQmAtmZApKuO8n9wEMPZBzKhS7TBAG7IrQzSvZC2M8NLenmpG7KBVALTE4ycOsvDyWgZD'
recipient_number = '57313 8645975'
template_name = 'defualt'
language_code = 'es'

response = send_whatsapp_template_message(access_token, recipient_number, template_name, language_code)
print(response)
