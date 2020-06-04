import autoit
import time

#NIU-RSA-PC1 - RSA SecurID Token /  RSA SecurID Token - the two titles my app has
# I believe the second one is what i need

rsa_path = "C:\\Program Files\\RSA SecurID Software Token\\SecurID.exe"
nc_path = "C:\\Program Files (x86)\\Juniper Networks\\Network Connect 7.4.0\\dsNetworkConnect.exe"

autoit.run(rsa_path)


active = autoit.win_wait_active("NIU-RSA-PC1 - RSA SecurID Token", 10) # perfect, waits until second, real window opens and acts immediately!
title = autoit.win_get_title("[CLASS:QWidget]")
prccessid = autoit.win_get_process("NIU-RSA-PC1 - RSA SecurID Token")

time.sleep(0.5)

RSA_Text = autoit.win_get_text("[CLASS:QWidget]")

#autoit.control_send("NIU-RSA-PC1 - RSA SecurID Token", 'edit', "dodo")

# text = autoit.win_get_text("NIU-RSA-PC1 - RSA SecurID Token")




print(active, title, prccessid, RSA_Text)



autoit.win_close("NIU-RSA-PC1 - RSA SecurID Token")




# autoit.control_send("[CLASS:Notepad]", "Edit1", "hello world{!}")
# autoit.win_close("[CLASS:Notepad]")
# autoit.control_click("[Class:#32770]", "Button2")
