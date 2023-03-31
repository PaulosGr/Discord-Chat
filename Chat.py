import discord
import openai
import os

# Define the intents you want to use
intents = discord.Intents.default()
intents.members = True

# Create a new instance of the client with the intents parameter
client = discord.Client(intents=intents)

# Set up the OpenAI API client
openai.api_key = os.environ.get(
  "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")


# Define the function that generates text using Chat GPT
def generate_text(prompt):
  response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
  )
  return response.choices[0].text.strip()


# Define the function that handles incoming messages
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  # Check if the message starts with the bot's mention or prefix
  if message.content.startswith(
      f"<@!{client.user.id}>") or message.content.startswith("!gpt"):
    # Get the text prompt from the message
    prompt = message.content.replace(f"<@!{client.user.id}>",
                                     "").replace("!gpt", "").strip()

    # Generate a response using Chat GPT
    response = generate_text(prompt)

    # Send the response back to the channel
    await message.channel.send(response)



# Start the bot
client.run(os.environ.get("MTA5MDI5NTE2NzE3ODc2ODUyNQ.G1LFXF._K_frlCjp1zYHKKpkNfd_Dm6sgemv7oKqb4rqI"))