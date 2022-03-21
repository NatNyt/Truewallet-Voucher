import requests
import json
async def twVoucher(tel, code = str, _callback = None):
    tel = tel.replace(' ', '')
    code = code.replace(' ', '')
    if len(tel) < 10:
        raise Exception("Invalid Phone number")
    code = code.split('https://gift.truemoney.com/campaign/?v=')
    code = list(filter(None, code))
    if  not len(code[0]) == 18:
        raise Exception("Invalid Voucher")
    res =  requests.post('https://fresh-shop.xyz/api/truewallet/voucher', data=json.dumps({'phone': tel, 'voucher': code[0]}), headers={'Content-Type': 'application/json'}).json()
    if str(res.get("data")["status"]["code"]).lower().replace('\n', '').replace(' ', '') == 'success':
        _callback(res.get("data")["data"]["voucher"]["redeemed_amount_baht"], res.get("data")["data"]["owner_profile"]["full_name"], code[0])
    else:
        raise Exception("Invalid Voucher")
