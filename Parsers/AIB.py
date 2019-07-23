import re
import pprint

sample = '''
+------------ AIB Options ------------+
| AIB Timeout in Seconds          150 |
+-------------------------------------+
+---------------+-------+-----------------+
|NexthopIp      |ifIndex|   Dmac          |
+---------------+-------+-----------------+
|200.200.2.58   |0000052|ec:b0:e1:7b:30:07|
|200.200.2.54   |0000053|ec:b0:e1:7b:30:07|
|200.200.2.114  |0000054|ec:b0:e1:7a:a8:07|
|200.200.2.110  |0000055|ec:b0:e1:7a:a8:07|
|200.200.2.118  |0000056|ec:b0:e1:78:f0:07|
|200.200.2.94   |0000057|ec:b0:e1:78:f0:07|
|200.200.2.46   |0000058|1c:11:61:bd:60:0c|
|200.200.2.50   |0000059|1c:11:61:bd:60:0c|
+---------------+-------+-----------------+
'''

AibDict = {}
for line in sample.split('\n'):

    try:
        matchObj1 = re.search(r'AIB Timeout in Seconds\s+(\d+)',line)
        timeout = matchObj1.group(1)
        AibDict['timeout'] = timeout

    except Exception:
        timeout = None

    try:
        matchObj = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})[\s|]+(\d+)\|(\w{1,2}:\w{1,2}:\w{1,2}:\w{1,2}:\w{1,2}:\w{1,2})',line)
        NextHop = matchObj.group(1)
        IfIndex = matchObj.group(2)
        Dmac = matchObj.group(3)
        AibDict[NextHop] = {}
        AibDict[NextHop]['ifindex'] = IfIndex
        AibDict[NextHop]['dmac'] = Dmac

    except Exception:
        IfIndex = None
        Dmac = None





pp = pprint.PrettyPrinter(indent=4, width=10)
pp.pprint(AibDict)


