##########################################################################
# Author:               ValeruS
# Date:                 April 2016
# Revised:
#
# EatonPduPower object class
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__="""EatonPduPower

EatonPduPower is a component of a EatonPduDevice Device

"""

from Globals import InitializeClass

from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class EatonPduPower(DeviceComponent, ManagedEntity):
    meta_type = portal_type = "EatonPduPower"

    inputPowerMeasType        = ''
    inputVA                   = 0
    inputWatts                = 0
    inputWh                   = 0
    inputWhTimer              = 0

    _properties = ManagedEntity._properties + (
        {'id': 'inputPowerMeasType',         'type': 'string', 'mode': ''},
        {'id': 'inputVA',                    'type': 'int',    'mode': ''},
        {'id': 'inputWatts',                 'type': 'int',    'mode': ''},
        {'id': 'inputWh',                    'type': 'int',    'mode': ''},
        {'id': 'inputWhTimer',               'type': 'int',    'mode': ''},
    )

    _relations = ManagedEntity._relations + (
        ('EatonPduDevPower', ToOne(ToManyCont, 'ZenPacks.community.EatonPdu.EatonPduDevice', 'EatonPduPower', ),),
    )

    # Defining the "perfConf" action here causes the "Graphs" display to be
    # available for components of this type.
    factory_type_information = ({
        'id'             : 'EatonPduPower',
        'meta_type'      : 'EatonPduPower',
        'description'    : """Eaton PDU Power info""",
        'product'        : 'EatonPdu',
        'immediate_view' : 'viewEatonPduPower',
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
        return self.EatonPduDevPower()

InitializeClass(EatonPduPower)
