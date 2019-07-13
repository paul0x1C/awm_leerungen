import bs4, requests

url = 'https://www.awm-muenchen.de/index/abfuhrkalender.html'

def abrufen(jahr, woche, strasze, hausnummer):
    data = {
      'tx_awmabfuhrkalender_pi1[selectweek]': '{:02}|{}'.format(woche, jahr),
      'tx_awmabfuhrkalender_pi1[strasse]': '{}'.format(strasze),
      'tx_awmabfuhrkalender_pi1[hausnummer]': '{}'.format(hausnummer),
      'tx_awmabfuhrkalender_pi1[section]': 'address',
      'tx_awmabfuhrkalender_pi1[submitAbfuhrkalender]': 'Weiter'
    }
    response = requests.post(url, data=data)

    soup = bs4.BeautifulSoup(response.text, features = "lxml")
    kalender = soup.find("table", {'class':'abfuhrkalender'})
    imgs = kalender.findAll("img")
    leerungen = {}
    for img in imgs:
        datum = img.parent.findPreviousSibling().text
        if datum not in leerungen:
            leerungen[datum] = []
        tonne = img.get("alt")
        if not tonne == "Geänderter Leerungstag":
            leerungen[datum].append(tonne)
    return leerungen
