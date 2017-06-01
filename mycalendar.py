import discord
from discord.ext import commands
from datetime import datetime

import config


class Calendar:
    def __init__(self, bot):
        self.bot = bot

        self.help_description = "Kalender"  # Description of our extension, for our help command
        self.help_commandname = "cal"  # Commandname, for our help command

    # The current event should be skipped
    def skip(self, member):
        #check if user is allowed to use this command
        return

    # Sets the current description of the event
    def set(self, member, text):
        return

    @staticmethod
    def cal_help(member):
        return "{0.mention},\n".format(member) + \
               "```md\nDu kannst zum Event an- bzw. abmelden.\n" \
               "#Drück einfach auf den jeweiligen Daumen.\n" \
               "```"

    @staticmethod
    def cal_help_admin(member):
        return "{0.mention},\n".format(member) + \
               "```md\nAls Admin des Bots kannst du folgende Befehle ausführen:\n" \
               "#Event überspringen: !cal skip\n" \
               "```"

    def add_date(self, ctx, date, message):
        print(message)

    def del_date(self, ctx, date, message):
        print(message)

    @commands.command(pass_context=True)
    async def cal(self, ctx, *args):
        member = ctx.message.author

        cmd = args[0]

        # args[0] = +/-
        if cmd == '+':
            self.accept(member)
            msg = await self.bot.say(member.name + " hat zugesagt.")
            await self.bot.add_reaction(msg, '👍')
            await self.bot.add_reaction(msg, '👎')
        elif args[0] == '-':
            self.decline(member)
            msg = await self.bot.say(member.name + " hat abgesagt.")
            await self.bot.add_reaction(msg, '👍')
            await self.bot.add_reaction(msg, '👎')
        elif cmd == "reg" or cmd == "register":
            self.register(member)
        elif cmd == "skip":
            self.skip(member)


def setup(bot):
    bot.add_cog(Calendar(bot))
