##########################################################################
# Author:               ValeruS
# Date:                 April 2016
# Revised:
#
# EatonPduOutlet modeler plugin
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__ = """EatonPduOutletMap

Gather table information from Eaton PDU devices outlets.
"""

import datetime

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap

class EatonPduOutletMap(SnmpPlugin):
    """Map Eaton PDU Outlet table to model."""
    maptype = "EatonPduOutletMap"
    modname = "ZenPacks.community.EatonPdu.EatonPduOutlet"
    relname = "EatonPduOutlet"

    snmpGetTableMaps = (
        GetTableMap('EatonPduOutletEntry',
                    '.1.3.6.1.4.1.534.6.6.7.6',
                    {
                        '.1.1.2.0': 'outletID',
                        '.1.1.3.0': 'outletName',
                        '.3.1.2.0': 'outletVoltage',
                        '.4.1.3.0': 'outletCurrent',
                        '.5.1.2.0': 'outletVA',
                        '.5.1.3.0': 'outletWatts',
                        '.3.1.3.0': 'outletVoltageThStatus',
                        '.4.1.4.0': 'outletCurrentThStatus',
                        '.5.1.5.0': 'outletWhTimer',
                        '.5.1.4.0': 'outletWh',
                        '.4.1.7.0': 'outletCThUW',
                        '.4.1.8.0': 'outletCThUC',
                        '.3.1.6.0': 'outletVThUW',
                        '.3.1.7.0': 'outletVThUC',
                    }
        ),
    )


    groupMap =  {1:'A',
                 2:'B',
                }


    outThStatusMap = { 0: (0, 'good'),
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
        outletentry = tabledata.get('EatonPduOutletEntry')


# If no data supplied then simply return
        if not outletentry:
            log.warn( 'No SNMP response from %s for the %s plugin', device.id, self.name() )
            log.warn( "Data= %s", tabledata )
            return

        for oid, data in outletentry.iteritems():
            try:
                om = self.objectMap(data)
                index1 = om.outletVoltageThStatus
                index2 = om.outletCurrentThStatus
                om.outletVoltageThStatus = self.outThStatusMap[index1][0]
                om.outletVoltageThStatusText = self.outThStatusMap[index1][1]
                om.outletCurrentThStatus = self.outThStatusMap[index2][0]
                om.outletCurrentThStatusText = self.outThStatusMap[index2][1]
                om.snmpindex = oid.strip('.')
                om.outletNumber = 10 + int(om.snmpindex)
                om.outletName = om.outletName.replace(' ','')
                if (int(om.snmpindex) == int(om.outletID) ): groupindex = 1
                elif (int(om.snmpindex) > int(om.outletID) ): groupindex = 2
                om.outletID = self.groupMap.get(int(groupindex), 'unknown') + om.outletID
                om.outletWhTimer = datetime.datetime.fromtimestamp(om.outletWhTimer).strftime('%d-%m-%Y %H:%M:%S')
                om.id = self.prepId(om.outletName)
            except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
                log.warn( ' Error in EatonPduOutletMap modeler plugin %s', errorInfo)
                continue
            rm.append(om)
        return rm
