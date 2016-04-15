##########################################################################
# Author:               ValeruS
# Date:                 April 2016
# Revised:
#
# EatonPduCurrent modeler plugin
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__ = """EatonPduCurrentMap

Gather table information from Eaton PDU devices current.
"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap

class EatonPduCurrentMap(SnmpPlugin):
    """Map Eaton PDU Voltage table to model."""
    maptype = "EatonPduCurrentMap"
    modname = "ZenPacks.community.EatonPdu.EatonPduCurrent"
    relname = "EatonPduCurrent"

    snmpGetTableMaps = (
        GetTableMap('EatonPduCurrentEntry',
                    '.1.3.6.1.4.1.534.6.6.7.3.3.1',
                    {
                        '.2.0': 'inputCurrentMeasType',
                        '.4.0': 'inputCurrent',
                        '.5.0': 'inputCurrentThStatus',
                        '.8.0': 'inputCThUW',
                        '.9.0': 'inputCThUC',
                    }
        ),
    )
    crnType   = {1:'singlePhase',
                 2:'neutral',
                 3:'phase1',
                 4:'phase2',
                 5:'phase3',
                }
    crnThStatusMap  = { 0: (0, 'good'),
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
        currententry = tabledata.get('EatonPduCurrentEntry')

# If no data supplied then simply return
        if not currententry:
            log.warn( 'No SNMP response from %s for the %s plugin', device.id, self.name() )
            log.warn( "Data= %s", tabledata )
            return

        for oid, data in currententry.iteritems():
            try:
                om = self.objectMap(data)
                index1 = om.inputCurrentThStatus
                om.inputCurrentThStatus = self.crnThStatusMap[index1][0]
                om.inputCurrentThStatusText = self.crnThStatusMap[index1][1]
                om.snmpindex = oid.strip('.')
                om.inputCurrentMeasType = self.crnType.get(int(om.inputCurrentMeasType), 'unknown')
                om.id = self.prepId(om.inputCurrentMeasType)
            except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
                log.warn( ' Error in EatonPduCurrentMap modeler plugin %s', errorInfo)
                continue
            rm.append(om)
        return rm
