##########################################################################
# Author:               ValeruS
# Date:                 April 2016
# Revised:
#
# EatonPduVoltage modeler plugin
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__ = """EatonPduVoltageMap

Gather table information from Eaton PDU devices voltage.
"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap

class EatonPduVoltageMap(SnmpPlugin):
    """Map Eaton PDU Voltage table to model."""
    maptype = "EatonPduVoltageMap"
    modname = "ZenPacks.community.EatonPdu.EatonPduVoltage"
    relname = "EatonPduVoltage"

    snmpGetTableMaps = (
        GetTableMap('EatonPduVoltageEntry',
                    '.1.3.6.1.4.1.534.6.6.7.3.2.1',
                    {
                        '.2.0': 'inputVoltageMeasType',
                        '.3.0': 'inputVoltage',
                        '.4.0': 'inputVoltageThStatus',
                        '.7.0': 'inputVThUW',
                        '.8.0': 'inputVThUC',
                    }
        ),
    )
    volType   = {1:'singlePhase',
                 2:'phase1toN',
                 3:'phase2toN',
                 4:'phase3toN',
                 5:'phase1to2',
                 6:'phase2to3',
                 7:'phase3to1',
                }
    volThStatusMap  = { 0: (0, 'good'),
                        1: (2, 'lowWarning'),
                        2: (3, 'lowCritical'),
                        3: (3, 'highWarning'),
                        4: (4, 'highCritical'),
                      }

    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        rm = self.relMap()
        voltageentry = tabledata.get('EatonPduVoltageEntry')

# If no data supplied then simply return
        if not voltageentry:
            log.warn( 'No SNMP response from %s for the %s plugin', device.id, self.name() )
            log.warn( "Data= %s", tabledata )
            return

        for oid, data in voltageentry.iteritems():
            try:
                om = self.objectMap(data)
                index1 = om.inputVoltageThStatus
                om.inputVoltageThStatus = self.volThStatusMap[index1][0]
                om.inputVoltageThStatusText = self.volThStatusMap[index1][1]
                om.snmpindex = oid.strip('.')
                om.inputVoltageMeasType = self.volType.get(int(om.inputVoltageMeasType), 'unknown')
                om.id = self.prepId(om.inputVoltageMeasType)
            except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
                log.warn( ' Error in EatonPduVoltageMap modeler plugin %s', errorInfo)
                continue
            rm.append(om)
        return rm
