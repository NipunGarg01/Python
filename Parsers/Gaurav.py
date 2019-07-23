import pprint

data = '''+------------------------------- MODULE SUMMARY ------------------------------+
|           |             | Admin    | Oper        | Protection  | Standby    |
| Slot      | Model       | State    | State       | Status(Role)| Status     |
+-----------+-------------+----------+-------------+-------------+------------+
| XC7       | XC-PTS      | Enabled  | Enabled     | Primary     | Protected  |
| XC8       | XC-PTS      | Enabled  | Enabled     | Secondary   | Hot-Stby   |
| LM1       | PDH-IF      | Enabled  | Enabled     | n/a         | n/a        |
| LM2       | MRO-16xSFP  | Enabled  | Enabled     | n/a         | n/a        |
+-----------+-------------+----------+-------------+-------------+------------+'''
header_start = False
header_end = False
header_list = []
first_line = True
final_dict = {}
for i in data.split('\n'):
    print(i)
    if i.startswith('+'):
        # print("started with +")
        if not header_start:
            header_start = True
        else:
            # print("header ends")
            header_end = True
    else:
        if not header_end:
            for i,v in enumerate(i.split('|')[1:-1]):
                v = v.strip()
                # print("X{}X".format(v))
                if first_line:
                    header_list.append(v)
                else:
                    if header_list[i]:
                        header_list[i] += " {}".format(v)
                    else:
                        header_list[i] = v

            first_line = False
        else:
            for i, v in enumerate(i.split('|')[1:-1]):
                v = v.strip()
                if header_list[i] == 'Slot':
                    key = v
                    final_dict[key] = {}
                else:
                    final_dict[key][header_list[i]] = v

#print(header_list)
#print(final_dict)
pp = pprint.PrettyPrinter(indent=4,width=10)
pp.pprint(final_dict)



