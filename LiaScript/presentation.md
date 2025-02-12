
# Machbarkeitsstudie zur Automatisierung des Postdienstes auf dem Gelände der DBI


<img src="../Img/Uebersicht-DBI.jpeg" width="900" height="600">


---


## 1. Planung

<figure>
   <h3 style="color: black; font-size: 20px;text-align: center;">Ausarbeiten der Methoden zum Vorgehen</h3>
    <img src="https://architektur-wispler.de/wp-content/uploads/2014/09/Planung.jpg" width="800" height="800">
    
</figure>

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

<figure>
   <h3 style="color: black; font-size: 20px;text-align: center;">Ausarbeiten der Methoden zum Vorgehen</h3>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/OSM_Logo.svg/1200px-OSM_Logo.svg.png" width="800" height="800">
    
</figure>

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


<figure>
   <h3 style="color: black; font-size: 20px;text-align: center;">Kürzeste Routen zu allen Eingängen</h3>
    <img src="../Img/Routing_to_all_entrances.png" width="800" height="800">
    
</figure>


* Routing zu allen neu gemappten Eingängen 

---

<figure>
   <h3 style="color: black; font-size: 20px;text-align: center;">Kürzeste Routen zu allen erreichbaren Eingängen</h3>
    <img src="../Img/Routing_to_all_accesible_entrances.png" width="800" height="800">
</figure>


* kürzesten Wege von Poststation zu allen barrierefreien Eingängen
* insgesamte Weglänge: 1702 Meter

---

<figure>
   <h3 style="color: black; font-size: 20px;text-align: center;">Kürzeste Route über alle erreichbaren Eingängen</h3>
    <img src="../Img/Optimized_TSP.png" width="800" height="800">
    
</figure>


* kürzeste Route mit allen barrierefreien Eingängen 
* Weglänge: 1483 Meter
* Benötigte Zeit (mit 6 km/h): 15 Minuten

---

<figure>
   <h3 style="color: black; font-size: 20px;text-align: center;">Erreichbarkeit in 30s Abständen von der Poststelle</h3>
    <img src="../Img/isochrones.png" width="800" height="800">
    
</figure>

## 4. Resultat

### Haupterkenntnisse


### Fazit


## Vielen Dank für Ihre Aufmerksamkeit!

Haben Sie Fragen?
