import awm_leerungen

# hier eigene Adresse eintragen
jahr = 2019
woche = 4
strasze = "Adamstr." # (da gibts ganz viel Müll)
hausnummer = "2"

leerungen = awm_leerungen.abrufen(jahr, woche, strasze, hausnummer)

print(leerungen)
