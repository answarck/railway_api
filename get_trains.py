import json
import httpx
import time

client = httpx.Client(http2=True)

def get_trains(src: str, dst: str, date: str) -> dict:
    url = "https://www.irctc.co.in/eticketing/protected/mapps1/altAvlEnq/TC"

    data = {
        "concessionBooking": False,
        "srcStn": src,
        "destStn": dst,
        "jrnyClass": "",
        "jrnyDate": date,
        "quotaCode": "GN",
        "currentBooking": "false",
        "flexiFlag": False,
        "handicapFlag": False,
        "ticketType": "E",
        "loyaltyRedemptionBooking": False,
        "ftBooking": False
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.0",
        "Content-Type": "application/json; charset=utf-8",
        "Referer": "https://www.irctc.co.in/nget/train-search",
        "greq": str(int(time.time() * 1000)),
        # "bmirak": "webbm",
        "Content-Language": "en",
        "Origin": "https://www.irctc.co.in",
        "DNT": "1",
        "Sec-GPC": "1",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Connection": "keep-alive"
    }


    response = client.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()


def get_fare(train_no: str, date: str, src: str, dst: str, cls: str = "2S", quota: str = "GN") -> dict:
    url = f"https://www.irctc.co.in/eticketing/protected/mapps1/avlFarenquiry/{train_no}/{date}/{src}/{dst}/{cls}/{quota}/N"

    data = {
        "paymentFlag": "N",
        "concessionBooking": False,
        "ftBooking": False,
        "loyaltyRedemptionBooking": False,
        "ticketType": "E",
        "quotaCode": quota,
        "moreThanOneDay": True,
        "trainNumber": train_no,
        "fromStnCode": src,
        "toStnCode": dst,
        "isLogedinReq": False,
        "journeyDate": date,
        "classCode": cls
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.0",
        "Content-Type": "application/json; charset=utf-8",
        "Referer": "https://www.irctc.co.in/nget/booking/train-list",
        "greq": str(int(time.time() * 1000)),
        # "bmirak": "webbm",
        "Content-Language": "en",
        # "bmiyek": "9F678373591861B10A3BF13260756730",
        "Origin": "https://www.irctc.co.in",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Connection": "keep-alive"
    }


    response = client.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()


if __name__ == '__main__':
    print(get_trains("PGI", "ERN", "20250802"))
