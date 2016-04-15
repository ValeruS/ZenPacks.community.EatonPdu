##########################################################################
# Author:               ValeruS
# Date:                 April 2016
# Revised:
#
# EatonPduPower modeler plugin
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__ = """EatonPduPowerMap

Gather table information from Eaton PDU devices power.
"""

import datetime

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap

class EatonPduPowerMap(SnmpPlugin):
    """Map Eaton PDU Group table to model."""
    maptype = "EatonPduPowerMap"
    modname = "ZenPacks.community.EatonPdu.EatonPduPower"
    relname = "EatonPduPower"

    snmpGetTableMaps = (
        GetTableMap('EatonPduPowerEntry',
                    '.1.3.6.1.4.1.534.6.6.7.3.4.1',
                    {
                        '.2.0': 'inputPowerMeasType',
                        '.3.0': 'inputVA',
                        '.4.0': 'inputWatts',
                        '.5.0': 'inputWh',
                        '.6.0': 'inputWhTimer',
                    }
        ),
    )
    MeasTypeMap = {0:'unknown',
                   1:'phase1',
                   2:'phase2',
                   3:'phase3',
                   4:'total',
                  }

    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        rm = self.relMap()
        powerentry = tabledata.get('EatonPduPowerEntry')

# If no data supplied then simply return
        if not powerentry:
            log.warn( 'No SNMP response from %s for the %s plugin', device.id, self.name() )
            log.warn( "Data= %s", tabledata )
            return

        for oid, data in powerentry.iteritems():
            try:
                om = self.objectMap(data)
                om.snmpindex = oid.strip('.')
                om.inputPowerMeasType = self.MeasTypeMap.get(int(om.inputPowerMeasType), 'unknown')
                om.inputWhTimer = datetime.datetime.fromtimestamp(om.inputWhTimer).strftime('%d-%m-%Y %H:%M:%S')
                om.id = self.prepId(om.inputPowerMeasType)
            except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
                log.warn( ' Error in EatonPduPowerMap modeler plugin %s', errorInfo)
                continue
            rm.append(om)
        return rm
