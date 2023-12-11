import requests
import pandas as pd

headers = {
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'accept': 'application/json',
    'Referer': 'https://ranking.glassdollar.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

response = requests.get('https://gdpr-api.sharethis.com/v2/cmp-list.json', headers=headers)
if response.status_code == 200:
    json_response = response.json()
    # print(json_response)
    # first_cmp = list(json_response['cmps'].values())[0]
    companies = list(json_response['cmps'].values())
    # print(companies)
    finalList = pd.DataFrame(companies)
    print(finalList)
    finalList.to_csv('enterprise_results.csv', index=False)
    
    '''
{'id': 2, 'name': 'AppConsent by SFBX® ', 'isCommercial': True}
    '''
