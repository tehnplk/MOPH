import requests


def read_token():
    with open('token.txt', 'r') as f:
        return f.read()


if __name__ == '__main__':
    url = "https://cvp1.moph.go.th/api/SendMessageTarget"  # app and line
    token = read_token()

    headers = {"Authorization": f"Bearer {token}"}

    html1 = """<h2>คิวหมายเลข A079</h2>
    อีก10คิวจะถึงคิวของท่าน   
    กรุณาไปรอที่จุดซักประวัติช่องหมายเลข 5
    """
    params1 = {  # app and line
        "hospital": {
            "hospital_code": "00051",
            "hospital_name": "รพ.ทดสอบ",
            "his_identifier": "QTerminal"
        },
        "message_ref_code": "20240731000000",
        "message_title": "แจ้งเตือนใกล้ถึงคิว",
        "message_content_html": html1,
        "message_confirm_url": "https://www.example.com/ConfirmMessage",
        "target": ["3650100810887"]
    }

    html2 = """
    <h2>แจ้งเตือนใกล้ถึงวันนัด</h2>
    ในวันพรุ่งนี้ 2สิงหาคม2567 เวลา7.30น.
    ท่านมีนัดเจาะเลือดที่ตึกผู้ป่วยนอก 
    ห้องเจาะเลือดหมายเลข10   
    คืนนี้กรุณางดน้ำงดอาหารหลัง 20.00น.เป็นต้นไป
    """
    params2 = {  # app and line
        "hospital": {
            "hospital_code": "00051",
            "hospital_name": "รพ.ทดสอบ",
            "his_identifier": "QTerminal"
        },
        "message_ref_code": "20240731000000",
        "message_title": "แจ้งเตือนใกล้ถึงวันนัด",
        "message_content_html": html2,
        "message_confirm_url": "https://www.example.com/ConfirmMessage",
        "target": ["3650100810887", "3501000302113"]
    }

    r = requests.post(url, json=params1, headers=headers)
    print(r.json())
