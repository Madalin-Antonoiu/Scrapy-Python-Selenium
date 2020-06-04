import autoit
import time

rsa_path = "C:\\Program Files\\RSA SecurID Software Token\\SecurID.exe"
autoit.run(rsa_path)

active = autoit.win_wait_active("NIU-RSA-PC1 - RSA SecurID Token", 10)
if active == 1:
    autoit.send("447887")
    autoit.send("{Enter}")
    time.sleep(0.3)
    autoit.send("{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{ENTER}{TAB}{TAB}{TAB}{TAB}{ENTER}")
    time.sleep(0.3)
    pin = autoit.clip_get()

    print(pin)
