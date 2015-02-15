import zimsoap.client
import zimsoap.utils
from zimsoap.zobjects import *

import pprint

zc = zimsoap.client.ZimbraAdminClient("172.16.58.128", "7071")
zc.login("zimbra", "vEXDlWOJ")
#zc.get_account(Account(name="admin@zimbralab.manens.org"))
#a = zc.search_account("(objectClass=*)")

a = zc.search_account("(&(objectClass=zimbraAccount)(mail=a*))", attrs=["description"])
pprint.pprint(a)
