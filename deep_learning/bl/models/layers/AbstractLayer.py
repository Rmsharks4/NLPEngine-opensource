from commons.config.StandardConfigParserImpl import StandardConfigParserImpl


class AbstractLayer(StandardConfigParserImpl):

    def __init__(self):
        super().__init__()

    @staticmethod
    def get_layer(args):
        pass
