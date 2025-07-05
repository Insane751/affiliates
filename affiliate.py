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
    },
  {
        'name': 'CAARDIONIX',
        'page_id': '615079858357284',
        'user_access_token': 'EAAQQfb0utnEBO079zgFKfYnXKZB2zXJii67seoZC0dK21JJlZAPJo82BR1VDQr25LZCkV0CoGuipP5ByOZC3HQhtNka7PtZBECUZBrFZBZBo9CEvYyyZBR8BwZB3gLNF2oAAjaLYAwYvERSt8IrE9nhGRh7vBYqQi6fDFO5sZCkrHDCLZAQ0WxGwe46booEEkw4xe',
        'place_ids': [
            '114897945188014',             
            '109318109087339',
            '111939165490631',
            '109486839070556'
            # Add more place IDs as needed
        ],
        'images': [
 'https://drive.google.com/uc?export=view&id=18a3lIOpdMwOvtMK4tqtyTPKD4jy83huV', 'https://drive.google.com/uc?export=view&id=18b6FsnXaQj8RJXvhDeE7w_9hxEw59XM0', 'https://drive.google.com/uc?export=view&id=1fvYmTiypDb0ikZLHA3ZNAi0Chh3aLeJP', 'https://drive.google.com/uc?export=view&id=1tZNxWjwVau2nvlNWjs5eQvofEvfwKlNe'],
        'message': '''
        ¿Cansado de que la HIPERTENSIÓN ARTERIAL y la ATEROSCLEROSIS te arruinen la vida?
¡Dile HOLA a CARDIONIX, la solución PODEROSA de la naturaleza!
Sin pastillas. Sin efectos secundarios. Solo RESULTADOS. 

👉👉- https://sites.google.com/view/cardionixhb/home

✔️ 100 % natural
✔️ Recomendado por médicos
✔️ Resultados rápidos: ¡presión arterial normal en 6 horas!
✔️ ¡Seguro para todas las edades!
¿Sientes alguno de estos síntomas?
⚡️ Dolores de cabeza
⚡️ Mareos
⚡️ Problemas de visión
⚡️ Entumecimiento en los dedos
⚡️ Fatiga o cambios de humor
⚡️ Picos de presión arterial 

¡Es la HIPERTENSIÓN llamando a la puerta! ¡No la ignores!  Cardionix te ayuda a:
🌿 Limpiar los vasos sanguíneos de colesterol
❤️ Fortalecer tu corazón
💪 Mejorar la circulación
🔥 Acelera el metabolismo y quema grasa
🧠 Calma los nervios y combate la ansiedad 

👉👉- https://sites.google.com/view/cardionixhb/home 

¡Todo con UN solo producto natural!
Y lo mejor:
¡EXISTENCIAS LIMITADAS! ¡SOLO QUEDAN 18 UNIDADES!
Precio original: ❌1780 MXN
SOLO HOY: ✅890 MXN – ¡50% DE DESCUENTO!
¡No esperes más! ¡Tu corazón se lo merece!
¡Pide ahora!                                                                            👉👉 -https://sites.google.com/view/cardionixhb/home 

#México #Cardionix #CorazónSaludable #AdiósHipertensión #CuraciónNatural #SinColesterol #ControlDePresiónAumento #CuidadoCardiológico #ApoyoCardiológico #AprobadoPorDoctores #SiénteteJovenDeVuelve #OfertaLimitada #OfertasMéxico
'''
    },
      {
        'name': 'Artrolux+ Cream',
        'page_id': '595101733697726',
        'user_access_token': 'EAAPDGinmhkcBOZBY6iDgAN9cJ5mzlsid6ETtrhBSLQTdcBiGuEBD33IgaiZBAxYMG98gSAdWhefeK09cRybx2gYJqrFULqNP3a896XZApJw564q608DSZCyMowTmeaTo7IRXtYWGgLKHTFTda8wMOpdVnuU9SkJHCTgIcJB3ZAi7agMUdw5xNLZA20MdSLr1mD',
        'place_ids': [
            '111175118906315',             
            '110221372332205',
            '116045151742857',
            '108100019211318'
            # Add more place IDs as needed
        ], 
        'images': [
'https://drive.google.com/uc?export=view&id=12Va5qOxsXUx4UGaqpzAzt5OqS0-ERHJK', 'https://drive.google.com/uc?export=view&id=14VMknJsH54V_dRG9u4jf6hip4BjToDZB', 'https://drive.google.com/uc?export=view&id=1W6RuyEZ-Jzil0skQyGk5UtIyZRCg0ock', 'https://drive.google.com/uc?export=view&id=1a0mVbI6AvF9zv8i-hbcoJCSJphlXcP5O', 'https://drive.google.com/uc?export=view&id=1ciilO_uy5P_NXzXQ-uHaZww9NE0BU6MF', 'https://drive.google.com/uc?export=view&id=1rCGroYN4mMA7O0S7jGJgl115_Ma-P4Rg', 'https://drive.google.com/uc?export=view&id=1w_9YyA__8BjshPnNjdSe0EBcEq2MdoJw', 'https://drive.google.com/uc?export=view&id=1zJCNnzR36OaB36FgZWy7XEGof_ihkpyt'
        ],            # Add more image URLs as needed
        'message': '''
        🔥 Rücken- oder Gelenkschmerzen? Schnelle Linderung! 🔥
🧴 ARTROLUX+ Creme – Nur 49 EUR! (vorher 98 EUR)
⚡ 50 % RABATT – Nur noch wenige Packungen verfügbar!

👉👉- https://sites.google.com/view/artroluxcreamhb/home

💥 Sofortige Linderung von Gelenk- und Rückenschmerzen!
🌿 100 % natürlich | 👨‍⚕️ Von Experten empfohlen | 🚫 Keine Nebenwirkungen
✅ Reduziert Entzündungen und Schwellungen
✅ Lindert Schmerzen und Muskelverspannungen
✅ Regeneriert Knorpel
✅ Wirkt ab der ersten Anwendung!

 👉👉- https://sites.google.com/view/artroluxcreamhb/home

📦 So bestellen Sie:
1️⃣ Bestellformular ausfüllen
2️⃣ Versandart wählen
3️⃣ Zahlung per Nachnahme – Keine Vorauszahlung!
🚚 Lieferung in 6–7 Tagen
🛡️ Zertifiziertes EU-Produkt – Originalverpackung mit Code!
🎯 Schnell sein – Nur noch wenige Artikel verfügbar!
👇 Klicken Sie auf „Jetzt bestellen“ und machen Sie den ersten Schritt in ein schmerzfreies Leben!

👉👉- https://sites.google.com/view/artroluxcreamhb/home

#Germany #Deutschland #ArtroluxPlus #Schmerzlinderung #Gelenkunterstützung #Lösung bei Rückenschmerzen #NatürlicheHeilung #Arthroselinderung #GesundeWirbelsäule #KeineSchmerzenMehr #WellnessPflege #Schnell Besser Fühlen
'''
    },
     {
        'name': 'TESTOSTERON BOOST',
        'page_id': '693694570497805',
        'user_access_token': 'EAAPtPy0O7EcBO3jtbGLMXIGA7OJbzBykB5cZC9DA2y2HN64F6adzYC5cZApAOiGWyxlhZCDDweGR9rfOrulrJBIG23ATbSHI0jAYhMZCRooOKZBg8ASEuiOwoV5HVUBai6ggMasbx4npHHUDv9MVWloBMDkQSbfmTsJmntDY7FbUaOyZCpiECiLxqxCi3B',
        'place_ids': [
            '115353315143936',             
            '115247758487174',
            '108581069173026',
            '113396132004585'
            # Add more place IDs as needed
        ], 
        'images': [
'https://i.imgur.com/3yJ6wfq.jpeg', 'https://i.imgur.com/zWeDQnz.jpeg','https://i.imgur.com/W8IYk9x.jpeg','https://i.imgur.com/6z0RMKZ.jpeg' ],            # Add more image URLs as needed
        'message': '''
        🔥 Ritrova la tua virilità con Testosteron Boost! 🔥
💪 Problemi di salute maschile? Prostatite, eiaculazione precoce, impotenza? Non lasciare che peggiori! 

👉👉- https://sites.google.com/view/testosteronboosthb/home 

✅ SOLO PER OGGI: Da €78 ➡️ SOLO €39!
🚚 Consegna rapida in tutta Europa
💰 Paga SOLO alla ricezione dell'ordine!
🔒 Qualità e risultati garantiti al 100%! 

🌿 Estratti naturali di Serenoa repens, Mirtillo rosso, Radice di ortica e Zinco per:
✔️ Aumentare i livelli di testosterone
✔️ Migliorare l'erezione
✔️ Aumentare la fertilità
✔️ Rafforzare il sistema immunitario maschile
✔️ Prevenire prostatite e tumori 

👉👉- https://sites.google.com/view/testosteronboosthb/home 

📦 Come ordinare?
1️⃣ Compila il modulo d'ordine sul nostro sito web 🌐
2️⃣ Conferma il tuo ordine con un nostro operatore 📞
3️⃣ Ricevilo a casa e paga alla consegna! 💸 

💊 Come si usa?
Assumere 1 capsula 1-2 volte al giorno con acqua per 45 giorni.
Ripetere il ciclo se necessario! 

⏰ QUESTA OFFERTA SPECIALE SCADE PRESTO! Non lasciartela sfuggire! 

👉👉- Ordina ora! Solo 39 €!
👉-https://sites.google.com/view/testosteronboosthb/home 

#TestosteroneBoost #SaluteMaschile #ProstataCura #PotenzaMaschile #IntegratoreNaturale #BenessereMaschile #OffertaSpeciale #Europa #UomoPiùForte
'''
    },
      {
        'name': 'ATROLEX ACTIVE',
        'page_id': '756142437571730',
        'user_access_token': 'EAAR9y1wuU0MBPCIX8ZCkI5yZBbJW9LA2uAGpcu2NWJqPVpQqh5YsJZBl9ym4Kv02roEZA30KxZCMaPb9FZA6PZBGUOWYQDgdgbA52kqAYg1r9gnkdbl0FXmIwIOb04aJKhXjZBNdcXk6be9SLQYxLsTAXRlo6OwXR1EbXpLyKufErKudE5PQjPjKCiCBohZAT6AqT',
        'place_ids': [
            '113396132004585',             
            '106071914131317',
            '108581069173026',
            '115353315143936'
            # Add more place IDs as needed
        ], 
        'images': [
'https://i.imgur.com/vXsUCyA.jpeg', 'https://i.imgur.com/lxEZ4En.jpeg','https://i.imgur.com/idnYIdn.jpeg','https://i.imgur.com/tLjGiD0.jpeg' ],            # Add more image URLs as needed
        'message': '''
        ✅ Di' addio al dolore articolare!
💯 100% naturale - Oltre 5.000 confezioni vendute!
🦵✨ Stanco di dolori a mani, gambe o articolazioni? Artrite o artrosi ti rallentano?

👉👉- https://sites.google.com/view/artroflexactivehb/home

ArtroFlex Active è la soluzione naturale ideale!
💥 Ora con il -50% di sconto!
💶 Solo 39 EUR invece di 78 EUR!
🟢 Cosa rende ArtroFlex Active così speciale?
✔️ Rigenera articolazioni e tessuti
✔️ Elimina dolore e gonfiore
✔️ Aiuta in caso di artrite, artrosi e osteocondrite
✔️ Contiene condroitina e collagene per la massima efficacia!

👉👉- https://sites.google.com/view/artroflexactivehb/home

⏰ Affrettati! Pacchetti limitati rimasti - Lo sconto termina presto!
 👉 Come ordinare:
1️⃣ Inserisci il tuo nome 📋
2️⃣ Inserisci il tuo numero di telefono ☎️
3️⃣ Clicca su "Ordina ora" e ti chiameremo noi: riservatezza garantita!

👉👉- https://sites.google.com/view/artroflexactivehb/home

#SaluteArticolari #SollievoArtrite #GuarigioneNaturale #VitaSenzaDolore #ArtroFlexActive
'''
    },

 {
        "name": "STEPLEX-hungary ",
        "page_id": "748985278291360",
        "user_access_token": "EAAPQiGeDh2QBPNTFZAu1qGEiGx10tNiroPOVIecGIdNhAi7Vpf4giWcD0Xb9G6834tlnBKv5AxgWBdftNEo9SIelJbtNrWZAxFhElndEpxxmRU7rNOPeZBPLPaKeAz0eAJQntxbGodLm41srmcxZCdZBy8aZAgdGPFua4u3R0Rq7d29LpGWWfR7ySf5mZB5",
        "default_place_id": [
None

],  # fallback
        "default_images": [
'https://drive.google.com/uc?export=view&id=1B-cB8nlzyWzWpSobN2NFm6oDdYa9RXCc', 'https://drive.google.com/uc?export=view&id=1X27oD9S1P3Uhtnuc2hM4nOoQ9GJ1itie', 'https://drive.google.com/uc?export=view&id=1jfFKB74fhd6XzFzdgqFProJqQ8iyFsqe', 'https://drive.google.com/uc?export=view&id=1tToyOSN-Dmldnfhf03f8eNgqrMauSmdu', 'https://drive.google.com/uc?export=view&id=1VGvv-Bgpp6Fhkxl8vsmuSS-keoaKScdF', 'https://drive.google.com/uc?export=view&id=18jr1hu_6tuBh4DFUxd9G5obxxRwNY9M0', 'https://drive.google.com/uc?export=view&id=1SjWOBLwhEX6VaheIwizWSIHqnktCqj61', 'https://drive.google.com/uc?export=view&id=1dMh8bcPRQKnBh-P0Zr2IizaTjMQ4Zmg6', 'https://drive.google.com/uc?export=view&id=115ujlY-7WbgdPvldWV1-o1RW95pRDnbs', 'https://drive.google.com/uc?export=view&id=1_s4_LQG9XdWGo0ybvYYWw9Inqaz2yx9l', 'https://drive.google.com/uc?export=view&id=1D63ZF4KJRxogKTB-jdZBZEGszbPqRa18', 'https://drive.google.com/uc?export=view&id=1vWlf0T22aZzHgx6NNeBa4X9pofiKhyjN', 'https://drive.google.com/uc?export=view&id=1EjviUESeKHj4bkMmLcmoL8m3_T1tICqt', 'https://drive.google.com/uc?export=view&id=1PRL3j7b51OsJHebVMe59aCHYi7DaCyLf', 'https://drive.google.com/uc?export=view&id=15Z7o2lE-UzLe38FEqUVs4cMUjV4rAZbQ', 'https://drive.google.com/uc?export=view&id=1Izy1RDfMfOFcm1farJ9_RkPA7Zm_fMlY', 'https://drive.google.com/uc?export=view&id=1ZPolNHIBFMWdmF4UFQ4lWZgdxuIllWx9', 'https://drive.google.com/uc?export=view&id=1nzrTUVl4rJWOT44zZbDpat1wtc-WtHeD', 'https://drive.google.com/uc?export=view&id=123AdgyvNjWicTQbRXvcecHhCFbRjxB6F', 'https://drive.google.com/uc?export=view&id=1ftJAnsrHj6eU5uj0qyrsppk7MDXVhNuV'

        ],
        "messages": [




#MESSAGE1




            {
                "text": '''
🎉🟢 Ints búcsút az ízületi fájdalomnak a Steplex-szel! 🟢🎉
Fáj a térded, vállad vagy derekad? Nem vagy egyedül — ezrek találtak megkönnyebbülést ezzel a természetes géllel!

🌿 A Steplex mentolt, ginkgo bilobát, vadgesztenyét és kapszaicint tartalmaz:
✅ Hűsíti és csökkenti a gyulladást
✅ Enyhíti az ízületi merevséget
✅ Segíti a szabadabb mozgást
✅ Kíméli a bőrt, nem okoz irritációt

📦 Rendelés egyszerűen, fizetés csak átvételkor.
👉 Kattints ide és rendeld meg most: https://sites.google.com/view/steplexhb/home
💬 Ne halogasd – érezd a különbséget már az első használat után!
''',
'place_id':[        #HUNGARY
    '106502519386806','107428052620200', '115947611748836'
]    
            },



#MESSAGE2


                        {
                "text": '''
😫 Nehéz reggelente felkelni? Ízületi fájdalom akadályoz a napi teendőkben?
Itt a megoldás: Steplex – természetes fájdalomcsillapító gél, amit az emberek imádnak!

🧴 Egyedi formulája segít:
🌿 Csökkenteni a gyulladást
💪 Visszanyerni az ízületeid rugalmasságát
🧘‍♀️ Élvezni a fájdalommentes mozgást újra

🛒 Egyszerű megrendelés – nincs előleg, nincs bonyodalom.
🚚 Rendelés után gyors szállítás, fizetés a kézbesítéskor!
👉 Jelentkezz most: https://sites.google.com/view/steplexhb/home

''',
'place_id':[        #HUNGARY
    '106502519386806','107428052620200', '115947611748836'
]    
            },



#MESSAGE3





                        {
                "text": '''
💚 Elveszett szabadságérzet? A fájdalom fogságában élsz?
Ne hagyd, hogy az ízületeid szabják meg, hogyan éled az életed!
✨ A Steplex lehet a fordulópont.

✅ Természetes összetevők – mellékhatások nélkül
✅ Hatékony korfüggő kopás, sérülések, gyulladások ellen
✅ Könnyen használható, gyorsan felszívódik

⚠️ Készlet korlátozott – ne maradj le!
📞 Csak töltsd ki a rendelési űrlapot, és visszahívunk a megerősítéshez
👉 Kattints most: https://sites.google.com/view/steplexhb/home
🎯 Válaszd a fájdalommentes életet – most!
''',
'place_id':[        #HUNGARY
    '106502519386806','107428052620200', '115947611748836'
]    
            }]
            },
























































        {
        "name": "STEPLEX-Romania ",
        "page_id": "748985278291360",
        "user_access_token": "EAAPQiGeDh2QBPNTFZAu1qGEiGx10tNiroPOVIecGIdNhAi7Vpf4giWcD0Xb9G6834tlnBKv5AxgWBdftNEo9SIelJbtNrWZAxFhElndEpxxmRU7rNOPeZBPLPaKeAz0eAJQntxbGodLm41srmcxZCdZBy8aZAgdGPFua4u3R0Rq7d29LpGWWfR7ySf5mZB5",
        "default_place_id": [
None

],  # fallback
        "default_images": [
'https://drive.google.com/uc?export=view&id=1B-cB8nlzyWzWpSobN2NFm6oDdYa9RXCc', 'https://drive.google.com/uc?export=view&id=1X27oD9S1P3Uhtnuc2hM4nOoQ9GJ1itie', 'https://drive.google.com/uc?export=view&id=1jfFKB74fhd6XzFzdgqFProJqQ8iyFsqe', 'https://drive.google.com/uc?export=view&id=1tToyOSN-Dmldnfhf03f8eNgqrMauSmdu', 'https://drive.google.com/uc?export=view&id=1VGvv-Bgpp6Fhkxl8vsmuSS-keoaKScdF', 'https://drive.google.com/uc?export=view&id=18jr1hu_6tuBh4DFUxd9G5obxxRwNY9M0', 'https://drive.google.com/uc?export=view&id=1SjWOBLwhEX6VaheIwizWSIHqnktCqj61', 'https://drive.google.com/uc?export=view&id=1dMh8bcPRQKnBh-P0Zr2IizaTjMQ4Zmg6', 'https://drive.google.com/uc?export=view&id=115ujlY-7WbgdPvldWV1-o1RW95pRDnbs', 'https://drive.google.com/uc?export=view&id=1_s4_LQG9XdWGo0ybvYYWw9Inqaz2yx9l', 'https://drive.google.com/uc?export=view&id=1D63ZF4KJRxogKTB-jdZBZEGszbPqRa18', 'https://drive.google.com/uc?export=view&id=1vWlf0T22aZzHgx6NNeBa4X9pofiKhyjN', 'https://drive.google.com/uc?export=view&id=1EjviUESeKHj4bkMmLcmoL8m3_T1tICqt', 'https://drive.google.com/uc?export=view&id=1PRL3j7b51OsJHebVMe59aCHYi7DaCyLf', 'https://drive.google.com/uc?export=view&id=15Z7o2lE-UzLe38FEqUVs4cMUjV4rAZbQ', 'https://drive.google.com/uc?export=view&id=1Izy1RDfMfOFcm1farJ9_RkPA7Zm_fMlY', 'https://drive.google.com/uc?export=view&id=1ZPolNHIBFMWdmF4UFQ4lWZgdxuIllWx9', 'https://drive.google.com/uc?export=view&id=1nzrTUVl4rJWOT44zZbDpat1wtc-WtHeD', 'https://drive.google.com/uc?export=view&id=123AdgyvNjWicTQbRXvcecHhCFbRjxB6F', 'https://drive.google.com/uc?export=view&id=1ftJAnsrHj6eU5uj0qyrsppk7MDXVhNuV'

        ],
        "messages": [










#MESSAGE1
            {
                "text": '''
🎉🟢 Spune adio durerilor articulare cu Steplex! 🟢🎉
Ai dureri de genunchi, umăr sau spate? Nu ești singurul - mii de oameni au găsit alinare cu acest gel natural!

🌿 Steplex conține mentol, ginkgo biloba, castan sălbatic și capsaicină:
✅ Răcorește și reduce inflamația
✅ Ameliorează rigiditatea articulațiilor
✅ Ajută la o mișcare mai liberă
✅ Delicat cu pielea, nu provoacă iritații

📦 Comandă ușor, plătește doar la primire.
👉 Apasă aici și comandă acum: https://sites.google.com/view/steplexhb/home
💬 Nu mai aștepta - simte diferența după prima utilizare!
''',
    'place_id': [
#ROMANIA
'106076642756874', 
'114304211920174', #BUCHAREST
'190714938396682', #Cluj-Napoca, Romania
    ]
            },
















#MESSAGE2
            {
                "text": '''
😫 Ai probleme cu trezirea dimineața? Durerile articulare îți împiedică activitățile zilnice?
Iată soluția: Steplex – un gel natural analgezic pe care oamenii îl adoră!

🧴 Formula sa unică ajută la:
🌿 Reduce inflamația
💪 Recâștigă flexibilitatea articulațiilor
🧘‍♀️ Bucură-te din nou de mișcare fără durere

🛒 Comandă ușoară – fără avans, fără bătaie de cap.
🚚 Livrare rapidă după comandă, plată la livrare!
👉 Aplică acum: https://sites.google.com/view/steplexhb/home
''',
    'place_id': [
#ROMANIA
'106076642756874', 
'114304211920174', #BUCHAREST
'190714938396682', #Cluj-Napoca, Romania
    ]
            },

















#MESSAGE3
            {
                "text": '''
💚 Ți-ai pierdut sentimentul de libertate? Trăiești cu dureri?

Nu lăsa articulațiile să-ți dicteze cum îți trăiești viața!

✨ Steplex ar putea fi punctul de cotitură.


✅ Ingrediente naturale – fără efecte secundare

✅ Eficient împotriva uzurii, deteriorării și inflamației legate de vârstă

✅ Ușor de utilizat, absorbție rapidă

⚠️ Stoc limitat – nu rata!

📞 Completează formularul de comandă și te vom suna înapoi pentru confirmare
👉 Click acum: https://sites.google.com/view/steplexhb/home
🎯 Alege o viață fără durere – acum!
''',
    'place_id': [
#ROMANIA
'106076642756874', 
'114304211920174', #BUCHAREST
'190714938396682', #Cluj-Napoca, Romania
    ]
            }









]
            }



























,


        {
        "name": "STEPLEX-greece ",
        "page_id": "748985278291360",
        "user_access_token": "EAAPQiGeDh2QBPNTFZAu1qGEiGx10tNiroPOVIecGIdNhAi7Vpf4giWcD0Xb9G6834tlnBKv5AxgWBdftNEo9SIelJbtNrWZAxFhElndEpxxmRU7rNOPeZBPLPaKeAz0eAJQntxbGodLm41srmcxZCdZBy8aZAgdGPFua4u3R0Rq7d29LpGWWfR7ySf5mZB5",
        "default_place_id": [
None

],  # fallback
        "default_images": [
'https://drive.google.com/uc?export=view&id=1B-cB8nlzyWzWpSobN2NFm6oDdYa9RXCc', 'https://drive.google.com/uc?export=view&id=1X27oD9S1P3Uhtnuc2hM4nOoQ9GJ1itie', 'https://drive.google.com/uc?export=view&id=1jfFKB74fhd6XzFzdgqFProJqQ8iyFsqe', 'https://drive.google.com/uc?export=view&id=1tToyOSN-Dmldnfhf03f8eNgqrMauSmdu', 'https://drive.google.com/uc?export=view&id=1VGvv-Bgpp6Fhkxl8vsmuSS-keoaKScdF', 'https://drive.google.com/uc?export=view&id=18jr1hu_6tuBh4DFUxd9G5obxxRwNY9M0', 'https://drive.google.com/uc?export=view&id=1SjWOBLwhEX6VaheIwizWSIHqnktCqj61', 'https://drive.google.com/uc?export=view&id=1dMh8bcPRQKnBh-P0Zr2IizaTjMQ4Zmg6', 'https://drive.google.com/uc?export=view&id=115ujlY-7WbgdPvldWV1-o1RW95pRDnbs', 'https://drive.google.com/uc?export=view&id=1_s4_LQG9XdWGo0ybvYYWw9Inqaz2yx9l', 'https://drive.google.com/uc?export=view&id=1D63ZF4KJRxogKTB-jdZBZEGszbPqRa18', 'https://drive.google.com/uc?export=view&id=1vWlf0T22aZzHgx6NNeBa4X9pofiKhyjN', 'https://drive.google.com/uc?export=view&id=1EjviUESeKHj4bkMmLcmoL8m3_T1tICqt', 'https://drive.google.com/uc?export=view&id=1PRL3j7b51OsJHebVMe59aCHYi7DaCyLf', 'https://drive.google.com/uc?export=view&id=15Z7o2lE-UzLe38FEqUVs4cMUjV4rAZbQ', 'https://drive.google.com/uc?export=view&id=1Izy1RDfMfOFcm1farJ9_RkPA7Zm_fMlY', 'https://drive.google.com/uc?export=view&id=1ZPolNHIBFMWdmF4UFQ4lWZgdxuIllWx9', 'https://drive.google.com/uc?export=view&id=1nzrTUVl4rJWOT44zZbDpat1wtc-WtHeD', 'https://drive.google.com/uc?export=view&id=123AdgyvNjWicTQbRXvcecHhCFbRjxB6F', 'https://drive.google.com/uc?export=view&id=1ftJAnsrHj6eU5uj0qyrsppk7MDXVhNuV'

        ],
        "messages": [




#MESSAGE1




            {
                "text": '''
🎉🟢 Ints búcsút az ízületi fájdalomnak a Steplex-szel! 🟢🎉
Fáj a térded, vállad vagy derekad? Nem vagy egyedül — ezrek találtak megkönnyebbülést ezzel a természetes géllel!

🌿 A Steplex mentolt, ginkgo bilobát, vadgesztenyét és kapszaicint tartalmaz:
✅ Hűsíti és csökkenti a gyulladást
✅ Enyhíti az ízületi merevséget
✅ Segíti a szabadabb mozgást
✅ Kíméli a bőrt, nem okoz irritációt

📦 Rendelés egyszerűen, fizetés csak átvételkor.
👉 Kattints ide és rendeld meg most: https://sites.google.com/view/steplexhb/home
💬 Ne halogasd – érezd a különbséget már az első használat után!
''',
'place_id':[        #HUNGARY
    '106502519386806','107428052620200', '115947611748836'
]    
            },



#MESSAGE2


                        {
                "text": '''
😫 Nehéz reggelente felkelni? Ízületi fájdalom akadályoz a napi teendőkben?
Itt a megoldás: Steplex – természetes fájdalomcsillapító gél, amit az emberek imádnak!

🧴 Egyedi formulája segít:
🌿 Csökkenteni a gyulladást
💪 Visszanyerni az ízületeid rugalmasságát
🧘‍♀️ Élvezni a fájdalommentes mozgást újra

🛒 Egyszerű megrendelés – nincs előleg, nincs bonyodalom.
🚚 Rendelés után gyors szállítás, fizetés a kézbesítéskor!
👉 Jelentkezz most: https://sites.google.com/view/steplexhb/home

''',
'place_id':[        #HUNGARY
    '106502519386806','107428052620200', '115947611748836'
]    
            },



#MESSAGE3





                        {
                "text": '''
💚 Elveszett szabadságérzet? A fájdalom fogságában élsz?
Ne hagyd, hogy az ízületeid szabják meg, hogyan éled az életed!
✨ A Steplex lehet a fordulópont.

✅ Természetes összetevők – mellékhatások nélkül
✅ Hatékony korfüggő kopás, sérülések, gyulladások ellen
✅ Könnyen használható, gyorsan felszívódik

⚠️ Készlet korlátozott – ne maradj le!
📞 Csak töltsd ki a rendelési űrlapot, és visszahívunk a megerősítéshez
👉 Kattints most: https://sites.google.com/view/steplexhb/home
🎯 Válaszd a fájdalommentes életet – most!
''',
'place_id':[        #HUNGARY
    '106502519386806','107428052620200', '115947611748836'
]    
            }]
            }













































,


        {
        "name": "STEPLEX-slovania ",
        "page_id": "748985278291360",
        "user_access_token": "EAAPQiGeDh2QBPNTFZAu1qGEiGx10tNiroPOVIecGIdNhAi7Vpf4giWcD0Xb9G6834tlnBKv5AxgWBdftNEo9SIelJbtNrWZAxFhElndEpxxmRU7rNOPeZBPLPaKeAz0eAJQntxbGodLm41srmcxZCdZBy8aZAgdGPFua4u3R0Rq7d29LpGWWfR7ySf5mZB5",
        "default_place_id": [
None

],  # fallback
        "default_images": [
'https://drive.google.com/uc?export=view&id=1B-cB8nlzyWzWpSobN2NFm6oDdYa9RXCc', 'https://drive.google.com/uc?export=view&id=1X27oD9S1P3Uhtnuc2hM4nOoQ9GJ1itie', 'https://drive.google.com/uc?export=view&id=1jfFKB74fhd6XzFzdgqFProJqQ8iyFsqe', 'https://drive.google.com/uc?export=view&id=1tToyOSN-Dmldnfhf03f8eNgqrMauSmdu', 'https://drive.google.com/uc?export=view&id=1VGvv-Bgpp6Fhkxl8vsmuSS-keoaKScdF', 'https://drive.google.com/uc?export=view&id=18jr1hu_6tuBh4DFUxd9G5obxxRwNY9M0', 'https://drive.google.com/uc?export=view&id=1SjWOBLwhEX6VaheIwizWSIHqnktCqj61', 'https://drive.google.com/uc?export=view&id=1dMh8bcPRQKnBh-P0Zr2IizaTjMQ4Zmg6', 'https://drive.google.com/uc?export=view&id=115ujlY-7WbgdPvldWV1-o1RW95pRDnbs', 'https://drive.google.com/uc?export=view&id=1_s4_LQG9XdWGo0ybvYYWw9Inqaz2yx9l', 'https://drive.google.com/uc?export=view&id=1D63ZF4KJRxogKTB-jdZBZEGszbPqRa18', 'https://drive.google.com/uc?export=view&id=1vWlf0T22aZzHgx6NNeBa4X9pofiKhyjN', 'https://drive.google.com/uc?export=view&id=1EjviUESeKHj4bkMmLcmoL8m3_T1tICqt', 'https://drive.google.com/uc?export=view&id=1PRL3j7b51OsJHebVMe59aCHYi7DaCyLf', 'https://drive.google.com/uc?export=view&id=15Z7o2lE-UzLe38FEqUVs4cMUjV4rAZbQ', 'https://drive.google.com/uc?export=view&id=1Izy1RDfMfOFcm1farJ9_RkPA7Zm_fMlY', 'https://drive.google.com/uc?export=view&id=1ZPolNHIBFMWdmF4UFQ4lWZgdxuIllWx9', 'https://drive.google.com/uc?export=view&id=1nzrTUVl4rJWOT44zZbDpat1wtc-WtHeD', 'https://drive.google.com/uc?export=view&id=123AdgyvNjWicTQbRXvcecHhCFbRjxB6F', 'https://drive.google.com/uc?export=view&id=1ftJAnsrHj6eU5uj0qyrsppk7MDXVhNuV'

        ],
        "messages": [




#MESSAGE1
            {
                "text": '''
🎉🟢 Poslovite se od bolečin v sklepih s Steplexom! 🟢🎉
Vas boli koleno, rama ali hrbet? Niste sami – na tisoče ljudi je s tem naravnim gelom našlo olajšanje!

🌿 Steplex vsebuje mentol, ginko bilobo, divji kostanj in kapsaicin:
✅ Hladi in zmanjšuje vnetje
✅ Lajša okorelost sklepov
✅ Pomaga pri prostem gibanju
✅ Nežen do kože, ne povzroča draženja

📦 Naročite enostavno, plačajte samo ob prejemu.
👉 Kliknite tukaj in naročite zdaj: https://sites.google.com/view/steplexhb/home
💬 Ne odlašajte – občutite razliko že po prvi uporabi!
''',
    'place_id': [
#SLOVENIA
'103787872993257', #SLOVENIA
'110270608999206',#Ljubljana-Polje, Bohinj, Slovenia
'109443675747716', #Slovenj-Gradec
    ]
            },











#MESSAGE2
            {
                "text": '''
😫 Imate težave z jutranjim vstajanjem? Vas bolečine v sklepih ovirajo pri vsakodnevnih aktivnostih?
Tukaj je rešitev: Steplex – naravni gel za lajšanje bolečin, ki ga ljudje obožujejo!

🧴 Njegova edinstvena formula pomaga:
🌿 Zmanjšati vnetje
💪 Ponovna pridobitev gibljivosti sklepov
🧘‍♀️ Ponovno uživajte v gibanju brez bolečin

🛒 Enostavno naročanje – brez pologa, brez težav.
🚚 Hitra dostava po naročilu, plačilo ob dostavi!
👉 Prijavite se zdaj: https://sites.google.com/view/steplexhb/home
''',
    'place_id': [
#SLOVENIA
'103787872993257', #SLOVENIA
'110270608999206',#Ljubljana-Polje, Bohinj, Slovenia
'109443675747716', #Slovenj-Gradec
    ]
            },












#MESSAGE3
            {
                "text": '''
💚 Ste izgubili občutek svobode? Vas bolijo mišice?
Ne dovolite, da vam sklepi narekujejo življenje!
✨ Steplex bi lahko bil prelomnica.

✅ Naravne sestavine – brez stranskih učinkov
✅ Učinkovito proti obrabi, poškodbam in vnetjem, povezanim s starostjo
✅ Enostaven za uporabo, se hitro vpije

⚠️ Omejena zaloga – ne zamudite!
📞 Samo izpolnite naročilnico in poklicali vas bomo nazaj za potrditev
👉 Kliknite zdaj: https://sites.google.com/view/steplexhb/home
🎯 Izberite življenje brez bolečin – zdaj!
''',
    'place_id': [
#SLOVENIA
'103787872993257', #SLOVENIA
'110270608999206',#Ljubljana-Polje, Bohinj, Slovenia
'109443675747716', #Slovenj-Gradec
    ]
            }

]
            }











































,


        {
        "name": "STEPLEX-slovakia ",
        "page_id": "748985278291360",
        "user_access_token": "EAAPQiGeDh2QBPNTFZAu1qGEiGx10tNiroPOVIecGIdNhAi7Vpf4giWcD0Xb9G6834tlnBKv5AxgWBdftNEo9SIelJbtNrWZAxFhElndEpxxmRU7rNOPeZBPLPaKeAz0eAJQntxbGodLm41srmcxZCdZBy8aZAgdGPFua4u3R0Rq7d29LpGWWfR7ySf5mZB5",
        "default_place_id": [
None

],  # fallback
        "default_images": [
'https://drive.google.com/uc?export=view&id=1B-cB8nlzyWzWpSobN2NFm6oDdYa9RXCc', 'https://drive.google.com/uc?export=view&id=1X27oD9S1P3Uhtnuc2hM4nOoQ9GJ1itie', 'https://drive.google.com/uc?export=view&id=1jfFKB74fhd6XzFzdgqFProJqQ8iyFsqe', 'https://drive.google.com/uc?export=view&id=1tToyOSN-Dmldnfhf03f8eNgqrMauSmdu', 'https://drive.google.com/uc?export=view&id=1VGvv-Bgpp6Fhkxl8vsmuSS-keoaKScdF', 'https://drive.google.com/uc?export=view&id=18jr1hu_6tuBh4DFUxd9G5obxxRwNY9M0', 'https://drive.google.com/uc?export=view&id=1SjWOBLwhEX6VaheIwizWSIHqnktCqj61', 'https://drive.google.com/uc?export=view&id=1dMh8bcPRQKnBh-P0Zr2IizaTjMQ4Zmg6', 'https://drive.google.com/uc?export=view&id=115ujlY-7WbgdPvldWV1-o1RW95pRDnbs', 'https://drive.google.com/uc?export=view&id=1_s4_LQG9XdWGo0ybvYYWw9Inqaz2yx9l', 'https://drive.google.com/uc?export=view&id=1D63ZF4KJRxogKTB-jdZBZEGszbPqRa18', 'https://drive.google.com/uc?export=view&id=1vWlf0T22aZzHgx6NNeBa4X9pofiKhyjN', 'https://drive.google.com/uc?export=view&id=1EjviUESeKHj4bkMmLcmoL8m3_T1tICqt', 'https://drive.google.com/uc?export=view&id=1PRL3j7b51OsJHebVMe59aCHYi7DaCyLf', 'https://drive.google.com/uc?export=view&id=15Z7o2lE-UzLe38FEqUVs4cMUjV4rAZbQ', 'https://drive.google.com/uc?export=view&id=1Izy1RDfMfOFcm1farJ9_RkPA7Zm_fMlY', 'https://drive.google.com/uc?export=view&id=1ZPolNHIBFMWdmF4UFQ4lWZgdxuIllWx9', 'https://drive.google.com/uc?export=view&id=1nzrTUVl4rJWOT44zZbDpat1wtc-WtHeD', 'https://drive.google.com/uc?export=view&id=123AdgyvNjWicTQbRXvcecHhCFbRjxB6F', 'https://drive.google.com/uc?export=view&id=1ftJAnsrHj6eU5uj0qyrsppk7MDXVhNuV'

        ],
        "messages": [


#MESSAGE1
            {
                "text": '''
🎉🟢 Rozlúčte sa s bolesťami kĺbov so Steplexom! 🟢🎉
Bolí vás koleno, rameno alebo chrbát? Nie ste sami – tisíce ľudí našli úľavu s týmto prírodným gélom!

🌿 Steplex obsahuje mentol, ginkgo bilobu, pagaštan konský a kapsaicín:
✅ Chladí a znižuje zápal
✅ Zmierňuje stuhnutosť kĺbov
✅ Pomáha voľnejšiemu pohybu
✅ Jemný k pokožke, nespôsobuje podráždenie

📦 Objednajte si jednoducho, plaťte až pri prevzatí.
👉 Kliknite sem a objednajte si teraz: https://sites.google.com/view/steplexhb/home
💬 Neváhajte – pocíťte rozdiel už po prvom použití!
''',
    'place_id': [
#SLOVAKIA
'105547606144717', #SLOVAKIA
'110507998976900', #BRATISLAVA
'1108460275955885', #NITRA
    ]
            },














#MESSAGE2
            {
                "text": '''
😫 Máte problém ráno vstať? Bránia vám bolesti kĺbov v každodenných činnostiach?
Tu je riešenie: Steplex – prírodný gél na zmiernenie bolesti, ktorý ľudia milujú!

🧴 Jeho jedinečné zloženie pomáha:
🌿 Znížiť zápal
💪 Znovu získať flexibilitu kĺbov
🧘‍♀️ Znovu si užívať pohyb bez bolesti

🛒 Jednoduchá objednávka – bez zálohy, bez problémov.
🚚 Rýchle doručenie po objednaní, platba pri doručení!
👉 Požiadajte teraz: https://sites.google.com/view/steplexhb/home
''',
    'place_id': [
#SLOVAKIA
'105547606144717', #SLOVAKIA
'110507998976900', #BRATISLAVA
'1108460275955885', #NITRA
    ]
            },















#MESSAGE3
            {
                "text": '''
💚 Stratili ste pocit slobody? Žijete v bolestiach?
Nenechajte svoje kĺby diktovať vám, ako žijete!
✨ Steplex by mohol byť zlomovým bodom.

✅ Prírodné zložky – žiadne vedľajšie účinky
✅ Účinné proti opotrebovaniu, poškodeniu a zápalom súvisiacim s vekom
✅ Jednoduché použitie, rýchlo sa vstrebáva

⚠️ Obmedzené zásoby – nenechajte si to ujsť!
📞 Stačí vyplniť objednávkový formulár a my vám zavoláme späť pre potvrdenie
👉 Kliknite teraz: https://sites.google.com/view/steplexhb/home
🎯 Vyberte si život bez bolesti – teraz!
''',
    'place_id': [
#SLOVAKIA
'105547606144717', #SLOVAKIA
'110507998976900', #BRATISLAVA
'1108460275955885', #NITRA
    ]
            }]
            }





















































,


        {
        "name": "STEPLEX-portugal ",
        "page_id": "748985278291360",
        "user_access_token": "EAAPQiGeDh2QBPNTFZAu1qGEiGx10tNiroPOVIecGIdNhAi7Vpf4giWcD0Xb9G6834tlnBKv5AxgWBdftNEo9SIelJbtNrWZAxFhElndEpxxmRU7rNOPeZBPLPaKeAz0eAJQntxbGodLm41srmcxZCdZBy8aZAgdGPFua4u3R0Rq7d29LpGWWfR7ySf5mZB5",
        "default_place_id": [
None

],  # fallback
        "default_images": [
'https://drive.google.com/uc?export=view&id=1B-cB8nlzyWzWpSobN2NFm6oDdYa9RXCc', 'https://drive.google.com/uc?export=view&id=1X27oD9S1P3Uhtnuc2hM4nOoQ9GJ1itie', 'https://drive.google.com/uc?export=view&id=1jfFKB74fhd6XzFzdgqFProJqQ8iyFsqe', 'https://drive.google.com/uc?export=view&id=1tToyOSN-Dmldnfhf03f8eNgqrMauSmdu', 'https://drive.google.com/uc?export=view&id=1VGvv-Bgpp6Fhkxl8vsmuSS-keoaKScdF', 'https://drive.google.com/uc?export=view&id=18jr1hu_6tuBh4DFUxd9G5obxxRwNY9M0', 'https://drive.google.com/uc?export=view&id=1SjWOBLwhEX6VaheIwizWSIHqnktCqj61', 'https://drive.google.com/uc?export=view&id=1dMh8bcPRQKnBh-P0Zr2IizaTjMQ4Zmg6', 'https://drive.google.com/uc?export=view&id=115ujlY-7WbgdPvldWV1-o1RW95pRDnbs', 'https://drive.google.com/uc?export=view&id=1_s4_LQG9XdWGo0ybvYYWw9Inqaz2yx9l', 'https://drive.google.com/uc?export=view&id=1D63ZF4KJRxogKTB-jdZBZEGszbPqRa18', 'https://drive.google.com/uc?export=view&id=1vWlf0T22aZzHgx6NNeBa4X9pofiKhyjN', 'https://drive.google.com/uc?export=view&id=1EjviUESeKHj4bkMmLcmoL8m3_T1tICqt', 'https://drive.google.com/uc?export=view&id=1PRL3j7b51OsJHebVMe59aCHYi7DaCyLf', 'https://drive.google.com/uc?export=view&id=15Z7o2lE-UzLe38FEqUVs4cMUjV4rAZbQ', 'https://drive.google.com/uc?export=view&id=1Izy1RDfMfOFcm1farJ9_RkPA7Zm_fMlY', 'https://drive.google.com/uc?export=view&id=1ZPolNHIBFMWdmF4UFQ4lWZgdxuIllWx9', 'https://drive.google.com/uc?export=view&id=1nzrTUVl4rJWOT44zZbDpat1wtc-WtHeD', 'https://drive.google.com/uc?export=view&id=123AdgyvNjWicTQbRXvcecHhCFbRjxB6F', 'https://drive.google.com/uc?export=view&id=1ftJAnsrHj6eU5uj0qyrsppk7MDXVhNuV'

        ],
        "messages": [



#MESSAGE1
            {
                "text": '''
🎉🟢 Diga adeus às dores nas articulações com Steplex! 🟢🎉
Tem dores no joelho, ombro ou costas? Não está sozinho — milhares de pessoas encontraram alívio com este gel natural!

🌿 Steplex contém mentol, ginkgo biloba, castanha-da-índia e capsaicina:
✅ Refresca e reduz a inflamação
✅ Alivia a rigidez nas articulações
✅ Ajuda a movimentar-se com mais liberdade
✅ Suave para a pele, não causa irritação

📦 Encomende facilmente, pague apenas no ato da receção.
👉 Clique aqui e encomende já: https://sites.google.com/view/steplexhb/home
💬 Não perca tempo - sinta a diferença após a primeira utilização!
''',
    'place_id': [
#PORTUGAL
'104023262966156',
'110432202311659', #LISBON
'108177419217114', #PORTO
    ]
            },








#MESSAGE2
            {
                "text": '''
😫 Tem dificuldade em acordar de manhã? A dor nas articulações perturba as suas atividades diárias?
Eis a solução: Steplex – um gel natural para aliviar a dor que as pessoas adoram!

🧴 A sua fórmula exclusiva ajuda a:
🌿 Reduzir a inflamação
💪 Recuperar a flexibilidade das suas articulações
🧘‍♀️ Desfrute novamente de movimentos sem dor

🛒 Fácil de comprar – sem depósito, sem complicações.
🚚 Entrega rápida após encomenda, pagamento no ato da entrega!
👉 Inscreva-se já: https://sites.google.com/view/steplexhb/home
''',
    'place_id': [
#PORTUGAL
'104023262966156',
'110432202311659', #LISBON
'108177419217114', #PORTO
    ]
            },







#MESSAGE3
            {
                "text": '''
💚 Perdeu a sensação de liberdade? Vive com dor?

Não deixe que as suas articulações ditem a forma como vive!
✨ O Steplex pode ser o ponto de viragem.

✅ Ingredientes naturais – sem efeitos secundários
✅ Eficaz contra o desgaste, danos e inflamações relacionados com a idade
✅ Fácil de usar, rápida absorção

⚠️ Stock limitado – não perca!
📞 Basta preencher o formulário de encomenda e entraremos em contacto consigo para confirmar
👉 Clique já: https://sites.google.com/view/steplexhb/home
🎯 Escolha uma vida sem dor – agora!
''',
    'place_id': [
#PORTUGAL
'104023262966156',
'110432202311659', #LISBON
'108177419217114', #PORTO
    ]
            }
]
            }
























































,


        {
        "name": "STEPLEX-czech ",
        "page_id": "748985278291360",
        "user_access_token": "EAAPQiGeDh2QBPNTFZAu1qGEiGx10tNiroPOVIecGIdNhAi7Vpf4giWcD0Xb9G6834tlnBKv5AxgWBdftNEo9SIelJbtNrWZAxFhElndEpxxmRU7rNOPeZBPLPaKeAz0eAJQntxbGodLm41srmcxZCdZBy8aZAgdGPFua4u3R0Rq7d29LpGWWfR7ySf5mZB5",
        "default_place_id": [
None

],  # fallback
        "default_images": [
'https://drive.google.com/uc?export=view&id=1B-cB8nlzyWzWpSobN2NFm6oDdYa9RXCc', 'https://drive.google.com/uc?export=view&id=1X27oD9S1P3Uhtnuc2hM4nOoQ9GJ1itie', 'https://drive.google.com/uc?export=view&id=1jfFKB74fhd6XzFzdgqFProJqQ8iyFsqe', 'https://drive.google.com/uc?export=view&id=1tToyOSN-Dmldnfhf03f8eNgqrMauSmdu', 'https://drive.google.com/uc?export=view&id=1VGvv-Bgpp6Fhkxl8vsmuSS-keoaKScdF', 'https://drive.google.com/uc?export=view&id=18jr1hu_6tuBh4DFUxd9G5obxxRwNY9M0', 'https://drive.google.com/uc?export=view&id=1SjWOBLwhEX6VaheIwizWSIHqnktCqj61', 'https://drive.google.com/uc?export=view&id=1dMh8bcPRQKnBh-P0Zr2IizaTjMQ4Zmg6', 'https://drive.google.com/uc?export=view&id=115ujlY-7WbgdPvldWV1-o1RW95pRDnbs', 'https://drive.google.com/uc?export=view&id=1_s4_LQG9XdWGo0ybvYYWw9Inqaz2yx9l', 'https://drive.google.com/uc?export=view&id=1D63ZF4KJRxogKTB-jdZBZEGszbPqRa18', 'https://drive.google.com/uc?export=view&id=1vWlf0T22aZzHgx6NNeBa4X9pofiKhyjN', 'https://drive.google.com/uc?export=view&id=1EjviUESeKHj4bkMmLcmoL8m3_T1tICqt', 'https://drive.google.com/uc?export=view&id=1PRL3j7b51OsJHebVMe59aCHYi7DaCyLf', 'https://drive.google.com/uc?export=view&id=15Z7o2lE-UzLe38FEqUVs4cMUjV4rAZbQ', 'https://drive.google.com/uc?export=view&id=1Izy1RDfMfOFcm1farJ9_RkPA7Zm_fMlY', 'https://drive.google.com/uc?export=view&id=1ZPolNHIBFMWdmF4UFQ4lWZgdxuIllWx9', 'https://drive.google.com/uc?export=view&id=1nzrTUVl4rJWOT44zZbDpat1wtc-WtHeD', 'https://drive.google.com/uc?export=view&id=123AdgyvNjWicTQbRXvcecHhCFbRjxB6F', 'https://drive.google.com/uc?export=view&id=1ftJAnsrHj6eU5uj0qyrsppk7MDXVhNuV'

        ],
        "messages": [




#MESSAGE1
            {
                "text": '''
🎉🟢 Rozlučte se s bolestmi kloubů se Steplexem! 🟢🎉
Bolí vás koleno, rameno nebo záda? Nejste sami – tisíce lidí našly úlevu s tímto přírodním gelem!

🌿 Steplex obsahuje mentol, ginkgo bilobu, jírovec kaštan a kapsaicin:
✅ Chladí a snižuje zánět
✅ Ulevuje od ztuhlosti kloubů
✅ Pomáhá volnějšímu pohybu
✅ Jemný k pokožce, nezpůsobuje podráždění

📦 Objednejte si snadno, plaťte pouze při převzetí.
👉 Klikněte zde a objednejte si nyní: https://sites.google.com/view/steplexhb/home
💬 Neváhejte – pocítíte rozdíl již po prvním použití!
''',
    'place_id': [
#CZECH REPUBLIC
'111741685508471', #CZECH REPUBLIC
'110589025635590', #PRAGUE
'317532474961848', #PLZEN
    ]
            },















#MESSAGE2
            {
                "text": '''
😫 Máte potíže s ranním vstáváním? Brání vám bolest kloubů v každodenních činnostech?
Zde je řešení: Steplex – přírodní gel proti bolesti, který lidé milují!

🧴 Jeho unikátní složení pomáhá:
🌿 Snižovat záněty
💪 Znovu získat flexibilitu kloubů
🧘‍♀️ Znovu si užívat pohyb bez bolesti

🛒 Snadná objednávka – bez zálohy, bez starostí.
🚚 Rychlé doručení po objednání, platba při doručení!
👉 Přihlaste se nyní: https://sites.google.com/view/steplexhb/home
''',
    'place_id': [
#CZECH REPUBLIC
'111741685508471', #CZECH REPUBLIC
'110589025635590', #PRAGUE
'317532474961848', #PLZEN
    ]
            },














#MESSAGE3
            {
                "text": '''
💚 Ztratili jste pocit svobody? Žijete v bolestech?
Nenechte si klouby diktovat, jak budete žít!
✨ Steplex by mohl být zlomovým bodem.

✅ Přírodní složení – žádné vedlejší účinky
✅ Účinné proti opotřebení, poškození a zánětu souvisejícímu s věkem
✅ Snadné použití, rychle se vstřebává

⚠️ Omezené zásoby – nenechte si to ujít!
📞 Stačí vyplnit objednávkový formulář a my vám zavoláme zpět pro potvrzení
👉 Klikněte nyní: https://sites.google.com/view/steplexhb/home
🎯 Vyberte si život bez bolesti – hned teď!
''',
    'place_id': [
#CZECH REPUBLIC
'111741685508471', #CZECH REPUBLIC
'110589025635590', #PRAGUE
'317532474961848', #PLZEN
    ]
            }       
            
            
            
            
            
            ]
            }










































,


        {
        "name": "STEPLEX-italy ",
        "page_id": "748985278291360",
        "user_access_token": "EAAPQiGeDh2QBPNTFZAu1qGEiGx10tNiroPOVIecGIdNhAi7Vpf4giWcD0Xb9G6834tlnBKv5AxgWBdftNEo9SIelJbtNrWZAxFhElndEpxxmRU7rNOPeZBPLPaKeAz0eAJQntxbGodLm41srmcxZCdZBy8aZAgdGPFua4u3R0Rq7d29LpGWWfR7ySf5mZB5",
        "default_place_id": [
None

],  # fallback
        "default_images": [
'https://drive.google.com/uc?export=view&id=1B-cB8nlzyWzWpSobN2NFm6oDdYa9RXCc', 'https://drive.google.com/uc?export=view&id=1X27oD9S1P3Uhtnuc2hM4nOoQ9GJ1itie', 'https://drive.google.com/uc?export=view&id=1jfFKB74fhd6XzFzdgqFProJqQ8iyFsqe', 'https://drive.google.com/uc?export=view&id=1tToyOSN-Dmldnfhf03f8eNgqrMauSmdu', 'https://drive.google.com/uc?export=view&id=1VGvv-Bgpp6Fhkxl8vsmuSS-keoaKScdF', 'https://drive.google.com/uc?export=view&id=18jr1hu_6tuBh4DFUxd9G5obxxRwNY9M0', 'https://drive.google.com/uc?export=view&id=1SjWOBLwhEX6VaheIwizWSIHqnktCqj61', 'https://drive.google.com/uc?export=view&id=1dMh8bcPRQKnBh-P0Zr2IizaTjMQ4Zmg6', 'https://drive.google.com/uc?export=view&id=115ujlY-7WbgdPvldWV1-o1RW95pRDnbs', 'https://drive.google.com/uc?export=view&id=1_s4_LQG9XdWGo0ybvYYWw9Inqaz2yx9l', 'https://drive.google.com/uc?export=view&id=1D63ZF4KJRxogKTB-jdZBZEGszbPqRa18', 'https://drive.google.com/uc?export=view&id=1vWlf0T22aZzHgx6NNeBa4X9pofiKhyjN', 'https://drive.google.com/uc?export=view&id=1EjviUESeKHj4bkMmLcmoL8m3_T1tICqt', 'https://drive.google.com/uc?export=view&id=1PRL3j7b51OsJHebVMe59aCHYi7DaCyLf', 'https://drive.google.com/uc?export=view&id=15Z7o2lE-UzLe38FEqUVs4cMUjV4rAZbQ', 'https://drive.google.com/uc?export=view&id=1Izy1RDfMfOFcm1farJ9_RkPA7Zm_fMlY', 'https://drive.google.com/uc?export=view&id=1ZPolNHIBFMWdmF4UFQ4lWZgdxuIllWx9', 'https://drive.google.com/uc?export=view&id=1nzrTUVl4rJWOT44zZbDpat1wtc-WtHeD', 'https://drive.google.com/uc?export=view&id=123AdgyvNjWicTQbRXvcecHhCFbRjxB6F', 'https://drive.google.com/uc?export=view&id=1ftJAnsrHj6eU5uj0qyrsppk7MDXVhNuV'

        ],
        "messages": [




#MESSAGE1

            {
                "text": '''
🎉🟢 Di' addio ai dolori articolari con Steplex! 🟢🎉
Hai dolori al ginocchio, alla spalla o alla schiena? Non sei solo: migliaia di persone hanno trovato sollievo con questo gel naturale!

🌿 Steplex contiene mentolo, ginkgo biloba, ippocastano e capsaicina:
✅ Rinfresca e riduce l'infiammazione
✅ Allevia la rigidità articolare
✅ Aiuta a muoversi più liberamente
✅ Delicato sulla pelle, non provoca irritazioni

📦 Ordina facilmente, paga solo alla consegna.
👉 Clicca qui e ordina ora: https://sites.google.com/view/steplexhb/home
💬 Non aspettare: senti la differenza dopo il primo utilizzo!
''',
    'place_id': [
#ITALY
'115353315143936', #ROME
'100172604907328', #VENICE
'108581069173026', #MILAN
    ]
            },






#MESSAGE2

            {
                "text": '''
😫 Hai difficoltà ad alzarti la mattina? Il dolore alle articolazioni ostacola le tue attività quotidiane?
Ecco la soluzione: Steplex, un gel naturale antidolorifico amato da tutti!

🧴 La sua formula unica aiuta a:
🌿 Ridurre l'infiammazione
💪 Recuperare la flessibilità delle articolazioni
🧘‍♀️ Godetevi di nuovo movimenti senza dolore

🛒 Ordinare è facile: nessun acconto, nessuna seccatura.
🚚 Consegna rapida dopo l'ordine, pagamento alla consegna!
👉 Iscriviti ora: https://sites.google.com/view/steplexhb/home
''',
    'place_id': [
#ITALY
'115353315143936', #ROME
'100172604907328', #VENICE
'108581069173026', #MILAN
    ]
            },







#MESSAGE3
            {
                "text": '''
💚 Hai perso il senso di libertà? Vivi nel dolore?
Non lasciare che le tue articolazioni ti guidino nella vita!
✨ Steplex potrebbe essere la svolta.

✅ Ingredienti naturali - senza effetti collaterali
✅ Efficace contro l'usura, i danni e le infiammazioni legate all'età
✅ Facile da usare, si assorbe rapidamente

⚠️ Scorte limitate - non perderle!
📞 Compila il modulo d'ordine e ti contatteremo per confermare
👉 Clicca ora: https://sites.google.com/view/steplexhb/home
🎯 Scegli una vita senza dolore - ora!
''',
    'place_id': [
#ITALY
'115353315143936', #ROME
'100172604907328', #VENICE
'108581069173026', #MILAN
    ]
            }

]
            }































































,


        {
        "name": "STEPLEX-poland ",
        "page_id": "748985278291360",
        "user_access_token": "EAAPQiGeDh2QBPNTFZAu1qGEiGx10tNiroPOVIecGIdNhAi7Vpf4giWcD0Xb9G6834tlnBKv5AxgWBdftNEo9SIelJbtNrWZAxFhElndEpxxmRU7rNOPeZBPLPaKeAz0eAJQntxbGodLm41srmcxZCdZBy8aZAgdGPFua4u3R0Rq7d29LpGWWfR7ySf5mZB5",
        "default_place_id": [
None

],  # fallback
        "default_images": [
'https://drive.google.com/uc?export=view&id=1B-cB8nlzyWzWpSobN2NFm6oDdYa9RXCc', 'https://drive.google.com/uc?export=view&id=1X27oD9S1P3Uhtnuc2hM4nOoQ9GJ1itie', 'https://drive.google.com/uc?export=view&id=1jfFKB74fhd6XzFzdgqFProJqQ8iyFsqe', 'https://drive.google.com/uc?export=view&id=1tToyOSN-Dmldnfhf03f8eNgqrMauSmdu', 'https://drive.google.com/uc?export=view&id=1VGvv-Bgpp6Fhkxl8vsmuSS-keoaKScdF', 'https://drive.google.com/uc?export=view&id=18jr1hu_6tuBh4DFUxd9G5obxxRwNY9M0', 'https://drive.google.com/uc?export=view&id=1SjWOBLwhEX6VaheIwizWSIHqnktCqj61', 'https://drive.google.com/uc?export=view&id=1dMh8bcPRQKnBh-P0Zr2IizaTjMQ4Zmg6', 'https://drive.google.com/uc?export=view&id=115ujlY-7WbgdPvldWV1-o1RW95pRDnbs', 'https://drive.google.com/uc?export=view&id=1_s4_LQG9XdWGo0ybvYYWw9Inqaz2yx9l', 'https://drive.google.com/uc?export=view&id=1D63ZF4KJRxogKTB-jdZBZEGszbPqRa18', 'https://drive.google.com/uc?export=view&id=1vWlf0T22aZzHgx6NNeBa4X9pofiKhyjN', 'https://drive.google.com/uc?export=view&id=1EjviUESeKHj4bkMmLcmoL8m3_T1tICqt', 'https://drive.google.com/uc?export=view&id=1PRL3j7b51OsJHebVMe59aCHYi7DaCyLf', 'https://drive.google.com/uc?export=view&id=15Z7o2lE-UzLe38FEqUVs4cMUjV4rAZbQ', 'https://drive.google.com/uc?export=view&id=1Izy1RDfMfOFcm1farJ9_RkPA7Zm_fMlY', 'https://drive.google.com/uc?export=view&id=1ZPolNHIBFMWdmF4UFQ4lWZgdxuIllWx9', 'https://drive.google.com/uc?export=view&id=1nzrTUVl4rJWOT44zZbDpat1wtc-WtHeD', 'https://drive.google.com/uc?export=view&id=123AdgyvNjWicTQbRXvcecHhCFbRjxB6F', 'https://drive.google.com/uc?export=view&id=1ftJAnsrHj6eU5uj0qyrsppk7MDXVhNuV'

        ],
        "messages": [

#MESSAGE1
            {
                "text": '''
🎉🟢 Pożegnaj się z bólem stawów dzięki Steplex! 🟢🎉
Czy masz ból kolana, ramienia lub pleców? Nie jesteś sam — tysiące osób znalazło ulgę dzięki temu naturalnemu żelowi!

🌿 Steplex zawiera mentol, miłorząb japoński, kasztanowiec i kapsaicynę:
✅ Chłodzi i zmniejsza stany zapalne
✅ Łagodzi sztywność stawów
✅ Pomaga poruszać się swobodniej
✅ Delikatny dla skóry, nie powoduje podrażnień

📦 Zamów łatwo, zapłać tylko przy odbiorze.
👉 Kliknij tutaj i zamów teraz: https://sites.google.com/view/steplexhb/home
💬 Nie zwlekaj — poczuj różnicę już po pierwszym użyciu!
''',
    'place_id': [
#PLOAND
'498943763778785', #WARSAW
'136077853136063', #Olsztyn, Poland
'1231914186933910', #Gdańsk, Poland
    ]
            },
















#MESSAGE2
            {
                "text": '''
😫 Masz problemy ze wstawaniem rano? Ból stawów utrudnia Ci codzienne czynności?
Oto rozwiązanie: Steplex – naturalny żel przeciwbólowy, który ludzie uwielbiają!

🧴 Jego unikalna formuła pomaga:
🌿 Zmniejszyć stan zapalny
💪 Odzyskać elastyczność stawów
🧘‍♀️ Ponownie cieszyć się bezbolesnym ruchem

🛒 Łatwe zamawianie – bez depozytu, bez kłopotów.
🚚 Szybka dostawa po zamówieniu, płatność przy odbiorze!
👉 Złóż wniosek już teraz: https://sites.google.com/view/steplexhb/home
''',
    'place_id': [
#PLOAND
'498943763778785', #WARSAW
'136077853136063', #Olsztyn, Poland
'1231914186933910', #Gdańsk, Poland
    ]
            },




















#MESSAGE3
            {
                "text": '''
💚 Utraciłeś poczucie wolności? Żyjesz w bólu?
Nie pozwól, aby Twoje stawy dyktowały Ci, jak żyjesz!

✨ Steplex może być punktem zwrotnym.

✅ Naturalne składniki – brak skutków ubocznych
✅ Skuteczny w walce z oznakami starzenia, uszkodzeniami i stanami zapalnymi
✅ Łatwy w użyciu, szybko się wchłania

⚠️ Ograniczona liczba sztuk – nie przegap!

📞 Wystarczy wypełnić formularz zamówienia, a my oddzwonimy, aby potwierdzić zamówienie
👉 Kliknij teraz: https://sites.google.com/view/steplexhb/home
🎯 Wybierz życie bez bólu – już teraz!
''',
    'place_id': [
#PLOAND
'498943763778785', #WARSAW
'136077853136063', #Olsztyn, Poland
'1231914186933910', #Gdańsk, Poland
    ]
            }

]
            }










































            ,


        {
        "name": "STEPLEX-spain ",
        "page_id": "748985278291360",
        "user_access_token": "EAAPQiGeDh2QBPNTFZAu1qGEiGx10tNiroPOVIecGIdNhAi7Vpf4giWcD0Xb9G6834tlnBKv5AxgWBdftNEo9SIelJbtNrWZAxFhElndEpxxmRU7rNOPeZBPLPaKeAz0eAJQntxbGodLm41srmcxZCdZBy8aZAgdGPFua4u3R0Rq7d29LpGWWfR7ySf5mZB5",
        "default_place_id": [
None

],  # fallback
        "default_images": [
'https://drive.google.com/uc?export=view&id=1B-cB8nlzyWzWpSobN2NFm6oDdYa9RXCc', 'https://drive.google.com/uc?export=view&id=1X27oD9S1P3Uhtnuc2hM4nOoQ9GJ1itie', 'https://drive.google.com/uc?export=view&id=1jfFKB74fhd6XzFzdgqFProJqQ8iyFsqe', 'https://drive.google.com/uc?export=view&id=1tToyOSN-Dmldnfhf03f8eNgqrMauSmdu', 'https://drive.google.com/uc?export=view&id=1VGvv-Bgpp6Fhkxl8vsmuSS-keoaKScdF', 'https://drive.google.com/uc?export=view&id=18jr1hu_6tuBh4DFUxd9G5obxxRwNY9M0', 'https://drive.google.com/uc?export=view&id=1SjWOBLwhEX6VaheIwizWSIHqnktCqj61', 'https://drive.google.com/uc?export=view&id=1dMh8bcPRQKnBh-P0Zr2IizaTjMQ4Zmg6', 'https://drive.google.com/uc?export=view&id=115ujlY-7WbgdPvldWV1-o1RW95pRDnbs', 'https://drive.google.com/uc?export=view&id=1_s4_LQG9XdWGo0ybvYYWw9Inqaz2yx9l', 'https://drive.google.com/uc?export=view&id=1D63ZF4KJRxogKTB-jdZBZEGszbPqRa18', 'https://drive.google.com/uc?export=view&id=1vWlf0T22aZzHgx6NNeBa4X9pofiKhyjN', 'https://drive.google.com/uc?export=view&id=1EjviUESeKHj4bkMmLcmoL8m3_T1tICqt', 'https://drive.google.com/uc?export=view&id=1PRL3j7b51OsJHebVMe59aCHYi7DaCyLf', 'https://drive.google.com/uc?export=view&id=15Z7o2lE-UzLe38FEqUVs4cMUjV4rAZbQ', 'https://drive.google.com/uc?export=view&id=1Izy1RDfMfOFcm1farJ9_RkPA7Zm_fMlY', 'https://drive.google.com/uc?export=view&id=1ZPolNHIBFMWdmF4UFQ4lWZgdxuIllWx9', 'https://drive.google.com/uc?export=view&id=1nzrTUVl4rJWOT44zZbDpat1wtc-WtHeD', 'https://drive.google.com/uc?export=view&id=123AdgyvNjWicTQbRXvcecHhCFbRjxB6F', 'https://drive.google.com/uc?export=view&id=1ftJAnsrHj6eU5uj0qyrsppk7MDXVhNuV'

        ],
        "messages": [


#MESSAGE1
            {
                "text": '''
¡Dile adiós al dolor articular con Steplex!

¿Tienes dolor de rodilla, hombro o espalda? ¡No estás solo/a! Miles de personas han encontrado alivio con este gel natural.


Stemplex contiene mentol, ginkgo biloba, castaño de Indias y capsaicina:
✅ Refresca y reduce la inflamación
✅ Alivia la rigidez articular
✅ Facilita la movilidad
✅ Suave con la piel, no causa irritación

Pídelo fácilmente y paga solo al recibirlo.

Haz clic aquí y pide ahora: https://sites.google.com/view/steplexhb/home

¡No esperes más y siente la diferencia desde el primer uso!
''',
'place_id':[        #SPAIN
'197582646953514', '106287062743373', '112812522066039',
]  
                },







#MESSAGE2
                {
                "text": '''
¿Te cuesta levantarte por la mañana? ¿El dolor articular te dificulta las actividades diarias?
Aquí tienes la solución: Steplex: ¡un gel analgésico natural que encanta!


Su fórmula única ayuda a:
Reducir la inflamación
Recuperar la flexibilidad de las articulaciones
Volver a disfrutar de movimientos sin dolor

Pedir es fácil: sin depósito ni complicaciones

Entrega rápida tras el pedido y pago contra reembolso

Solicita ahora: https://sites.google.com/view/steplexhb/home
''',
'place_id':[        #SPAIN
'197582646953514', '106287062743373', '112812522066039',
]  
                },






#MESSAGE3
                {
                "text": '''
¿Has perdido la libertad? ¿Vives con dolor?
¡No dejes que tus articulaciones dicten tu vida!
✨ Steplex podría ser el punto de inflexión.

✅ Ingredientes naturales: sin efectos secundarios
✅ Eficaz contra el desgaste, los daños y la inflamación relacionados con la edad
✅ Fácil de usar, de rápida absorción

⚠️ ¡Existencias limitadas! ¡No te lo pierdas!
📞 Solo completa el formulario de pedido y te llamaremos para confirmar.
👉 Haz clic ahora: https://sites.google.com/view/steplexhb/home
🎯 ¡Elige una vida sin dolor ahora!
''',
'place_id':[        #SPAIN
'197582646953514', '106287062743373', '112812522066039',
]  
                }

]
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
