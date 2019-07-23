import re
import pprint

sample = '''
+------------------+----------------+---+---+----+------+-----------+
| Destination/     |  NexthopIp     |oif|Act|Path|Entry |Path Cost  |
|  NetMaskLen      |                |Idx|ion|Type|Id    |(AdmDist.) |
+------------------+----------------+---+---+----+------+-----------+
|1.1.1.1/32        |-               |-  |loc|IF  |0     |0          |
|2.2.2.2/32        |200.200.2.54    |53 |fwd|I1I |0     |115        |
|3.3.3.3/32        |200.200.2.110   |55 |fwd|I1I |0     |115        |
|4.4.4.4/32        |200.200.2.94    |57 |fwd|I1I |0     |115        |
|5.5.5.5/32        |200.200.2.46    |58 |fwd|I1I |0     |115        |
|6.6.6.6/32        |200.200.2.54    |53 |fwd|I1I |0     |115        |
|200.200.2.44/30   |-               |-  |loc|IF  |0     |0          |
|200.200.2.44/32   |-               |-  |loc|IF  |0     |0          |
|200.200.2.45/32   |-               |-  |loc|IF  |0     |0          |
|200.200.2.46/32   |200.200.2.46    |58 |loc|ADJ |0     |0          |
|200.200.2.47/32   |-               |-  |loc|IF  |0     |0          |
|200.200.2.48/30   |-               |-  |loc|IF  |0     |0          |
|200.200.2.48/32   |-               |-  |loc|IF  |0     |0          |
|200.200.2.49/32   |-               |-  |loc|IF  |0     |0          |
|200.200.2.50/32   |200.200.2.50    |59 |loc|ADJ |0     |0          |
|200.200.2.51/32   |-               |-  |loc|IF  |0     |0          |
|200.200.2.52/30   |-               |-  |loc|IF  |0     |0          |
|200.200.2.52/32   |-               |-  |loc|IF  |0     |0          |
|200.200.2.53/32   |-               |-  |loc|IF  |0     |0          |
|200.200.2.54/32   |200.200.2.54    |53 |loc|ADJ |0     |0          |
|200.200.2.55/32   |-               |-  |loc|IF  |0     |0          |
|200.200.2.56/30   |-               |-  |loc|IF  |0     |0          |
|200.200.2.56/32   |-               |-  |loc|IF  |0     |0          |
|200.200.2.57/32   |-               |-  |loc|IF  |0     |0          |
|200.200.2.58/32   |200.200.2.58    |52 |loc|ADJ |0     |0          |
|200.200.2.59/32   |-               |-  |loc|IF  |0     |0          |
|200.200.2.60/30   |200.200.2.54    |53 |fwd|I1I |0     |115        |
|200.200.2.64/30   |200.200.2.54    |53 |fwd|I1I |0     |115        |
|200.200.2.68/30   |200.200.2.94    |57 |fwd|I1I |0     |115        |
|200.200.2.72/30   |200.200.2.94    |57 |fwd|I1I |0     |115        |
|200.200.2.76/30   |200.200.2.110   |55 |fwd|I1I |0     |115        |
|200.200.2.80/30   |200.200.2.94    |57 |fwd|I1I |0     |115        |
|200.200.2.84/30   |200.200.2.46    |58 |fwd|I1I |0     |115        |
|200.200.2.88/30   |200.200.2.110   |55 |fwd|I1I |0     |115        |
|200.200.2.92/30   |-               |-  |loc|IF  |0     |0          |
|200.200.2.92/32   |-               |-  |loc|IF  |0     |0          |
|200.200.2.93/32   |-               |-  |loc|IF  |0     |0          |
|200.200.2.94/32   |200.200.2.94    |57 |loc|ADJ |0     |0          |
|200.200.2.95/32   |-               |-  |loc|IF  |0     |0          |
|200.200.2.96/30   |200.200.2.54    |53 |fwd|I1I |0     |115        |
|200.200.2.100/30  |200.200.2.54    |53 |fwd|I1I |0     |115        |
|200.200.2.104/30  |200.200.2.54    |53 |fwd|I1I |0     |115        |
|200.200.2.108/30  |-               |-  |loc|IF  |0     |0          |
|200.200.2.108/32  |-               |-  |loc|IF  |0     |0          |
|200.200.2.109/32  |-               |-  |loc|IF  |0     |0          |
|200.200.2.110/32  |200.200.2.110   |55 |loc|ADJ |0     |0          |
|200.200.2.111/32  |-               |-  |loc|IF  |0     |0          |
|200.200.2.112/30  |-               |-  |loc|IF  |0     |0          |
|200.200.2.112/32  |-               |-  |loc|IF  |0     |0          |
|200.200.2.113/32  |-               |-  |loc|IF  |0     |0          |
|200.200.2.114/32  |200.200.2.114   |54 |loc|ADJ |0     |0          |
|200.200.2.115/32  |-               |-  |loc|IF  |0     |0          |
|200.200.2.116/30  |-               |-  |loc|IF  |0     |0          |
|200.200.2.116/32  |-               |-  |loc|IF  |0     |0          |
|200.200.2.117/32  |-               |-  |loc|IF  |0     |0          |
|200.200.2.118/32  |200.200.2.118   |56 |loc|ADJ |0     |0          |
|200.200.2.119/32  |-               |-  |loc|IF  |0     |0          |
|200.200.2.120/30  |200.200.2.54    |53 |fwd|I1I |0     |115        |
+------------------+----------------+---+---+----+------+-----------+
| oif: Outgoing Interface                                           |
| entryId: Internal Id from Route Module (=0 local)                 |
| Action: fwd: Forward, loc: Local, rej: Reject, bck: BlackHole     |
| PathType: IF: Local Interface, ADJ: Adjacency, Sta: Static        |
| I1I: Isis L1 Int, I2I: Isis L2 Int                                |
| BGP: BGP, unk: Unknown                                            |
+-------------------------------------------------------------------+
'''

FibDict = {}
for line in sample.split('\n'):
    try:
        matchObj = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2})[\s|]+([\d.-]+)[\s|]+([\d-]+)[\s|]+(\w+)\|(\w+)[\s|]+(\d+)[\s|]+(\d+)', line)
        Destination = matchObj.group(1)
        Nexthop = matchObj.group(2)
        OifIndex = matchObj.group(3)
        Action = matchObj.group(4)
        PathType = matchObj.group(5)
        EntryID = matchObj.group(6)
        PathCost = matchObj.group(7)
        FibDict[Destination] = {}
        FibDict[Destination]['Nexthop'] = Nexthop
        FibDict[Destination]['OifIndex'] = OifIndex
        FibDict[Destination]['Action'] = Action
        FibDict[Destination]['PathType'] = PathType
        FibDict[Destination]['EntryID'] = EntryID
        FibDict[Destination]['PathCost'] = PathCost

    except Exception:
        Nexthop = None
        OifIndex = None
        Action = None
        PathCost = None
        PathType = None
        EntryID = None

pp = pprint.PrettyPrinter(indent=4, width=10)
pp.pprint(FibDict)
