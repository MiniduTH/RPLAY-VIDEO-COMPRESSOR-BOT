#    This file is part of the CompressorQueue distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from .worker import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🌋Pɪɴɢ = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    await event.reply(
        f"Hi `{event.sender.first_name}`\nThis is A RPLAY-COMPRESSOR-BOT Which Can Encode & compress Videos.\nReduce Size of Videos With Negligible Quality Change\nMAKE YOUR OVEN BOT IT'S DON'T WORK FOR YOU",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
                Button.url(
                    "MAKE YOUR",
                    url="github.com/Rplayoriginal/RPLAY-VIDEO-COMPRESSOR-BOT",
                ),
                Button.url("RENISH", url="t.me/renishrplay"),
            ],
            [
                Button.url(
                    "RPLAY ™ MOVIE",
                    url="t.me/rplaymovie",
                ),
                Button.url(
                    "RPLAY ™ STICKERS",
                    url="t.me/addstickers/Rplay_movies_stickers_by_stickersthiefbot",
                ),
            ],
            [
                Button.url(
                    "SUPPORT",
                    url="t.me/rplay_support",
                ),
                Button.url(
                    "DONATE",
                    url="www.paypal.com/signin?returnUri=https%3A%2F%2Fwww.paypal.com%2Fmyaccount%2Ftransfer%2Fhomepage%2Fexternal%2Fprofile%3FflowContextData%3DMTmBtYhrkZP8YFR-JHtgXOUrxejjPEh9HS56sk7xZrppgt-1uDDEe4amvWiOxFkKxbAfcNKLkf7viZbjvFboJ6NIosgnmFsJ9djlWz06a3lBM4QCkVCaxInU-S1wnY2bywgHXq0QGfQBVuzKD3iLj25qfqWugUxLezZC4-2qEwkHwkWlB6CwIycu5bvyC4IxsO29MpDtWfojP9Rf3xwQJzxrsE3dEHGenrO9rTGkJlfimzCwFJbOEHVFCzo9ZpU5cMrR70qBd-FX6LIC&onboardData=%7B%22country.x%22%3A%22CD%22%2C%22locale.x%22%3A%22en_US%22%2C%22intent%22%3A%22paypalme%22%2C%22redirect_url%22%3A%22https%253A%252F%252Fwww.paypal.com%252Fmyaccount%252Ftransfer%252Fhomepage%252Fexternal%252Fprofile%253FflowContextData%253DMTmBtYhrkZP8YFR-JHtgXOUrxejjPEh9HS56sk7xZrppgt-1uDDEe4amvWiOxFkKxbAfcNKLkf7viZbjvFboJ6NIosgnmFsJ",
                ),
            ],
        ],
    )


async def help(event):
    await event.reply(
        "**🐠 A Quality CompressorQueue**\n\n+This Bot Compress Videos With Negligible Quality Change.\n+Easy to Use\n-Due to Quality Settings Bot Takes Time To Compress.\nSo Be patience Nd Send videos One By One After Completing.\nDont Spam Bot.\n\nJust Forward Video To Get Options"
    )


async def ihelp(event):
    await event.edit(
        "**🐠 A Quality CompressorQueue**\n\n+This Bot Compress Videos With Negligible Quality Change.\n+Easy to Use\n-Due to Quality Settings Bot Takes Time To Compress.\nSo Be patience Nd Send videos One By One After Completing.\nDont Spam Bot.\n\nJust Forward Video To Get Options",
        buttons=[Button.inline("BACK", data="beck")],
    )


async def beck(event):
    await event.edit(
        f"Hi `{event.sender.first_name}`\nThis is A RPLAY-COMPRESSOR-BOT Which Can Encode & compress Videos.\nReduce Size of Videos With Negligible Quality Change\nMAKE YOUR OVEN BOT IT'S DON'T WORK FOR YOU.",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
                Button.url(
                    "MAKE YOUR",
                    url="github.com/Rplayoriginal/RPLAY-VIDEO-COMPRESSOR-BOT",
                ),
                Button.url("RENISH", url="t.me/renishrplay"),
            ],
            [
                Button.url(
                    "RPLAY ™ MOVIE",
                    url="t.me/rplaymovie",
                ),
                Button.url(
                    "RPLAY ™ STICKERS",
                    url="t.me/addstickers/Rplay_movies_stickers_by_stickersthiefbot",
                ),
            ],
            [
                Button.url(
                    "SUPPORT",
                    url="t.me/rplay_support",
                ),
                Button.url(
                    "DONATE",
                    url="www.paypal.com/signin?returnUri=https%3A%2F%2Fwww.paypal.com%2Fmyaccount%2Ftransfer%2Fhomepage%2Fexternal%2Fprofile%3FflowContextD",
                ),
            ],
        ],
    )
