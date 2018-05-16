# BakalarskaPraca
Kognitivna narocnost uloh sutaze iBobor

Prácu som písala na Univerzite Komenského v Bratislave, Fakulte Matematiky, Fyziky a Informatiky pod vedením Mgr. Karolíny Mayerovej PhD.

Abstrakt
Na Slovensku prebieha už 10 rokov medzinárodná informatická súťaž iBobor, ktorá spracúva rôzne informatické koncepty a rozvíja zručnosti u žiakov na základných a stredných školách. Každý rok tak získavame veľké množstvo dát (60-70 000 súťažiacich), ktoré ponúkajú množstvo informácií, ktoré však nie sú dostatočne analyzované. Jednou z oblastí, ktorá stále nie je doriešená, je zaraďovanie úloh do kategórií podľa obťažnosti. Cieľom práce je oboznámiť sa s doterajším vývojom tejto problematiky, novou obsahovou kategorizáciou úloh a s využitím dát od súťažiacich (úspešnosť, pohlavie, odpovede, ročník, ...) a nástrojov data miningu (dolovania dát), teda algoritmov rozhodovacích stromov, zautomatizovať určovanie obťažnosti úloh.  Využijeme na to voľne dostupný program RapidMiner, v ktorom otestujeme základný algoritmus na učenie rozhodovacích stromov ID3 a algoritmus CHAID. Ako vstupné dáta použijeme klasifikované úlohy s atribútmi z novej kategorizácie úloh, ktoré predstavujú vzťahy medzi dvoma konjunkciami odvodenými z atribútov(stĺpcov) tabuľky analyzovaných dát.  

Kľúčové slová: kognitívna náročnosť, rozhodovacie stromy, datamining, ID3, CHAID

Tento repozitár obsahuje:
celú prácu vo formáte .pdf :bakalarka.pdf \n
proces modelovania rozhodovacieho stromu pre algorimty ID3 a CHAID aj s určením presnosti predikcie Rozhodovací_stromCHAID.rmp , Rozhodovací_stromID3.rmp \n
program na výpočet entropie, informačného zisku a podielu zisku v jazyku python informationGain.py \n
kompletná trénovacia množina dát z rokov 2012-2018 v tabuľke .xls VstupneData.xls \n
tabuľka popisujúca všetky klasifikované úlohy a porovnanie náročností odhadovaných, reálnych a predikovaných rozhodovacím stromom Porovnanie narocnosti.xls \n
