import discord
from discord.ext import commands 
import requests 
import requests
import google.generativeai as genai
import os
import asyncio
from googletrans import Translator
# import aiohttp
# from PIL import Image 
# from joke_api_code import get_joke


intents = discord.Intents.default()
intents = True
client = commands.Bot(command_prefix = '!', intents=discord.Intents.all())


@client.event
async def on_ready():
   await client.change_presence(
    status=discord.Status.online,
    activity=discord.Activity(
        type=discord.ActivityType.watching,
        name="YouTube"
    )
)
# print(f"Logged in as {client.user.name} ({client.user.id})")
print("The bot is now ready to use")
print("----------------------------")


@client.command()
async def hello(ctx):
    # print("Hello command triggered!")  
    await ctx.send("Hello, I am the Leo bot, your best friend!")



@client.event
async def on_member_join(member):
    # Joke API
  

  url = "https://jokes-always.p.rapidapi.com/erJoke"

  headers = {
	"X-RapidAPI-Key": " API_KEY ",
	"X-RapidAPI-Host": "jokes-always.p.rapidapi.com"
 }

  response = requests.get(url, headers=headers)



  channel = client.get_channel("your channel ID")
  await channel.send(f"Hey {member.mention}, welcome to this server")
#   await channel.send(json.loads(response.text))['content']
  await channel.send(response.text)


@client.event
async def on_member_remove(member):
    channel = client.get_channel("your channel ID")
    await channel.send(f"Goodbye {member.mention}")

@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author.bot:
        return

    # Check if the bot is mentioned and the message contains "hello"
    if client.user in message.mentions and "hello" in message.content.lower():
        await message.channel.send("Hello! How can I assist you?")

    # Process other commands

    await client.process_commands(message)





# To make the bot join the voice cnannel or disconnect from voice channel
@client.command(pass_context = True)
async def join(ctx):
 if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    await ctx.send("voice connected")
 else:
    await ctx.send("You are not in the voice channel, You must be in voice channel to run this command  ")

@client.command(pass_context = True)
async def leave(ctx):
   if (ctx.voice_client):
      await ctx.guild.voice_client.disconnect()
      await ctx.send("I left the voice channel")
   else:
      await ctx.send("i am not in the voice channel")
    




# FFMPEG_OPTIONS = {
#     'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
#     'options': '-vn -filter:a "volume=25"'
# }

      
# to detact specific word in text channel
@client.event
async def on_message(message):
   await client.process_commands(message)

   badwords =["fuck", ] 

   for word in badwords:
    if word in message.content.lower():
      await message.delete() 
      member = message.author
      await message.channel.send(f" {member.mention} Ayeeeee gali galoz yaha mat karo ")

#    print(message)
      

# code for embed command
@client.command()
async def angrycat(ctx):
    embed = discord.Embed(
        title="Cat",
        url="https://i.pinimg.com/originals/ba/92/7f/ba927ff34cd961ce2c184d47e8ead9f6.jpg",
        description="meow meow",
        color=0xe80c0c
    )
    embed.set_author(
        name=ctx.author.display_name,
        url="https://google.com",
        icon_url=ctx.author.display_avatar.url
    )
    embed.set_thumbnail(url="https://media1.tenor.com/m/r0R0N3dI3kIAAAAd/dancing-cat-dance.gif")
    embed.add_field(name="Angry cat", value="Angriest cat of all time", inline=False)
    embed.set_image(url="https://media1.tenor.com/m/EaaKVocJwckAAAAd/kitten-angry.gif")
    
    #only one gif/image is supported by discord in embed message
    # embed.add_field(name="cute cat", value="Cutest cat of all time", inline=False) 
    # embed.set_image(url="https://media1.tenor.com/m/r0R0N3dI3kIAAAAd/dancing-cat-dance.gif") 
    embed.set_footer(text="We all love cats")
    await ctx.send(embed=embed)


@client.command()
async def dancingcat(ctx):
    embed = discord.Embed(
        title="Cat",
        url="https://i.pinimg.com/originals/ba/92/7f/ba927ff34cd961ce2c184d47e8ead9f6.jpg",
        description="meow meow",
        color=0xe80c0c
    )
    embed.set_author(
        name=ctx.author.display_name,
        url="https://google.com",
        icon_url=ctx.author.display_avatar.url
    )
    
    embed.set_thumbnail(url="https://media1.tenor.com/m/YR1hxyktKYYAAAAC/cat.gif")
    embed.add_field(name="Dancing cat", value="you can't beat this cat", inline=False) 
    embed.set_image(url="https://media1.tenor.com/m/r0R0N3dI3kIAAAAd/dancing-cat-dance.gif") 
    embed.set_footer(text="We all love cats")
    await ctx.send(embed=embed)




# gemini ai chat-bot
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

 # Model and chat session configuration (adjust parameters as needed)
generation_config = {
     "temperature": 1,  # Controls randomness (higher = more creative, less coherent)
     "top_p": 0.95,  # Probability weighting for likely continuations
     "top_k": 64,  # Maximum number of vocabulary tokens to consider
     "max_output_tokens": 8192,  # Maximum number of tokens in the response
     "response_mime_type": "text/plain",
 }
safety_settings = [
     {
         "category": "HARM_CATEGORY_HARASSMENT",
         "threshold": "BLOCK_MEDIUM_AND_ABOVE",
     },
     {
         "category": "HARM_CATEGORY_HATE_SPEECH",
         "threshold": "BLOCK_MEDIUM_AND_ABOVE",
     },
     {
         "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
         "threshold": "BLOCK_MEDIUM_AND_ABOVE",
     },
     {
         "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
         "threshold": "BLOCK_MEDIUM_AND_ABOVE",
     },
 ]

model = genai.GenerativeModel(
     model_name="gemini-1.5-flash",
     safety_settings=safety_settings,
     generation_config=generation_config,
 )

chat_session = model.start_chat(history=[])




@client.event #separate the decorators for !ask and !translate
async def on_message(message):
    if message.author == client.user:
        return  # Ignore messages from the bot itself

    if message.content.lower().startswith("!translate"):
        # This creates a new task for the translation command
        asyncio.create_task(handle_translate(message))

    elif message.content.lower().startswith("!ask"):
        # This creates a new task for the Gemini API calls
        asyncio.create_task(handle_ask(message))


async def handle_ask(message):
    if message.author == client.user:
        return  # Ignore messages from the bot itself



    if message.content.startswith("!ask"):
        # Extract user input
        user_input = message.content[len("!ask"):].strip()

        # Generate Gemini AI response
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_input)

        member = message.author

        # max response to 2000 characters
        fragment_response = response.text[:1800]

        # Send the first fragment (first 2000 characters)
        await message.channel.send(f"{member.mention}  {fragment_response}")

        # Add a delay (e.g., 1-2 seconds) to avoid rate limits
        await asyncio.sleep(1)

        # If the full response exceeds 2000 characters, send the remaining fragment
        if len(response.text) > 1800:
            remaining_fragment = response.text[2000:]
            await message.channel.send(remaining_fragment)

        print(message)


# to translate from any language to english
translator = Translator()
async def handle_translate(message):
   if message.author == client.user:
      return
   if message.content.lower().startswith("!translate"):
        # Extract remaining message after "!trans " 
        message_to_translate = message.content[10:].strip()

   try:
     # Translate to English
    translation_english = translator.translate(message_to_translate, dest='english')
    translated_text_english = translation_english.text


    member = message.author

    await message.channel.send(f"{member.mention} **Translation in English:** {translated_text_english}")

   except Exception as e:
    await message.channel.send(f"An error occurred during translation: {e}")





client.run(discord_token)

