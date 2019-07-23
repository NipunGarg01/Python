import re
import pprint


class SHOW_CSM_MPLS_Extended_tgrp:

    """
    This class is made for design/IT use for core switch manager tunnel-group related stuff
    Sample Output:

   {16002:   {   'LogicalID': 16002},
    16004:   {   'LogicalID': 16004},
    16005:   {   'LogicalID': 16005},
    16006:   {   'LogicalID': 16006},
    24320:   {   'LogicalID': 24320},
    24321:   {   'LogicalID': 24321},
    24323:   {   'LogicalID': 24323},
    8404610: {   'LogicalID': 8404610},
    8404612: {   'LogicalID': 8404612},
    8404613: {   'LogicalID': 8404613},
    8404614: {   'LogicalID': 8404614},
    8412928: {   'LogicalID': 8412928},
    8412931: {   'LogicalID': 8412931}}
    """

    def __init__(self, device, tgrp):
        self.device = device
        self.tgrp = tgrp

    def fetch(self):

        """
        This function fetches data from XC bash prompt
        And Returns data
        """

        data = """
+------------------------ MPLS TUNNEL GROUP INFO ------------------------------+
| Parameter                      | Value                                       |
+--------------------------------+---------------------------------------------+
| Name                           | 24321                                       |
| Logical Id                     | 24321                                       |
| Tunnel Group Policy            | BGP_PIC-Transit                             |
| Selected Encap LSP             | None                                        |
| Allow Hardware Selection       | 1                                           |
| Mesh                           | 0                                           |
| Tunnel Direction Mode          | unidir                                      |
| Basic RxTx Stats               | Off                                         |
| Dynamic Based Pair-0           | 0                                           |
| Dynamic Based Pair-1           | 0                                           |
| MBB-In-Progress                | 0                                           |
| Swap Protection Roles          | 0                                           |
| Opaque Id                      | 0x8005f01                                   |
| Select Backup                  | 1                                           |
| failover Resource              | 0.0.0.0                                     |
|                                |                                             |
| Num Encap Lsps                      | 0                                      |
| Num Decap Lsps                      | 0                                      |
| Num Transit Lsps                    | 0                                      |
| Current LM Slot Mask                | 0x0                                    |
| Potential LM Slot Mask              | 0x0                                    |
| Num VCs                             | 0                                      |
| Current Member-0 LM Slot Mask       | 0x0                                    |
| Potential Member-0 LM Slot Mask     | 0x0                                    |
| Current Member-1 LM Slot Mask       | 0x0                                    |
| Potential Member-1 LM Slot Mask     | 0x0                                    |
| MBB Current Member-0 LM Slot Mask   | 0x0                                    |
| MBB Current Member-1 LM Slot Mask   | 0x0                                    |
| lspPairInUse[0]                     | False                                  |
| lspPairInUse[1]                     | False                                  |
| oldEncapLspLiIndex[0]               | 0                                      |
| oldEncapLspLiIndex[1]               | 0                                      |
| oldDecapLspLiIndex[0]               | 0                                      |
| oldDecapLspLiIndex[1]               | 0                                      |
| MbbRevertStage                      | NoRevert                               |
+-------------------------------------+----------------------------------------+
|          MPAL PLATFORM DATA         |                                        |
+-------------------------------------+----------------------------------------+
| FEC-Pointer                         | 0                                      |
| [0] MP-Entry-ID                     | 0                                      |
| [1] MP-Entry-ID                     | 0                                      |
+------------------------------------------------------------------------------+

        """

        return data

    def parse(self, data):

        """
        This function takes input from fetch function
        Returns dictionary for verification related to Core Switch Manager tunnel grp info
        """

        self.csmTgrpExtendedDict = {}

        try:

            matchObj = re.search(r'Name[\s|]+(\d+)[\s|]+Logical Id[\s|]+(\d+)[\s|]+Tunnel Group Policy[\s|]+([\w-]+)'
                                 r'[\s|]+Selected Encap LSP[\s|]+(\w+)[\s|]+Allow Hardware Selection[\s|]+(\d+)[\s|]+'
                                 r'Mesh[\s|]+(\d+)[\s|]+Tunnel Direction Mode[\s|]+(\w+)[\s|]+Basic RxTx Stats[\s|]+'
                                 r'(\w+)[\s|]+Dynamic Based Pair-0[\s|]+(\d+)[\s|]+Dynamic Based Pair-1[\s|]+(\d+)'
                                 r'[\s|]+MBB-In-Progress[\s|]+(\d+)[\s|]+Swap Protection Roles[\s|]+(\d+)[\s|]+'
                                 r'Opaque Id[\s|]+([\wx]+)[\s|]+Select Backup[\s|]+(\d+)[\s|]+failover Resource[\s|]+'
                                 r'([\d.]+)[\s|]+Num Encap Lsps[\s|]+(\d+)[\s|]+Num Decap Lsps[\s|]+(\d+)[\s|]+'
                                 r'Num Transit Lsps[\s|]+(\d+)[\s|]+Current LM Slot Mask[\s|]+([\dx]+)[\s|]+'
                                 r'Potential LM Slot Mask[\s|]+([\dx]+)[\s|]+Num VCs[\s|]+(\d+)[\s|]+Current Member-0'
                                 r' LM Slot Mask[\s|]+([\dx]+)[\s|]+Potential Member-0 LM Slot Mask[\s|]+([\dx]+)[\s|]+'
                                 r'Current Member-1 LM Slot Mask[\s|]+([\dx]+)[\s|]+Potential Member-1 LM Slot Mask'
                                 r'[\s|]+([\dx]+)[\s|]+MBB Current Member-0 LM Slot Mask[\s|]+([\dx]+)[\s|]+'
                                 r'MBB Current Member-1 LM Slot Mask[\s|]+([\dx]+)[\s|]+lspPairInUse\[0\][\s|]+(\w+)'
                                 r'[\s|]+lspPairInUse\[1\][\s|]+(\w+)[\s|]+oldEncapLspLiIndex\[0\][\s|]+(\d+)[\s|]+'
                                 r'oldEncapLspLiIndex\[1\][\s|]+(\d+)[\s|]+oldDecapLspLiIndex\[0\][\s|]+(\d+)[\s|]+'
                                 r'oldDecapLspLiIndex\[1\][\s|]+(\d+)[\s|]+MbbRevertStage[\s|]+(\w+)', data)

            name = matchObj.group(1)
            print(name)
            logicalID = matchObj.group(2)
            print(logicalID)
            tunnelGroupPolicy = matchObj.group(3)
            print(tunnelGroupPolicy)
            selectedEncapLsp = matchObj.group(4)
            print(selectedEncapLsp)
            allowHardwareSelection = matchObj.group(5)
            print(allowHardwareSelection)
            mesh = matchObj.group(6)
            print(mesh)
            tunnelDirectionMode = matchObj.group(7)
            print(tunnelDirectionMode)
            BasicRxTxStats = matchObj.group(8)
            print(BasicRxTxStats)
            dynamicBasedPair0 = matchObj.group(9)
            print(dynamicBasedPair0)
            dynamicBasedPair1 = matchObj.group(10)
            print(dynamicBasedPair1)
            mbbInProgress = matchObj.group(11)
            print(mbbInProgress)
            swapProtectionRoles = matchObj.group(12)
            print(swapProtectionRoles)
            opaqueID = matchObj.group(13)
            print(opaqueID)
            selectBackup = matchObj.group(14)
            print(selectBackup)
            failoverResource = matchObj.group(15)
            print(failoverResource)
            numEncapLsps = matchObj.group(16)
            print(numEncapLsps)
            numDecapLsps = matchObj.group(17)
            print(numDecapLsps)
            numTransitLps = matchObj.group(18)
            print(numTransitLps)
            currentLmSlotMask = matchObj.group(19)
            print(currentLmSlotMask)
            potentialLmSlotMask = matchObj.group(20)
            print(potentialLmSlotMask)
            numVcs = matchObj.group(21)
            print(numVcs)
            currentMember0LmSlotMask = matchObj.group(22)
            print(currentMember0LmSlotMask)
            potentialMember0LmSlotMask = matchObj.group(23)
            print(potentialMember0LmSlotMask)
            currentMember1LmSlotMask = matchObj.group(24)
            print(currentMember1LmSlotMask)
            potentialMember1LmSlotMask = matchObj.group(25)
            print(potentialMember1LmSlotMask)
            mbbCurrentMember0LMSlotMask = matchObj.group(26)
            print(mbbCurrentMember0LMSlotMask)
            mbbCurrentMember1LMSlotMask = matchObj.group(27)
            print(mbbCurrentMember1LMSlotMask)
            lspPairInUse0 = matchObj.group(28)
            print(lspPairInUse0)
            lspPairInUse1 = matchObj.group(29)
            print(lspPairInUse1)
            oldEncapLspLiIndex0 = matchObj.group(30)
            print(oldEncapLspLiIndex0)
            oldEncapLspLiIndex1 = matchObj.group(31)
            print(oldEncapLspLiIndex1)
            oldDecapLspLiIndex0 = matchObj.group(32)
            print(oldDecapLspLiIndex0)
            oldDecapLspLiIndex1 = matchObj.group(33)
            print(oldDecapLspLiIndex1)
            mbbRevertStage = matchObj.group(34)
            print(mbbRevertStage)

            self.csmTgrpExtendedDict[self.tgrp] = {}
            self.csmTgrpExtendedDict[self.tgrp]['name'] = name
            self.csmTgrpExtendedDict[self.tgrp]['logicalID'] = logicalID
            self.csmTgrpExtendedDict[self.tgrp]['tunnelGroupPolicy'] = tunnelGroupPolicy
            self.csmTgrpExtendedDict[self.tgrp]['selectedEncapLsp'] = selectedEncapLsp
            self.csmTgrpExtendedDict[self.tgrp]['allowHardwareSelection'] = allowHardwareSelection
            self.csmTgrpExtendedDict[self.tgrp]['mesh'] = mesh
            self.csmTgrpExtendedDict[self.tgrp]['tunnelDirectionMode'] = tunnelDirectionMode
            self.csmTgrpExtendedDict[self.tgrp]['BasicRxTxStats'] = BasicRxTxStats
            self.csmTgrpExtendedDict[self.tgrp]['dynamicBasedPair0'] = dynamicBasedPair0
            self.csmTgrpExtendedDict[self.tgrp]['dynamicBasedPair1'] = dynamicBasedPair1
            self.csmTgrpExtendedDict[self.tgrp]['mbbInProgress'] = mbbInProgress
            self.csmTgrpExtendedDict[self.tgrp]['swapProtectionRoles'] = swapProtectionRoles
            self.csmTgrpExtendedDict[self.tgrp]['opaqueID'] = opaqueID
            self.csmTgrpExtendedDict[self.tgrp]['selectBackup'] = selectBackup
            self.csmTgrpExtendedDict[self.tgrp]['failoverResource'] = failoverResource
            self.csmTgrpExtendedDict[self.tgrp]['numEncapLsps'] = numEncapLsps
            self.csmTgrpExtendedDict[self.tgrp]['numDecapLsps'] = numDecapLsps
            self.csmTgrpExtendedDict[self.tgrp]['numTransitLps'] = numTransitLps
            self.csmTgrpExtendedDict[self.tgrp]['currentLmSlotMask'] = currentLmSlotMask
            self.csmTgrpExtendedDict[self.tgrp]['potentialLmSlotMask'] = potentialLmSlotMask
            self.csmTgrpExtendedDict[self.tgrp]['numVcs'] = numVcs
            self.csmTgrpExtendedDict[self.tgrp]['currentMember0LmSlotMask'] = currentMember0LmSlotMask
            self.csmTgrpExtendedDict[self.tgrp]['potentialMember0LmSlotMask'] = potentialMember0LmSlotMask
            self.csmTgrpExtendedDict[self.tgrp]['currentMember1LmSlotMask'] = currentMember1LmSlotMask
            self.csmTgrpExtendedDict[self.tgrp]['potentialMember1LmSlotMask'] = potentialMember1LmSlotMask
            self.csmTgrpExtendedDict[self.tgrp]['mbbCurrentMember0LMSlotMask'] = mbbCurrentMember0LMSlotMask
            self.csmTgrpExtendedDict[self.tgrp]['mbbCurrentMember1LMSlotMask'] = mbbCurrentMember1LMSlotMask
            self.csmTgrpExtendedDict[self.tgrp]['lspPairInUse0'] = lspPairInUse0
            self.csmTgrpExtendedDict[self.tgrp]['lspPairInUse1'] = lspPairInUse1
            self.csmTgrpExtendedDict[self.tgrp]['oldEncapLspLiIndex0'] = oldEncapLspLiIndex0
            self.csmTgrpExtendedDict[self.tgrp]['oldEncapLspLiIndex1'] = oldEncapLspLiIndex1
            self.csmTgrpExtendedDict[self.tgrp]['oldDecapLspLiIndex0'] = oldDecapLspLiIndex0
            self.csmTgrpExtendedDict[self.tgrp]['oldDecapLspLiIndex1'] = oldDecapLspLiIndex1
            self.csmTgrpExtendedDict[self.tgrp]['mbbRevertStage'] = mbbRevertStage

        except Exception:
            name = None
            logicalID = None
            tunnelGroupPolicy = None
            selectedEncapLsp = None
            allowHardwareSelection = None
            mesh = None
            tunnelDirectionMode = None
            BasicRxTxStats = None
            dynamicBasedPair0 = None
            dynamicBasedPair1 = None
            mbbInProgress = None
            swapProtectionRoles = None
            opaqueID = None
            selectBackup = None
            failoverResource = None
            numEncapLsps = None
            numDecapLsps = None
            numTransitLps = None
            currentLmSlotMask = None
            potentialLmSlotMask = None
            numVcs = None
            currentMember0LmSlotMask = None
            potentialMember0LmSlotMask = None
            currentMember1LmSlotMask = None
            potentialMember1LmSlotMask = None
            mbbCurrentMember0LMSlotMask = None
            mbbCurrentMember1LMSlotMask = None
            lspPairInUse0 = None
            lspPairInUse1 = None
            oldEncapLspLiIndex0 = None
            oldEncapLspLiIndex1 = None
            oldDecapLspLiIndex0 = None
            oldDecapLspLiIndex1 = None
            mbbRevertStage= None

        try:
            mpalObj = re.search(r'FEC-Pointer[\s|]+(\d+)[\s|]+\[0\] MP-Entry-ID[\s|]+(\d+)[\s|]+\[1\]'
                                r' MP-Entry-ID[\s|]+(\d+)',data)
            fecPointer = mpalObj.group(1)
            mpEntryID0 = mpalObj.group(2)
            mpEntryID1 = mpalObj.group(3)
            self.csmTgrpExtendedDict[self.tgrp]['fecPointer'] = fecPointer
            self.csmTgrpExtendedDict[self.tgrp]['mpEntryID0'] = mpEntryID0
            self.csmTgrpExtendedDict[self.tgrp]['mpEntryID1'] = mpEntryID1

        except Exception:
            fecPointer = None
            mpEntryID0 = None
            mpEntryID1 = None


        return self.csmTgrpExtendedDict


Obj = SHOW_CSM_MPLS_Extended_tgrp('a', '12')
data1 = Obj.fetch()
result = Obj.parse(data=data1)
pp = pprint.PrettyPrinter(indent=4,width=10)
pp.pprint(result)
