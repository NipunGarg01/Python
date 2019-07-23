import re
import pprint

sample = '''
+---------------------------- MPLS TUNNEL GROUP TABLE -------------------------+
| Name                            | Logical Id                                 |
+---------------------------------+--------------------------------------------+
| 16002                           | 16002                                      |
| 16004                           | 16004                                      |
| 16005                           | 16005                                      |
| 16006                           | 16006                                      |
| 24320                           | 24320                                      |
| 24321                           | 24321                                      |
| 24323                           | 24323                                      |
| 8404610                         | 8404610                                    |
| 8404612                         | 8404612                                    |
| 8404613                         | 8404613                                    |
| 8404614                         | 8404614                                    |
| 8412928                         | 8412928                                    |
| 8412931                         | 8412931                                    |
+------------------------------------------------------------------------------+
'''

csmTgrpDict = {}
n  = 0
for line in sample.split('\n'):
    try:
        matchObj = re.search(r'(\d+)[\s|]+(\d+)',line)
        logicalID = int(matchObj.group(2))
        name = int(matchObj.group(1))


        csmTgrpDict[name] = {}
        csmTgrpDict[name]['LogicalID'] = logicalID

        n = n+1

    except Exception:
        logicalID = None
        name = None



pp = pprint.PrettyPrinter(indent=4, width=10)
pp.pprint(csmTgrpDict)
print(n)
#print(csmEncapDict['16001']['decapLabel'])

# label = 16001
# if int(csmEncapDict[str(label)]['decapLabel']) == 16001:
#     print("yes")
# else:
#     print("No")
#
