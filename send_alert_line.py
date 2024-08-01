import requests


def read_token():
    with open('token.txt', 'r') as f:
        return f.read()


if __name__ == '__main__':
    url = f"https://morpromt2c.moph.go.th/api/v2/send-message/send-now"  # line
    token = read_token()
    headers = {"Authorization": f"Bearer {token}"}
    params = {  # line
        "datas": [
            "3650100810887",
            "3501000302113"
        ],
        "messages": [
            {
                "type": "text",
                "text": "ผู้รับบริการหมายเลข A099 อีก 10 คิว จะถึงคิวของท่าน\nกรุณาไปรอที่จุดซักประวัติ"
            }
        ]
    }

    r = requests.post(url, json=params, headers=headers)
    print(r.json())
