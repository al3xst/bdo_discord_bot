from discord.ext import commands

import config


bot = commands.Bot(command_prefix=config.BOT_COMMAND_PREFIX)

# this specifies what extensions to load when the bot starts up
startup_extensions = ["failstacks"]

bot.remove_command("help")  # we will write our own help command


@bot.event
async def on_ready():
    print("Link to add bot: https://discordapp.com/oauth2/authorize?client_id={0}&scope=bot&permissions=0".format(bot.user.id))


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run(config.TOKEN)
