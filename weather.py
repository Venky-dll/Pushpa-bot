import requests
from discord.ext import commands


@commands.command(name='weather')
async def weather(ctx, city):
    weather_info = get_weather(city)
    await ctx.send(f'Weather in {city}: {weather_info}')


def get_weather(city):
    url = f'http://wttr.in/{city}?format=3'
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip()
    else:
        return f'Unable to retrieve weather information for {city}.'