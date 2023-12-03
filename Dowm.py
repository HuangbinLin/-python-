import requests
import json
# 设置请求头

def Dowm_data(page):
    # headers = {
    #     'accept': '*/*',
    #     'accept-encoding': 'gzip, deflate, br',
    #     'accept-language': 'zh-CN,zh;q=0.9',
    #     'cookie': '_gid=GA1.2.678790149.1701082584; SSESS434783100c680fee468371c19ab1c999=rRrhyIEzj%2CmYi1y4lI57mJdiSwwlzm6WU7tE52InSE976Vge; _ga=GA1.2.1202352791.1701082583; _ga_3Y05NLKEBB=GS1.1.1701099722.4.1.1701102345.60.0.0',
    #     'referer': 'https://www.nber.org/papers?endDate=2021-12-31&page=6&perPage=50&sortBy=public_date&startDate=2021-01-01',
    #     'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    #     'sec-ch-ua-mobile': '?0',
    #     'sec-ch-ua-platform': 'Windows',
    #     'sec-fetch-dest': 'empty',
    #     'sec-fetch-mode': 'cors',
    #     'sec-fetch-site': 'same-origin',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    # }

    # 设置请求参数
    params = {
        'endDate': '2022-12-31',
        'page': '{}'.format(page),
        'perPage': '50',
        'sortBy': 'public_date',
        'startDate': '2022-01-01'
    }

    # 设置请求URL
    url = 'https://www.nber.org/api/v1/working_page_listing/contentType/working_paper/_/_/search'

    # 发送GET请求
    # response = requests.get(url, params=params, headers=headers)
    response = requests.get(url, params=params)

    # 检查响应状态码
    if response.status_code == 200:
        # 打印响应内容
        data = response.json()
        filename = f"data/2022/page_{page}_data.json"
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        return data
    else:
        print(f"请求失败，状态码: {response.status_code}")
        return None

if __name__ == "__main__": 
    Dowm_data(1)