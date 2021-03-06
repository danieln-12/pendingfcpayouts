import json
import requests

cookies = {
#PERSONAL COOKIES REQUIRED, fixing this
}

headers = {
    'authority': 'sell.flightclub.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'dnt': '1',
    'pragma': 'no-cache',
    'referer': 'https://sell.flightclub.com/account/transactions',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'x-user-email': 'your email', #auto grab updating
    'x-user-token': 'your user token', #auto grab updating
}


params = {
    'direction': 'desc',
    'page': '1',
    'sort': 'created_at',
    'perPage': '100'
}



response = requests.get('https://sell.flightclub.com/api/me/ledger', params=params, cookies=cookies, headers=headers)
data = response.json()
f1 = [result['debitCents'] for result in data['results']]
f2 = list(filter(lambda x: x != 0, f1))
payouts = []
for result in data['results']:
    p1 = result["debitCents"]
    p2 = p1-(p1 * 2.9 / 100)
    if result["status"] == "requested":
        payouts.append(result["debitCents"])
        print(f'Payout => ${p2/100:.2f} '
              f'| Date => {result["createdAt"]}' 
              f' | Status => {result["status"]}')

total = 0
for ele in range(0, len(payouts)):
    total = total + payouts[ele]
    t2 = total-(total * 2.9 / 100)
print(f'Total Pending => ${t2/100:.2f}')
    
