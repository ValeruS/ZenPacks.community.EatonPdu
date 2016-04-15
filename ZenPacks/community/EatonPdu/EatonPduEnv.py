##########################################################################
# Author:               ValeruS
# Date:                 April 2016
# Revised:
#
# EatonPduEnv object class
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__="""EatonPduEnv

EatonPduEnv is a component of a EatonPduDevice Device

"""

from Globals import InitializeClass

from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class EatonPduEnv(DeviceComponent, ManagedEntity):
    meta_type = portal_type = "EatonPduEnv"

    idName             = ''
    thsnmpindex        = ''
    ProbeStatus        = 0
    ProbeStatusText    = ''
    Value              = ''
    ThStatus           = 0
    ThStatusText       = ''
    ThUW               = 0
    ThUC               = 0

    _properties = ManagedEntity._properties + (
        {'id': 'idName',          'type': 'string', 'mode': ''},
        {'id': 'thsnmpindex',     'type': 'string', 'mode': ''},
        {'id': 'ProbeStatus',     'type': 'int',    'mode': ''},
        {'id': 'ProbeStatusText', 'type': 'string', 'mode': ''},
        {'id': 'Value',           'type': 'string', 'mode': ''},
        {'id': 'ThStatus',        'type': 'int',    'mode': ''},
        {'id': 'ThStatusText',    'type': 'string', 'mode': ''},
        {'id': 'ThUW',            'type': 'int',    'mode': ''},
        {'id': 'ThUC',            'type': 'int',    'mode': ''},
    )

    _relations = ManagedEntity._relations + (
        ('EatonPduDevEnv', ToOne(ToManyCont, 'ZenPacks.community.EatonPdu.EatonPduDevice', 'EatonPduEnv', ),),
    )

    # Defining the "perfConf" action here causes the "Graphs" display to be
    # available for components of this type.
    factory_type_information = ({
        'id'             : 'EatonPduEnv',
        'meta_type'      : 'EatonPduEnv',
        'description'    : """Eaton PDU Env info""",
        'product'        : 'EatonPdu',
        'immediate_view' : 'viewEatonPduEnv',
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
        return self.EatonPduDevEnv()

    def getRRDTemplates(self):
        templates = []
        tnames = ['EatonPduEnv',]
        if self.thsnmpindex == "Temperature": tnames.append('EatonPduEnvTemp')
        if self.thsnmpindex == "Humidity":    tnames.append('EatonPduEnvHumi')
        for tname in tnames:
            templ = self.getRRDTemplateByName(tname)
            if templ: templates.append(templ)
        return templates

InitializeClass(EatonPduEnv)
