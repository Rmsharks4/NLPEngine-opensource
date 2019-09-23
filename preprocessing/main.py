
from preprocessing.bl.ExpandContractionsDialoguePreProcessorImpl import ExpandContractionsDialoguePreProcessorImpl
from commons.config.AbstractConfig import AbstractConfig
from commons.config.AbstractConfigParser import AbstractConfigParser

var = ExpandContractionsDialoguePreProcessorImpl()
var.parse({
    AbstractConfigParser.__class__.__name__: ExpandContractionsDialoguePreProcessorImpl.__class__.__name__.join('.csv'),
    AbstractConfig.__class__.__name__: [{
        'data': var.config_pattern.properties.req_data,
        'args': var.config_pattern.properties.req_args
    }]
})
