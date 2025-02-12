<!--
Gewerbepark: @Gewerbepark.withStyle("width: 100%; height: 600px; border: 0; overflow: hidden;")
Gewerbepark.withStyle: <iframe src="[https://github.com/Bigfire3/DBI-Postdienst/blob/main/Img/Gewerbepark%20Deutsches%20Brennstoffinstitut.html](https://github.com/Bigfire3/DBI-Postdienst/blob/336a074e3e228249a36e6fa2edbdd9fbfbaaf8b8/Img/Gewerbepark%20Deutsches%20Brennstoffinstitut.html)" style=@0></iframe>

-->


# Machbarkeitsstudie zur Automatisierung des Postdienstes auf dem Gelände der DBI

<!--"Karte DBI inklusive ansässiger Firmen"-->
<img src="../Img/Uebersicht-DBI.jpeg" width="900" height="600">


---


## 1. Planung

### Methodik

**Zu erreichende Ziele:**

* Postverteilung analysieren
* Wege kartieren und kritische Stellen analysieren
* Feedback von Mitarbeitenden sammeln

---

**Angewante Methoden:**

1. Interview mit den Verantwortlichen/Mitarbeitenden:

    * Was ist machbar und in welchem Umfang ist eine Übernahme des Postdienstes erwünscht 

    * Klärung von Rahmenbedingungen für späteres Mapping

    * Ausräumen von Fragen und Unstimmigkeiten

2. Aufnahme von Daten über das Gebiet mittels OSM:

    * Überblick über Ist-Stand erhalten

    * Konkretes Wissen wo Anpassung nötig ist 

    * Planbarkeit für weiteres Vorgehen

## 2. Datensammlung

### Interviews 

**Aktueller Prozess:**

* feste Öffnungszeiten (9:30 Uhr bis 10:15 Uhr) zur Paketabholung und Abgabe
* 25-30 Briefe und 5-25 Pakete pro Monat versendet
* 15-40 Pakete pro Monat angekommen
* größere Paktete meistens direkt an Firmen geliefert
* manche Pakete haben hohe Priorität 

---

**Ursprünglicher Plan:**

* Post wird an Poststelle angenommen und sortiert
* Roboter wird von Hand beladen
* fährt Post autonom zum Ziel
* Angstellter entnimmt Ladung 
* Roboter kehrt zur Poststelle zurück  

---

**Änderungen:**

* Roboter kann nicht von Hand beladen werden (zu Zeitaufwenig)

    * Automatisierte Beladung des Roboters
    * unklar in Umsetztbarkeit 

* Mitarbeiter können nicht auf Roboter warten (ineffizient)

    * Abladeboxen vor jeder Firma nötig 
    * Roboter entlädt Post in jeweilige Box 
    * Automatischer Verschluss (Diebstahlschutz)

---

**Frage der autonomen Lieferbarkeit muss durch OMS Daten erfolgen**

### Dateneingabe in OMS

**Randbedingungen für den Roboter:**

* Befahrbarkeit der Strecke (Qualität der Straße)
* Absätze, Treppen oder andere nicht überfahrbare Hindernisse 
* Abschnitte die nicht befahren werden dürfen
* Gefahr durch andere Verkehrsteilnehmer 
* Erreichbarkeit der Firmeneingänge und Kartierung dieser

---

**Aufgenommene Daten:**

* Genaue Position der Eingänge 
* Zugänglichkeit der Eingänge und eventuelle Hindernisse wie Zäune 

    -> Eintragung dieser Daten in OSM und festhalten durch Bilder
<!-- "Bordstein am Eingang des Teilobjektes 7a (unten)." -->
<img src="../Img/Zugang-Teilobjekt-7a-unten.jpg" width="800" height="800">

## 3. Datenauswertung

**Auswertung der in OSM eingetragenen Daten mittels bereitgestellten Python Packages**

Erstellung von Grafiken mit OSMnx zur Visalisierung und Auswertung der Daten.

`import: https://github.com/Bigfire3/DBI-Postdienst/edit/main/LiaScript/presentation.md`
```
@Gewerbepark

```
@Gewerbepark

<!-- "Kürzeste Routen zu allen Eingängen" -->
<img src="../Img/Routing_to_all_entrances.png" width="800" height="800">

* Routing zu allen neu gemappten Eingängen 

---
<!-- "Kürzeste Routen zu allen erreichbaren Eingängen" -->
<img src="../Img/Routing_to_all_accesible_entrances.png" width="800" height="800">

* kürzesten Wege von Poststation zu allen barrierefreien Eingängen
* insgesamte Weglänge: 1702 Meter

---
<!--"Kürzeste Routen zu den bereits Verfügbaren Eingängen" -->
<img src="../Img/Optimized_TSP.png" width="800" height="800">

* kürzeste Route mit allen Eingängen 
* Weglänge: 1483 Meter
* Benötigte Zeit (mit 6 km/h): 15 Minuten

---
<!--"Erreichbarkeit in 30s Abständen von der Poststelle"-->
<img src="../Img/isochrones.png" width="800" height="800">

## 4. Resultat

### Haupterkenntnisse


### Fazit


## Vielen Dank für Ihre Aufmerksamkeit!

Haben Sie Fragen?
