import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content("""
{
**Task**: Identify the correct category from the provided guidelines for the received customer message.

**Context**: You will receive messages from customers that ask about various issues related to the services offered by StarNet. Your sole purpose is to categorize the message based on the specific question types in the provided JSON guidelines. Each key represents a different service or issue that the customer may inquire about, they keys themselves were categorized in tehnical and comercial types.

**Rules**:
1. Act as an expert in identifying categories.
2. Focus solely on the message content to match it with the appropriate category from the guidelines.
3. Respond ONLY with the corresponding JSON key that matches the customer message.
4. Do not provide additional explanations, comments, or details—only the key that categorizes the message correctly.
5. Use proper grammar in processing messages, as there may be minor errors.
6. Always prioritize accuracy and ensure that the selected category key aligns with the message intent.  
  "guidelines":{
{
    "script_support": {
        "INFORMAȚIE COMERCIALĂ": {
            "INFORMAȚIE_COMERCIALĂ_EXISTENTĂ": "Profitați de oferta noastră specială: planuri mari la prețuri mici! Alegeți dintre abonamentele noastre avantajoase, toate cu reducere. Bucurați-vă de internet rapid, televiziune HD și minute gratuite. Detalii complete: https://promo.starnet.md/ro *Condiții:** Promoția este valabilă pentru clienții noi și existenți, cu contract activ, și nu se cumulează cu alte oferte.",
            "CABINET_PERSONAL": "Accesează-ți contul personal aici: https://my.starnet.md/. Folosește ID-ul din contract și resetează parola dacă este necesar.",
            "CONTROL_PARENTAL": "Activează sau dezactivează controlul parental în cabinetul personal: Alte servicii > Control parental. Pentru detalii, accesează https://www.starnet.md/news/optiunea-control-parental-serviciu-gratuit-starnet/ sau sună la (022) 844-555.",
            "STELE DE FIDELITATE": {
                "Cum te înscrii?": "Înregistrează-te pe my.starnet.md, folosește datele din contract și completează chestionarul. Primești 500 de stele la înscriere.",
                "Cum acumulezi stele?": "Află cum să câștigi mai multe stele: plăți în avans, ziua de naștere, invitarea prietenilor. Detalii: https://www.starnet.md/prietenii-starnet-2/"
            },
            "STAR SHOP": "Comenzile StarShop se livrează în maxim 30 de zile. Vei fi contactat când comanda este gata.",
            "A UITAT PAROLA": "Resetează-ți parola folosind ID-ul și adresa de e-mail. Vei primi instrucțiuni pe e-mail.",
            "REZILIERE": {
                "PESTE HOTAR": "Trimite o cerere scrisă și semnată, împreună cu o copie a buletinului/pașaportului, la adresa de e-mail a oficiului tău.",
                "ÎN ȚARĂ": "Vizitează un oficiu StarNet cu buletinul de identitate."
            },
            "SISTARE": {
                "PESTE HOTAR": "Trimite o cerere de sistare scrisă și semnată, împreună cu o copie a buletinului/pașaportului, la adresa de e-mail a oficiului tău. Indică perioada dorită de sistare (până la 60 de zile).",
                "ÎN ȚARĂ": "Vizitează un oficiu StarNet cu buletinul de identitate și indică perioada dorită de sistare (până la 60 de zile)."
            },
            "SCHIMB DE ADRESĂ": {
                "PESTE HOTAR": "Trimite o cerere de schimb de adresă scrisă și semnată, împreună cu o copie a buletinului/pașaportului, la adresa de e-mail a oficiului tău. Indică adresa nouă și datele persoanei responsabile.",
                "ÎN ȚARĂ": "Vizitează un oficiu StarNet cu buletinul de identitate și indică adresa nouă."
            },
            "SCHIMB DE TITULAR": "Vizitează un oficiu StarNet cu buletinul de identitate al ambilor titulari pentru a efectua schimbul.",
            "WI-FI PUBLIC": {
                "CLIENT NOU": "Procurați un abonament StarBox Eco sau StarBox Guest pentru a conecta la Wi-Fi public StarNet.",
                "CLIENT EXISTENT": "Folosiți datele din contract pentru a conecta la Wi-Fi public StarNet."
            },
            "YOUTUBE": "Ne pare rău pentru blocajul YouTube. Echipa noastră lucrează pentru a rezolva problema. Vă mulțumim pentru înțelegere.",
            "MODALITĂȚI DE ACHITARE": "Plățiți prin bancă, centre StarNet, terminale, online banking sau pe site-ul StarNet.",
            "ACHITARE ERONATĂ": "Trimiteți o cerere cu ID-ul corect, ID-ul eronat și detaliile plății.",
            "SCHIMB DE ABONAMENT": "Vizitează un oficiu StarNet pentru a modifica abonamentul tău. Poți vedea lista de abonamente aici: https://www.starnet.md/pachete-3-servicii-3/."
        },
        "DERANJAMENT TEHNIC": {
            "AVARIERE": "Înțelegem că întâmpinați o problemă cu serviciile noastre. Echipa noastră tehnică lucrează deja la rezolvarea avariei în zona dumneavoastră. Vă mulțumim pentru răbdare.",
            "A UITAT PAROLA": "Resetați parola accesând contul dumneavoastră și urmând instrucțiunile. Veți primi un e-mail cu pașii necesari. Parola nouă trebuie să conțină minim 8 caractere, cu majuscule și cifre.",
            "VERIFICAREA PREZENȚEI CLIENTULUI PE CHAT": "Suntem încă aici pentru a vă ajuta. Dacă nu veți mai trimite mesaje, chat-ul se va închide în 10 minute.",
            "ÎNCHEIERE": "Ne bucurăm că am putut fi de ajutor. Dacă aveți alte întrebări, nu ezitați să ne contactați.",
            "CONCRETIZAREA LIPSEI ALTOR ÎNTREBĂRI": "Dacă aveți nevoie de asistență suplimentară, suntem aici pentru dumneavoastră.",
            "SOLICITĂRII DE ANGAJARE": "Pentru a aplica pentru un job la StarNet, accesați https://www.starnet.md/pozitii_vacante/ și trimiteți CV-ul la hr@starnet.md.",
            "ESCROCHERIE": "Ignorați orice mesaj care vă solicită informații confidențiale. Informații oficiale despre campanii și concursuri găsiți pe https://www.starnet.md/.",
            "INFO": "Pentru a rezolva problema, vă rugăm să ne furnizați următoarele informații: [Lista detaliilor necesare]. Puteți efectua un test de viteză aici: http://calitate.starnet.md/. Dacă problema persistă, contactați serviciul de asistență tehnică.",
            "VERIFICĂRI": "Vom avea nevoie de câteva detalii pentru a vă ajuta. Vă rugăm să ne furnizați: [Lista detaliilor necesare].",
            "LUCRARE PLANIFICATĂ": "Suntem conștienți de lucrările planificate în zona dumneavoastră. Echipa noastră depune toate eforturile pentru a finaliza lucrările cât mai repede posibil.",
            "SCHIMB DENUMIRE/PAROLA WI-FI": "Pentru a schimba numele sau parola rețelei Wi-Fi, accesați contul dumneavoastră și urmați instrucțiunile sau consultați acest ghid: https://www.starnet.md/wp-content/uploads/2018/09/ghid.pdf.",
            "ACCES PE ROUTER": "Din motive de securitate, accesul la router este restricționat. Pentru a schimba setările Wi-Fi, accesați contul dumneavoastră sau contactați serviciul de asistență tehnică."
    }
}
}
      
"user_question":"care ii  nahui parola la huineaua asta prost ce esti"
}

""")
print(response.text)