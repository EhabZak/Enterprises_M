import requests
# from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'Referer': 'https://ranking.glassdollar.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get('https://gdpr-api.sharethis.com/v3/vendor-list.json', headers=headers)
if response.status_code == 200:
    json_response = response.json()
    # soup = BeautifulSoup(response.text, 'html.parser')
    # print(json_response)
    # print(soup)


    venders = list(json_response['vendors'].values())
    # print(venders)
vendersList= pd.DataFrame(venders)
print(vendersList)
pd.DataFrame(venders).to_clipboard()
vendersList.to_csv('vender_results.csv', index=False)
