import discord
import openpyxl
import datetime
import self
import asyncio
from discord.ext import commands
from discord.ext.commands import bot

bot = commands.Bot(command_prefix='!')


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("서버주소 Wdrpg.kr")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!명령어"):
        embed = discord.Embed(title="IRA ONLINE", description="명령어", color=0xff9900)
        embed.add_field(name="!명령어", value="명령어를 보실 수 있습니다!", inline=False)
        embed.add_field(name= "!후원", value="후원을 하시면 서버에 큰 힘이 됩니다!", inline = False)
        embed.add_field(name= "!카카오", value="많이 와주세요!", inline = False)
        embed.add_field(name= "!디스코드", value="패치노트를 확인하실 수 있습니다!", inline = False)
        embed.add_field(name= "!유튜브", value="구독해주시면 감사하겠습니다!", inline = False)
        embed.add_field(name= "!카페", value="많이 가입 해주세요!", inline = False)
        embed.add_field(name="!추방", value="해당 유저를 추방시킵니다.", inline=False)
        embed.add_field(name="!법전", value="서버의 법을 보실수 있어요!", inline=False)
        embed.add_field(name="!정보", value ="자신의 정보를 보실수 있어요!", inline = False)
        embed.add_field(name="/뮤트", value="해당 유저를 뮤트 시킵니다!", inline=False)
        embed.add_field(name="/언뮤트", value="해당 유저를 언뮤트 합니다!", inline=True)
        await message.channel.send(message.channel, embed=embed)
    if message.content.startswith("!정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(title="IRA ONLINE", color=0xff9900)
        embed.add_field(name="마인크래프트 닉네임", value="None", inline=True)
        embed.add_field(name="디스코드 닉네임", value=message.author.name, inline=True)
        embed.add_field(name="디스코드 가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        await message.channel.send(message.channel, embed=embed)
    if message.content.startswith("!후원"):
        await message.channel.send("https://skhcs.com/iraonline")
    if message.content.startswith("!카카오"):
        await message.channel.send("https://open.kakao.com/o/ghbYlgcc")
    if message.content.startswith("!디스코드"):
        await message.channel.send("https://discord.gg/w86dmVq")
    if message.content.startswith("!유튜브"):
        await message.channel.send("https://www.youtube.com/channel/UCpiL4aTHwPXENm24VdAFLXw")
    if message.content.startswith("!카페"):
        await message.channel.send("http://naver.me/GVbs0m8y")
    if message.content.startswith("!법전"):
        await message.channel.send("아직 미공개")



    if message.content.startswith("/뮤트"):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await author.add_roles(role)

    if message.content.startswith("/언뮤트"):
        author = message.guild.get_member(int(message.content[5:23]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await author.remove_roles(role)

    if (message.content.split(" ")[0] == "!추방"):
        if (message.author.guild_permissions.kick_members):
            try:
                user = message.guild.get_member(int(message.content.split(' ')[1][3:21]))
                reason = message.content[25:]
                if (len(message.content.split(" ")) == 2):
                    reason = "None"
                await user.send(embed=discord.Embed(title="[ 추방 ]",
                                                    description=f'당신은 {message.guild.name} 서버에서 추방당했습니다. 사유는 다음과 같습니다. ```{reason}```',
                                                    color=0xff0000))
                await user.kick(reason=reason)
                await message.channel.send(embed=discord.Embed(title="[ 추방 ]",
                                                               description=f"{message.author.mention} 님은 해당 서버에서 추방당하셨습니다. 사유:```{reason}```",
                                                               color=0x00ff00))
            except Exception as e:
                await message.channel.send(embed=discord.Embed(title="Error", description=str(e), color=0xff0000))
                return
        else:
            await message.channel.send(
                embed=discord.Embed(title="권한이 부족합니다.", description=message.author.mention + "님은 유저를 추방할 수 있는 권한이 없습니다.",
                                    color=0xff0000))
            return





client.run("NzExODUwNzYwMjgzMDk1MDcx.XsJA8A.91YjhPvGcJKX56Xh1ybb43clae8")