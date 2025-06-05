import random
import requests
import time


# Configurations for each campaign
campaigns = [
{
    'name': 'BIONICA',
    'place_ids': [
        '114897945188014','246106268792844', '111939165490631'
     ],
    'images': [
        'https://drive.google.com/uc?export=view&id=1VRb4s-TAWLSBNsZG7Ej_FJxCIZ3PXsh6',
        'https://drive.google.com/uc?export=view&id=1XY077S5bLmWXkA9F93P2afQ1zDaOv63n',
        'https://drive.google.com/uc?export=view&id=1cAmyW4FEWpCxODku7EYy7Nd30jT-wR_9',
        'https://drive.google.com/uc?export=view&id=1aXGSW0uImdOEcDxOJedIkkIBkMREUphh'
        ],
    'user_access_token': 'EAAOw0hQlw90BOyTQDz855rwbwadBUXOgyNOiNr26HVCnY88Amj8AssX0v6YS2EveYCiqAnwZBOkGDB7rqkcDZA6YZCTrAEPeN5IZABPON6HmEcYuadknWX4H48mKd4qPBMbgm7mByx6tcgdqEX8zrzOGNAoJ5oDuZABUZA2gxWik7LVCMxHJU6eJJB9T7K',
    'page_id': '589154177608220',
    'message': '''
🔥 ¡Dile adiós al dolor de articulaciones y espalda con Bionica! 🔥 

👉👉- https://tinyurl.com/3fz85hxs

¿Las articulaciones rígidas, el dolor de espalda o la hinchazón te impiden disfrutar de la vida? ¡Bionica está aquí para ayudarte! Esta poderosa fórmula natural está diseñada para curar las articulaciones, reducir la inflamación y restaurar la movilidad, ¡para que puedas moverte libremente y vivir sin límites! 💃🏃‍♂️ 

👉👉-  https://tinyurl.com/3fz85hxs

✨ ¿Por qué elegir Bionica?  ✨
✅ Alivia el dolor y la rigidez al instante ⚡️
✅ Reduce la hinchazón y el enrojecimiento 🌡️
✅ Elimina los molestos crujidos de las articulaciones 🔇
✅ Fortalece el cartílago y los huesos 🦴💪
✅ 100 % natural y seguro: ¡sin efectos secundarios! 🍃
✅ ¡Funciona desde la semana 1! ⏳
🔬 Recomendado por especialistas: ¡confiado por miles de personas! 👩‍⚕️👨‍⚕️
💥 ¡OFERTA POR TIEMPO LIMITADO! 💥
💰 Precio anterior: 1180 MXN
🔥 Precio nuevo: ¡SOLO 590 MXN! (¡Ahorra un 50 %!)
🛒 ¡Haz tu pedido AHORA antes de que termine el descuento! No dejes que el dolor controle tu vida: ¡da el primer paso hacia un futuro sin dolor hoy mismo! 

👉👉- https://tinyurl.com/3fz85hxs

🔹 #México#Biónica #SaludArticular #AlivioDelDolor #MuéveteLibremente #AlivioDelDolorDeEspalda #CuraciónNatural #ArticulacionesSaludables
    '''
},
{
    'name': 'Flexacil Ultra',
    'place_ids': [
'108446732520456','111977915487788', '116201475057063', '111838148832983'
     ],
    'images': [
'https://drive.google.com/uc?export=view&id=198WA5yrBhIQfUJmScQV1qAWiOqQniD1i', 'https://drive.google.com/uc?export=view&id=1UaIiiQyZSVxPrlCPzLj1uns7dYMntWFy', 'https://drive.google.com/uc?export=view&id=1VTNMECWlBjMlGL9ek-9nfy84MBlkZiSD', 'https://drive.google.com/uc?export=view&id=1kjEWuVZFrgO8_vSdOupXyBvr8_pat4gh', 'https://drive.google.com/uc?export=view&id=1mMYE8tsCOjOilHrQNbtlUtv7AOzEA5Fz'
],
    'user_access_token': 'EAASxCueM5bYBO4ZBUozZAYd5OcOdX3ubEkOh8RZCrQyos5KC193UALTEiTMTewpmBUkSSM6y1jMeQvxC3IZBynNJYgk9AYTIYJv3aTDabZAOZBo0MZBZCUMNHER6pZCvcu7nZBwimQMjWdKJZAaZBibylwKBDJV2eMPzYiyOuhcZAkOrHIhItG619QTemw4EmZB0szMUDR',    'page_id': '566302159902808',
    'message': '''
¡Dígale adiós al dolor articular en solo 10 días!
🚨 ¡SOLO 1500 paquetes producidos por año! 🚨
🛒 OFERTA POR TIEMPO LIMITADO: ¡-50% DE DESCUENTO!
💰 Ahora solo 149 PEN (Precio regular: 298 PEN)
👉👉 https://tinyurl.com/mbx5fwk8

✅ Cápsulas Flexacil: ¡comprobado para combatir el dolor articular, la artritis y la osteoartritis!
🌿 Fórmula 100 % natural: con condroitina y glucosamina para restaurar la función articular sin cirugía.
🔥 Alivia el dolor y la hinchazón: repara las articulaciones, los tejidos y los ligamentos.
💪 Eficaz para la osteocondrosis y la artritis
👉👉 https://tinyurl.com/mbx5fwk8

📌 Modo de uso:
1️⃣ Tome 1 cápsula con agua.
2️⃣ Úselo 3 veces al día para obtener mejores resultados.
🔥 ¡Reclame su descuento AHORA! 🔥
👉👉 https://tinyurl.com/mbx5fwk8

#Perú
#AlivioDelDolorArticular #Flexacil #VidaSinDolor #ArticulacionesSaludables
    '''
}


]

def get_page_access_token(page_id, user_token):
    version = 'v20.0'
    url = f'https://graph.facebook.com/{version}/{page_id}?fields=access_token&access_token={user_token}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()['access_token']
    except requests.RequestException as e:
        print(f"❌ Error retrieving access token for page {page_id}:", e)
        return None

def post_with_photo(page_id, token, image_url, place_id, message):
    url = f'https://graph.facebook.com/v20.0/{page_id}/photos'
    payload = {
        'access_token': token,
        'message': message,
        'place': place_id,
        'url': image_url  # Use 'url' to post an image from an internet URL
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print(f"✅ Posted successfully: {image_url} at {place_id}")
    else:
        print(f"❌ Failed to post: {response.status_code} {response.text}")


# Run through each campaign
for campaign in campaigns:
    print(f"\n📢 Starting campaign: {campaign['name']}")
    token = get_page_access_token(campaign['page_id'], campaign['user_access_token'])

    if token:
        while campaign['place_ids'] and campaign['images']:
            place = campaign['place_ids'].pop(random.randint(0, len(campaign['place_ids']) - 1))
            image = campaign['images'].pop(random.randint(0, len(campaign['images']) - 1))
            print(f"Posting image: {image} | place: {place}")
            post_with_photo(campaign['page_id'], token, image, place, campaign['message'])
            time.sleep(2)  # Optional rate-limiting
    else:
        print(f"❌ Skipping campaign {campaign['name']} due to token issue.")

print("✅ All campaigns finished.")
