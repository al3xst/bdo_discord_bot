from discord.ext import commands
import discord
import config


bot = commands.Bot(command_prefix=config.BOT_COMMAND_PREFIX)

bot.remove_command("help")  # we will write our own help command

# this specifies what extensions to load when the bot starts up
startup_extensions = ["failstacks"]


@bot.event
async def on_command_error(error, ctx):
    if (ctx.message.channel.name not in config.CHANNEL_LIST) and not ctx.message.channel.is_private:
        #  print(ctx.message.channel.name + " not in " + str(config.CHANNEL_LIST))
        return

    try:
        if not ctx.message.channel.is_private:
            await bot.delete_message(ctx.message)
    except discord.Forbidden:
        print("I have no rights, to remove messages in this channel: {}".format(ctx.message.channel.name))
    return await bot.send_message(ctx.message.author,
                                  "{}.".format(error))#  !help `command`  will be implemented later


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
