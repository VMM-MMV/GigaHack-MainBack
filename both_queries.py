
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
suport_script="""
{
    "script_support": {
        "INFORMAȚIE_COMERCIALĂ_EXISTENTĂ": "Oferta actuală la serviciile StarNet include: prețuri mici pentru planuri mari! Am pregătit cele mai avantajoase abonamente, toate cu reducere. Conectează-te acum și bucură-te de o experiență digitală unică: internet cu super viteză, televiziune interactivă în format HD și telefonie IP cu 1200 de minute gratuite. Mai multe detalii pot fi vizualizate aici: https://promo.starnet.md/ro. *Condițiile ofertei: Promoția este valabilă pentru clienții noi și existenți, cu termen minim contractual executat, care vor semna/resemna, și nu este compatibilă cu alte oferte active.",
        "CABINET_PERSONAL": "Pentru a intra în Cabinetul personal, accesați acest link: https://my.starnet.md/. ID personal (este indicat în contract și în factura Dvs), dar dacă nu cunoașteți parola, o puteți activa utilizând comanda „Restabilește parola”, Login: ID: E-mail:",
        "CONTROL_PARENTAL": "Pentru a activa sau dezactiva controlul parental, este necesar să accesați: cabinet personal >> alte servicii >> control parental >> selectați categoria >> „Salvează”. Pentru mai multe detalii, accesați link-ul https://www.starnet.md/news/optiunea-control-parental-serviciu-gratuit-starnet/ sau telefonați Serviciul Asistență Tehnică (persoane fizice) Tel: (022) 844-555.",
        "STELE DE FIDELITATE": {
            "Cum te înscrii în sistemul de fidelitate?": "Pentru a beneficia de programul de fidelitate, este necesar să te înregistrezi în program. ---Accesează my.starnet.md ---Conectează-te cu loginul și parola din contractul pe care l-ai primit la conectare ---Completează chestionarul de înscriere și obține primele 500 de stele.",
            "Cum acumulezi suplimentar stele de fidelitate?":  "---Când achiți în avans abonamentul pentru 1 an, primești 1000 stele cadou ---La ziua ta de naștere, îți oferim 200 de stele ---Invită un prieten la StarNet și obține stele în valoarea abonamentului acestuia (conform tarifului contractual) SAU Pentru mai multe detalii, accesați link-ul: https://www.starnet.md/prietenii-starnet-2/. Înscrieți-vă la programul de loialitate 'Prieteni StarNet'  https://www.starnet.md/prietenii-starnet-2/. Accesând cabinetul personal >> compartimentul MY STARNET >> PRIETENII STARNET >> Apoi puteți începe să colectați puncte de loialitate! Acest program se bazează pe sistemul de acumulare a punctelor de loialitate. Numărul de stele de fidelitate depinde de plata la timp a facturii, valoarea pachetului și de timpul petrecut în rețeaua StarNet. Puteți folosi loialitatea acestor stele pentru: 1. Reîncărcarea contului StarNet prin convertirea stelelor de fidelitate: Accesând cabinetul personal, accesați compartimentul MY STARNET >> PRIETENII STARNET >> CATALOG SERVICII. După, accesați coșul și confirmați cumpărarea. Convertirea este posibilă: 500/1000/2000 stele de fidelitate echivalent cu 50/100/200 lei. 2. Accesorii StarNet (Gadgeturi, multimedia etc.): Accesați site-ul companiei: https://www.starnet.md/ru/ >> compartimentul StarShop accesând linkul https://www.starnet.md/starshop/ >> Selectați produsul >> Adăugare produs în coș >> Vă logați în cabinetul personal (ID/parola) >> accesați coșul >> completați Detalii facturare >> la adresă indicați V. Pircalab (toate comenzile sunt primite la această adresă, apoi direcționate la centrul StarNet unde sunteți deservit) >> Plasați comanda."
        },
        "STAR SHOP": "În cazul în care comanda StarShop a fost plasată cu succes, termenul de a primi comanda este de până la 30 de zile. Managerul personal va reveni cu un apel preventiv când comanda este la oficiul care Vă deservește și poate fi ridicată. Vă mulțumim pentru colaborare.",
        "A UITAT PAROLA DE LA CABINETUL PERSONAL": "Este necesar să utilizați comanda „Ai uitat parola?” și să introduceți următoarele date pentru reactivare: ID: Login: E-mail: După introducerea datelor de mai sus, veți recepționa un mesaj pe adresa de e-mail. Accesați mesajul și continuați prin „apasați aici pentru a continua”. Urmează să se deschidă 2 câmpuri. Indicați parola nouă și confirmarea acesteia. Parola necesită să conțină minim 8 caractere, o literă mare, o literă mică și cifre.",
        "REZILIERE": {
            "PESTE HOTARE": "Este necesar ca titularul contractului să scrie o cerere de reziliere către adresa de e-mail a oficiului din sectorul care vă deservește: ------------------------@starnet.md. 1. Cererea de reziliere în formă liberă trebuie să fie scrisă de mână și semnată. 2. Cererea trebuie să fie scanată sau fotografiată. 3. Fotografiați sau scanați buletinul de identitate MD sau pașaportul MD (semnăturile de pe cerere și actul de identitate trebuie să coincidă). Managerul personal va reveni cu detalii conform solicitării Dvs.",
            "ÎN ȚARĂ": "Este necesar ca titularul contractului să se apropie cu un act de identitate (buletin, pașaport, permis de conducere) la oficiile StarNet și să depună cererea de reziliere."
        },
        "SISTARE": {
            "PESTE HOTARE": "În cazul în care titularul este peste hotare, este necesar ca titularul contractului să scrie o cerere de sistare către adresa de e-mail a oficiului din sectorul care vă deservește. 1. Cererea de sistare în formă liberă trebuie să fie scrisă de mână și semnată. Indicați pe ce perioadă doriți sistarea serviciilor, de la data/lună până la data/lună (până la 60 de zile). 2. Cererea trebuie să fie scanată sau fotografiată. 3. Fotografiați sau scanați buletinul de identitate sau pașaportul (semnăturile de pe cerere și actul de identitate trebuie să coincidă).",
            "ÎN ȚARĂ": "În cazul în care solicitați sistarea, este necesar să indicați: - ID personal - perioada exactă de sistare, de la (data/lună) până la (data/lună). Sistarea poate fi de până la 60 de zile. - numărul Dvs de contact. Managerul personal va reveni cu detalii. *** Sistarea serviciilor este posibilă pe termen de 60 de zile într-un an calendaristic. Sistarea este posibilă pe 7-30 zile, cu un cost de 40 lei pentru internet+tv. *** Vă rugăm să concretați un număr de contact. ------------ Solicitarea Dvs a fost preluată și expediată către managerul personal. În cel mai scurt timp, managerul va reveni cu detalii."
        },
        "SCHIMB DE ADRESĂ":"Pentru schimbul de adresă este necesar să indicați: - ID personal - adresa nouă, pentru a verifica aria de acoperire - numărul Dvs de contact. Toate modificările pot fi efectuate doar de către titularul contractului. Managerul personal va reveni cu detalii. În cazul în care titularul este peste hotare, este necesar ca titularul contractului să scrie o cerere de schimb de adresă către adresa de e-mail a oficiului din sectorul care vă deservește. 1. Cererea de schimb de adresă în formă liberă trebuie să fie scrisă de mână și semnată. Indicați în cerere: - adresa nouă - numele/prenumele persoanei responsabile care va fi la domiciliu în timp ce se va efectua schimbul de adresă - numărul de contact al persoanei responsabile. 2. Cererea trebuie să fie scanată sau fotografiată. 3. Fotografiați sau scanați buletinul de identitate sau pașaportul (semnăturile de pe cerere și actul de identitate trebuie să coincidă).",
        "SCHIMB DE TITULAR": "Pentru a efectua schimbul de titular, este necesar ca titularul existent și noul titular să se prezinte în Centrul de Vânzări care vă deservește, amândoi cu buletinul de identitate. Pe loc se vor efectua toate modificările, iar managerul personal va oferi toate informațiile conform solicitării.",
        "WI-FI PUBLIC": {
            "CLIENT NOU": "În cazul în care nu dețineți servicii StarNet, iar la adresa Dvs. beneficiați de Wi-Fi public StarNet, pentru conectare urmați pașii de mai jos: - accesați rețeaua StarNet Wi-Fi pe dispozitiv - după conectare, se va deschide portalul de conectare - utilizați butonul „Client Nou” - procurați un abonament StarBox Eco sau StarBox Guest - achitarea se efectuează doar prin card bancar - viteza va fi de până la 10 Mbps/sec. - durata unei sesiuni este de 3 ore - conexiunea este valabilă doar pentru un singur dispozitiv.",
            "CLIENT EXISTENT": "În cazul în care dețineți servicii StarNet, iar la adresa Dvs. beneficiați de Wi-Fi public StarNet, pentru conectare urmați pașii de mai jos: - accesați rețeaua StarNet Wi-Fi pe dispozitiv - după conectare, se va deschide portalul de conectare - utilizați butonul „Client Existent” - utilizați datele conform contractului: ID/Login - viteza va fi de până la 10 Mbps/sec. *** În cazul în care la ecranul dispozitivului Dvs. nu este indicat client nou/client existent, înseamnă că nu dispuneți de Wi-Fi public StarNet, ci accesați rețeaua personală a unui client StarNet (Wi-Fi public este disponibil doar în unele parcuri din Chișinău)."
        },
        "YOUTUBE": "Ne pare rău de situația actuală, dar în acest moment există anumite blocaje din partea companiei YouTube. Se negociază cu furnizorul, iar echipa responsabilă face tot posibilul pentru a soluționa situația cât mai curând. Așteptăm un răspuns din partea companiei YouTube. Vă mulțumim pentru înțelegere. SAU Aplicațiile instalate pe Set Top Box: YouTube, ivi, megogo etc. sunt prestate de furnizori. Vă informăm că există anumite blocaje din partea furnizorului de servicii YouTube și așteptăm un răspuns din partea lor. Pentru mai multe detalii, accesați link-ul: https://www.starnet.md/news/aplicatia-youtube-nu-mai-este-disponibila-pentru-mai-multe-dispozitive/. Vă mulțumim pentru înțelegere.",
        "MODALITĂȚI DE ACHITARE": "Plățile pot fi efectuate prin modalitățile cunoscute: --- ghișeele băncilor și bancomatelor (Energbank, EuroCreditBank, Eximbank, Victoriabank, Mobiasbanca, Moldova Agroindbank, Fincombank, Moldindconbank), --- centrele de vânzări StarNet, --- terminale de plăți electronice, servicii de online banking și online payment. --- online, direct de pe site-ul StarNet https://pay.starnet.md, utilizând cardul bancar Visa sau MasterCard (inclusiv Visa Electron și Maestro).",
        "ACHITARE ERONATĂ": "În cazul în care ați efectuat o achitare eronată, este necesar să indicați: * ID corect: * ID eronat: * indicați primele 4 cifre și ultimele 4 cifre ale cardului cu care a fost efectuată achitarea * prezentați confirmarea plății foto/screen pentru a expedia solicitarea Dvs. echipei responsabile.",
        "SCHIMB DE ABONAMENT":"Pentru modificarea abonamentului (adăugare/excludere TV), este necesar să vă apropiați de oficiile StarNet, iar managerii vor oferi mai multe detalii. Între timp, puteți vizualiza lista de abonamente aici: https://www.starnet.md/pachete-3-servicii-3/ sau oferta actuală aici: https://promo.starnet.md/ro.",
        "AVARIERE": "Vă mulțumim pentru sesizare. Ne pare rău că vă confruntați cu această situație. Vă rugăm să ne acordați câteva momente pentru a verifica. În prezent, este înregistrată o avariere în sectorul Dvs., dar primiți asigurările noastre că echipa tehnică se ocupă deja de remediere. Ne cerem scuze pentru inconveniențele create.",
        "VERIFICAREA PREZENȚEI CLIENTULUI PE CHAT": "Mai sunteți cu noi? În caz de inactivitate, chat-ul va fi încheiat în 10 minute. Sunteți online? În caz de inactivitate, chat-ul va fi încheiat în 10 minute.",
        "ÎNCHEIERE": "Vă mulțumim pentru adresarea Dvs. Echipa StarNet vă urează o zi reușită! Vă mulțumim pentru adresarea Dvs. Echipa StarNet vă urează o seară frumoasă!",
        "CONCRETIZAREA LIPSEI ALTOR ÎNTREBĂRI / DERANJAMENTE": "Dacă vă mai putem ajuta cu ceva, vă rugăm să nu ezitați să ne scrieți sau să ne contactați. Dacă considerați că vă putem ajuta cu ceva, vă rugăm să nu ezitați să ne scrieți.",
        "SOLICITĂRII DE ANGAJARE": "Bună ziua! Dacă doriți să faceți parte din echipa StarNet, accesați link-ul: https://www.starnet.md/pozitii_vacante/ pentru a analiza pozițiile vacante. Expediți CV-ul Dvs. către Departamentul Resurse Umane pe adresa hr@starnet.md, specificând postul.",
        "ESCROCHERIE": "Vă mulțumim pentru sesizare. Vă rugăm să ignorați astfel de informații/mesaje. Toate informațiile privind campaniile și concursurile pot fi vizualizate pe pagina oficială StarNet: https://www.starnet.md/.",
        "INFO": "O clipă, vă rog, să verificăm. Indicați, vă rog, cine este titularul contractului. Telecomanda poate fi procurată de la oficiile StarNet. Prețul minim al telecomenzii este 100 lei, iar telecomanda de model mai nou costă 150 lei. Vă sugerăm să apelați preventiv oficiul StarNet pentru a vă asigura că telecomenzile sunt în stoc. Au fost efectuate verificări și modificări. Este necesar: - să accesați internetul prin cablu și să efectuați un test de viteză conform linkului http://calitate.starnet.md/. Rezultatul testului să fie expediat aici (screen/poza) - verificați funcționalitatea canalelor TV. În cazul în care situația Dvs. se repetă, apelați Serviciul Asistență Tehnică (persoane fizice) la (022) 844-555 sau support@starnet.md pentru a verifica în momentul actual și a nu întreprinde măsuri individuale.",
        "VERIFICĂRI": "Vă rugăm să ne acordați câteva momente pentru a verifica. O să vă rog să ne oferiți mai multe detalii referitoare la: ID: Login: [Date tehnice de care au nevoie colegii din suport tehnic].",
        "LUCRARE PLANIFICATĂ": "Din datele pe care le deținem în acest moment, în sectorul Dvs. sunt înregistrate lucrări planificate, dar primiți asigurările noastre că echipa tehnică se ocupă deja de remediere. Ne cerem scuze pentru inconveniențele create.",
        "SCHIMB DENUMIRE/PAROLA WI-FI": "În cazul în care solicitați schimbarea denumirii/parolei Wi-Fi, va fi necesar să urmați pașii: accesați cabinetul personal >> alte servicii >> Wi-Fi >> schimbă parola / denumirea rețelei. Apare SSID și efectuați modificările sau puteți vizualiza instrucțiuni detaliate aici: https://www.starnet.md/wp-content/uploads/2018/09/ghid.pdf.",
        "ACCES PE ROUTER": "Din motive de confidențialitate, clienții nu dețin acces pe router. În cazul în care solicitați schimbarea denumirii/parolei Wi-Fi, aveți posibilitatea să le efectuați prin accesarea cabinetului personal >> alte servicii >> Wi-Fi >> schimbă parola sau schimbă denumirea rețelei. Apare SSID și efectuați modificările sau apelați Serviciul Asistență Tehnică (persoane fizice) la (022) 844-555 sau support@starnet.md.",
        "VITEZA INTERNET": "Pentru a verifica viteza internetului, va rog accesati: https://www.speedtest.net/, si apsati pe butonul mare din mijloc"
    }
}
"""
pre_prompt = """
You are senior customer support professional. You will be given a question from a Moldovian user,
who will ask the question using 'Moldovian'(Romanian with moldovan dialect, with some latinized russian),
which will also have poor grammar. Sometimes even writen in cirilic instead of latin.
Your job is to classify that question, according to one of the given templates, to which the values are the Support professional's response to the user. Respond in such a manner {"Class": <found_class>}
If the users question cannot be clearly atributed to one of the classes, put it as DONT KNOW.
"""

# pre_prompt = """
# Task: Translate Moldavian text to proper Romanian

# Context: As a senior customer support professional, you'll receive questions from Moldavian users written in a mix of Romanian with Moldavian dialect, Latinized Russian, and potentially poor grammar. Some parts might be written in Cyrillic instead of Latin script.

# Guidelines:

# Act as an expert translator familiar with both Moldavian and standard Romanian.
# Pay attention to the unique characteristics of Moldavian speech, including dialect-specific words and phrases.
# Be prepared to handle mixed-language input, particularly Latinized Russian terms.
# Correct grammatical errors while maintaining the original meaning.
# Convert any Cyrillic text to Latin script if necessary.
# Provide a polished, error-free translation in standard Romanian.
# Ensure the translation captures the nuances and intent of the original message.
# Handle idiomatic expressions and colloquialisms appropriately.
# Maintain a neutral, professional tone in the translation.
# Deliver the translated text without any additional commentary or explanations.
# Format the output as a single block of text, preserving paragraph structure where applicable.
# Be consistent in spelling and punctuation throughout the translation.
# Please proceed with translating the Moldavian text into proper Romanian.
# Do not include the script_suport reference templates in your response
# """

# prompt = "Wa brat cum pula di si nahui nu arata NTV"
# prompt = "Cum nahui schimb nnumele la cacatu ista care huawei ZXC90 BLYATI"
# prompt = " ваи, еу вреу са лукрез ла вои"
# prompt = "wai brat eu am ramas fara abricosi, pidarii vostri io furat"
# prompt = " Mersi, am rezolvat problema, tot normal, spasiba"
# prompt = " Bai eu vreuu wifi di aista public caroci cum nafig fac"
prompt = " bai abonamentu ista ii fignea polnaia da ceva mai bun"
response = model.generate_content(pre_prompt + "Response template: " + suport_script + "\nThe question: " + prompt)
print(response.text)