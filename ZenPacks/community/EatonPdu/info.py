##########################################################################
# Author:               ValeruS
# Date:                 April 2016
# Revised:
#
# info.py for EatonPdu ZenPack
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""info.py

Representation of EatonPdu components.

"""


from zope.interface import implements

from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.device import DeviceInfo
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.decorators import info

from ZenPacks.community.EatonPdu import interfaces


class EatonPduDeviceInfo(DeviceInfo):
    implements(interfaces.IEatonPduDeviceInfo)

    inputType                  = ProxyProperty("inputType")
    inputCount                 = ProxyProperty("inputCount")
    groupCount                 = ProxyProperty("groupCount")
    outletCount                = ProxyProperty("outletCount")
    inputVoltageCount          = ProxyProperty("inputVoltageCount")
    inputCurrentCount          = ProxyProperty("inputCurrentCount")
    inputPowerCount            = ProxyProperty("inputPowerCount")


class EatonPduOutletInfo(ComponentInfo):
    implements(interfaces.IEatonPduOutletInfo)

    outletNumber                = ProxyProperty("outletNumber")
    outletID                    = ProxyProperty("outletID")
    outletName                  = ProxyProperty("outletName")
    outletVoltage               = ProxyProperty("outletVoltage")
    outletCurrent               = ProxyProperty("outletCurrent")
    outletVA                    = ProxyProperty("outletVA")
    outletWatts                 = ProxyProperty("outletWatts")
    outletVoltageThStatus       = ProxyProperty("outletVoltageThStatus")
    outletVoltageThStatusText   = ProxyProperty("outletVoltageThStatusText")
    outletCurrentThStatus       = ProxyProperty("outletCurrentThStatus")
    outletCurrentThStatusText   = ProxyProperty("outletCurrentThStatusText")
    outletWhTimer               = ProxyProperty("outletWhTimer")
    outletWh                    = ProxyProperty("outletWh")
    outletCThUW                 = ProxyProperty("outletCThUW")
    outletCThUC                 = ProxyProperty("outletCThUW")
    outletVThUW                 = ProxyProperty("outletCThUW")
    outletVThUC                 = ProxyProperty("outletCThUW")

class EatonPduGroupInfo(ComponentInfo):
    implements(interfaces.IEatonPduGroupInfo)

    groupID                     = ProxyProperty("groupID")
    groupName                   = ProxyProperty("groupName")
    groupType                   = ProxyProperty("groupType")
    groupChildCount             = ProxyProperty("groupChildCount")
    groupCurrent                = ProxyProperty("groupCurrent")
    groupVA                     = ProxyProperty("groupVA")
    groupWatts                  = ProxyProperty("groupWatts")
    groupCurrentThStatus        = ProxyProperty("groupCurrentThStatus")
    groupCurrentThStatusText    = ProxyProperty("groupCurrentThStatusText")
    groupWhTimer                = ProxyProperty("groupWhTimer")
    groupWh                     = ProxyProperty("groupWh")
    groupCThUW                  = ProxyProperty("groupCThUW")
    groupCThUC                  = ProxyProperty("groupCThUC")

class EatonPduEnvInfo(ComponentInfo):
    implements(interfaces.IEatonPduEnvInfo)

    idName                      = ProxyProperty("idName")
    thsnmpindex                 = ProxyProperty("thsnmpindex")
    ProbeStatus                 = ProxyProperty("ProbeStatus")
    ProbeStatusText             = ProxyProperty("ProbeStatusText")
    Value                       = ProxyProperty("Value")
    ThStatus                    = ProxyProperty("ThStatus")
    ThStatusText                = ProxyProperty("ThStatusText")
    ThUW                        = ProxyProperty("ThUW")
    ThUC                        = ProxyProperty("ThUC")

class EatonPduPowerInfo(ComponentInfo):
    implements(interfaces.IEatonPduPowerInfo)

    inputPowerMeasType          = ProxyProperty("inputPowerMeasType")
    inputVA                     = ProxyProperty("inputVA")
    inputWatts                  = ProxyProperty("inputWatts")
    inputWh                     = ProxyProperty("inputWh")
    inputWhTimer                = ProxyProperty("inputWhTimer")

class EatonPduVoltageInfo(ComponentInfo):
    implements(interfaces.IEatonPduVoltageInfo)

    inputVoltageMeasType         = ProxyProperty("inputVoltageMeasType")
    inputVoltage                 = ProxyProperty("inputVoltage")
    inputVoltageThStatus         = ProxyProperty("inputVoltageThStatus")
    inputVoltageThStatusText     = ProxyProperty("inputVoltageThStatusText")
    inputVThUW                   = ProxyProperty("inputVThUW")
    inputVThUC                   = ProxyProperty("inputVThUC")

class EatonPduCurrentInfo(ComponentInfo):
    implements(interfaces.IEatonPduCurrentInfo)

    inputCurrentMeasType         = ProxyProperty("inputCurrentMeasType")
    inputCurrent                 = ProxyProperty("inputCurrent")
    inputCurrentThStatus         = ProxyProperty("inputCurrentThStatus")
    inputCurrentThStatusText     = ProxyProperty("inputCurrentThStatusText")
    inputCThUW                   = ProxyProperty("inputCThUW")
    inputCThUC                   = ProxyProperty("inputCThUC")
