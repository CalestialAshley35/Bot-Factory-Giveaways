import discord
import random
from discord.ext import commands
import datetime

intents = discord.Intents.default()
intents.reactions = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} is online and ready to manage giveaways!')

@bot.command()
@commands.has_permissions(administrator=True)
async def giveaway(ctx, minutes: int, *, prize: str):
    """Starts a giveaway."""
    embed = discord.Embed(title="🎉 Giveaway Time! 🎉", 
                          description=f"Prize: **{prize}**\nReact with 🎉 to enter!\nTime: {minutes} minutes", 
                          color=discord.Color.blue())
    embed.set_footer(text=f"Hosted by {ctx.author.name}", icon_url=ctx.author.avatar.url)
    giveaway_message = await ctx.send(embed=embed)

    await giveaway_message.add_reaction("🎉")

    end_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=minutes)
    await discord.utils.sleep_until(end_time)

    new_message = await ctx.channel.fetch_message(giveaway_message.id)
    users = await new_message.reactions[0].users().flatten()
    users.remove(bot.user)

    if len(users) == 0:
        await ctx.send("No one entered the giveaway! 😢")
    else:
        winner = random.choice(users)
        await ctx.send(f"Congratulations {winner.mention}, you won the **{prize}**!")

@bot.command()
@commands.has_permissions(administrator=True)
async def reroll(ctx, giveaway_message_id: int):
    """Rerolls the winner of a giveaway."""
    giveaway_message = await ctx.channel.fetch_message(giveaway_message_id)
    users = await giveaway_message.reactions[0].users().flatten()
    users.remove(bot.user)

    if len(users) == 0:
        await ctx.send("No one entered the giveaway to reroll!")
    else:
        winner = random.choice(users)
        await ctx.send(f"The new winner is {winner.mention}! 🎉")

# Replace 'YOUR_BOT_TOKEN' with your Discord bot token
bot.run('YOUR_BOT_TOKEN')
