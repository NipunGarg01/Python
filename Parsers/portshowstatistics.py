import re
import pprint

sample = '''
+-------------------------- PORT STATISTICS SUMMARY (PACKETS) 20 SECOND SAMPLE -------------------------+
| Port      Port                      |                               Pkt                               |
| Name      AID                       |               Tx               |               Rx               |
+-------------------------------------+--------------------------------+--------------------------------+
| __1-402   ETTP-1-1-402              | Stats not monitored by PM - create PM instance                  |
| __1-401   ETTP-1-1-401              | Stats not monitored by PM - create PM instance                  |
| 2/14      ETTP-1-2-14               |                          7,543 |                              0 |
| __2-402   ETTP-1-2-402              | Stats not monitored by PM - create PM instance                  |
| __2-401   ETTP-1-2-401              | Stats not monitored by PM - create PM instance                  |
| 7/2-4000  ETTP-1-7-2                |                          8,017 |                         24,092 |
| 7/3       ETTP-1-7-3                |                             14 |                             14 |
| 8/2       ETTP-1-8-2                |                             15 |                             15 |
| 8/3       ETTP-1-8-3                |                          8,114 |                         24,801 |
| __LAG_1-1                           | Stats not monitored by PM - create PM instance                  |
| __LAG_1-2                           | Stats not monitored by PM - create PM instance                  |
| __LAG_1-P                           | Stats not monitored by PM - create PM instance                  |
| __LAG_2-P                           | Stats not monitored by PM - create PM instance                  |
| __LAG_2-U                           | Stats not monitored by PM - create PM instance                  |
+-------------------------------------+--------------------------------+--------------------------------+

'''
portstatsdict = {}

for line in sample.split('\n'):
    try:
        match = re.search(r'([\d/-]+)\s+(ETTP-\d+-\d+-[\d\w]+)[\s|]+([\d,]+)[\s|]+([\d,]+)', line)
        port = match.group(1)
        portaid = match.group(2)
        porttx = match.group(3)
        portrx = match.group(4)

        portstatsdict[port] = {}
        portstatsdict[port]['portaid'] = portaid
        portstatsdict[port]['tx'] = porttx
        portstatsdict[port]['rx'] = portrx

    except Exception:
        portaid = None
        porttrx = None
        porttx = None

#pp = pprint.PrettyPrinter(indent=4, width=10)
#pp.pprint(portstatsdict)
print(portstatsdict)



