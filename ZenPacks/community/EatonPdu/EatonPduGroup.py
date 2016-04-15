##########################################################################
# Author:               ValeruS
# Date:                 April 2016
# Revised:
#
# EatonPduGroup object class
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__="""EatonPduGroup

EatonPduGroup is a component of a EatonPduDevice Device

"""

from Globals import InitializeClass

from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class EatonPduGroup(DeviceComponent, ManagedEntity):
    meta_type = portal_type = "EatonPduGroup"

    groupID                   = ''
    groupName                 = ''
    groupType                 = 0
    groupChildCount           = 0
    groupCurrent              = 0
    groupVA                   = 0
    groupWatts                = 0
    groupCurrentThStatus      = 0
    groupCurrentThStatusText  = ''
    groupWhTimer              = 0
    groupWh                   = 0
    groupCThUW                = 0
    groupCThUC                = 0

    _properties = ManagedEntity._properties + (
        {'id': 'groupID',                    'type': 'string', 'mode': ''},
        {'id': 'groupName',                  'type': 'string', 'mode': ''},
        {'id': 'groupType',                  'type': 'int',    'mode': ''},
        {'id': 'groupChildCount',            'type': 'int',    'mode': ''},
        {'id': 'groupCurrent',               'type': 'int',    'mode': ''},
        {'id': 'groupVA',                    'type': 'int',    'mode': ''},
        {'id': 'groupWatts',                 'type': 'int',    'mode': ''},
        {'id': 'groupCurrentThStatus',       'type': 'int',    'mode': ''},
        {'id': 'groupCurrentThStatusText',   'type': 'string', 'mode': ''},
        {'id': 'groupWhTimer',               'type': 'int',    'mode': ''},
        {'id': 'groupWh',                    'type': 'int',    'mode': ''},
        {'id': 'groupCThUW',                 'type': 'int',    'mode': ''},
        {'id': 'groupCThUC',                 'type': 'int',    'mode': ''},
    )

    _relations = ManagedEntity._relations + (
        ('EatonPduDevGroup', ToOne(ToManyCont, 'ZenPacks.community.EatonPdu.EatonPduDevice', 'EatonPduGroup', ),),
    )

    # Defining the "perfConf" action here causes the "Graphs" display to be
    # available for components of this type.
    factory_type_information = ({
        'id'             : 'EatonPduGroup',
        'meta_type'      : 'EatonPduGroup',
        'description'    : """Eaton PDU Group info""",
        'product'        : 'EatonPdu',
        'immediate_view' : 'viewEatonPduGroup',
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
        return self.EatonPduDevGroup()

InitializeClass(EatonPduGroup)
