/*
 * Based on the configuration in ../../configure.zcml this JavaScript will only
 * be loaded when the user is looking at an ExampleDevice in the web interface.
 */

(function(){

var ZC = Ext.ns('Zenoss.component');

function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}


Ext.onReady(function() {
    var DEVICE_OVERVIEW_ID = 'deviceoverviewpanel_summary';
    Ext.ComponentMgr.onAvailable(DEVICE_OVERVIEW_ID, function(){
        var overview = Ext.getCmp(DEVICE_OVERVIEW_ID);
        overview.removeField('memory');

        overview.addField({
            name: 'outletCount',
            fieldLabel: _t('Number of Outlets')
        });
    });
});

Ext.onReady(function() {
    var DEVICE_SNMP_ID = 'deviceoverviewpanel_snmpsummary';
    Ext.ComponentMgr.onAvailable(DEVICE_SNMP_ID, function() {
        var snmp = Ext.getCmp(DEVICE_SNMP_ID);
        snmp.removeField('snmpSysName');
        snmp.removeField('snmpLocation');
        snmp.removeField('snmpContact');
        snmp.removeField('snmpDescr');
        snmp.removeField('snmpCommunity');
        snmp.removeField('snmpVersion');

        snmp.addField({
            xtype: 'displayfield',
            id: 'inputType-displayfield',
            name: 'inputType',
            fieldLabel: _t('Type of Input')
        });
        snmp.addField({
            xtype: 'displayfield',
            id: 'inputCount-displayfield',
            name: 'inputCount',
            fieldLabel: _t('Input Count')
        });
        snmp.addField({
            xtype: 'displayfield',
            id: 'groupCount-displayfield',
            name: 'groupCount',
            fieldLabel: _t('Group Count')
        });
        snmp.addField({
            xtype: 'displayfield',
            id: 'inputVoltageCount-displayfield',
            name: 'inputVoltageCount',
            fieldLabel: _t('Voltage Count')
        });
        snmp.addField({
            xtype: 'displayfield',
            id: 'inputCurrentCount-displayfield',
            name: 'inputCurrentCount',
            fieldLabel: _t('Current Count')
        });
        snmp.addField({
            xtype: 'displayfield',
            id: 'inputPowerCount-displayfield',
            name: 'inputPowerCount',
            fieldLabel: _t('Power Count')
        });

    });
});


ZC.EatonPduOutletPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'EatonPduOutlet',
            alias:['widget.EatonPduOutletPanel'],
            sortInfo: {
                field: 'outletNumber',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'outletNumber'},
                {name: 'outletID'},
                {name: 'outletVoltage'},
                {name: 'outletCurrent'},
                {name: 'outletVA'},
                {name: 'outletWatts'},
                {name: 'outletVoltageThStatus'},
                {name: 'outletVoltageThStatusText'},
                {name: 'outletCurrentThStatus'},
                {name: 'outletCurrentThStatusText'},
                {name: 'outletWhTimer'},
                {name: 'outletWh'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'outletID',
                dataIndex: 'outletID',
                header: _t('Group'),
                sortable: true,
                width: 70
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Outlet'),
                width: 100
            },{
                id: 'outletVoltage',
                dataIndex: 'outletVoltage',
                header: _t('Voltage (V)'),
                sortable: true,
                width: 100,
//                renderer: function(x){ return x + ' mV';}
                renderer: function(x){ return (x/1000);}
            },{
                id: 'outletCurrent',
                dataIndex: 'outletCurrent',
                header: _t('Current (A)'),
                sortable: true,
                width: 100,
                renderer: function(x){ return (x/1000);}
            },{
                id: 'outletVA',
                dataIndex: 'outletVA',
                header: _t('Apparent Power (VA)'),
                sortable: true,
                width: 120,
            },{
                id: 'outletWatts',
                dataIndex: 'outletWatts',
                header: _t('Active Power (W)'),
                sortable: true,
                width: 120,
            },{
                id: 'outletVoltageThStatus',
                dataIndex: 'outletVoltageThStatus',
                header: _t(''),
                renderer: Zenoss.render.severity,
                width: 21,
            },{
                id: 'outletVoltageThStatusText',
                dataIndex: 'outletVoltageThStatusText',
                header: _t('Voltage Status'),
                sortable: true,
                width: 100,
            },{
                id: 'outletCurrentThStatus',
                dataIndex: 'outletCurrentThStatus',
                header: _t(''),
                renderer: Zenoss.render.severity,
                width: 21,
            },{
                id: 'outletCurrentThStatusText',
                dataIndex: 'outletCurrentThStatusText',
                header: _t('Current Status'),
                sortable: true,
                width: 100,
            },{
                id: 'outletWhTimer',
                dataIndex: 'outletWhTimer',
                header: _t('Since from Date'),
                sortable: true,
                width: 150,
            },{
                id: 'outletWh',
                flex: 1,
                dataIndex: 'outletWh',
                header: _t('Watt Hour (kWh)'),
                sortable: true,
                width: 100,
                renderer: function(x){ return (x/1000);}
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.EatonPduOutletPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('EatonPduOutletPanel', ZC.EatonPduOutletPanel);
ZC.registerName('EatonPduOutlet', _t('ePDU Outlet'), _t('ePDU Outlets'));


ZC.EatonPduGroupPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'EatonPduGroup',
            alias:['widget.EatonPduGroupPanel'],
            sortInfo: {
                field: 'groupID',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'groupID'},
                {name: 'groupType'},
                {name: 'groupChildCount'},
                {name: 'groupCurrent'},
                {name: 'groupVA'},
                {name: 'groupWatts'},
                {name: 'groupCurrentThStatus'},
                {name: 'groupCurrentThStatusText'},
                {name: 'groupWhTimer'},
                {name: 'groupWh'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'groupID',
                dataIndex: 'groupID',
                header: _t('Group'),
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                width: 100
            },{
                id: 'groupType',
                dataIndex: 'groupType',
                header: _t('Type'),
                sortable: true,
                width: 100,
            },{
                id: 'groupChildCount',
                dataIndex: 'groupChildCount',
                header: _t('Count of Outlets'),
                sortable: true,
                width: 100,
            },{
                id: 'groupCurrent',
                dataIndex: 'groupCurrent',
                header: _t('Current (A)'),
                sortable: true,
                width: 100,
                renderer: function(x){ return (x/1000);}
            },{
                id: 'groupVA',
                dataIndex: 'groupVA',
                header: _t('Apparent Power (VA)'),
                sortable: true,
                width: 120,
            },{
                id: 'groupWatts',
                dataIndex: 'groupWatts',
                header: _t('Active Power (W)'),
                sortable: true,
                width: 120,
            },{
                id: 'groupCurrentThStatus',
                dataIndex: 'groupCurrentThStatus',
                header: _t(''),
                renderer: Zenoss.render.severity,
                width: 21,
            },{
                id: 'groupCurrentThStatusText',
                dataIndex: 'groupCurrentThStatusText',
                header: _t('Current Status'),
                sortable: true,
                width: 100,
            },{
                id: 'groupWhTimer',
                dataIndex: 'groupWhTimer',
                header: _t('Since from Date'),
                sortable: true,
                width: 150,
            },{
                id: 'groupWh',
                flex: 1,
                dataIndex: 'groupWh',
                header: _t('Watt Hour (kWh)'),
                sortable: true,
                width: 100,
                renderer: function(x){ return (x/1000);}
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.EatonPduGroupPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('EatonPduGroupPanel', ZC.EatonPduGroupPanel);
ZC.registerName('EatonPduGroup', _t('ePDU Group'), _t('ePDU Groups'));


ZC.EatonPduEnvPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'EatonPduEnv',
            alias:['widget.EatonPduEnvPanel'],
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'Value'},
                {name: 'ProbeStatus'},
                {name: 'ProbeStatusText'},
                {name: 'ThStatus'},
                {name: 'ThStatusText'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                width: 100
            },{
                id: 'Value',
                dataIndex: 'Value',
                header: _t('Value (% / °C)'),
                sortable: true,
                width: 100,
                renderer: function(x){ return (x/10);}
            },{
                id: 'ProbeStatus',
                dataIndex: 'ProbeStatus',
                header: _t(''),
                renderer: Zenoss.render.severity,
                width: 21,
            },{
                id: 'ProbeStatusText',
                dataIndex: 'ProbeStatusText',
                header: _t('Sensor Status'),
                sortable: true,
                width: 100,
            },{
                id: 'ThStatus',
                dataIndex: 'ThStatus',
                header: _t(''),
                renderer: Zenoss.render.severity,
                width: 21,
            },{
                id: 'ThStatusText',
                flex: 1,
                dataIndex: 'ThStatusText',
                header: _t('Measured Status'),
                sortable: true,
                width: 100,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.EatonPduEnvPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('EatonPduEnvPanel', ZC.EatonPduEnvPanel);
ZC.registerName('EatonPduEnv', _t('ePDU Env'), _t('ePDU Envs'));


ZC.EatonPduPowerPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'EatonPduPower',
            alias:['widget.EatonPduPowerPanel'],
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'inputVA'},
                {name: 'inputWatts'},
                {name: 'inputWhTimer'},
                {name: 'inputWh'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                width: 100
            },{
                id: 'inputVA',
                dataIndex: 'inputVA',
                header: _t('Apparent Power (VA)'),
                sortable: true,
                width: 120,
            },{
                id: 'inputWatts',
                dataIndex: 'inputWatts',
                header: _t('Active Power (W)'),
                sortable: true,
                width: 100,
            },{
                id: 'inputWhTimer',
                dataIndex: 'inputWhTimer',
                header: _t('Since from Date'),
                sortable: true,
                width: 120,
            },{
                id: 'inputWh',
                flex: 1,
                dataIndex: 'inputWh',
                header: _t('Watt-hour (kWh)'),
                width: 100,
                renderer: function(x){ return (x/1000);}
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.EatonPduPowerPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('EatonPduPowerPanel', ZC.EatonPduPowerPanel);
ZC.registerName('EatonPduPower', _t('ePDU Input Power'), _t('ePDU Input Powers'));


ZC.EatonPduVoltagePanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'EatonPduVoltage',
            alias:['widget.EatonPduVoltagePanel'],
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'inputVoltage'},
                {name: 'inputVoltageThStatus'},
                {name: 'inputVoltageThStatusText'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Type'),
                width: 100
            },{
                id: 'inputVoltage',
                dataIndex: 'inputVoltage',
                header: _t('Voltage (V)'),
                sortable: true,
                width: 120,
                renderer: function(x){ return (x/1000);}
            },{
                id: 'inputVoltageThStatusText',
                flex: 1,
                dataIndex: 'inputVoltageThStatusText',
                header: _t('Voltage Status'),
                sortable: true,
                width: 120,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.EatonPduVoltagePanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('EatonPduVoltagePanel', ZC.EatonPduVoltagePanel);
ZC.registerName('EatonPduVoltage', _t('ePDU Input Voltage'), _t('ePDU Input Voltages'));

ZC.EatonPduCurrentPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'EatonPduCurrent',
            alias:['widget.EatonPduCurrentPanel'],
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'inputCurrent'},
                {name: 'inputCurrentThStatus'},
                {name: 'inputCurrentThStatusText'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Type'),
                width: 100
            },{
                id: 'inputCurrent',
                dataIndex: 'inputCurrent',
                header: _t('Current (A)'),
                sortable: true,
                width: 120,
                renderer: function(x){ return (x/1000);}
            },{
                id: 'inputCurrentThStatusText',
                flex: 1,
                dataIndex: 'inputCurrentThStatusText',
                header: _t('Current Status'),
                sortable: true,
                width: 120,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.EatonPduCurrentPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('EatonPduCurrentPanel', ZC.EatonPduCurrentPanel);
ZC.registerName('EatonPduCurrent', _t('ePDU Input Current'), _t('ePDU Input Currents'));


})();
