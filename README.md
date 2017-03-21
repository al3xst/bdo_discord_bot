# bdo discord bot
Ein Discord Bot für unsere Black Desert Online Gilde.

Der Code wurde mit Python 3.6 entwickelt. Version 2.7 wurde nicht getestet und wird nicht unterstüzt.


# Installation
1. Packet `discord.py` installieren mit pip
`pip3 install discord.py`

2. Bot token von Discord kopieren (https://discordapp.com/developers/applications/me/) und in der Datei `config.py` in die Variable `token` einsetzen

3. Im Discordserver einen Channel mit dem Namen `bot` erstellen

4. Den Bot in den Server einlanden. Dazu folgende URL anpassen: https://discordapp.com/oauth2/authorize?client_id=CLIENT_ID&scope=bot&permissions=0 `CLIENT_ID` muss durch die Bot ID (Siehe Link aus Punkt 2) ersetzt werden.

5. Den Bot starten mit `python3 main.py`



Unterstütze Befehle:
`!fs <Dein aktuelles +> <Failstacks>`
