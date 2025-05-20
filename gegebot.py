import discord
import wikipedia

intents = discord.Intents.all()
bot = discord.Bot(intents=intents)

sniped_message = None

@bot.event
# This event triggers when the bot is ready
# It will print the bot's username and set its Discord presence
async def on_ready():
    print(f'We have logged in as {bot.user}.')
    activity = discord.Game("with Kanda's patience..")
    await bot.change_presence(activity=activity)
    print("gegebot activated!")

# We define server IDs to avoid the global update delay
servers = [1264749652595703908]

# This function is for the poke command
@bot.slash_command(guild_ids=servers, name = "poke", description = "poke gege")
async def poke(ctx):
    await ctx.channel.trigger_typing() # shows that the bot is typing
    # Respond with a message containing the latency of the bot
    try:
        await ctx.respond(f"i'm awake! \n\nLatency: {round(bot.latency * 1000)}ms")
    except:
        await ctx.send(f"i'm awake! \n\nLatency: {round(bot.latency * 1000)}ms")

# This function is for the snipe command
@bot.event
async def on_message_delete(message):
    # Check if the message is not from a bot
    if not message.author.bot:
        # Store the deleted message
        global sniped_message
        sniped_message = message

@bot.slash_command(guild_ids=servers, name = "snipe", description = "snipe the last deleted message")
async def snipe(ctx):
    # Check if there is a sniped message
    await ctx.channel.trigger_typing() # shows that the bot is typing
    if sniped_message is None:
        try:
            await ctx.respond(f'no messages to snipe!')
        except:
            await ctx.send(f'no messages to snipe!')
    else:
        # Create an embed with the sniped message content and author
        embed = discord.Embed(description=sniped_message.content, color=0x00ff00)
        embed.set_author(name=sniped_message.author.name, icon_url=sniped_message.author.avatar.url)
        try:
            await ctx.respond(embed=embed)
            await ctx.respond(f'get sniped bitch')
        except:
            await ctx.send(embed=embed)
            await ctx.send(f'get sniped bitch')

# This function is for the wikisearch command
@bot.slash_command(guild_ids=servers, name = "wikisearch", description = "search Wikipedia for your search term")
async def wikisearch(ctx, search):
    # Search Wikipedia for the provided content
    await ctx.channel.trigger_typing() # shows that the bot is typing
    try:
        summary = wikipedia.summary(search, chars = 1950)
        try:
            await ctx.respond(summary)
        except:
            await ctx.send(summary)
    except:
        try:
            await ctx.respond(f'failed to find a Wikipedia article based on your search, sorry :3')
        except:
            await ctx.send(f'failed to find a Wikipedia article based on your search, sorry :3')

# This function is for the wikirandom command
@bot.slash_command(guild_ids=servers, name = "wikirandom", description = "get a random Wikipedia article")
async def wikirandom(ctx):
    await ctx.channel.trigger_typing()
    try:
        title = wikipedia.random()
        # Fix up the title so we can find the URL
        fixed_title = title.replace(' ', '_')
        summary = wikipedia.summary(fixed_title, chars = 1950)
        try:
            await ctx.respond(summary)
        except:
            await ctx.send(summary)
    except:
        try:
            await ctx.respond(f'failed to find a random Wikipedia article, sorry :3')
        except:
            await ctx.send(f'failed to find a random Wikipedia article, sorry :3')

bot.run('Your_Token_Here')