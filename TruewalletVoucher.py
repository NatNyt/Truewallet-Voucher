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
    res =  requests.post('https://gift.truemoney.com/campaign/vouchers/' + code[0] + '/redeem', data=json.dumps({'mobile': tel, 'voucher_hash': code[0]}), headers={'Content-Type': 'application/json'}).json()
    print(str(res.get("status")["code"]).lower().replace('\n', '').replace(' ', ''))
    if str(res.get("status")["code"]).lower().replace('\n', '').replace(' ', '') == 'success':
        _callback(res.get("data")["voucher"]["redeemed_amount_baht"], res.get("data")["owner_profile"]["full_name"], code[0])
    else:
        raise Exception("Invalid Voucher : " + code[0])
