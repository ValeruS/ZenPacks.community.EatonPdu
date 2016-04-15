##########################################################################
# Author:               ValeruS
# Date:                 April 2016
# Revised:
#
# EatonPduEnv modeler plugin
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__ = """EatonPduEnvMap

Gather table information from Eaton PDU devices environmental.
"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap

class EatonPduEnvMap(SnmpPlugin):
    """Map Eaton PDU Env table to model."""
    maptype = "EatonPduEnvMap"
    modname = "ZenPacks.community.EatonPdu.EatonPduEnv"
    relname = "EatonPduEnv"

    snmpGetTableMaps = (
        GetTableMap('EatonPduTempEntry',
                    '.1.3.6.1.4.1.534.6.6.7.7.1',
                    {
                        '.1.2.0': 'idName',
                        '.1.3.0': 'ProbeStatus',
                        '.1.4.0': 'Value',
                        '.1.5.0': 'ThStatus',
                        '.1.8.0': 'ThUW',
                        '.1.9.0': 'ThUC',
                    }
        ),

        GetTableMap('EatonPduHumiEntry',
                    '.1.3.6.1.4.1.534.6.6.7.7.2',
                    {
                        '.1.2.0': 'idName',
                        '.1.3.0': 'ProbeStatus',
                        '.1.4.0': 'Value',
                        '.1.5.0': 'ThStatus',
                        '.1.8.0': 'ThUW',
                        '.1.9.0': 'ThUC',
                    }
        ),
    )

    ProbeStatusMap = {-1: (3, 'bad'),
                       0: (1, 'disconnected'),
                       1: (0, 'connected'),
                     }

    ThStatusMap    = { 0: (0, 'good'),
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
        tempentry = tabledata.get('EatonPduTempEntry')
        humientry = tabledata.get('EatonPduHumiEntry')

# If no data supplied then simply return
        if not (tempentry and humientry):
            log.warn( 'No SNMP response from %s for the %s plugin', device.id, self.name() )
            log.warn( "Data= %s", tabledata )
            return

        for oid, data in humientry.iteritems():
            try:
                om = self.objectMap(data)
                index1 = om.ThStatus
                index2 = om.ProbeStatus
                om.ThStatusText = self.ThStatusMap[index1][1]
                om.ThStatus = self.ThStatusMap[index1][0]
                om.ProbeStatusText = self.ProbeStatusMap[index2][1]
                om.ProbeStatus = self.ProbeStatusMap[index2][0]
                om.thsnmpindex = "Humidity"
                om.snmpindex = int(oid.strip('.'))
                if not om.idName: om.idName = "Humidity" + oid.strip('.')
                om.id = self.prepId(om.idName)
            except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
                log.warn( ' Error in EatonPduHumiMap modeler plugin %s', errorInfo)
                continue
            rm.append(om)

        for oid, data in tempentry.iteritems():
            try:
                om = self.objectMap(data)
                index1 = om.ThStatus
                index2 = om.ProbeStatus
                om.ThStatusText = self.ThStatusMap[index1][1]
                om.ThStatus = self.ThStatusMap[index1][0]
                om.ProbeStatusText = self.ProbeStatusMap[index2][1]
                om.ProbeStatus = self.ProbeStatusMap[index2][0]
                om.thsnmpindex = "Temperature"
                om.snmpindex = oid.strip('.')
                if not om.idName: om.idName = "Temperature" + oid.strip('.')
                om.id = self.prepId(om.idName)
            except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
                log.warn( ' Error in EatonPduTempMap modeler plugin %s', errorInfo)
                continue
            rm.append(om)

        return rm
