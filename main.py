import discord 
import requests
from discord.ext import commands
import discord.ui
import os
import time
import json
from time import sleep 
import colorama
from colorama import *

token = "MTA3OTg3OTU1MTMwOTU5ODg1Mw.GzjT34.fZ1709lUR15UMUlNUdVqaFKn20ubAyftG-QZ1E"
prefix = "*"
version = "v1.0" 


intents = discord.Intents().all()


bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    print("Ready")

@bot.command()
async def ping(ctx):
    latency = bot.latency
    embed = discord.Embed(title="MS Diagnostic :ping_pong:", description=f"Ping : {latency*1000:.2f} ms", color=0x300000)
    await ctx.send(embed=embed)


@bot.command()
async def help(ctx):
    embed = discord.Embed(title=":seedling:", description="**List of all commands/tools : **", color=0x300000)
    embed.add_field(name=f"``` *ping ```", value="See if the CardX is satured or not.", inline=False)
    embed.add_field(name=f"``` *help ```", value="Send this embed..", inline=False)
    embed.add_field(name=f"``` *proxygen ```", value="Generate a HQ proxy.", inline=False)
    embed.add_field(name=f"``` *ccgen ```", value="Generate a random CC with CVV, Date.", inline=False)
    embed.add_field(name=f"``` *binanalysor ```", value="Get informations of the bin.", inline=False)
    embed.set_footer(text="CardX Tools")
    await ctx.send(embed=embed)


@bot.command()
async def binanalysor(ctx, arg: str):
    url = "https://bin-ip-checker.p.rapidapi.com/"
    querystring = {"bin": arg}
    payload = {"bin": arg}
    headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "c675acdf3emsh140b802b812ddd5p104155jsna5ea688bb245",
	"X-RapidAPI-Host": "bin-ip-checker.p.rapidapi.com"
}
    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
    mydict = json.loads(response.text)

    print(mydict)

    scheme = mydict["BIN"]["scheme"]
    number = mydict["BIN"]["number"]
    level = mydict["BIN"]["level"]
    type = mydict["BIN"]["type"]


    embed = discord.Embed(title=":seedling:", description="**Analysed Successfully **", color=0x300000)

    embed.add_field(name=f"``` SCHEME  :```", value=f"{scheme}", inline=False)
    embed.add_field(name=f"``` BIN  :```", value=f"{number}", inline=False)
    embed.add_field(name=f"``` LEVEL  :```", value=f"{level}", inline=False)
    embed.add_field(name=f"``` TYPE  :```", value=f"{type}", inline=False)

    embed.set_footer(text="CardX Tools")

    await ctx.send(embed=embed)

  

@bot.command()
async def proxygen(ctx):
    url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=50&country=all&ssl=all&anonymity=all"
    payload= {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    proxy = response.text

    embed = discord.Embed(title=":seedling:", description="** Generated Successfully **", color=0x300000)
    embed.add_field(name=f"``` 100 Proxy UHQ Valid  ```", value=f"{proxy}", inline=False)

    embed.set_footer(text="CardX Tools")

    await ctx.send(embed=embed)


@bot.command()
async def ccgen(ctx):
    url = "https://api.apistacks.com/v1/generatecard?api_key=78bb5c82-5ed3-488b-a0a3-df0db2d85402"
    payload= {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    mydict = json.loads(response.text)

    cvv = mydict["data"]["cvv"]
    cc = mydict["data"]["number"]
    exp = mydict["data"]["expiration"]

    embed = discord.Embed(title=":seedling:", description="** Generated Successfully **", color=0x300000)
    embed.add_field(name=f"```  CC  :  ```", value=f"{cc}", inline=False)
    embed.add_field(name=f"```  EXPIRATION  :  ```", value=f"{exp}", inline=False)
    embed.add_field(name=f"```  CVV :  ```", value=f"{cvv}", inline=False)

    embed.set_footer(text="CardX Tools")

    await ctx.send(embed=embed)


bot.run(token) 
