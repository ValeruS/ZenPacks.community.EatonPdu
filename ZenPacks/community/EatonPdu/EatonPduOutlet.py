##########################################################################
# Author:               ValeruS
# Date:                 April 2016
# Revised:
#
# EatonPduOutlet object class
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__="""EatonPduOutlet

EatonPduOutlet is a component of a EatonPduDevice Device

"""

from Globals import InitializeClass

from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class EatonPduOutlet(DeviceComponent, ManagedEntity):
    meta_type = portal_type = "EatonPduOutlet"

    outletNumber               = 0
    outletID                   = ''
    outletName                 = ''
    outletVoltage              = 0
    outletCurrent              = 0
    outletVA                   = 0
    outletWatts                = 0
    outletVoltageThStatus      = 0
    outletVoltageThStatusText  = ''
    outletCurrentThStatus      = 0
    outletCurrentThStatusText  = ''
    outletWhTimer              = ''
    outletWh                   = 0
    outletCThUW                = 0
    outletCThUC                = 0
    outletVThUW                = 0
    outletVThUC                = 0

    _properties = ManagedEntity._properties + (
        {'id': 'outletNumber',                'type': 'int',    'mode': ''},
        {'id': 'outletID',                    'type': 'string', 'mode': ''},
        {'id': 'outletName',                  'type': 'string', 'mode': ''},
        {'id': 'outletVoltage',               'type': 'int',    'mode': ''},
        {'id': 'outletCurrent',               'type': 'int',    'mode': ''},
        {'id': 'outletVA',                    'type': 'int',    'mode': ''},
        {'id': 'outletWatts',                 'type': 'int',    'mode': ''},
        {'id': 'outletVoltageThStatus',       'type': 'int',    'mode': ''},
        {'id': 'outletVoltageThStatusText',   'type': 'string', 'mode': ''},
        {'id': 'outletCurrentThStatus',       'type': 'int',    'mode': ''},
        {'id': 'outletCurrentThStatusText',   'type': 'string', 'mode': ''},
        {'id': 'outletWhTimer',               'type': 'string', 'mode': ''},
        {'id': 'outletWh',                    'type': 'int',    'mode': ''},
        {'id': 'outletCThUW',                 'type': 'int',    'mode': ''},
        {'id': 'outletCThUC',                 'type': 'int',    'mode': ''},
        {'id': 'outletVThUW',                 'type': 'int',    'mode': ''},
        {'id': 'outletVThUC',                 'type': 'int',    'mode': ''},
    )

    _relations = ManagedEntity._relations + (
        ('EatonPduDevOutlet', ToOne(ToManyCont, 'ZenPacks.community.EatonPdu.EatonPduDevice', 'EatonPduOutlet', ),),
    )

    # Defining the "perfConf" action here causes the "Graphs" display to be
    # available for components of this type.
    factory_type_information = ({
        'id'             : 'EatonPduOutlet',
        'meta_type'      : 'EatonPduOutlet',
        'description'    : """Eaton PDU Outlet info""",
        'product'        : 'EatonPdu',
        'immediate_view' : 'viewEatonPduOutlet',
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
        return self.EatonPduDevOutlet()

InitializeClass(EatonPduOutlet)
