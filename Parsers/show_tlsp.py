import re
import pprint

sample = '''
+--------------------------- MPLS TRANSIT LSP TABLE ---------------------------+
| Logical Id                      | Decap Label          | Encap Label         |
+---------------------------------+----------------------+---------------------+
| 16001                           | 16001                | 3                   |
| 16002                           | 16002                | 16002               |
| 16003                           | 16003                | 3                   |
| 16004                           | 16004                | 16004               |
| 16006                           | 16006                | 16006               |
| 24321                           | 24321                | 3                   |
| 30003                           | 30003                | 16006               |
| 30004                           | 30004                | 16006               |
+------------------------------------------------------------------------------+
'''

csmEncapDict = {}
n  = 0
for line in sample.split('\n'):
    try:
        matchObj = re.search(r'(\d+)[\s|]+(\d+)[\s|]+(\d+)',line)
        logicalID = matchObj.group(1)
        decapLabel = matchObj.group(2)
        encapLabel = matchObj.group(3)

        csmEncapDict[logicalID] = {}
        csmEncapDict[logicalID]['decapLabel'] = decapLabel
        csmEncapDict[logicalID]['encapLabel'] = encapLabel
        n = n+1

    except Exception:
        logicalID = None
        decapLabel = None
        encapLabel = None


pp = pprint.PrettyPrinter(indent=4, width=10)
pp.pprint(csmEncapDict)
print(n)
#print(csmEncapDict['16001']['decapLabel'])

label = 16001
if int(csmEncapDict[str(label)]['decapLabel']) == 16001:
    print("yes")
else:
    print("No")



