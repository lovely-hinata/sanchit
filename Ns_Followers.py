from pypasser import reCaptchaV3;from requests import*;import asyncio,websockets,names,time,random,telebot,json;from fake_useragent import UserAgent;from requests.utils import quote;from telebot import types as t
bot = telebot.TeleBot("7014906584:AAEnlVn3DvH1J4mqxCIxKWSbfCbksJuVp4M")
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, f"👋 Hello! Welcome to the Instagram Account Creator Bot!\n\nHere's how you can create an Instagram account effortlessly:\n1. Use the /create command to start the account creation process.😊\n2. Sit back and relax while we do the heavy lifting! 🛠️\n\nBY: [SANCHIT](tg://user_id=1866299978)",parse_mode="markdown")
@bot.message_handler(commands=['create'])
def sanchit(message):
    wait = bot.send_message(message.chat.id, f"<i>Creating An Account For You....!</i>", parse_mode="HTML")
    us = str(UserAgent().random)
    Country, Language = "US", "en"
    code = reCaptchaV3("https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfEUPkgAAAAAKTgbMoewQkWBEQhO2VPL4QviKct&co=aHR0cHM6Ly9oaTIuaW46NDQz&hl=en&v=8k85QBI-qzxmenDv318AZH30&size=invisible&cb=qd0swd9lds9t")
    new = post("https://hi2.in/api/new", data={"recaptcha": code}).json()
    exp, em, hash = new["expiry"], new["email"], new["hash"]
    datr = get("https://www.facebook.com/", headers={'user-agent': us}, timeout=30).text.split('["_js_datr","')[1].split('",')[0]
    r = get('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers={'user-agent': us}, timeout=30).cookies
    rex = get('https://www.instagram.com/', headers={'authority': 'www.instagram.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': f'{Language}-{Country},en-GB;q=0.9,en-US;q=0.8,en;q=0.7', 'cookie': f'dpr=3; csrftoken={r["csrftoken"]}; mid={r["mid"]}; ig_nrcb=1; ig_did={r["ig_did"]}; datr={datr}', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': us, 'viewport-width': '980'}, timeout=30)
    appid = rex.text.split('APP_ID":"')[1].split('"')[0]
    rollout = rex.text.split('rollout_hash":"')[1].split('"')[0]
    Headers = {'authority': 'www.instagram.com', 'accept': '*/*', 'accept-language': f'{Language}-{Country},en-GB;q=0.9,en-US;q=0.8,en;q=0.7', 'content-type': 'application/x-www-form-urlencoded', 'cookie': f'dpr=3; csrftoken={r["csrftoken"]}; mid={r["mid"]}; ig_nrcb=1; ig_did={r["ig_did"]}; datr={datr}', 'origin': 'https://www.instagram.com', 'referer': 'https://www.instagram.com/accounts/signup/email/', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': us, 'viewport-width': '360', 'x-asbd-id': '198387', 'x-csrftoken': r["csrftoken"], 'x-ig-app-id': str(appid), 'x-ig-www-claim': '0', 'x-instagram-ajax': str(rollout), 'x-requested-with': 'XMLHttpRequest', 'x-web-device-id': r["ig_did"]}
    send = post("https://www.instagram.com/api/v1/accounts/send_verify_email/", headers=Headers, data={'device_id': Headers['cookie'].split('mid=')[1].split(';')[0], 'email': em}, timeout=30)    
    asyncio.run(connect(Headers, exp, em, hash, message, wait))
async def connect(Headers, exp, em, hash, message, wait):
    async with websockets.connect("wss://ws.checker.in:8443/") as ws:
        while True:
            await ws.send(f"{exp}-{em}-{hash}")
            response = await ws.recv()
            try:
                res = json.loads(response)
                code = res['headers']['subject'].split()[0]
                updict = {"referer": 'https://www.instagram.com/accounts/signup/emailConfirmation/'}
                Headers = {key: updict.get(key, Headers[key]) for key in Headers}
                check = post("https://www.instagram.com/api/v1/accounts/check_confirmation_code/", headers=Headers, data={'code': code, 'device_id': Headers['cookie'].split('mid=')[1].split(';')[0], 'email': em}).json()["signup_code"]
                firstname = names.get_first_name()
                Password = firstname.strip() + '_.@\_' + str(random.randint(111, 999))
                attempt = post("https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/", headers=Headers, data={'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{round(time.time())}:{Password}', 'email': em, 'first_name': firstname, 'username': "", 'seamless_login_enabled': 1}).json()['username_suggestions']
                UserName = random.choice(attempt)
                updict = {"referer": 'https://www.instagram.com/accounts/signup/username/'}
                Headers = {key: updict.get(key, Headers[key]) for key in Headers}
                create = post('https://www.instagram.com/api/v1/web/accounts/web_create_ajax/', headers=Headers, data={'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{round(time.time())}:{Password}', 'email': em, 'username': UserName, 'first_name': firstname, 'month': random.randint(1, 12), 'day': random.randint(1, 28), 'year': random.randint(1990, 2001), 'client_id': Headers['cookie'].split('mid=')[1].split(';')[0], 'seamless_login_enabled': '1', 'tos_version': 'row', 'force_sign_up_code': check}).text
                bot.edit_message_text(f"<b>THIS IS YOUR ACCOUNT</b>\n<b>===================================</b>\n<b>[+] Username:</b> <code>{UserName}</code>\n<b>[+] Password:</b> <code>{Password}</code>\n<b>[+] Response:</b> " + create + "\n<b>===================================</b>\n<b>BY: [SANCHIT](@X668F.t.me)</b>", message.chat.id, wait.message_id, parse_mode="HTML")
            except json.JSONDecodeError:
                pass
            await asyncio.sleep(1)
bot.polling(True)
