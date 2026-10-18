# Aufgabe:
#
# Lies von zwei Personen jeweils Vor- und Nachnamen sowie das Geburtsjahr ein.
# Achte zunächst darauf, dass die zuerst eingegebene Person älter ist.
# Gib aus, um wie viel Jahre die erste Person älter ist als die Zweite. 
# Ausgabe mit Vor- und Nachnamen von beiden Personen
#
# Wir lesen die Daten der ersten Person ein
#
# Wir verwenden zum Unterscheiden eine Zahl als 1. und 2.
#
nummer = 1
#
p1Vorname  = input("Gib den Vornamen der " + str(nummer) + ". Person ein: ")
p1Nachname = input("gin den Nachnamen der " + str(nummer) + ". Person ein: ") 
p1Alter    = int(input("Gib das Geburtsjahr von " + p1Vorname + " " + p1Nachname + " ein: "))
#
# Wir lesen die Daten der zweiten Person ein
#
# gleichzeitig erhöhen wir den Inhalt der Variablen nummer um 1
nummer = nummer + 1
#
p2Vorname  = input("Gib den Vornamen der " + str(nummer) + ". Person ein: ")
p2Nachname = input("Gib den Nachnamen der " + str(nummer) + ". Person ein: ") 
p2Alter    = int(input("Gib das Geburtsjahr von " + p2Vorname + " " + p2Nachname + " ein: "))
#
# Wir berechnen die Altersdifferenz
#
differenz = p2Alter - p1Alter
#
# Wir setzen unsere Ausgabe zusammen
ausgabe = p1Vorname + " " + p1Nachname + " ist " + str(differenz) + " Jahre "
ausgabe = ausgabe + "älter als " + p2Vorname + " " + p2Nachname
#
# und geben sie aus
#
print(ausgabe)
