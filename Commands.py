import discord
from typing import List

SHELL_PROMPT = "pengu@pengu_os"

# ====== Helper Commands ====== #

# create funky shell prompt
def shell_prompt(serverName: str) -> str:
    return f"{SHELL_PROMPT}:~/{serverName}$"

# create a string in the format of linux terminal
def format_message(serverName: str, command: str, content: str) -> str:
    comment = f"```dos\n{shell_prompt(serverName)} {command}\n{content}```"
    return comment

# gets all roles and puts them into a string
def get_roles(roles: discord.Guild.roles) -> str:
    return ", ".join([role.name for role in roles])


# ====== Linux Commands ====== #

# list all contents in format of linux terminal as a string
def ls(list: List[str]) -> str:
    contents = []

    for x in list:
        contents.append(x)

    sortedContents = sorted(contents)

    # wrap contents in quotes with spaces
    for i, content in enumerate(sortedContents):
        if (any(char.isspace() for char in content)):
            sortedContents[i] = (f"'{content}'")
        
    return ' '.join(sortedContents)

# funky linux neofetch
def neofetch(serverInfo: discord.Guild) -> str:
    return f"""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀ ⢀⣀⣀⣀⣀⣀⣀⡀⡄⣄⡀⣄⣀⡀⣀⠀⠀⢀⣠⣤⣤⣤⣤⣠⣤     {SHELL_PROMPT}
⠀⠄⠠⠀⠄⠠⠀⠄⠠⠀⠄⠠⠀⠄⠠⠀⠄⣀⣤⣴⣶⡿⢿⡻⢟⡻⣛⡟⡟⣷⢶⣤⣄⡀⠀⢀⠀⠠⢀⠀⢰⣿⣿⣿⣿⣿⣿     -------------
⠠⠈⢀⠐⠀⠂⠐⠀⠂⠐⠀⠂⢀⢂⣤⣶⣿⣿⢿⢯⣷⣹⢧⣻⣭⣳⣝⣾⣱⣏⡾⣭⣟⣿⣷⣤⡀⠂⢀⠠⢸⣿⣿⣿⣿⣿⣿     Server Name: {serverInfo.name}
⠀⡐⠀⠠⠈⠀⠂⠁⠐⠈⠀⢰⣴⣿⣿⣿⣯⣿⣯⣿⣾⣽⣿⣷⣿⣷⣿⣾⣷⣯⣿⣳⣟⣾⣽⣟⣿⣦⠀⠀⣾⣿⣿⣿⣿⣿⣿     Description: {serverInfo.description} 
⠀⡀⠐⠀⡀⠁⠠⠈⠀⢠⣵⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣯⣿⢿⣿⣿⣷⡀⣿⣿⣿⣿⣿⣿⣿     Member Count: {serverInfo.member_count} 
⠀⢀⠐⠀⠀⠐⠀⠀⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿     Roles: {get_roles(serverInfo.roles)}
⠀⠀⡀⠀⠁⠀⠀⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠙⢿⣿⣿⣿⣿     
⠀⠀⠀⢀⠀⠁⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠁⣀⡉⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠈⠛⠿⣿
⠀⠀⠁⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀⠠⣾⣿⣿⣷⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⢾
⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠻⠿⠿⠋⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⢸
⠀⠀⠀⠀⠀⠸⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢯⣛⢷⣲⣾
⠀⠀⠀⠀⠀⢰⡏⢠⣍⢿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⣷⣯⣿
⠀⠀⠀⠀⠀⠈⢳⣸⣿⡞⣿⣿⣿⣿⡟⢯⠹⡘⠦⡉⢖⡡⢏⡿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣷⣿
⠀⠀⠀⠀⠀⠀⠀⢳⡛⢃⣿⣿⠿⣭⡙⢆⢣⡙⠴⣉⢦⡹⣎⣷⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⢏⡿⣴⡹⣎⢦⣝⣮⣳⢯⣷⣻⢾⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⢯⢾⣵⣻⣽⣻⣞⡷⣯⣟⡾⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣯⢟⣼⣳⣳⢯⢾⣝⣳⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠘⠿⢶⣭⡷⠯⠟⠚⢛⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⢀⣾⣿⣿⣿⣿⡟⠁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠛⠛⠛⠛⠛⠛⠛⠛⠀⠀⠀
    """