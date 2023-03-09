# Analiza navad spanja

Na podlagi podatkov pridobljenih iz mobilne aplikacije [Alarmy](https://play.google.com/store/apps/details?id=droom.sleepIfUCan&hl=en&gl=US), nameravam odkriti, analizirati ter napovedovati lastne navade spanca.



## Opis problema

Med prvim koronskim lockdownom sem si zaradi vedno slabšega spanca naložil aplikacijo, ki naj bi pomagala pri prebujanju ter vzdrževanju zdravih navad spanja. Kmalu po njeni namestitvi sem opazil, da se v aplikaciji shranjujejo podatki o izklopljenih budilkah, kar me je spodbudilo k njeni uporabi. Po treh letih rabe aplikacije, imam nakopičeno že kar veliko količino podatkov o mojem prebujanju, iz katerih želim izvedeti, kaj največ vpliva na moje spanje, ter kako bi lahko le to izboljšal.



## Cilji in vprašanja

Nekaj vprašanj na katera nameravam odgovoriti v projektu so:

- Kako se moje navade spanca razvijajo s časom
- Kaj najbolj vpliva na moj spanec (obveznosti, letni časi, stres, ...)
- Koliko časa potrebujem, da se prebudim
- Lahko za določeno obdobje napovem svoje navade spanca
- So moje navade spanca relativno običajne
- ...



## Vir in oblika podatkov

Podatki so v [aplikaciji](https://play.google.com/store/apps/details?id=droom.sleepIfUCan&hl=en&gl=US) shranjeni v obliki preprostega menija. Screenshotal sem vse [podmenije](https://github.com/MitxSte/PR23MS/tree/main/podatki/screens) (določeni z letom in mesecem) in pridobljene slike preimenoval v pravilni vrstni red. Prvi podatki so bili zabeleženi 26. marca 2020, zato nameravam kot zadnji vir uporabiti podatke 26. marca 2023.

Primer screenshota:

![Podatki za marec 2020](https://github.com/MitxSte/PR23MS/blob/main/podatki/downsized/rsz_121.jpg "Podatki za marec 2020")



## Dodatne možnosti

Ker imam žal le podatke o prebujanju in ne tudi o začetku spanca, bo nemogoče analizirati npr. količino spanja in podobne koristne informacije. Potrebne (a nepopolne) podatke bi pa za to lahko pridobil iz spletne aplikacije [Last.fm](https://www.last.fm/home), s katero sem septembra 2022 začel beležiti poslušano glasbo. Predvidevam, da bi lahko npr. ura zadnje poslušane glasbe napovedovala približen čas, kdaj se zbudim naslednji dan.
