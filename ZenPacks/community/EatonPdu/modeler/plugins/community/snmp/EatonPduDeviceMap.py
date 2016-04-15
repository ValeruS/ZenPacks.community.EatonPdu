##########################################################################
# Author:               ValeruS
# Date:                 April 2016
# Revised:
#
# EatonPduDevice modeler plugin
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__ = """EatonPduDeviceMap

Gather table information from Eaton PDU devices.
"""


from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import MultiArgs


class EatonPduDeviceMap(SnmpPlugin):
    """Map Eaton PDU Device table to model."""
    maptype = "EatonPduDeviceMap"
#    modname = "ZenPacks.community.EatonPdu.EatonPduDevice"
#    relname = "EatonPduDevice"



    snmpGetMap = GetMap({
#        '': '_HWManufacturer',
        '.1.3.6.1.4.1.534.6.6.7.1.2.1.2.0': 'setHWProductKey',
        '.1.3.6.1.4.1.534.6.6.7.1.2.1.6.0': '_OSManufacturer',
        '.1.3.6.1.4.1.534.6.6.7.1.2.1.5.0': 'setOSProductKey',
        '.1.3.6.1.4.1.534.6.6.7.1.2.1.4.0': 'setHWSerialNumber',
        '.1.3.6.1.4.1.534.6.6.7.1.2.1.3.0': 'setHWTag',
        '.1.3.6.1.4.1.534.6.6.7.1.2.1.20.0': 'inputCount',
        '.1.3.6.1.4.1.534.6.6.7.1.2.1.21.0': 'groupCount',
        '.1.3.6.1.4.1.534.6.6.7.1.2.1.22.0': 'outletCount',
        '.1.3.6.1.4.1.534.6.6.7.3.1.1.2.0.1': 'inputType',
        '.1.3.6.1.4.1.534.6.6.7.3.1.1.5.0.1': 'inputVoltageCount',
        '.1.3.6.1.4.1.534.6.6.7.3.1.1.6.0.1': 'inputCurrentCount',
        '.1.3.6.1.4.1.534.6.6.7.3.1.1.7.0.1': 'inputPowerCount',
         })

    inTypeMap = {1:'singlePhase',
                 2:'splitPhase',
                 3:'threePhaseDelta',
                 4:'threePhaseWye',
                }


    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results

#Uncomment next 2 lines for debugging when modeling
#        log.info( "Get Data= %s", getdata )
#        log.info( "Table Data= %s", tabledata )

        if not getdata:
            log.warn(' No SNMP response from %s for the %s plugin ' % ( device.id, self.name() ) )
            return

        om = self.objectMap(getdata)
        try:
            HWmanufacturer = "Eaton Corporation"
            om.setHWProductKey = MultiArgs(om.setHWProductKey, HWmanufacturer)
            OSmanufacturer = om._OSManufacturer
            om.setOSProductKey = MultiArgs(om.setOSProductKey, OSmanufacturer)
            om.inputType = self.inTypeMap.get(int(om.inputType), 'unknown')
        except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
            log.warn( ' Attribute error in LibraryHPDeviceMap modeler plugin %s', errorInfo)
        return om

