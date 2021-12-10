import instaloader, glob, telebot, shutil

# YOUR BOT TOKEN HERE
bot_token = '******************************************'
bot = telebot.TeleBot(bot_token, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

# YOUR IG USERNAME & PASSWORD HERE
ig_user = 'USERNAME_HERE'
ig_pass = 'PASSWORD_HERE'

# DEFINE A FUNCTION TO LOGIN ONCE YOU RUN THE SCRIPT
def login_insta(ig_user, ig_pass):
    L = instaloader.Instaloader()
    L.login(ig_user, ig_pass)
    print('\n\n ****Login Successfull.****\n\n\n')
    return L

# /start & /help commands
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, 'Howdy, how are you doing? \nIt is a profile loader bot. (: \nJust send me the ID with or without @')

  
# TO PROCESS USER REQUESTS
@bot.message_handler()
def profile_get(message):
    id = message.text.lower().replace('@', '')
    bot.reply_to(message, f'Fetching profile picture for @{id}, wait...')
    print('ID: ',id)
    mod.download_profile(id, profile_pic_only=True)
    query = f'{id}/*.jpg'
    for file in glob.glob(query): pic = file
    pic = open(pic, 'rb')
    user_id = message.from_user.id
    bot.send_photo(user_id, pic)
    shutil.rmtree(id)
    
 # HAVE FUN (:
if (__name__ == '__main__'):
    mod = login_insta(ig_user, ig_pass)
    bot.infinity_polling()
