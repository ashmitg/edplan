import discord
from generatecourses import process

intents = discord.Intents().all()
client = discord.Client(intents=intents)

# A dictionary to store user settings
user_settings = {}
default_parameters = {'qmax': 3, 'smax': 2, 'interest': 'ECON, POLI'}


# Event: Logging in
@client.event
async def on_ready():
  print("Successful login as {0.user}".format(client))


# Event: Receiving messages
@client.event
async def on_message(message):
  # Check if the bot is the sender or if the message doesn't start with '!'
  desired_channel_id = 1141517653228388422
  if message.channel.id != desired_channel_id:
    return
  if message.author == client.user or not message.content.startswith('!'):
    return
  user_mention = message.author.mention
  command = message.content.lower().split()[0]
  if command == '!generate':
    # Check for user-specified parameters
    params = parse_parameters(message.content)
    if not params:
      params = default_parameters

    if message.attachments:
      for attachment in message.attachments:
        if attachment.filename.lower().endswith('.pdf'):
          pdf_data = await attachment.read()

          # Extract parameters from user input or use defaults
          qmax = int(params.get('qmax', 3))
          smax = int(params.get('smax', 2))

          interests = params.get('interest', '').split(',')

          interests = [interest.upper() for interest in interests]

          schedule = process(pdf_data, qmax, smax, interests)
          user_id = message.author.id
          user_settings[user_id] = params  # Store the user's settings

          await send_long_message(
            message.channel,
            f"{user_mention}, here's your generated schedule:",
            format_schedule(schedule))
          return
    else:
      await message.channel.send(
        "Please attach a Assist.org transfer PDF file for processing.")
  elif command == '!generatehelp':
    help_message = (
      "Bot Commands:\n"
      "!generate - !generate qmax:3, smax:2, interest:(ECON, POLI) qmax sets the quarter class limit while smax sets the summer class limit.\n"
      "!generatesettings - Display your stored settings.\n"
      "!generatehelp - Display this help message.")
    await message.channel.send(help_message)
  elif command == '!generatesettings':
    user_id = message.author.id
    if user_id in user_settings:
      settings = user_settings[user_id]
      settings_text = "\n".join(
        [f"{param}: {value}" for param, value in settings.items()])
      await message.channel.send(f"Your stored settings:\n{settings_text}")
    else:
      await message.channel.send("No stored settings found for you.")


# Send a long message in chunks
async def send_long_message(channel, header, text, chunk_size=2000):
  for i in range(0, len(text), chunk_size):
    chunk = text[i:i + chunk_size]
    await channel.send(f"{header}\n{chunk}")


# Parse user-specified parameters from message content
def parse_parameters(content):
  params = {}
  parts = content.split()[1:]
  for part in parts:
    key_value = part.split(':')
    if len(key_value) == 2:
      key, value = key_value
      params[key.lower()] = value
  return params


# Modify the format_schedule function to return a formatted string
def format_schedule(schedule):
  formatted_schedule = ""
  for i, quarter in enumerate(schedule):
    if len(quarter) == 0 and i % 4 != 0:
      continue
    if i % 4 == 0:
      formatted_schedule += f"Summer Quarter {i + 1} Courses:\n"
    else:
      formatted_schedule += f"Quarter {i + 1} Courses:\n"
    for course in quarter:
      formatted_schedule += (
        f"{course.name} (Category: {course.category}, Credits: {course.credits})\n"
      )
    formatted_schedule += "\n"
  return formatted_schedule


# Run the bot
client.run('MTE0MTI1MDMyODY2MzE3OTI5NA.G-PRbJ.CCnELtPaPDKKTwFJ427jrh3snupSJOTEb6nBzc')
