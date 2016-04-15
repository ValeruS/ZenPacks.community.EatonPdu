##########################################################################
# Author:               ValeruS
# Date:                 April 2016
# Revised:
#
# EatonPduCurrent object class
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__="""EatonPduCurrent

EatonPduCurrent is a component of a EatonPduDevice Device

"""

from Globals import InitializeClass

from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class EatonPduCurrent(DeviceComponent, ManagedEntity):
    meta_type = portal_type = "EatonPduCurrent"

    inputCurrentMeasType        = ''
    inputCurrent                = 0
    inputCurrentThStatus        = 0
    inputCurrentThStatusText    = ''
    inputCThUW                  = 0
    inputCThUC                  = 0

    _properties = ManagedEntity._properties + (
        {'id': 'inputCurrentMeasType',       'type': 'string', 'mode': ''},
        {'id': 'inputCurrent',               'type': 'int',    'mode': ''},
        {'id': 'inputCurrentThStatus',       'type': 'int',    'mode': ''},
        {'id': 'inputCurrentThStatusText',   'type': 'string', 'mode': ''},
        {'id': 'inputCThUW',                 'type': 'int',    'mode': ''},
        {'id': 'inputVThUC',                 'type': 'int',    'mode': ''},
    )

    _relations = ManagedEntity._relations + (
        ('EatonPduDevCurrent', ToOne(ToManyCont, 'ZenPacks.community.EatonPdu.EatonPduDevice', 'EatonPduCurrent', ),),
    )

    # Defining the "perfConf" action here causes the "Graphs" display to be
    # available for components of this type.
    factory_type_information = ({
        'id'             : 'EatonPduCurrent',
        'meta_type'      : 'EatonPduCurrent',
        'description'    : """Eaton PDU Voltage info""",
        'product'        : 'EatonPdu',
        'immediate_view' : 'viewEatonPduCurrent',
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
        return self.EatonPduDevCurrent()

InitializeClass(EatonPduCurrent)
