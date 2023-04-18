# Analiza navad spanja

Na podlagi podatkov pridobljenih iz mobilne aplikacije [Alarmy](https://play.google.com/store/apps/etails?id=droom.sleepIfUCan&hl=en&gl=US), nameravam odkriti, analizirati ter napovedovati lastne navade spanca.



## Opis problema

Med prvim koronskim lockdownom sem si zaradi vedno slabšega spanca naložil aplikacijo, ki naj bi pomagala pri prebujanju ter vzdrževanju zdravih navad spanja. Kmalu po njeni namestitvi sem opazil, da se v aplikaciji shranjujejo podatki o izklopljenih budilkah, kar me je spodbudilo k njeni uporabi. Po treh letih rabe aplikacije, imam nakopičeno že kar veliko količino podatkov o mojem prebujanju, iz katerih želim izvedeti, kaj največ vpliva na moje spanje, ter kako bi lahko le to izboljšal.



## Pridobivanje podatkov

Podatki so v [aplikaciji](https://play.google.com/store/apps/details?id=droom.sleepIfUCan&hl=en&gl=US) shranjeni v obliki preprostega menija. Screenshotal sem vse [podmenije](https://github.com/MitxSte/PR23MS/tree/main/podatki/screens) (določeni z letom in mesecem) in pridobljene slike preimenoval v pravilni vrstni red. Prvi podatki so bili zabeleženi 26. marca 2020, zadnji upoštevani podatki pa 31. januarja 2023.

Primer screenshota:

![Podatki za marec 2020](https://github.com/MitxSte/PR23MS/blob/main/podatki/downsized/rsz_121.jpg "Podatki za marec 2020")


### Pretvorba podatkov

Sledila je pretvorba zaslonskih skik v uporabne podatke. Za to sem uporabil python knjižnice cv2, pytesseract in PIL. Z napisano [skripto](https://github.com/MitxSte/PR23MS/blob/main/scripts/branjeSlik.py) sem prebrane podatke filtriral, veljavne vnose pa zapisal v ločeno [datoteko](https://github.com/MitxSte/PR23MS/blob/main/podatki/test.txt).

Ugotovil sem, da sem od 26. marca 2020 do 31. januarja 2023 (1042 dni) ugasnil kar 3812 budilk, pri branju slik pa je do napak prišlo pri 82, torej jih lahko za analizo uporabim 3730. Ker sem torej za prebujanje uporabil v povprečju 3.57 budilk na dan, bom za številne analize upošteval le zadnje ugašnjene budilke dneva (recimo da je prva budilka zvonila ob 6:30, druga ob 6:45, tretja pa 7:00 - seveda bom za analizo prebujanja upošteval le budilko ob 7:00, saj so očitno bile prvi dve v nalogi prebujanja neuspešne). Za analizo tovrstnih navad, za katere bo potrebno Upoštevati le zadnjo budilko dneva, je za analizo ostalo 893 le teh. Seveda pa bom lahko za ugotavljanje številnih navad uporabil tudi ostale budilke, npr. koliko časa potrebujem za prebujanje (čas od prve budilke do zadnje).


## Dosedanje ugotovitve in analize

Za lažjo predstavo podatkov sem le te najprej vizualiziral s številnimi grafi.

### Graf vseh zadnjih dnevnih budilk

![Graf vseh zadnjih dnevnih budilk](https://github.com/MitxSte/PR23MS/blob/main/slike_prikaz/vsi%20podatki.PNG "Graf vseh zadnjih dnevnih budilk")

### Graf vseh budilk ob pričetku šolskega leta 2020/21

V grafu se zelo očitno razbere pričetek novega šolskega leta, prav tako se lepo razloči vikende.

![Graf vseh budilk ob pričetku šolskega leta 2020/21](https://github.com/MitxSte/PR23MS/blob/main/slike_prikaz/2020_konec_poletja.PNG "Graf vseh budilk ob pričetku šolskega leta 2020/21")


## Analiza povprečnih mesečnih časov prebujanj

