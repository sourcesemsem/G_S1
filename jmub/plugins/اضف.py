# jmub-Thon
# Copyright (C) 2022 jmub-Thon . All Rights Reserved
#
# This file is a part of < https://github.com/jmub-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/jmub-Thon/ZelZal/blob/main/LICENSE/>.

""" وصـف الملـف : اوامـر اضـافة الفـارات باللغـة العربيـة كـاملة ولا حـرف انكلـش🤘 تخمـط اذكـر المصـدر يولـد
اضـافة فـارات صـورة ( الحمايـة - الفحـص - الوقتـي ) بـ امـر واحـد فقـط
حقـوق للتـاريخ : @FTTUTY
@zzzzl1l - كتـابـة الملـف :  زلــزال الهيبــه"""
#زلـزال_الهيبـه يولـد هههههههههههههههههههههههههه

import asyncio
import math
import os

import heroku3
import requests
import urllib3
import random
import string
from datetime import datetime

from PIL import Image
from telegraph import Telegraph, exceptions, upload_file
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_display_name
from urlextract import URLExtract

from jmub import jmub

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import delete_conv
from ..sql_helper.globals import addgvar, delgvar, gvarstatus

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY
from . import BOTLOG_CHATID, mention


plugin_category = "الادوات"
LOGS = logging.getLogger(__name__)

extractor = URLExtract()
telegraph = Telegraph()
r = telegraph.create_account(short_name=Config.TELEGRAPH_SHORT_NAME)
auth_url = r["auth_url"]


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")


ZelzalVP_cmd = (
    "𓆩 [سۅٛࢪس سيمـو - اوامـر الفـارات](t.me/FTTUTY) 𓆪\n\n"
    "**⎉╎قائـمه اوامر تغييـر فـارات الصـور بأمـر واحـد فقـط - لـ اول مـره ع سـورس تليثـون يوزر بـوت 🦾 :** \n\n"
    "⪼ `.اضف صورة الحماية` بالـرد ع صـورة او ميديـا\n\n"
    "⪼ `.اضف صورة الفحص` بالـرد ع صـورة او ميديـا\n\n"
    "⪼ `.اضف صورة الوقتي` بالـرد ع صـورة او ميديـا\n\n"
    "⪼ `.اضف صورة الاوامر` بالـرد ع صـورة او ميديـا\n\n"
    "⪼ `.اضف صورة السورس` بالـرد ع صـورة او ميديـا\n\n"
    "⪼ `.اضف صورة الكتم` بالـرد ع صـورة او ميديـا\n\n"
    "⪼ `.اضف صورة البوت` بالـرد ع صـورة او ميديـا لـ اضـافة صـورة ستـارت للبـوت\n\n"
    "⪼ `.اوامر الفارات` لعـرض بقيـة اوامـر الفـارات\n\n\n"
    "**⎉╎قائـمه اوامر تغييـر كليشـة الايـدي :** \n\n"
    "⪼ `.اضف ايموجي الايدي` بالـرد ع الرمـز او الايموجـي\n\n"
    "⪼ `.اضف عنوان الايدي` بالـرد ع نـص العنـوان\n\n"
    "⪼ `.اضف خط الايدي` بالـرد ع الخـط او المستقيـم\n\n\n"
    "**⎉╎قائـمه اوامر تغييـر بقيـة الفـارات بأمـر واحـد فقـط :** \n\n"
    "⪼ `.اضف كليشة الحماية` بالـرد ع الكليشـة\n\n"
    "⪼ `.اضف كليشة الفحص` بالـرد ع الكليشـة\n\n"
    "⪼ `.اضف كليشة الحظر` بالـرد ع الكليشـة\n\n"
    "⪼ `.اضف كليشة البوت` بالـرد ع الكليشـة لـ اضـافة كليشـة ستـارت\n\n"
    "⪼ `.اضف رمز الوقتي` بالـرد ع رمـز\n\n"
    "⪼ `.اضف زخرفة الوقتي` بالـرد ع ارقـام الزغـرفه\n\n"
    "⪼ `.اضف البايو الوقتي` بالـرد ع البـايـو\n\n"
    "⪼ `.اضف اسم المستخدم` بالـرد ع اسـم\n\n"
    "⪼ `.اضف كروب الرسائل` بالـرد ع ايدي الكـروب\n\n"
    "⪼ `.اضف كروب السجل` بالـرد ع ايدي الكـروب\n\n"
    "⪼ `.اضف ايديي` بالـرد ع ايدي حسـابك\n\n"
    "⪼ `.اضف نقطة الاوامر` بالـرد ع الـرمز الجديـد\n\n"
    "⪼ `.اضف رسائل الحماية` بالـرد ع رقـم لعدد رسائل تحذيـرات حماية الخاص\n\n\n"
    "⪼ `.جلب` + اسـم الفـار\n\n"
    "⪼ `.حذف` + اسـم الفـار\n\n"
    "⪼ `.رفع مطور` بالـرد ع الشخـص لرفعـه مطـور تحكـم كامـل بالاوامـر\n\n"
    "⪼ `.حذف المطورين`\n\n"
    "**⎉╎قائـمه اوامر تغييـر المنطقـة الزمنيـة للوقـت 🌐:** \n\n"
    "⪼ `.وقت العراق` \n\n"
    "⪼ `.وقت اليمن` \n\n"
    "⪼ `.وقت سوريا` \n\n"
    "⪼ `.وقت مصر` \n\n"
    "🛃 سيتـم اضـافة المزيـد من الدول قريبـاً\n\n"
    "\n𓆩 [سۅٛࢪس سيمو - قنـاة الفـارات](https://t.me/FTTUTY) 𓆪"
)


# Copyright (C) 2022 jmub-Thon . All Rights Reserved
@jmub.ar_cmd(pattern=r"اضف (.*)")
async def variable(event):
    input_str = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    vinfo = reply.text
    jmub = await edit_or_reply(event, "**⎉╎جـاري اضـافة الفـار الـى بـوتك ...**")
    # All Rights Reserved for "jmub-Thon" "زلـزال الهيبـه"
    if input_str == "كليشة الفحص" or input_str == "كليشه الفحص":
        variable = "ALIVE_TEMPLATE"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_TEMPLATE") is None:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الان قـم بـ ارسـال الامـر ↶** `.فحص` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await jmub.edit("**⎉╎تم اضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الان قـم بـ ارسـال الامـر ↶** `.فحص` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("ALIVE_TEMPLATE", vinfo)
    elif input_str == "كليشة الحماية" or input_str == "كليشه الحمايه" or input_str == "كليشه الحماية" or input_str == "كليشة الحمايه":
        variable = "pmpermit_txt"
        await asyncio.sleep(1.5)
        if gvarstatus("pmpermit_txt") is None:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الان قـم بـ ارسـال الامـر ↶** `.الحمايه تفعيل` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await jmub.edit("**⎉╎تم اضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الان قـم بـ ارسـال الامـر ↶** `.الحمايه تفعيل` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("pmpermit_txt", vinfo)
    elif input_str == "كليشة البوت" or input_str == "كليشه البوت":
        variable = "START_TEXT"
        await asyncio.sleep(1.5)
        if gvarstatus("START_TEXT") is None:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الان قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await jmub.edit("**⎉╎تم اضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الان قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("START_TEXT", vinfo)
    elif input_str == "كليشة الحظر" or input_str == "كليشه الحظر":
        variable = "pmblock"
        await asyncio.sleep(1.5)
        if gvarstatus("pmblock") is None:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الان قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await jmub.edit("**⎉╎تم اضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الان قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("pmblock", vinfo)
    elif input_str == "رمز الوقتي" or input_str == "رمز الاسم الوقتي":
        variable = "CUSTOM_ALIVE_EMjmub"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_EMjmub") is None:
            addgvar(variable, vinfo)
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الـرمـز الجـديـد** \n {} \n\n**⎉╎الان قـم بـ ارسـال الامـر ↶** `.الاسم تلقائي` **لـ التحقـق مـن الـرمز . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await jmub.edit("**⎉╎تم اضـافـة {} بنجـاح ☑️**\n**⎉╎الـرمـز المضـاف** \n {} \n\n**⎉╎الان قـم بـ ارسـال الامـر ↶** `.الاسم تلقائي` **لـ التحقـق مـن الـرمز . .**".format(input_str, vinfo))
    elif input_str == "البايو" or input_str == "البايو الوقتي" or input_str == "النبذه" or input_str == "البايو تلقائي":
        variable = "DEFAULT_BIO"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_BIO") is None:
            addgvar(variable, vinfo)
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎البـايـو الجـديـد** \n {} \n\n**⎉╎الان قـم بـ ارسـال الامـر ↶** `.البايو تلقائي` **لـ التحقـق مـن البايـو . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await jmub.edit("**⎉╎تم اضـافه {} بنجـاح ☑️**\n**⎉╎البـايـو المضـاف** \n {} \n\n**⎉╎الان قـم بـ ارسـال الامـر ↶** `.البايو تلقائي` **لـ التحقـق مـن البايـو . .**".format(input_str, vinfo))
    elif input_str == "كاشف الاباحي" or input_str == "كشف الاباحي":
        variable = "DEEP_API"
        await asyncio.sleep(1.5)
        if gvarstatus("DEEP_API") is None:
            addgvar(variable, vinfo)
            await jmub.edit("**⎉╎تم تغييـر توكـن {} بنجـاح ☑️**\n**⎉╎التوكـن الجـديـد** \n {} \n\n**⎉╎الان قـم بـ ارسـال الامـر ↶** `.قفل الاباحي` **لـ تفعيـل كاشـف الاباحي . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await jmub.edit("**⎉╎تم إضافـة توكـن {} بنجـاح ☑️**\n**⎉╎التوكـن المضـاف** \n {} \n\n**⎉╎الان قـم بـ ارسـال الامـر ↶** `.قفل الاباحي` **لـ تفعيـل كاشـف الاباحي . .**".format(input_str, vinfo))
    elif input_str == "ايموجي الايدي" or input_str == "ايموجي ايدي" or input_str == "رمز الايدي" or input_str == "رمز ايدي" or input_str == "الرمز ايدي":
        variable = "CUSTOM_ALIVE_EMOJI"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_EMOJI") is None:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الان** `.ايدي`".format(input_str, vinfo))
        else:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الان** `.ايدي`".format(input_str, vinfo))
        addgvar("CUSTOM_ALIVE_EMOJI", vinfo)
    elif input_str == "عنوان الايدي" or input_str == "عنوان ايدي":
        variable = "CUSTOM_ALIVE_TEXT"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_TEXT") is None:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الان** `.ايدي`".format(input_str, vinfo))
        else:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الان** `.ايدي`".format(input_str, vinfo))
        addgvar("CUSTOM_ALIVE_TEXT", vinfo)
    elif input_str == "خط الايدي" or input_str == "خط ايدي" or input_str == "خطوط الايدي" or input_str == "خط ايدي":
        variable = "CUSTOM_ALIVE_FONT"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_FONT") is None:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الان** `.ايدي`".format(input_str, vinfo))
        else:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الان** `.ايدي`".format(input_str, vinfo))
        addgvar("CUSTOM_ALIVE_FONT", vinfo)
    elif input_str == "اشتراك الخاص" or input_str == "اشتراك خاص":
        variable = "Custom_Pm_Channel"
        await asyncio.sleep(1.5)
        if gvarstatus("Custom_Pm_Channel") is None:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الان** `.اشتراك خاص`".format(input_str, vinfo))
        else:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الان** `.اشتراك خاص`".format(input_str, vinfo))
        delgvar("Custom_Pm_Channel")
        addgvar("Custom_Pm_Channel", vinfo)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#قنـاة_الاشتـراك_الاجبـاري_للخـاص\
                        \n**- القنـاة {input_str} تم اضافتهـا في قاعده البيانات ..بنجـاح ✓**",
            )
    elif input_str == "اشتراك كروب" or input_str == "اشتراك الكروب":
        variable = "Custom_G_Channel"
        await asyncio.sleep(1.5)
        if gvarstatus("Custom_G_Channel") is None:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الان** `.اشتراك كروب`".format(input_str, vinfo))
        else:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الان** `.اشتراك كروب`".format(input_str, vinfo))
        delgvar("Custom_G_Channel")
        addgvar("Custom_G_Channel", vinfo)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#قنـاة_الاشتـراك_الاجبـاري_للكـروب\
                        \n**- القنـاة {input_str} تم اضافتهـا في قاعده البيانات ..بنجـاح ✓**",
            )
    elif input_str == "اسم المستخدم" or input_str == "الاسم":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ")

        if Config.HEROKU_APP_NAME is not None:
            app = Heroku.app(Config.HEROKU_APP_NAME)
        else:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.")
        heroku_var = app.config()
        variable = "ALIVE_NAME"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await jmub.edit("**⎉╎تم اضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo

    elif input_str == "رسائل الحماية" or input_str == "رسائل الحمايه" or input_str == "رسائل الخاص" or input_str == "رسائل حماية الخاص" or input_str == "عدد التحذيرات":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "✾╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ")

        if Config.HEROKU_APP_NAME is not None:
            app = Heroku.app(Config.HEROKU_APP_NAME)
        else:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.")
        heroku_var = app.config()
        variable = "MAX_FLOOD_IN_PMS"
        await asyncio.sleep(1.5)
        if vinfo.isdigit():
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            return await jmub.edit("**⎉╎خطـأ .. قم بالـرد ع رقـم فقـط ؟!**")
        heroku_var[variable] = vinfo

    elif input_str == "كروب الرسائل" or input_str == "كروب التخزين" or input_str == "كروب الخاص":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ")

        if Config.HEROKU_APP_NAME is not None:
            app = Heroku.app(Config.HEROKU_APP_NAME)
        else:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.")
        heroku_var = app.config()
        variable = "PM_LOGGER_GROUP_ID"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await jmub.edit("**⎉╎تم اضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "السجل" or input_str == "كروب السجل":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ")

        if Config.HEROKU_APP_NAME is not None:
            app = Heroku.app(Config.HEROKU_APP_NAME)
        else:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.")
        heroku_var = app.config()
        variable = "PRIVATE_GROUP_BOT_API_ID"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await jmub.edit("**⎉╎تم اضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "السجل 2" or input_str == "كروب السجل 2":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ")

        if Config.HEROKU_APP_NAME is not None:
            app = Heroku.app(Config.HEROKU_APP_NAME)
        else:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.")
        heroku_var = app.config()
        variable = "PRIVATE_GROUP_ID"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await jmub.edit("**⎉╎تم اضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "قناة السجل" or input_str == "قناة السجلات":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ")

        if Config.HEROKU_APP_NAME is not None:
            app = Heroku.app(Config.HEROKU_APP_NAME)
        else:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.")
        heroku_var = app.config()
        variable = "PRIVATE_CHANNEL_BOT_API_ID"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await jmub.edit("**⎉╎تم اضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "قناة الملفات" or input_str == "قناة الاضافات":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ")

        if Config.HEROKU_APP_NAME is not None:
            app = Heroku.app(Config.HEROKU_APP_NAME)
        else:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.")
        heroku_var = app.config()
        variable = "PLUGIN_CHANNEL"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await jmub.edit("**⎉╎تم اضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "ايديي" or input_str == "ايدي الحساب":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ")

        if Config.HEROKU_APP_NAME is not None:
            app = Heroku.app(Config.HEROKU_APP_NAME)
        else:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.")
        heroku_var = app.config()
        variable = "OWNER_ID"
        await asyncio.sleep(1.5)
        if vinfo.isdigit():
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            return await jmub.edit("**⎉╎خطـأ .. قم بالـرد ع رقـم فقـط ؟!**")
        heroku_var[variable] = vinfo
    elif input_str == "نقطة الاوامر" or input_str == "نقطه الاوامر":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ")

        if Config.HEROKU_APP_NAME is not None:
            app = Heroku.app(Config.HEROKU_APP_NAME)
        else:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.")
        heroku_var = app.config()
        variable = "COMMAND_HAND_LER"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await jmub.edit("**⎉╎تم اضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "التوكن" or input_str == "توكن البوت":
        variable = "TG_BOT_TOKEN"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await jmub.edit("**⎉╎تم اضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "معرف البوت" or input_str == "معرف بوت":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ")

        if Config.HEROKU_APP_NAME is not None:
            app = Heroku.app(Config.HEROKU_APP_NAME)
        else:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.")
        heroku_var = app.config()
        variable = "TG_BOT_USERNAME"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await jmub.edit("**⎉╎تم اضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "الريبو" or input_str == "السورس":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ")

        if Config.HEROKU_APP_NAME is not None:
            app = Heroku.app(Config.HEROKU_APP_NAME)
        else:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.")
        heroku_var = app.config()
        variable = "UPSTREAM_REPO"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await jmub.edit("**⎉╎تم اضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "توكن المكافح" or input_str == "كود المكافح" or input_str == "مكافح التخريب" or input_str == "مكافح التفليش":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ")

        if Config.HEROKU_APP_NAME is not None:
            app = Heroku.app(Config.HEROKU_APP_NAME)
        else:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.")
        heroku_var = app.config()
        variable = "SPAMWATCH_API"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await jmub.edit("**⎉╎تم اضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "توكن الذكاء" or input_str == "مفتاح الذكاء" or input_str == "الذكاء":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ")
        if Config.HEROKU_APP_NAME is not None:
            app = Heroku.app(Config.HEROKU_APP_NAME)
        else:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.")
        heroku_var = app.config()
        variable = "OPENAI_API_KEY"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await jmub.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await jmub.edit("**⎉╎تم اضافـة {} بنجـاح ☑️** \n**⎉╎المضاف اليه :**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    else:
        if input_str:
            return await jmub.edit("**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))

        return await edit_or_reply(event, "**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))



# Copyright (C) 2022 jmub-Thon . All Rights Reserved
@jmub.ar_cmd(pattern="حذف(?:\s|$)([\s\S]*)")
async def variable(event):
    if Config.HEROKU_API_KEY is None:
        return await ed(
            event,
            "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ",
        )
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await ed(
            event,
            "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.",
        )
    input_str = event.text[5:]
    heroku_var = app.config()
    jmub = await edit_or_reply(event, "**⎉╎جـاري حـذف الفـار مـن بـوتك 🚮...**")
    # All Rights Reserved for "jmub-Thon" "زلـزال الهيبـه"
    if input_str == "كليشة الفحص" or input_str == "كليشه الفحص":
        variable = gvarstatus("ALIVE_TEMPLATE")
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_TEMPLATE") is None:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, variable))
        delgvar("ALIVE_TEMPLATE")
        
    elif input_str == "كليشة الحماية" or input_str == "كليشه الحمايه" or input_str == "كليشه الحماية" or input_str == "كليشة الحمايه":
        variable = gvarstatus("pmpermit_txt")
        await asyncio.sleep(1.5)
        if gvarstatus("pmpermit_txt") is None:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, variable))
        delgvar("pmpermit_txt")

    elif input_str == "كليشة البوت" or input_str == "كليشه البوت":
        variable = gvarstatus("START_TEXT")
        await asyncio.sleep(1.5)
        if gvarstatus("START_TEXT") is None:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, variable))
        delgvar("START_TEXT")

    elif input_str == "كليشة الحظر" or input_str == "كليشه الحظر":
        variable = gvarstatus("pmblock")
        await asyncio.sleep(1.5)
        if gvarstatus("pmblock") is None:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, variable))
        delgvar("pmblock")

    elif input_str == "صورة الفحص" or input_str == "صوره الفحص":
        variable = "ALIVE_PIC"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_PIC") is None:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("ALIVE_PIC")

    elif input_str == "صورة الاوامر" or input_str == "صوره الاوامر":
        variable = "CMD_PIC"
        await asyncio.sleep(1.5)
        if gvarstatus("CMD_PIC") is None:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("CMD_PIC")

    elif input_str == "صورة السورس" or input_str == "صوره السورس":
        variable = "ALIVE_PIC"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_PIC") is None:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("ALIVE_PIC")

    elif input_str == "صورة الكتم" or input_str == "صوره الكتم":
        variable = "KTM_PIC"
        await asyncio.sleep(1.5)
        if gvarstatus("KTM_PIC") is None:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("KTM_PIC")

    elif input_str == "صورة البوت" or input_str == "صوره البوت":
        variable = "BOT_START_PIC"
        await asyncio.sleep(1.5)
        if gvarstatus("BOT_START_PIC") is None:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
        delgvar("BOT_START_PIC")

    elif input_str == "صورة الحماية" or input_str == "صوره الحمايه" or input_str == "صورة الحمايه" or input_str == "صوره الحماية":
        variable = "pmpermit_pic"
        await asyncio.sleep(1.5)
        if gvarstatus("pmpermit_pic") is None:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        delgvar("pmpermit_pic")
        await jmub.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))

    elif input_str == "صورة الوقتي" or input_str == "صوره الوقتي":
        variable = gvarstatus("DIGITAL_PIC")
        await asyncio.sleep(1.5)
        if gvarstatus("DIGITAL_PIC") is None:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, variable))
        delgvar("DIGITAL_PIC")

    elif input_str == "رمز الوقتي" or input_str == "رمز الاسم الوقتي":
        variable = "CUSTOM_ALIVE_EMjmub"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_EMjmub") is None:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        delgvar("CUSTOM_ALIVE_EMjmub")
        await jmub.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
    elif input_str == "زخرفه الوقتي" or input_str == "زخرفة الوقتي":
        variable = "ZI_FN"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]
    elif input_str == "رسائل الحماية" or input_str == "رسائل الحمايه" or input_str == "رسائل الخاص" or input_str == "رسائل حماية الخاص" or input_str == "عدد التحذيرات":
        variable = "MAX_FLOOD_IN_PMS"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]
    elif input_str == "البايو" or input_str == "البايو الوقتي" or input_str == "النبذه الوقتيه":
        variable = "DEFAULT_BIO"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_BIO") is None:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        delgvar("DEFAULT_BIO")
        await jmub.edit("**⎉╎تم حـذف فـار {} . . بنجـاح ☑️**".format(input_str))
    elif input_str == "اسم المستخدم" or input_str == "الاسم":
        variable = "ALIVE_NAME"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]
    elif input_str == "كروب الرسائل" or input_str == "كروب التخزين" or input_str == "كروب الخاص":
        variable = "PM_LOGGER_GROUP_ID"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "السجل" or input_str == "كروب السجل":
        variable = "PRIVATE_GROUP_BOT_API_ID"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "السجل 2" or input_str == "كروب السجل 2":
        variable = "PRIVATE_GROUP_ID"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "قناة السجل" or input_str == "قناة السجلات":
        variable = "PRIVATE_CHANNEL_BOT_API_ID"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "قناة الملفات" or input_str == "قناة الاضافات":
        variable = "PLUGIN_CHANNEL"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "ايديي" or input_str == "ايدي الحساب":
        variable = "OWNER_ID"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "نقطة الاوامر" or input_str == "نقطه الاوامر":
        variable = "COMMAND_HAND_LER"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "التوكن" or input_str == "توكن البوت":
        variable = "TG_BOT_TOKEN"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "معرف البوت" or input_str == "معرف بوت":
        variable = "TG_BOT_USERNAME"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "الريبو" or input_str == "السورس":
        variable = "UPSTREAM_REPO"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "اسمي التلقائي" or input_str == "الاسم التلقاائي":
        variable = "AUTONAME"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت  سـيـمـو يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]
    elif input_str == "ايموجي الايدي" or input_str == "ايموجي ايدي" or input_str == "رمز الايدي" or input_str == "رمز ايدي" or input_str == "الرمز ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_EMOJI")
        await asyncio.sleep(1.5)
        if variable is None:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}`".format(input_str, variable))
        delgvar("CUSTOM_ALIVE_EMOJI")
    elif input_str == "عنوان الايدي" or input_str == "عنوان ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_TEXT")
        await asyncio.sleep(1.5)
        if variable is None:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}`".format(input_str, variable))
        delgvar("CUSTOM_ALIVE_TEXT")
    elif input_str == "خط الايدي" or input_str == "خط ايدي" or input_str == "خطوط الايدي" or input_str == "خط ايدي":
        variable = gvarstatus("CUSTOM_ALIVE_FONT")
        await asyncio.sleep(1.5)
        if variable is None:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}`".format(input_str, variable))
        delgvar("CUSTOM_ALIVE_FONT")
    elif input_str == "كاشف الاباحي" or input_str == "كشف الاباحي":
        variable = gvarstatus("DEEP_API")
        await asyncio.sleep(1.5)
        if variable is None:
        	return await jmub.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة فـار {} اصـلاً...**".format(input_str))
        await jmub.edit("**⎉╎تم حـذف {} بنجـاح ☑️**\n**⎉╎المتغيـر المحـذوف : ↶**\n `{}`".format(input_str, variable))
        delgvar("DEEP_API")
    else:
        if input_str:
            return await jmub.edit("**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))
        return await edit_or_reply(event, "**⎉╎عـذࢪاً .. لايوجـد هنالك فـار بإسـم {} ؟!.. ارسـل (.اوامر الفارات) لـعرض قائمـة الفـارات**".format(input_str))


# Copyright (C) 2022 jmub-Thon . All Rights Reserved
@jmub.ar_cmd(pattern="جلب(?:\s|$)([\s\S]*)")
async def custom_jmub(event):
    input_str = event.text[5:]
    jmub = await edit_or_reply(event, "**⎉╎جــاري جلـب معلـومـات الفــار 🛂. . .**")
    if (input_str == "كليشة الحماية" or input_str == "كليشة الحمايه" or input_str == "كليشه الحماية" or input_str == "كليشه الحمايه"):
        variable = gvarstatus("pmpermit_txt")
        if variable is None:
            await jmub.edit("**⎉╎فـار كليشـة الحمايـة غيـر موجـود ❌**\n**⎉╎لـ اضـافته بالـرد ع الكليشـة استخـدم الامـر : ↶**\n `.اضف كليشة الحماية` \n\n**⎉╎قنـاة السـورس : @FTTUTY**")
        else:
            await jmub.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @FTTUTY**".format(input_str, variable))
            
    elif input_str == "كليشة الفحص" or input_str == "كليشه الفحص":
        variable = gvarstatus("ALIVE_TEMPLATE")
        if variable is None:
            await jmub.edit("**⎉╎فـار كليشـة الفحص غيـر موجـود ❌**\n**⎉╎لـ اضـافته بالـرد ع الكليشـة استخـدم الامـر : ↶**\n `.اضف كليشة الفحص` \n\n**⎉╎قنـاة السـورس : @FTTUTY**")
        else:
            await jmub.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @FTTUTY**".format(input_str, variable))

    elif input_str == "كليشة البوت" or input_str == "كليشه البوت":
        variable = gvarstatus("START_TEXT")
        if variable is None:
            await jmub.edit("**⎉╎فـار كليشـة البـوت غيـر موجـود ❌**\n**⎉╎لـ اضـافته بالـرد ع الكليشـة استخـدم الامـر : ↶**\n `.اضف كليشة البوت` \n\n**⎉╎قنـاة السـورس : @FTTUTY**")
        else:
            await jmub.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @FTTUTY**".format(input_str, variable))

    elif input_str == "كليشة الحظر" or input_str == "كليشه الحظر":
        variable = gvarstatus("pmblock")
        if variable is None:
            await jmub.edit("**⎉╎فـار كليشـة الحظـر غيـر موجـود ❌**\n**⎉╎لـ اضـافته بالـرد ع الكليشـة استخـدم الامـر : ↶**\n `.اضف كليشة الحظر` \n\n**⎉╎قنـاة السـورس : @FTTUTY**")
        else:
            await jmub.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @FTTUTY**".format(input_str, variable))

    elif input_str == "رمز الوقتي" or input_str == "رمز الاسم الوقتي":
        variable = gvarstatus("CUSTOM_ALIVE_EMjmub")
        if variable is None:
            await jmub.edit("**⎉╎فـار رمـز الوقتـي غيـر موجـود ❌**\n**⎉╎لـ اضـافته بالـرد ع الرمـز استخـدم الامـر : ↶**\n `.اضف رمز الوقتي` \n\n**⎉╎قنـاة السـورس : @FTTUTY**")
        else:
            await jmub.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @FTTUTY**".format(input_str, variable))

    elif input_str == "كاشف الاباحي" or input_str == "كشف الاباحي":
        variable = gvarstatus("DEEP_API")
        if variable is None:
            await jmub.edit("**⎉╎فـار كشـف الاباحي غيـر موجـود ❌**\n**⎉╎لـ اضـافته بالـرد ع الكـود استخـدم الامـر : ↶**\n `.اضف كاشف الاباحي` \n\n**⎉╎قنـاة السـورس : @FTTUTY**")
        else:
            await jmub.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @FTTUTY**".format(input_str, variable))

    elif input_str == "البايو" or input_str == "البايو الوقتي" or input_str == "النبذه" or input_str == "البايو تلقائي":
        variable = gvarstatus("DEFAULT_BIO")
        if variable is None:
            await jmub.edit("**⎉╎فـار البايـو الوقتـي غيـر موجـود ❌**\n**⎉╎لـ اضـافته بالـرد ع نـص استخـدم الامـر : ↶**\n `.اضف البايو` \n\n**⎉╎قنـاة السـورس : @FTTUTY**")
        else:
            await jmub.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @FTTUTY**".format(input_str, variable))

    elif input_str == "اسم المستخدم" or input_str == "الاسم":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ")
        if Config.HEROKU_APP_NAME is not None:
            app = Heroku.app(Config.HEROKU_APP_NAME)
        else:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.")
        heroku_var = app.config()
        variable = "ALIVE_NAME"
        if variable not in heroku_var:
            await jmub.edit("**⎉╎فـار اسـم المستخـدم غيـر موجـود ❌**\n**⎉╎لـ اضـافته بالـرد ع الاسم استخـدم الامـر : ↶**\n `.اضف اسم المستخدم` \n\n**⎉╎قنـاة السـورس : @FTTUTY**")
        else:
            await jmub.edit("**⎉╎الفـار {} موجـود ☑️**\n**⎉╎قيمـة الفـار : ↶**\n `{}` \n\n**⎉╎قنـاة السـورس : @FTTUTY**".format(input_str, variable))

    elif input_str == "ايديي" or input_str == "ايدي الحساب":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك ف