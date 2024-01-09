from dataclasses import dataclass
from typing import List

import discord

@dataclass
class Members:
    id: int = 0
    username: str = ""
    isBot: bool = False

class MemberManagement:
    def __init__(self):
        self.userData: List[Members] = []
        
    def on_ready(self, bot: discord.Client) -> None:
        for guild in bot.guilds:
            for member in guild.members:
                self.userData.append(Members(id=member.id, username=member.name, isBot=member.bot))
                
    def on_member_join(self, member: discord.Member) -> None:
        member_data = Members(id=member.id, username=member.name, isBot=member.bot)
        self.userData.append(member_data)
        
    def on_member_remove(self, member: discord.Member) -> None:
        for i, user in enumerate(self.userData):
            if (user.id == member.id):
                self.userData.pop(i)
        
    def get_all_users(self) -> List[Members]:
        return self.userData
    
    def get_all_usernames(self) -> List[str]:
        usernames = [user.username for user in self.userData]
        return usernames