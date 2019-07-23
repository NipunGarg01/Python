import re
import pprint

sample = '''
-------------------------------
This card is: primary
-------------------------------

Evaluation info for LOCAL CARD:
-------------------------------
        Allow Primary : YES
        Primeship bit : SET
        Last Restart  : WARM
        Ejector       : CLOSED

Evaluation info for PEER CARD:
------------------------------
        Present       : YES
        2kCCM State   : UP
        Primeship bit : CLEARED
        Last Restart  : COLD
        WDTO          : CLEARED
        Ejector       : CLOSED
        PRT           : COLD
        PRR           : CLEARED
        NI State      : SwGood
-------------------------------
        CTRL FSM      : 1, 2, 5
        SYNC FSM      : 1, 2, 5
        DATA FSM      : 1, 2, 5
'''

cardredundancyDict = {}

try:
    localMatchObj = re.search(r'Evaluation info for LOCAL CARD:[\s-]+Allow Primary[\s:]+(\w+)[\s]+Primeship bit[\s:]+'
                              r'(\w+)[\s]+Last Restart[\s:]+(\w+)[\s]+Ejector[\s:]+(\w+)', sample)
    allowPrimary = localMatchObj.group(1)
    primeshipBit = localMatchObj.group(2)
    lastRestart = localMatchObj.group(3)
    ejector = localMatchObj.group(4)
    cardredundancyDict['localInfo'] = {}
    cardredundancyDict['localInfo']['allowprimary'] = allowPrimary
    cardredundancyDict['localInfo']['primeshitbit'] = primeshipBit
    cardredundancyDict['localInfo']['lastrestart'] = lastRestart
    cardredundancyDict['localInfo']['ejector'] = ejector

except Exception:
    allowPrimary = None
    primeshipBit = None
    lastRestart = None
    ejector = None

try:
    peerMatchObj = re.search(r'Evaluation info for PEER CARD:[\s-]+Present[\s:]+(\w+)[\s]+2kCCM State[\s:]+(\w+)[\s]+'
                             r'Primeship bit[\s:]+(\w+)[\s]+Last Restart[\s:]+(\w+)[\s]+WDTO[\s:]+(\w+)[\s]+Ejector'
                             r'[\s:]+(\w+)[\s]+PRT[\s:]+(\w+)[\s]+PRR[\s:]+(\w+)[\s]+NI State[\s:]+(\w+)',sample)
    present = peerMatchObj.group(1)
    ccmState = peerMatchObj.group(2)
    peerPrimeshipBit = peerMatchObj.group(3)
    peerLastRestart = peerMatchObj.group(4)
    wdto = peerMatchObj.group(5)
    peerEjector = peerMatchObj.group(6)
    prt = peerMatchObj.group(7)
    prr = peerMatchObj.group(8)
    niState = peerMatchObj.group(9)

    cardredundancyDict['peerInfo'] = {}
    cardredundancyDict['peerInfo']['present'] = present
    cardredundancyDict['peerInfo']['ccmState'] = ccmState
    cardredundancyDict['peerInfo']['peerPrimeshipbit'] = peerPrimeshipBit
    cardredundancyDict['peerInfo']['peerLastrestart'] = peerLastRestart
    cardredundancyDict['peerInfo']['wdto'] = wdto
    cardredundancyDict['peerInfo']['peerEjector'] = peerEjector
    cardredundancyDict['peerInfo']['prt'] = prt
    cardredundancyDict['peerInfo']['prr'] = prr
    cardredundancyDict['peerInfo']['niState'] = niState

except Exception:
    present = None
    ccmState = None
    peerPrimeshipBit = None
    peerLastrestart = None
    wdto = None
    peerEjector = None
    prt = None
    prr = None
    niState = None

try:
    fsmObj = re.search(r'CTRL FSM[\s:]+([\d\s,]+)[\s]+SYNC FSM[\s:]+([\d\s,]+)[\s]+DATA FSM[\s:]+([\d\s,]+)',sample)
    controlFsmStack = [val.strip() for val in fsmObj.group(1).split(',')]
    syncFsmStack = [val.strip() for val in fsmObj.group(2).split(',')]
    dataFsmStack = [val.strip() for val in fsmObj.group(3).split(',')]

    cardredundancyDict['fsmState'] = {}
    cardredundancyDict['fsmState']['controlFsmStack'] = controlFsmStack
    cardredundancyDict['fsmState']['syncFsmStack'] = syncFsmStack
    cardredundancyDict['fsmState']['dataFsmStack'] = dataFsmStack

except Exception:
    controlFsm = None
    syncFsmStack = None
    dataFsmStack = None

pp = pprint.PrettyPrinter(indent=4,width=10)
pp.pprint(cardredundancyDict)
