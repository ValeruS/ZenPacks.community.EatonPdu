##########################################################################
# Author:               ValeruS
# Date:                 April 2016
# Revised:
#
# interfaces.py for EatonPdu ZenPack
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""interfaces

describes the form field to the user interface.

"""
from Products.Zuul.form import schema
from Products.Zuul.interfaces.device import IDeviceInfo
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.utils import ZuulMessageFactory as _t

from Products.ZenModel.ZVersion import VERSION as ZENOSS_VERSION
from Products.ZenUtils.Version import Version

if Version.parse('Zenoss %s' % ZENOSS_VERSION) >= Version.parse('Zenoss 4'):
    SingleLineText = schema.TextLine
    MultiLineText = schema.Text
else:
    SingleLineText = schema.Text
    MultiLineText = schema.TextLine


class IEatonPduDeviceInfo(IDeviceInfo):
    """
    Info adapter for EatonPduDevice component
    """
    inputType                      = SingleLineText(title=_t(u"Type of Input"))
    inputCount                     = SingleLineText(title=_t(u"Input Count"))
    groupCount                     = SingleLineText(title=_t(u"Group Count"))
    outletCount                    = SingleLineText(title=_t(u"Number of Outlets"))
    inputVoltageCount              = SingleLineText(title=_t(u"Voltage Count"))
    inputCurrentCount              = SingleLineText(title=_t(u"Current Count"))
    inputPowerCount                = SingleLineText(title=_t(u"Power Count"))


class IEatonPduOutletInfo(IComponentInfo):
    """
    Info adapter for EatonPduOutlet component
    """
    outletID                    = SingleLineText(title=_t(u"Group"))
    outletName                  = SingleLineText(title=_t(u"Name"))
    outletVoltage               = SingleLineText(title=_t(u"Voltage(mV)"))
    outletCurrent               = SingleLineText(title=_t(u"Current(mA)"))
    outletVA                    = SingleLineText(title=_t(u"Apparent Power (VA)"))
    outletWatts                 = SingleLineText(title=_t(u"Active Power (W)"))
    outletVoltageThStatus       = SingleLineText(title=_t(u"Voltage Status"))
#    outletVoltageThStatusText   = SingleLineText(title=_t(u"Voltage Status"))
    outletCurrentThStatus       = SingleLineText(title=_t(u"Current Status"))
#    outletCurrentThStatusText   = SingleLineText(title=_t(u"Current Status"))
    outletWhTimer               = SingleLineText(title=_t(u"Since from Date"))
    outletWh                    = SingleLineText(title=_t(u"Watt-hours (Wh)"))

class IEatonPduGroupInfo(IComponentInfo):
    """
    Info adapter for EatonPduGroup component
    """

    groupID                     = SingleLineText(title=_t(u"Group"))
    groupName                   = SingleLineText(title=_t(u"Name"))
    groupType                   = SingleLineText(title=_t(u"Type"))
    groupChildCount             = SingleLineText(title=_t(u"Count of Outlets"))
    groupCurrent                = SingleLineText(title=_t(u"Current (mA)"))
    groupVA                     = SingleLineText(title=_t(u"Apparent Power (VA)"))
    groupWatts                  = SingleLineText(title=_t(u"Active Power (W)"))
    groupCurrentThStatus        = SingleLineText(title=_t(u"Current Status"))
#    groupCurrentThStatusText    = SingleLineText(title=_t(u"Current Status"))
    groupWhTimer                = SingleLineText(title=_t(u"Since from Date"))
    groupWh                     = SingleLineText(title=_t(u"Watt-hours (Wh)"))


class IEatonPduEnvInfo(IComponentInfo):
    """
    Info adapter for EatonPduEnv component
    """

    idName                      = SingleLineText(title=_t(u"Name"))
    Value                       = SingleLineText(title=_t(u"Value"))
    ProbeStatus                 = SingleLineText(title=_t(u"Seonsrs Status"))
    ThStatus                    = SingleLineText(title=_t(u"Measured Status"))

class IEatonPduPowerInfo(IComponentInfo):
    """
    Info adapter for EatonPduPower component
    """

    inputPowerMeasType          = SingleLineText(title=_t(u"Type"))
    inputVA                     = SingleLineText(title=_t(u"Apparent Power (VA)"))
    inputWatts                  = SingleLineText(title=_t(u"Active Power (W)"))
    inputWhTimer                = SingleLineText(title=_t(u"Since from Date"))
    inputWh                     = SingleLineText(title=_t(u"Watt-hour (Wh)"))

class IEatonPduVoltageInfo(IComponentInfo):
    """
    Info adapter for EatonPduVoltage component
    """

    inputVoltageMeasType         = SingleLineText(title=_t(u"Type"))
    inputVoltage                 = SingleLineText(title=_t(u"Voltage(mV)"))
    inputVoltageThStatus         = SingleLineText(title=_t(u"Voltage Status"))

class IEatonPduCurrentInfo(IComponentInfo):
    """
    Info adapter for EatonPduCurrent component
    """

    inputCurrentMeasType         = SingleLineText(title=_t(u"Type"))
    inputCurrent                 = SingleLineText(title=_t(u"Current (mA)"))
    inputCurrentThStatus         = SingleLineText(title=_t(u"Current Status"))
