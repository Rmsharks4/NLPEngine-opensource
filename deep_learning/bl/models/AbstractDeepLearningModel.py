from commons.config.StandardConfigParserImpl import StandardConfigParserImpl


class AbstractDeepLearningModel(StandardConfigParserImpl):

    def __init__(self):
        super().__init__()
        self.cls_layers = None

    @property
    def layers(self):
        return self.cls_layers

    @layers.setter
    def layers(self, args):
        self.cls_layers = args

    def train(self, args):
        pass

    def test(self, args):
        pass

    def predict(self, args):
        pass

    def add(self, args):
        pass

    def drop(self, args):
        pass

    def compile(self, args):
        pass

    def evaluate(self, args):
        pass