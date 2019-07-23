import re
import pprint


class SHOW_PTS_XC_Redundancy:

    """

    """

    def __init__(self, device):
        self.device = device

    def fetch(self):

        """
        """
        data = """
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
        NI State      : SwnotGood
-------------------------------
        CTRL FSM      : 1, 2, 5
        SYNC FSM      : 1, 2, 5
        DATA FSM      : 0, 2, 5
        
        """

        return data

    def parse(self, data):

        """
        """

        self.cardRedundancyDict = {}

        try:
            localMatchObj = re.search(r'Evaluation info for LOCAL CARD:[\s-]+Allow Primary[\s:]+(\w+)[\s]+'
                                      r'Primeship bit[\s:]+(\w+)[\s]+Last Restart[\s:]+(\w+)[\s]+Ejector'
                                      r'[\s:]+(\w+)', data)

            allowPrimary = localMatchObj.group(1)
            primeshipBit = localMatchObj.group(2)
            lastRestart = localMatchObj.group(3)
            ejector = localMatchObj.group(4)

            self.cardRedundancyDict['localInfo'] = {}
            self.cardRedundancyDict['localInfo']['allowprimary'] = allowPrimary
            self.cardRedundancyDict['localInfo']['primeshitbit'] = primeshipBit
            self.cardRedundancyDict['localInfo']['lastrestart'] = lastRestart
            self.cardRedundancyDict['localInfo']['ejector'] = ejector

        except Exception:
            allowPrimary = None
            primeshipBit = None
            lastRestart = None
            ejector = None

        try:
            peerMatchObj = re.search(r'Evaluation info for PEER CARD:[\s-]+Present[\s:]+(\w+)[\s]+2kCCM State'
                                     r'[\s:]+(\w+)[\s]+Primeship bit[\s:]+(\w+)[\s]+Last Restart[\s:]+(\w+)[\s]+'
                                     r'WDTO[\s:]+(\w+)[\s]+Ejector[\s:]+(\w+)[\s]+PRT[\s:]+(\w+)[\s]+PRR[\s:]+'
                                     r'(\w+)[\s]+NI State[\s:]+(\w+)', data)

            present = peerMatchObj.group(1)
            ccmState = peerMatchObj.group(2)
            peerPrimeshipBit = peerMatchObj.group(3)
            peerLastRestart = peerMatchObj.group(4)
            wdto = peerMatchObj.group(5)
            peerEjector = peerMatchObj.group(6)
            prt = peerMatchObj.group(7)
            prr = peerMatchObj.group(8)
            niState = peerMatchObj.group(9)

            self.cardRedundancyDict['peerInfo'] = {}
            self.cardRedundancyDict['peerInfo']['present'] = present
            self.cardRedundancyDict['peerInfo']['ccmState'] = ccmState
            self.cardRedundancyDict['peerInfo']['peerPrimeshipbit'] = peerPrimeshipBit
            self.cardRedundancyDict['peerInfo']['peerLastrestart'] = peerLastRestart
            self.cardRedundancyDict['peerInfo']['wdto'] = wdto
            self.cardRedundancyDict['peerInfo']['peerEjector'] = peerEjector
            self.cardRedundancyDict['peerInfo']['prt'] = prt
            self.cardRedundancyDict['peerInfo']['prr'] = prr
            self.cardRedundancyDict['peerInfo']['niState'] = niState

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
            fsmObj = re.search(r'CTRL FSM[\s:]+([\d\s,]+)[\s]+SYNC FSM[\s:]+([\d\s,]+)[\s]+DATA FSM[\s:]+'
                               r'([\d\s,]+)', data)
            controlFsmStack = [val.strip() for val in fsmObj.group(1).split(',')]
            syncFsmStack = [val.strip() for val in fsmObj.group(2).split(',')]
            dataFsmStack = [val.strip() for val in fsmObj.group(3).split(',')]

            self.cardRedundancyDict['fsmState'] = {}
            self.cardRedundancyDict['fsmState']['controlFsmStack'] = controlFsmStack
            self.cardRedundancyDict['fsmState']['syncFsmStack'] = syncFsmStack
            self.cardRedundancyDict['fsmState']['dataFsmStack'] = dataFsmStack

        except Exception:
            controlFsm = None
            syncFsmStack = None
            dataFsmStack = None

        return self.cardRedundancyDict




Obj = SHOW_PTS_XC_Redundancy('a')
data1 = Obj.fetch()
result = Obj.parse(data=data1)
pp = pprint.PrettyPrinter(indent=4,width=10)
pp.pprint(result)



