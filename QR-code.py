import qrcode

upi_id = input("Enter your UPI ID = ")
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(phonepe_url)
google_pay_qr = qrcode.make(phonepe_url)

phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('phonepe_qr.png')
google_pay_qr.save('phonepe_qr.png')

phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

