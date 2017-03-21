# bdo discord bot
Ein Discord Bot für unsere Black Desert Online Gilde.

Der Code wurde mit Python 3.6 entwickelt. Version 2.7 wurde nicht getestet und wird nicht unterstüzt.


# Installation
1. Packet `discord.py` installieren mit pip
`pip3 install discord.py`

2. Bot token von Discord kopieren (https://discordapp.com/developers/applications/me/) und in der Datei `config.py` in die Variable `token` einsetzen
3. In der `config.py` die gewünschten Channels einstellen (z.b. `CHANNEL_LIST=["bot","info"]`)
4. Den Bot starten mit `python3 main.py`
5. Sobald der Bot online ist, generiert er einen Link, diesen anklicken und dann auswählen zu welchem Server der Bot hinzugefügt werden soll

Unterstütze Befehle:
`!fs <Dein aktuelles +> <Failstacks>`


# Anmerkung
Der Bot antwortet auf deutsch. Sollten mehrere Sprachen gewünscht sein, so bitte bei mir melden, dann kann man über Internationalisierung sich paar Gedanken machen.

Der Prefix des Bots kann frei gewählt werden. Anstatt des `!`-Zeichen kann z.b. auch ein `?`-Zeichen benutzt werden. Das gewünschte Zeichen einfach in der `config.py` im Wert `BOT_COMMAND_PREFIX` einsetzen.

Das Projekt wurde in Python geschrieben um die eigenen Python-Kenntnisse aufzufrischen und natürlich neues zu lernen. Für Kritik bin ich gerne jederzeit zu haben. Verbesserungsvorschläge sind jederzeit willkommen! 
Am besten über die Github-Issues.
