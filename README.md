# ZenPack Template

ZenPacks.community.EatonPdu


Description

This ZenPack gathers information about Eaton ePDU (Power Distribution Units) with component and performance information for Power Supplies, Outlets and Groups/Banks.
(Tested on: Eaton ePDU AM 1P IN 16A OUT 20xC13, 4xC19)


Requirements & Dependencies
* Zenoss Versions Supported: 4.x - tested against Zenoss Core 4.2.5 SUP 671
* External Dependencies:
* ZenPack Dependencies:
* Installation Notes: zenoss restart after installing this ZenPack

About this ZenPack
* The ZenPack has the following new Device Class  -   /Devices/Power/EatonPdu
* Added MIB
* Added Event Classes  -  Status/Eaton/ePDU  with some mappings (and some transforms ex:"snmp trap notifyUserLogin (UserName:admin)")

Components
 - ePDU Groups
 - ePDU Outlets
 - ePDU Input Currents
 - ePDU Input Powers
 - ePDU Input Voltages
 - ePDU Envs


Modeler plugins
  - EatonPduDeviceMap  :
            Gathers Hardware and Software manufacturer and product
            Serial number
  - EatonPduGroupMap   :
            Gathers group/bank number and state
  - EatonPduOutletMap  :
            Gathers outlet name, number state and group/bank association
  - EatonPduCurrentMap :
            Gathers current type, state
  - EatonPduPowerMap   :
            Gathers power phase, state
  - EatonPduVoltageMap :
            Gathers voltage type, state
  - EatonPduEnvMap     :
            Gathers temperature, humidity from sensors




Some screenshots
