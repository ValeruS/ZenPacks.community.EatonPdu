##########################################################################
# Author:               ValeruS
# Date:                 April 2016
# Revised:
#
# EatonPduGroup modeler plugin
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__ = """EatonPduGroupMap

Gather table information from Eaton PDU devices groups.
"""

import datetime

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap

class EatonPduGroupMap(SnmpPlugin):
    """Map Eaton PDU Group table to model."""
    maptype = "EatonPduGroupMap"
    modname = "ZenPacks.community.EatonPdu.EatonPduGroup"
    relname = "EatonPduGroup"

    snmpGetTableMaps = (
        GetTableMap('EatonPduGroupEntry',
                    '.1.3.6.1.4.1.534.6.6.7.5',
                    {
                        '.1.1.2.0': 'groupID',
                        '.1.1.3.0': 'groupName',
                        '.1.1.4.0': 'groupType',
                        '.1.1.6.0': 'groupChildCount',
                        '.4.1.3.0': 'groupCurrent',
                        '.5.1.2.0': 'groupVA',
                        '.5.1.3.0': 'groupWatts',
                        '.4.1.4.0': 'groupCurrentThStatus',
                        '.5.1.5.0': 'groupWhTimer',
                        '.5.1.4.0': 'groupWh',
                        '.4.1.7.0': 'groupCThUW',
                        '.4.1.8.0': 'groupCThUC',
                    }
        ),
    )
    grType    = {0:'notApplicable',
                 1:'breaker1pole',
                 2:'breaker2pole',
                 3:'breaker3pole',
                 4:'outletSection',
                 5:'userDefined',
                }
    grThStatusMap  = { 0: (0, 'good'),
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
        groupentry = tabledata.get('EatonPduGroupEntry')

# If no data supplied then simply return
        if not groupentry:
            log.warn( 'No SNMP response from %s for the %s plugin', device.id, self.name() )
            log.warn( "Data= %s", tabledata )
            return

        for oid, data in groupentry.iteritems():
            try:
                om = self.objectMap(data)
                index1 = om.groupCurrentThStatus
                om.groupCurrentThStatus = self.grThStatusMap[index1][0]
                om.groupCurrentThStatusText = self.grThStatusMap[index1][1]
                om.snmpindex = oid.strip('.')
                om.groupName = om.groupName.replace(' ','')
                om.groupType = self.grType.get(int(om.groupType), 'unknown')
                om.groupWhTimer = datetime.datetime.fromtimestamp(om.groupWhTimer).strftime('%d-%m-%Y %H:%M:%S')
                om.id = self.prepId(om.groupName)
            except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
                log.warn( ' Error in EatonPduGroupMap modeler plugin %s', errorInfo)
                continue
            rm.append(om)
        return rm
