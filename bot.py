import requests, random
num = 0
randomParent = ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") for i in range(64))

headers = {
    'authority': 'api.discord.gx.games',
    'accept': '*/*',
    'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
    'origin': 'https://www.opera.com',
    'referer': 'https://www.opera.com/',
    'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0',
}

json_data = {
    'partnerUserId': randomParent,
}

while True:
    randomParent = ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") for i in range(64))
    discordCode = requests.post('https://api.discord.gx.games/v1/direct-fulfillment', headers=headers, json=json_data).content.decode().removeprefix('{"token":"').removesuffix('"}')
    fullLink = "https://discord.com/billing/partner-promotions/1180231712274387115/" + discordCode
    if discordCode != "":
        file = open("fuckdiscord.txt", "a")
        file.write(fullLink+'\n')
        file.close()
        num += 1
        print(num, fullLink)
