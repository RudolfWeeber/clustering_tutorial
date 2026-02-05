# Workshop: Perkolation und Cluster-Labeling

---

---

## Übung 1: Zufällige Belegung generieren

Datei: `01-random_occupancy/gen_occupancy.py`

* Vervollständigen Sie die Funktion `gen_random_occupancy(shape, prob, rng)` (Zeilen 34-38)
    * Erzeugen Sie mit `rng.random(shape)` ein 2D-Array aus Zufallszahlen zwischen 0 und 1
    * Vergleichen Sie jedes Element mit `prob`, um ein Boolean-Array zu erhalten
* Unten im Skript, berechnen Sie mittels `np.sum()` welcher Anteil der Gitterplätze tatsächlich besetst ist (Zeilen 48-49)
* Im Mittel sollte ein Anteil `prob` der Elemente `True` sein
* Testen Sie mit `python gen_occupancy.py`
* Wenn sie es mehrfach aufrufen: warum sind nicht immer gleich viele Gitterpunkte belegt?

---

## Übung 2: Erster Durchgang (Pass 1)

Datei: `02-pass1/pass1.py`

* Der Hoshen-Kopelman Algorithmus durchläuft das Gitter zeilenweise von links nach rechts
* Für jeden besetzten Punkt werden die Nachbarn oben (`up`) und links (`left`) betrachtet
* Vervollständigen Sie die Logik in der `pass1`-Funktion (Zeilen 46-58):

---

## Übung 2: Pass 1 - Logik

* **Fall 1**: Beide Nachbarn unbesetzt (= 0)
  * Neuer Cluster gefunden → mit `next_label` beschriften, `next_label` erhöhen
* **Fall 2**: Nur ein Nachbar besetzt
  * Label des besetzten Nachbarn übernehmen
* **Fall 3**: Beide Nachbarn besetzt
  * Gleiches Label → dieses übernehmen
  * Verschiedene Labels → Label von oben übernehmen, Paar `(up, left)` zu `to_be_merged` hinzufügen

---

## Cluster zusammenführen

* Annahme: im 1. Durchgang wurden folgende Label vergeben: 1, 2, 3, 4, 5, 6, 7
* Außerdem wurde festgestellt, dass sich folgende Cluster treffen:  (1, 2), (2, 3), (2, 4), (5, 6),(3,7)

Auf einem Blatt Papier:

1. Verteilen Sie die Label 1..7 über das Blatt
2. Zeichnen Sie Verbindungen zwischen den Label ein, wenn sich die Cluster getroffen haben, z.B. zwischen 2 und 4 und zwischen 5 un 6. Zeichnen Sie einen Pfeil von der größeren zur kleineren Zahl
3. Wie können Sie jetzt für jedes Cluster aus verbundenen Labels eindeutig ein representatives Label bestimmen?




---


## Übung 3: Labels ersetzen

Datei: `03-replace_labels/replace_labels.py`

* Vervollständigen Sie die Funktion `replace_labels(old_labels, replace_by)` (Zeilen 32-38)
* Iterieren Sie über alle Elemente von `old_labels`
* Prüfen Sie für jeden Eintrag, ob ein Ersatz im Dictionary `replace_by` existiert
* Falls ja, tragen Sie den Ersatzwert in `new_labels` ein, sonst den ursprünglichen
* Beispiel: `replace_by={3: 1, 5: 4}` ersetzt 3→1 und 5→4
* Testen Sie mit `python replace_labels.py`

---

## Übung 4: Perkolation prüfen

Datei: `04-percolate/percolate.py`

* Vervollständigen Sie die Funktion `percolates_lr(labels_lattice)` (Zeilen 26-36)
* Ein Cluster perkoliert von links nach rechts, wenn dasselbe Label am linken **und** rechten Rand vorkommt
* Erzeugen Sie die Mengen `left` und `right` mit den Labels an den Rändern:
  * Nutzen Sie `set()` und `np.unique()` mit einer Slice
* Prüfen Sie, ob die Schnittmenge (ohne 0) nicht leer ist

---

## Übung 5: Labels umnummerieren

Datei: `05-renumber_clusters/renumber_labels.py`

* Nach dem Zusammenführen von Clustern können Lücken in der Nummerierung entstehen (z.B. 1, 2, 4 statt 1, 2, 3)
* Vervollständigen Sie die Funktion `_get_replacements(unique_labels)` (Zeilen 25-29):
  * Erzeugen Sie eine Liste mit neuen Labels von 1 bis N (Anzahl der unique Labels)
  * Erstellen Sie mittels Dictionary Comprehension ein Dictionary `replacements`, das vom alten auf das neue Label abbildet
  * Beispiel: `unique_labels = (1, 2, 4)` → `replacements = {1: 1, 2: 2, 4: 3}`
* Testen Sie mit `python renumber_labels.py`

---

## Hinweise zu NumPy

* `rng.random(shape)` erzeugt Zufallszahlen zwischen 0 und 1
* Vergleichsoperatoren auf Arrays: `arr < 0.5` ergibt Boolean-Array
* `np.unique(arr)` gibt eindeutige Werte zurück
* `set(arr)` erzeugt eine Python-Menge
* `menge.discard(wert)` schmeißt dne Wert aus der Menge
* Mengen-Schnittmenge: `set_a & set_b` oder `set_a.intersection(set_b)`


