import re
import pprint

sample = '''
+------------------------------- MODULE SUMMARY ------------------------------+
|           |             | Admin    | Oper        | Protection  | Standby    |
| Slot      | Model       | State    | State       | Status(Role)| Status     |
+-----------+-------------+----------+-------------+-------------+------------+
| XC7       | XC-PTS      | Enabled  | Enabled     | Primary     | Protected  |
| XC8       | XC-PTS      | Enabled  | Enabled     | Secondary   | Hot-Stby   |
| LM1       | PDH-IF      | Enabled  | Enabled     | n/a         | n/a        |
| LM2       | MRO-16xSFP  | Enabled  | Enabled     | n/a         | n/a        |
+-----------+-------------+----------+-------------+-------------+------------+
'''



mod_dict = {}

for line in sample.split('\n'):

    try:
        match = re.search(r'(\w+)[\s|]+([A-Z0-9\-x]+)[\s|]+(\w+)[\s|]+(\w+)[\s|]+([\w[n/a]+)[\s|]+([\w\-[n/a]+)', line)
        slot = match.group(1)
        model = match.group(2)
        adminstate = match.group(3)
        operstate = match.group(4)
        protectionstatus = match.group(5)
        standybystatus = match.group(6)
        mod_dict[slot] = {}
        mod_dict[slot]['model'] = model
        mod_dict[slot]['adminstate'] = adminstate
        mod_dict[slot]['operstate'] = operstate
        mod_dict[slot]['protectionstatus'] = protectionstatus
        mod_dict[slot]['standbystatus'] = standybystatus

    except Exception:
        model = None
        adminstate = None
        operstate = None
        protectionstatus = None
        standybystatus = None

for x,y in mod_dict.items():
    if (x == 'XC7' or 'XC8' or 'CTM41' or 'CTM42') and (mod_dict[x]['protectionstatus'] == 'Primary'):
        print("Primary card is {}".format(x))
    else:
        break

pp = pprint.PrettyPrinter(indent=4,width=10)
pp.pprint(mod_dict)












# match = re.search(r'(\w+)\s+\D\s([A-Z0-9\-x]+)\s+\D\s(\w+)\s+\D\s(\w+)\s+\D\s([\w[n/a]+)\s+\D\s([\w[n/a]+)', data)
# card=match.group(1)
# cardtype=match.group(2)
# adminstate=match.group(3)
# operstate=match.group(4)
# protectionstatus=match.group(5)
# standybystatus=match.group(6)
# print(card)
# print(cardtype)
# print(adminstate)
# print(operstate)
# print(protectionstatus)
# print(standybystatus)






