import asyncio
import TruewalletVoucher
def redeem(amount, full_name, code):
    print("redeeming" + amount + " " + full_name +" "+ code)
 
async def main():
     await TruewalletVoucher.twVoucher( 'เบอร์', 'https://gift.truemoney.com/campaign/?v=cs1izU8mCYkxxxx', redeem)
asyncio.run(main())
