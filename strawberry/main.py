import discord
from discord.ext import bridge
import dotenv
import os
import llm

dotenv.load_dotenv()

token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents()
intents.message_content = True

bot = bridge.Bot(command_prefix="ai!", intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.bridge_command(name="grok", description="Grok AI", guild_ids=["1324297515524423690"])
async def grok(ctx: bridge.BridgeApplicationContext, prompt: str):
    messages = [
        {"content": prompt, "role": "user"}
    ]

    try:
        ai_call = llm.llm_call("openrouter/x-ai/grok-3-beta", messages)
    except Exception as e:
        await ctx.respond(f"Exception: {e}")
        return
    
    response_content = ai_call.choices[0].message.content
    await ctx.respond(response_content)

bot.run(token)