from Token import *
from Commands import *
from MemberTracker import *

import discord

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.mTracker = MemberManagement()
        
    async def on_ready(self) -> None:
        self.mTracker.on_ready(self)

    async def on_message(self, message: discord.Message) -> None:
        if (message.author == self.user): return
        
        guild = message.guild
        serverName = guild.name
        
        if (self.start_with(message, "neofetch")):
            await self.send_message(message, format_message(serverName, "neofetch", neofetch(guild)))

        if (self.start_with(message, "ls")):
            await self.send_message(message, format_message(serverName, "ls", ls(self.mTracker.get_all_usernames())))
            
        if message.content.startswith("echo"):
            if message.content.endswith(" | rev"):
                reversed_content = message.content[5:-6][::-1]
                await message.channel.send(reversed_content)
            else:
                await message.channel.send(message.content[5:])
        
    async def on_member_join(self, message) -> None:
        await self.mTracker.on_member_join(message)
        
    async def on_member_remove(self, message) -> None:
        await self.mTracker.on_member_remove(message)

    async def send_message(self, message: discord.Message, contents: str) -> None:
        await message.channel.send(contents) 
        
    def start_with(self, message: discord.Message, prefix: str) -> bool:
        return message.content.startswith(prefix)
        
def main():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    
    bot = MyClient(intents=intents)
    bot.run(TOKEN)
    
    return

if (__name__ == "__main__"):
    main()