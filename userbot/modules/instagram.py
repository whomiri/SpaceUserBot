import asyncio
from userbot.events import register
import os
import requests

@register(pattern="^.instagram (.*)",outgoing=True)
@register(pattern="^.whoin (.*)",outgoing=True)
async def whoin(event):
    username = event.pattern_match.group(1)
    last = username.lower()
    try:
        await event.edit(LANG['INFO_STATUS'])
        os.system("pip install instaloader")
        import instaloader
        L = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(L.context, last)
        pp = profile.get_profile_pic_url()
        ad = profile.full_name
        if not ad:
          ad = "Bu istifadəçinin ad qoymağa ehtiyyacı var."
        bio = profile.biography
        if not bio:
          bio = "Bu istifadəçinin bio qoymağa ehtiyyacı var."
        follover = profile.followers
        res = profile.is_verified
        post = profile.mediacount
        folloving = profile.followees
        url = profile.external_url
        biznes = profile.is_business_account
        gizli = profile.is_private
        space = profile.userid
        r = requests.get(pp) 
        with open("oyeman.jpg", "wb")as file: 
          file.write(r.content) 
        igtv = profile.igtvcount
        msg = f'''
       **USER INFO:**
         **Username:** [{last}](https://instagram.com/{last})
         **ID:** `{space}`
         **Name:** `{ad}`
         **Bio:** `{bio}`
         **Followers:** `{follover}`
         **Following:** `{folloving}`
         **Post sayı:** `{post}`
         **IgTv sayı:** `{igtv}`
         **Account verified:** `{res}`
         **Url:** `{url}`
         **Private(gizli) hesap:** `{gizli}`
         **Biznes hesabı?:** `{biznes}`
           '''
        await event.delete()
        await event.client.send_file(event.chat_id,"oyeman.jpg",caption=msg)
        os.remove("oyeman.jpg")
    except:
        await event.edit("xəta")
