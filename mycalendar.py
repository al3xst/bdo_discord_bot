import discord
from discord.ext import commands
from datetime import datetime

import config
import sqlite3


class Calendar():
    def __init__(self, bot):
        self.bot = bot

        self.help_description = "Kalender"  # Description of our extension, for our help command
        self.help_commandname = "cal"  # Commandname, for our help command
        self.help_explain = "Syntax: `!cal (add|del) <Datum> (optional: <Uhrzeit>) " \
                            "<Name des Eintrags>`\n"  # Short explenation how to use this command

        self.db_conn = sqlite3.connect('calendar.db')
        self.init_sqlite()

    def init_sqlite(self):
        # DB layout:
        # table calendar:
        # id | serverid | createdby | dateandtime | description | timestamp
        # eg:
        # 1 | "123412341234123412" | "al3xst#1234" | "30.03.2017 15:00" | "GW in Serendia4, Treffpunkt Heidel!" | "2017-03-23T21:20:24.200"

        self.db_conn.execute("CREATE TABLE IF NOT EXISTS calendar("
                             "id INTEGER PRIMARY KEY, "
                             "serverid TEXT, "
                             "createdby TEXT, "
                             "dateandtime TEXT, "
                             "description TEXT, "
                             "timestamp DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL)")

    @staticmethod
    def cal_help(member):
        return "{0.mention},\n".format(member) + \
               "```md\nIch habe dich leider nicht verstanden.\n" \
               "#Syntax hinzufügen: !cal add <Datum> (optional: <Uhrzeit>) <Name des Eintrags>\n" \
               "#Syntax löschen: !cal del <Datum> (ggf: <Uhrzeit>)\n" \
               "Datumsformat: TT.MM oder TT.MM.YYYY\n" \
               "Uhrzeitformat: HH:MM\n\n" \
               "Beispiele:\n" \
               "==========\n" \
               "Du möchtest am 21.03.2017 einen Eintrag für einen Postenkrieg um 19:20 erstellen:\n" \
               "!cal 21.03 19:20 Postenkrieg Mediah1\n" \
               "oder: !cal 21.03.2017 19:20 Postenkrieg Mediah1\n\n" \
               "Angaben ohne Uhrzeiten gelten als Ganztagesevent\n" \
               "Es kann also jeweils nur ein Ganztagesevent geben und pro Uhrzeit nur ein Event\n" \
               "```"

    def add_date(self, ctx, date, message):
        print(message)

    def del_date(self, ctx, date, message):
        print(message)

    @commands.command(pass_context=True)
    async def cal(self, ctx, *args):
        if (ctx.message.channel.name not in config.CHANNEL_LIST) and not ctx.message.channel.is_private:
            #  print(ctx.message.channel.name + " not in " + str(config.CHANNEL_LIST))
            return

        member = ctx.message.author

        mydate = None

        try:
            cmd = args[0]
            if (cmd != "del") and (cmd != "add"):
                raise Exception

            date = args[1]
            time = args[2]

            message = ""

            if len(date.split('.')) == 2:
                date += "." + str(datetime.today().year)

            if len(time.split(':')) == 2:
                date += " " + time
                mydate = datetime.strptime(date, '%d.%m.%Y %H:%M')
                message = " ".join(list(args[3:]))
            else:
                mydate = datetime.strptime(date, '%d.%m.%Y')
                message = " ".join(list(args[2:]))

            if mydate < datetime.today() and mydate.hour != 0 and mydate.minute != 0:
                print("Das Datum liegt in der Vergangenheit")
                return
        except:
            await self.bot.say(self.cal_help(member))
            print("Irgendetwas lief aus dem Ruder. Hier sind die Argumente: " + str(args))
            return

        # args[0] = add/del
        if args[0] == "add":
            self.add_date(ctx, mydate, message)

        if args[0] == "del":
            self.del_date(ctx, mydate)

        # mydate

        await self.bot.say(self.cal_help(member))


def setup(bot):
    bot.add_cog(Calendar(bot))
