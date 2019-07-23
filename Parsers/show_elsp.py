import re
import pprint

sample = '''
+--------------------------- MPLS ENCAP LSP TABLE -----------------------------+
| Name                            | Logical Id           | Label               |
+---------------------------------+----------------------+---------------------+
|                                 | 8404609              | 1048575             |
|                                 | 8404610              | 1048575             |
|                                 | 8404611              | 1048575             |
|                                 | 8404612              | 1048575             |
|                                 | 8404614              | 1048575             |
|                                 | 8412929              | 1048575             |
|                                 | 8418611              | 1048575             |
|                                 | 8418625              | 1048575             |
|                                 | 8418626              | 1048575             |
|                                 | 8418627              | 1048575             |
|                                 | 8418628              | 1048575             |
|                                 | 8418629              | 1048575             |
|                                 | 8418630              | 1048575             |
|                                 | 8418631              | 1048575             |
+------------------------------------------------------------------------------+
'''

csmEncapDict = {}
n  = 0
for line in sample.split('\n'):
    try:
        matchObj = re.search(r'(\d+)[\s|]+(\d+)',line)
        logicalID = matchObj.group(1)
        label = matchObj.group(2)


        csmEncapDict[logicalID] = {}
        csmEncapDict[logicalID]['label'] = label
        n = n+1

    except Exception:
        logicalID = None
        label = None



pp = pprint.PrettyPrinter(indent=4, width=10)
pp.pprint(csmEncapDict)
print(n)

