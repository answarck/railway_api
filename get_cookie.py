import requests

def get_cookie() -> str:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Accept': 'text/html,application/xhtml+xml',
        'Accept-Language': 'en-US,en;q=0.5',
    }

    response = requests.get('https://www.irctc.co.in/nget/train-search', headers=headers)
    return response.cookies.get('bm_sz')


if __name__ == '__main__':
    print(get_cookie())

