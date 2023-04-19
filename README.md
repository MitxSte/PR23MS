# Analiza navad spanja

Na podlagi podatkov pridobljenih iz mobilne aplikacije [Alarmy](https://play.google.com/store/apps/etails?id=droom.sleepIfUCan&hl=en&gl=US), nameravam odkriti, analizirati ter napovedovati lastne navade spanca.



## Opis problema

Med prvim koronskim lockdownom sem si zaradi vedno slabšega spanca naložil aplikacijo, ki naj bi pomagala pri prebujanju ter vzdrževanju zdravih navad spanja. Kmalu po njeni namestitvi sem opazil, da se v aplikaciji shranjujejo podatki o izklopljenih budilkah, kar me je spodbudilo k njeni uporabi. Po treh letih rabe aplikacije, imam nakopičeno že kar veliko količino podatkov o mojem prebujanju, iz katerih želim izvedeti, kaj največ vpliva na moje spanje, ter kako bi lahko le to izboljšal.



## Pridobivanje podatkov

Podatki so v [aplikaciji](https://play.google.com/store/apps/details?id=droom.sleepIfUCan&hl=en&gl=US) shranjeni v obliki preprostega menija. Screenshotal sem vse [podmenije](https://github.com/MitxSte/PR23MS/tree/main/podatki/screens). Prvi podatki so bili zabeleženi 26. marca 2020, zadnji upoštevani podatki pa 31. januarja 2023.

Primer screenshota:

![Podatki za marec 2020](https://github.com/MitxSte/PR23MS/blob/main/podatki/downsized/rsz_121.jpg "Podatki za marec 2020")


### Pretvorba podatkov

Sledila je pretvorba zaslonskih slik v uporabne podatke. Najprej sem slike pravilno obrezal, tako da so se posamezne budilke pojavile le enrat, ter tako tudi pomanjšal pogostost napak pri OCR. Nato sem napisal [skripto](https://github.com/MitxSte/PR23MS/blob/main/scripts/branjeSlik.py), v kateri sem za OCR uporabil python knjižnice cv2, pytesseract in PIL. Skripta vse slike "prebere", prebrane podatke filtrira (izloči neveljavne), veljavne vnose pa zapiše v ločeno [datoteko](https://github.com/MitxSte/PR23MS/blob/main/podatki/test.txt).

### Opis podatkov

Ugotovil sem, da sem od 26. marca 2020, do 31. januarja 2023 (1042 dni), ugasnil kar 3812 budilk, pri branju slik pa je do napak prišlo pri 82, torej jih lahko za analizo uporabim 3730. Ker sem torej za prebujanje uporabil v povprečju nekaj manj kot 4 budilke na dan, bom za številne analize moral podatke dodatno urediti. Če bi  želel analizirati npr. uro vstajanja, bi kot podatke seveda upošteval le zadnje ugašnjene budilke dneva (recimo da je prva budilka zvonila ob 6:30, druga ob 6:45, tretja pa 7:00 - upošteval bi le budilko ob 7:00, saj so očitno bile prvi dve v nalogi prebujanja neuspešne). Za omenjeno filtriranje podatkov sem napisal [funkcijo filter_alarms_zadnji_v_dnevu](https://github.com/MitxSte/PR23MS/blob/main/scripts/prva_s.py). Po filtriranju je ostalo še 893 budilk (kar tudi pomeni, da v skoraj 3 letih nisem imel vklopljene budilke le 149 dni). 

Seveda pa bom lahko za ugotavljanje številnih navad uporabil tudi celotne podatke (ne le zadnje budilke dneva), npr. koliko časa potrebujem za prebujanje (čas od prve budilke do zadnje), koliko budilk potrebujem, da se prebudim med tednom in koliko med vikendom ipd.


## Dosedanje ugotovitve in analize

Za lažjo predstavo podatkov sem le te najprej vizualiziral s številnimi grafi.

### Graf vseh zadnjih dnevnih budilk

![Graf vseh zadnjih dnevnih budilk](https://github.com/MitxSte/PR23MS/blob/main/slike_prikaz/vsi%20podatki.PNG "Graf vseh zadnjih dnevnih budilk")

### Graf vseh budilk ob pričetku šolskega leta 2020/21

V grafu se zelo očitno razbere pričetek novega šolskega leta, prav tako se lepo razloči vikende.

![Graf vseh budilk ob pričetku šolskega leta 2020/21](https://github.com/MitxSte/PR23MS/blob/main/slike_prikaz/2020_konec_poletja.PNG "Graf vseh budilk ob pričetku šolskega leta 2020/21")


## Analiza povprečnih mesečnih časov prebujanj

Zanimalo me je, ob kateri uri se v povprečju prebujam na različne mesece. Predvideval sem, da bodo ure prebujanja opazno poznejše med poletnimi meseci, rezultati pa so me kar pošteno presenetili. 

```
January: 10:19
February: 10:18
March: 10:07
April: 10:09
May: 09:42
June: 09:40
July: 10:31
August: 10:11
September: 10:08
October: 09:41
November: 09:35
December: 10:30
```

Pričakoval sem, da bodo povprečja "šolskih" mesecev precej nižja, po hitrem pomisleku pa so rezultati zelo smiselni. Od marca 2020 (pričetka beleženja poodatkov) smo namreč šolanje v srednji šoli opravili večinoma na daljavo, na faksu pa je bilo zgodnje prebujanje redko potrebno zahvaljujoč fleksibilnim urnikov. Za podatke beležene po srednji šoli se je namreč zgodilo ravno obratno od pričakovanega, povprečno prebujanje med poletjem je bilo opazno bolj zgodnje zaradi službe.

## Nadaljevanje
V nadaljevanju nameravam podatke dodatno opredeliti (letni časi, stresna obdobja (izpiti, matura, ...),...), ter na njih izvedeti številne zanimive analize.
