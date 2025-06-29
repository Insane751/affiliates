import random
import requests
import time

# Configurations for each campaign
campaigns = [
    {
        'name': 'BIONICA',
        'place_ids': [
            '114897945188014', '246106268792844', '111939165490631'
        ],
        'images': [
            'https://drive.google.com/uc?export=view&id=1VRb4s-TAWLSBNsZG7Ej_FJxCIZ3PXsh6',
            'https://drive.google.com/uc?export=view&id=1XY077S5bLmWXkA9F93P2afQ1zDaOv63n',
            'https://drive.google.com/uc?export=view&id=1cAmyW4FEWpCxODku7EYy7Nd30jT-wR_9',
            'https://drive.google.com/uc?export=view&id=1aXGSW0uImdOEcDxOJedIkkIBkMREUphh'
        ],
        'user_access_token': 'EAAOw0hQlw90BOyTQDz855rwbwadBUXOgyNOiNr26HVCnY88Amj8AssX0v6YS2EveYCiqAnwZBOkGDB7rqkcDZA6YZCTrAEPeN5IZABPON6HmEcYuadknWX4H48mKd4qPBMbgm7mByx6tcgdqEX8zrzOGNAoJ5oDuZABUZA2gxWik7LVCMxHJU6eJJB9T7K',
        'page_id': '589154177608220',
        'message': '''🔥 ¡Dile adiós al dolor de articulaciones y espalda con Bionica! 🔥 

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
            '108446732520456', '111977915487788', '116201475057063', '111838148832983'
        ],
        'images': [
            'https://drive.google.com/uc?export=view&id=198WA5yrBhIQfUJmScQV1qAWiOqQniD1i',
            'https://drive.google.com/uc?export=view&id=1UaIiiQyZSVxPrlCPzLj1uns7dYMntWFy',
            'https://drive.google.com/uc?export=view&id=1VTNMECWlBjMlGL9ek-9nfy84MBlkZiSD',
            'https://drive.google.com/uc?export=view&id=1kjEWuVZFrgO8_vSdOupXyBvr8_pat4gh',
            'https://drive.google.com/uc?export=view&id=1mMYE8tsCOjOilHrQNbtlUtv7AOzEA5Fz'
        ],
        'user_access_token': 'EAASxCueM5bYBO4ZBUozZAYd5OcOdX3ubEkOh8RZCrQyos5KC193UALTEiTMTewpmBUkSSM6y1jMeQvxC3IZBynNJYgk9AYTIYJv3aTDabZAOZBo0MZBZCUMNHER6pZCvcu7nZBwimQMjWdKJZAaZBibylwKBDJV2eMPzYiyOuhcZAkOrHIhItG619QTemw4EmZB0szMUDR',
        'page_id': '566302159902808',
        'message': '''¡Dígale adiós al dolor articular en solo 10 días!
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
#AlivioDelDolorArticular #Flexacil #VidaSinDolor #ArticulacionesSaludables'''
    },





   {
        'name': 'INSULUX',
        'page_id': '684674071395453',
        'user_access_token': 'EAASLVpBBZBd0BOyznHs5tHEnqZCNm1R6l934BlqA7HLctNAEPZB70iaZCGjs6x1OTYGjqUYsQf2AXAROGB8biicrZC9kc57BsomsgTgYAVAb1caWOCvLquPo07OlewAMOMYcER8K44kqquLLVHWXDw17t3zUdR7bZCFuSPLRgpmPCaIQjRSdQVEphucSjJ',
        'place_ids': [
            '107674002595670',
            '164636974246744',
            '104223529609899',
            '106031246101831'
            # Add more place IDs as needed
        ],
        'images': [
'https://drive.google.com/uc?export=view&id=190hkNPiVxGWClEq9lWczfEeX7Fm7p3ue', 'https://drive.google.com/uc?export=view&id=192k_n6IpVXCelbuPmgZ8Q1MKvt3sRauA', 'https://drive.google.com/uc?export=view&id=195v7Zhss1IfvjCSdPWPBeQIxbOskIx33', 'https://drive.google.com/uc?export=view&id=19GPpnNzc-MzM1R1GrGJZvHwkm9kchRTn', 'https://drive.google.com/uc?export=view&id=19KakmrwOoQh4NYnGQkS43OVDbVLxCpvj'        ],
        'message': '''
        🔥 Ucapkan Selamat Tinggal kepada Gula Darah Tinggi dengan INSULUX!  🔥
Bergelut dengan keletihan, mengidam, atau lonjakan gula?  Jangan biarkan diabetes mengawal hidup anda.  Dengan hanya 2 kapsul semulajadi sehari, Insulux membantu anda mengawal semula — cepat, selamat dan sangat berkesan!  💊💪 

👉👉- https://tinyurl.com/mr3pt6bh 

✅ Mengapa Insulux Berfungsi:
• Meningkatkan pengeluaran insulin secara semulajadi
• Meremajakan pankreas & hati anda
• Menstabilkan gula dalam darah & mengurangkan rasa mengidam
• Melawan keradangan & menguatkan imuniti
• Dikuasakan oleh Gymnema, Fenugreek, Soursop & banyak lagi 🌿
🎯 Diuji secara klinikal – 89% melihat hasil dalam masa 40 hari sahaja!
👉👉- https://tinyurl.com/mr3pt6bh 

🛒 CARA ORDER:
🚨 HARI INI SAHAJA – DISKAUN 50%!
💰 Harga Asal: 338 RM
🔥 Kini Sahaja: 169 RM
📲 Letakkan nama & nombor telefon anda di bawah – pasukan kami akan menghubungi anda terus untuk mengesahkan pesanan anda! 

👉👉- https://tinyurl.com/mr3pt6bh 

#Malaysia #Insulux #DiabetesSupport #BloodSugarControl #RendahkanGulaDarahSecaraSemulajadi #NaturalHealth #SugarBalance #PancreasHealth #InsulinSupport #MalaysiaHealth #DiabetesSolution #HealthyHid #NaturalRemedy #ImmuneBoost
'''
    }   
    
]

def get_page_access_token(page_id, user_token):
    url = f'https://graph.facebook.com/v20.0/{page_id}?fields=access_token&access_token={user_token}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get('access_token')
    except requests.RequestException as e:
        print(f"❌ Error retrieving access token for page {page_id}: {e}")
        return None

def post_with_location(page_id, token, image_url, place_id, message):
    photo_url = f'https://graph.facebook.com/v20.0/{page_id}/photos'
    photo_payload = {
        'access_token': token,
        'url': image_url,
        'published': 'false'
    }
    photo_response = requests.post(photo_url, data=photo_payload)
    if photo_response.status_code != 200:
        print(f"❌ Failed to upload photo: {photo_response.text}")
        return

    photo_id = photo_response.json().get('id')
    if not photo_id:
        print("❌ No photo ID returned.")
        return

    feed_url = f'https://graph.facebook.com/v20.0/{page_id}/feed'
    feed_payload = {
        'access_token': token,
        'message': message,
        'place': place_id,
        'attached_media': [{'media_fbid': photo_id}]
    }
    feed_response = requests.post(feed_url, json=feed_payload)
    if feed_response.status_code == 200:
        print(f"✅ Post successful at place {place_id}")
    else:
        print(f"❌ Failed to post to feed: {feed_response.status_code} {feed_response.text}")

# Main loop through campaigns
for campaign in campaigns:
    print(f"\n📢 Starting campaign: {campaign['name']}")
    token = get_page_access_token(campaign['page_id'], campaign['user_access_token'])

    if not token:
        print(f"❌ Skipping campaign {campaign['name']} due to token issue.")
        continue

    place_ids = campaign['place_ids'][:]
    images = campaign['images'][:]

    while place_ids:
        place = place_ids.pop(random.randint(0, len(place_ids) - 1))
        image = random.choice(images)  # reuse images
        print(f"📸 Posting image: {image} | 📍 Place: {place}")
        post_with_location(campaign['page_id'], token, image, place, campaign['message'])
        time.sleep(2)

print("✅ All campaigns finished.")
