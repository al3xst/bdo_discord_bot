import discord
from discord.ext.commands import Bot

import config


my_bot = Bot(command_prefix="!")

#  failstack and probabilty table from https://imgur.com/a/D5ngu
fs_table = {'acc': {1: {'Base': 15, 'perFS': 1.5, 'maxFS': 25},  # to pri
                    2: {'Base': 7.5, 'perFS': 0.75, 'maxFS': 35},
                    3: {'Base': 5, 'perFS': 0.5, 'maxFS': 44},
                    4: {'Base': 2, 'perFS': 0.25, 'maxFS': 90},
                    5: {'Base': 1.5, 'perFS': 0.25, 'maxFS': 124}},
            'wep': {1: {'Base': 100, 'perFS': 0, 'maxFS': 0},  # to +1
                    2: {'Base': 100, 'perFS': 0, 'maxFS': 0},
                    3: {'Base': 100, 'perFS': 0, 'maxFS': 0},
                    4: {'Base': 100, 'perFS': 0, 'maxFS': 0},
                    5: {'Base': 100, 'perFS': 0, 'maxFS': 0},
                    6: {'Base': 100, 'perFS': 0, 'maxFS': 0},
                    7: {'Base': 100, 'perFS': 0, 'maxFS': 0},
                    8: {'Base': 20, 'perFS': 2.5, 'maxFS': 13},
                    9: {'Base': 17.5, 'perFS': 2, 'maxFS': 14},
                    10: {'Base': 15, 'perFS': 1.5, 'maxFS': 15},
                    11: {'Base': 12.5, 'perFS': 1.25, 'maxFS': 16},
                    12: {'Base': 10, 'perFS': 0.75, 'maxFS': 18},
                    13: {'Base': 7.5, 'perFS': 0.63, 'maxFS': 20},
                    14: {'Base': 5, 'perFS': 0.5, 'maxFS': 25},
                    15: {'Base': 2.5, 'perFS': 0.5, 'maxFS': 25},
                    16: {'Base': 15, 'perFS': 1.5, 'maxFS': 25},  # to pri
                    17: {'Base': 7.5, 'perFS': 0.75, 'maxFS': 35},
                    18: {'Base': 5, 'perFS': 0.5, 'maxFS': 44},
                    19: {'Base': 2, 'perFS': 0.25, 'maxFS': 90},
                    20: {'Base': 1.5, 'perFS': 0.15, 'maxFS': 124}},
            'arm': {1: {'Base': 100, 'perFS': 0, 'maxFS': 0},  # to +1
                    2: {'Base': 100, 'perFS': 0, 'maxFS': 0},
                    3: {'Base': 100, 'perFS': 0, 'maxFS': 0},
                    4: {'Base': 100, 'perFS': 0, 'maxFS': 0},
                    5: {'Base': 100, 'perFS': 0, 'maxFS': 0},
                    6: {'Base': 20, 'perFS': 2.5, 'maxFS': 13},
                    7: {'Base': 17.5, 'perFS': 2, 'maxFS': 14},
                    8: {'Base': 16.25, 'perFS': 1.75, 'maxFS': 14},
                    9: {'Base': 15, 'perFS': 1.5, 'maxFS': 15},
                    10: {'Base': 12.5, 'perFS': 1.25, 'maxFS': 16},
                    11: {'Base': 11.25, 'perFS': 1, 'maxFS': 17},
                    12: {'Base': 10, 'perFS': 0.75, 'maxFS': 18},
                    13: {'Base': 7.5, 'perFS': 0.63, 'maxFS': 20},
                    14: {'Base': 5, 'perFS': 0.5, 'maxFS': 25},
                    15: {'Base': 2.5, 'perFS': 0.5, 'maxFS': 25}}}


def fs_help(member):
    return "{0.mention},\n".format(member) + \
           "```md\nIch habe dich leider nicht verstanden.\n" \
           "#Syntax: !fs <aktuelles +> <Failstacks>\n" \
           "zb: Du hast eine +14 Waffe und 22 Stacks\n" \
           "Dann schreibe bitte: !fs 14 22\n```"


def fs_getprob(equip, args):
    toplus = int(args[0]) + 1
    failstacks = 0
    if len(args) == 2:
        failstacks = int(args[1])

    # icon
    res = ""
    if equip == "wep":
        res = ":crossed_swords:"
    elif equip == "arm":
        res = ":shield:"
    elif equip == "acc":
        res = ":ring:"

    eq_tab = fs_table[equip]

    if eq_tab[toplus]['maxFS'] > failstacks:
        res += " " + str(eq_tab[toplus]['Base'] + failstacks * eq_tab[toplus]['perFS']) + "%"
    else:
        res += " " + str(eq_tab[toplus]['Base'] + eq_tab[toplus]['maxFS'] * eq_tab[toplus]['perFS']) + "%"

    eqch = "Basischance: **" + str(eq_tab[toplus]['Base']) + "%**\n"
    eqch += "+ **" + str(eq_tab[toplus]['perFS']) + "%** pro Failstack\n"
    eqch += "max Failstack: **" + str(eq_tab[toplus]['maxFS']) + "**"

    result = (res, eqch)

    return result


def fs_calc(args):
    currentplus = int(args[0])
    toplus = int(args[0]) + 1
    failstacks = "0"

    if len(args) == 2:
        failstacks = str(int(args[1]))

    embed = discord.Embed(title="Failstack Tabelle (Quelle)", color=0x00ccff)
    discord.Embed()
    embed.set_author(name="Failstack Rechner", icon_url='http://666kb.com/i/dhow7qdv1s39pw4f2.png')
    embed.url = "https://imgur.com/a/D5ngu"

    embed.add_field(name="Von +" + str(currentplus) + " nach +" + str(toplus) + " mit "
                         + str(failstacks) + " Failstacks",
                    value="hast du eine Wahrscheinlichkeit von:", inline=False)

    wep = fs_getprob("wep", args)
    embed.add_field(name=wep[0], value=wep[1], inline=True)

    if currentplus < 15:
        arm = fs_getprob("arm", args)
        embed.add_field(name=arm[0], value=arm[1], inline=True)

    if currentplus < 5:
        acc = fs_getprob("acc", args)
        embed.add_field(name=acc[0], value=acc[1], inline=True)

    #  embed.set_footer(text="Die Vier Winde")

    return embed


@my_bot.command(pass_context=True)
async def fs(ctx, *args):
    #  if not ((ctx.message.channel.name == "bot") or ctx.message.channel.is_private):
    #    return

    member = ctx.message.author

    if len(args) < 1 or len(args) > 2:
        return await my_bot.say(fs_help(member))

    try:
        ia = int(args[0])
        ib = int(args[0])
        if ia < 0 or ia > 19:
            raise ValueError()
    except ValueError:
        return await my_bot.say(fs_help(member))

    await my_bot.say("{0.mention}".format(member))

    return await my_bot.say(embed=fs_calc(args))


my_bot.run(config.token)
