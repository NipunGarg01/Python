import re
import pprint
from Parsers.SHOW_PTS_XC_Redundancy import SHOW_PTS_XC_Redundancy
from Parsers.ErrorCodes import ErrorCodes


class Verify_XC_Master:

    def __init__(self, device):

        self.device = device
        self.cpMasterSlot = None
        self.dpMasterSlot = None

    def getMasterSlot(self):

        try:
            logInfo = ''
            brdData = "Slot = 8"
            slotObj = re.search(r'Slot[\s=]+(\d)', brdData)
            self.cpMasterSlot = slotObj.group(1)
            showPTSRedundancy = SHOW_PTS_XC_Redundancy('A')
            data = showPTSRedundancy.fetch()
            showPTSRedundancy.parse(data=data)
            if showPTSRedundancy.cardRedundancyDict['fsmState']['dataFsmStack'][0] != "1" and\
                    showPTSRedundancy.cardRedundancyDict['peerInfo']['present'] == 'YES':
                if self.cpMasterSlot == "7":
                    self.dpMasterSlot = "8"
                    logInfo = 'Current XC{} is a CP Master and XC{} is a DP Master'.format\
                        (self.cpMasterSlot, self.dpMasterSlot)
                else:
                    self.dpMasterSlot = '7'
                    logInfo = 'Current XC{} is a CP Master and XC{} is a DP Master'.format\
                        (self.cpMasterSlot, self.dpMasterSlot)
            else:
                self.dpMasterSlot = self.cpMasterSlot
                logInfo = 'Current XC{} is a CP/DP master'.format(self.cpMasterSlot)

        except Exception:
            #logInfo = 'Exception occured during XC master slot finding'
            return ErrorCodes.VERIFY_XC_Mate_Status.value, "Exception occured during XC master slot finding"
        # This function returns a tuple of CP MASTER SLOT, DP MASTER SLOT , and respective logInfo
        return self.cpMasterSlot, self.dpMasterSlot

    def isLocalEjectorClosed(self):
        getSlot = self.getMasterSlot()
        log = ''
        showPTSRedundancy = SHOW_PTS_XC_Redundancy('A')
        data = showPTSRedundancy.fetch()
        showPTSRedundancy.parse(data=data)
        if getSlot[0] != getSlot[1] and showPTSRedundancy.cardRedundancyDict['localInfo']['ejector'] == 'CLOSED':
            log = 'Ejector for CP Master XC{} is closed'.format(getSlot[0])
            return "SUCCESS", None
        elif getSlot[0] != getSlot[1] and showPTSRedundancy.cardRedundancyDict['localInfo']['ejector'] == 'OPEN':
            #log = 'Ejector for CP Master XC{} is open'.format(getSlot[0])
            return ErrorCodes.VERIFY_XC_Mate_Status.value, "Ejector for CP Master XC{} is open".format(getSlot[0])
        elif getSlot[0] == getSlot[1] and showPTSRedundancy.cardRedundancyDict['localInfo']['ejector'] == 'CLOSED':
            log = 'Ejector for CP/DP Master XC{} is closed'.format(getSlot[0])
            return "SUCCESS", None
        else:
            #log = 'Ejector for CP/DP Master XC{} is open'.format(getSlot[0])
            return ErrorCodes.VERIFY_XC_Mate_Status.value, "Ejector for CP/DP Master XC{} is open".format(getSlot[0])

    def isPeerEjectorClosed(self):
        getSlot = self.getMasterSlot()
        log = ''
        showPTSRedundancy = SHOW_PTS_XC_Redundancy('A')
        data = showPTSRedundancy.fetch()
        showPTSRedundancy.parse(data=data)
        if getSlot[0] != getSlot[1] and showPTSRedundancy.cardRedundancyDict['peerInfo']['peerEjector'] == 'CLOSED':
            log = 'Ejector for DP Master XC{} is closed'.format(getSlot[1])
            return "SUCCESS", None
        elif getSlot[0] != getSlot[1] and showPTSRedundancy.cardRedundancyDict['peerInfo']['peerEjector'] == 'OPEN':
            log = 'Ejector for DP Master XC{} is open'.format(getSlot[1])
            return ErrorCodes.VERIFY_XC_Mate_Status.value, "Ejector for DP Master XC{} is open".format(getSlot[1])
        elif getSlot[0] == getSlot[1] and showPTSRedundancy.cardRedundancyDict['peerInfo']['peerEjector'] == 'CLOSED':
            log = 'ejector of XC{}\'s peer XC is closed and peer card is non CP/DP master'.format(getSlot[0])
            return "SUCCESS", None
        else:
            #log = 'ejector of XC{}\'s peer XC is open and peer card is non CP/DP master'.format(getSlot[0])
            return ErrorCodes.VERIFY_XC_Mate_Status.value, "ejector of XC{}\'s peer XC is open and peer card is non " \
                                                           "CP/DP master".format(getSlot[0])

    def peerNIState(self):

        """
        This method checks for peerCard nodal state condition
        :return: True/False and respective logInfo
        """

        getSlot = self.getMasterSlot()
        log = ''
        showPTSRedundancy = SHOW_PTS_XC_Redundancy('A')
        data = showPTSRedundancy.fetch()
        showPTSRedundancy.parse(data=data)
        if getSlot[0] != getSlot[1] and showPTSRedundancy.cardRedundancyDict['peerInfo']['niState'] == 'SwGood':
            log = 'Nodal state for DP Master XC{} is in good state'.format(getSlot[1])
            return "SUCCESS", None
        elif getSlot[0] != getSlot[1] and showPTSRedundancy.cardRedundancyDict['peerInfo']['niState'] != 'SwGood':
            log = 'Nodal state for DP Master XC{} is not in good state'.format(getSlot[1])
            return ErrorCodes.VERIFY_XC_Mate_Status.value, "Nodal state for DP Master XC{} is not in good" \
                                                           " state".format(getSlot[1])
        elif getSlot[0] == getSlot[1] and showPTSRedundancy.cardRedundancyDict['peerInfo']['niState'] == 'SwGood':
            log = 'Nodal state of XC{}\'s peer card is in good state and peer card is non CP/DP master'.\
                format(getSlot[0])
            return "SUCCESS", None
        else:
            #log = 'Nodal state of XC{}\'s peer card is not in good state and peer card is non CP/DP master'.format(getSlot[0])
            return ErrorCodes.VERIFY_XC_Mate_Status.value, "Nodal state of XC{}\'s peer card is not in good state " \
                                                           "and peer card is non CP/DP master".format(getSlot[0])

obj1 = Verify_XC_Master('a')
#result = obj1.getMasterSlot()
result = obj1.peerNIState()
#print(type(result))
print(result)
#pp = pprint.PrettyPrinter(indent=4,width=10)
#pp.pprint(obj1.getDataPlaneMaster())
