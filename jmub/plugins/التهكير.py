import asyncio

from jmub import jmub

from ..core.managers import edit_or_reply
from ..helpers.utils import _format
from . import ALIVE_NAME


@jmub.ar_cmd(pattern="تهكير$")
async def _(event):
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        idd = reply_message.sender_id
        if idd == 5607917250:
            await edit_or_reply(event, "هذا مطوري\nلا يمكنني اختراق روسيا يمغفل")
        else:
            event = await edit_or_reply(event, "- يتم التهكير انتظر قليلا")
            animation_chars = [
                "يتم الربط بالسيرفرات الخاصة بالاختراق ",
                "تم تحديد الضحيه بنجاح",
                "جار الاختراق... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "جار الاختراق... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "جار الاختراق... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "جار الاختراق... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "جار الاختراق... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "جار الاختراق... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "جار الاختراق... 84%\n█████████████████████▒▒▒▒ ",
                "جار الاختراق... 100%\n████████████████████████ ",
                f"حساب الضحيه تم اختراقه بنجاح...\n\nادفع 69$ الى  {ALIVE_NAME} . لحذف هذا التهكير",
            ]
            animation_interval = 3
            animation_ttl = range(11)
            for i in animation_ttl:
                await asyncio.sleep(animation_interval)
                await event.edit(animation_chars[i % 11])
    else:
        await edit_or_reply(
            event,
            "لم يتم التعرف المستخدم \nلا يمكنني اختراق الحساب ",
            parse_mode=_format.parse_pre,
        )


