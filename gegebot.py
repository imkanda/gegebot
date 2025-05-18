import discord

bot = discord.Bot()

sniped_message = None

@bot.event
# This event triggers when the bot is ready
# It will print the bot's username and set its Discord presence
async def on_ready():
    print(f'We have logged in as {bot.user}.')
    await bot.change_presence(activity=discord.ActivityType.listening(name="Kanda's complaining.."))
    print("gegebot activated!")

# We define server IDs to avoid the global update delay
servers = []

# This function is for the poke command
@bot.slash_command(guild_ids=servers, name = "poke", description = "poke gege")
async def poke(ctx):
    # Respond with a message containing the latency of the bot
    await ctx.respond(f"i'm awake! \n\nLatency: {round(bot.latency * 1000)}ms")

# This function is for the snipe command
@bot.event
async def on_message_delete(message):
    global sniped_message
    # Check if the message is not from a bot
    if not message.author.bot:
        # Store the deleted message
        sniped_message = message

@bot.slash_command(guild_ids=servers, name = "snipe", description = "snipe the last deleted message")
async def snipe(ctx):
    # Check if there is a sniped message
    if sniped_message is None:
        await ctx.respond(f'no messages to snipe!')
    else:
        # Create an embed with the sniped message content and author
        embed = discord.Embed(description=sniped_message.content, color=0x00ff00)
        embed.set_author(name=sniped_message.author.name, icon_url=sniped_message.author.avatar.url)
        await ctx.respond(embed=embed)
        await ctx.respond(f'get sniped bitch')

bot.run('Your_Token_Here')