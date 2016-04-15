##########################################################################
# Author:               ValeruS
# Date:                 April 2016
# Revised:
#
# EatonPduVoltage object class
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__="""EatonPduVoltage

EatonPduVoltage is a component of a EatonPduDevice Device

"""

from Globals import InitializeClass

from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class EatonPduVoltage(DeviceComponent, ManagedEntity):
    meta_type = portal_type = "EatonPduVoltage"

    inputVoltageMeasType        = ''
    inputVoltage                = 0
    inputVoltageThStatus        = 0
    inputVoltageThStatusText    = ''
    inputVThUW                  = 0
    inputVThUC                  = 0

    _properties = ManagedEntity._properties + (
        {'id': 'inputVoltageMeasType',       'type': 'string', 'mode': ''},
        {'id': 'inputVoltage',               'type': 'int',    'mode': ''},
        {'id': 'inputVoltageThStatus',       'type': 'int',    'mode': ''},
        {'id': 'inputVoltageThStatusText',   'type': 'string', 'mode': ''},
        {'id': 'inputVThUW',                 'type': 'int',    'mode': ''},
        {'id': 'inputVThUC',                 'type': 'int',    'mode': ''},
    )

    _relations = ManagedEntity._relations + (
        ('EatonPduDevVoltage', ToOne(ToManyCont, 'ZenPacks.community.EatonPdu.EatonPduDevice', 'EatonPduVoltage', ),),
    )

    # Defining the "perfConf" action here causes the "Graphs" display to be
    # available for components of this type.
    factory_type_information = ({
        'id'             : 'EatonPduVoltage',
        'meta_type'      : 'EatonPduVoltage',
        'description'    : """Eaton PDU Voltage info""",
        'product'        : 'EatonPdu',
        'immediate_view' : 'viewEatonPduVoltage',
        'actions'        : 
        (
           {'id'            : 'perfConf',
            'name'          : 'Template',
            'action'        : 'objTemplates',
            'permissions'   : (ZEN_CHANGE_DEVICE,),
           },
        ),
    },)


    # Custom components must always implement the device method. The method
    # should return the device object that contains the component.
    def device(self):
        return self.EatonPduDevVoltage()

InitializeClass(EatonPduVoltage)
