from discord.ext import commands

import config  # config.py
import discord
import logging

bot = commands.Bot(command_prefix=config.BOT_COMMAND_PREFIX)

bot.remove_command("help")  # we will write our own help command

# this specifies what extensions to load when the bot starts up
startup_extensions = ["failstacks", "mycalendar"]


# Log everything to discord.log
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


@bot.event
async def on_command_error(error, ctx):
    if (ctx.message.channel.name not in config.CHANNEL_LIST) and not ctx.message.channel.is_private:
        return

    try:
        if not ctx.message.channel.is_private:
            await bot.delete_message(ctx.message)
    except discord.Forbidden:
        print("I have no rights, to remove messages in this channel: {}".format(ctx.message.channel.name))
    return await bot.send_message(ctx.message.author,
                                  "{}. Use `!help` to list all available commands".format(error))


@bot.event
async def on_ready():
    print("Link to add bot: https://discordapp.com/oauth2/authorize?client_id={0}&scope=bot&permissions=0".format(bot.user.id))

#  For a voting plugin
@bot.event
async def on_reaction_add(reaction, user):
    if user.id == bot.user.id:  # ignore self
        return

    if (reaction.message.channel.name not in config.CHANNEL_LIST) and not reaction.message.channel.is_private:  # ignore all other channels
        return

    if reaction.emoji[0] != '👍' and reaction.emoji[0] != '👎':  # remove unwanted reactions
        try:
            await bot.remove_reaction(reaction.message, reaction.emoji, user)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed {}'.format(exc))
        return

    # remove the opposite reaction from the user, if available
    if reaction.emoji[0] == '👍':
        await bot.remove_reaction(reaction.message, '👎', user)
    else:
        await bot.remove_reaction(reaction.message, '👍', user)


@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:  # ignore self
        return

    if(message.channel.name not in config.CHANNEL_LIST) and not message.channel.is_private:  # ignore all other channels
        return

    if not message.content.startswith(config.BOT_COMMAND_PREFIX):  # delete all messages without prefix in main channel
        await bot.delete_message(message)
        return

    await bot.process_commands(message)

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run(config.TOKEN)
