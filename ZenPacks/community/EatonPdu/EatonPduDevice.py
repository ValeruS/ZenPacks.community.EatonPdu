##########################################################################
# Author:               ValeruS
# Date:                 April 2016
# Revised:
#
# EatonPduDevice object class
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################


from Globals import InitializeClass

from Products.ZenModel.Device import Device
from Products.ZenRelations.RelSchema import ToManyCont, ToOne
from Products.ZenModel.ZenossSecurity import ZEN_VIEW

from copy import deepcopy

class EatonPduDevice(Device):
    "Eaton PDU Device"
    meta_type = portal_type = 'EatonPduDevice'


    inputType              = None
    inputCount             = None
    groupCount             = None
    outletCount            = None
    inputVoltageCount      = None
    inputCurrentCount      = None
    inputPowerCount        = None

    _properties = Device._properties + (
        {'id': 'inputType',                'type': 'int'},
        {'id': 'inputCount',               'type': 'int'},
        {'id': 'groupCount',               'type': 'int'},
        {'id': 'outletCount',              'type': 'int'},
        {'id': 'inputVoltageCount',        'type': 'int'},
        {'id': 'inputCurrentCount',        'type': 'int'},
        {'id': 'inputPowerCount',          'type': 'int'},
    )


    _relations = Device._relations + (
        ('EatonPduOutlet',  ToManyCont(ToOne, 'ZenPacks.community.EatonPdu.EatonPduOutlet',  'EatonPduDevOutlet',),),
        ('EatonPduGroup',   ToManyCont(ToOne, 'ZenPacks.community.EatonPdu.EatonPduGroup',   'EatonPduDevGroup',),),
        ('EatonPduEnv',     ToManyCont(ToOne, 'ZenPacks.community.EatonPdu.EatonPduEnv',     'EatonPduDevEnv',),),
        ('EatonPduPower',   ToManyCont(ToOne, 'ZenPacks.community.EatonPdu.EatonPduPower',   'EatonPduDevPower',),),
        ('EatonPduVoltage', ToManyCont(ToOne, 'ZenPacks.community.EatonPdu.EatonPduVoltage', 'EatonPduDevVoltage',),),
        ('EatonPduCurrent', ToManyCont(ToOne, 'ZenPacks.community.EatonPdu.EatonPduCurrent', 'EatonPduDevCurrent',),),
    )

InitializeClass(EatonPduDevice)
