import subprocess
import json
from get_cookie import get_cookie

def get_trains(src: str, dst: str , date: str) -> str:
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

    headers = [
        "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
        "Accept: application/json, text/plain, */*",
        "Accept-Language: en-US,en;q=0.0",
        "Accept-Encoding: gzip, deflate, br, zstd",
        "Content-Type: application/json; charset=utf-8",
        "Referer: https://www.irctc.co.in/nget/train-search",
        "greq: 1752992839434",
        "bmirak: webbm",
        "Content-Language: en",
        "Origin: https://www.irctc.co.in",
        "DNT: 1",
        "Sec-GPC: 1",
        "Sec-Fetch-Dest: empty",
        "Sec-Fetch-Mode: cors",
        "Sec-Fetch-Site: same-origin",
        "Connection: keep-alive",
        f"Cookie: bm_sz={get_cookie()}",
    ]

    command = ["curl", "https://www.irctc.co.in/eticketing/protected/mapps1/altAvlEnq/TC", "--compressed", "-X", "POST"]
    for h in headers:
        command += ["-H", h]
    command += ["--data-raw", json.dumps(data)]

    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return json.loads(result.stdout)


def get_fare(train_no: str, date: str, src: str, dst: str, cls: str = "2S", quota: str = "GN") -> dict:
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

    headers = [
        "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
        "Accept: application/json, text/plain, */*",
        "Accept-Language: en-US,en;q=0.0",
        "Accept-Encoding: gzip, deflate, br, zstd",
        "Content-Type: application/json; charset=utf-8",
        "Referer: https://www.irctc.co.in/nget/booking/train-list",
        "greq: 1752995665214",
        "bmirak: webbm",
        "Content-Language: en",
        "bmiyek: 9F678373591861B10A3BF13260756730",
        "Origin: https://www.irctc.co.in",
        "Sec-Fetch-Dest: empty",
        "Sec-Fetch-Mode: cors",
        "Sec-Fetch-Site: same-origin",
        "Connection: keep-alive",
        f"Cookie: bm_sz={get_cookie()}"
    ]

    url = f"https://www.irctc.co.in/eticketing/protected/mapps1/avlFarenquiry/{train_no}/{date}/{src}/{dst}/{cls}/{quota}/N"

    command = ["curl", url, "--compressed", "-X", "POST"]
    for h in headers:
        command += ["-H", h]
    command += ["--data-raw", json.dumps(data)]

    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return json.loads(result.stdout)

def get_no_of_seats()
if __name__ == '__main__':
    print(get_trains("PGI", "ERN", "20250802"))