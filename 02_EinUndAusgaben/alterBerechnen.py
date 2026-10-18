# Demonstration von Ein- und Ausgaben
# 
# Lies das Geburtsjahr ein und gib das berechnete
# Alter aus
#
# JEDE EINGABE ÜBER DEN INPUT-BEFEHL IST EINE ZEICHENKETTE
# Damit wir mit der Eingabe rechnen können müssen wir diese
# zuerst mit Hilfe des int-Befehls in eine Ganzzahl umwandeln.
#
aktuellesJahr = int(input("Welches Jahr haben wir ?: "))
geburtsjahr   = int(input("In welchem Jahr bist Du geboren ?: "))
#
# Wir berechnen das Alter und legen es in der Variablen alter ab
#
alter = aktuellesJahr - geburtsjahr
#
# Wir geben das Alter aus
#
print("Du bist " + str(alter) + " Jahre alt.")

