from deep_learning.bl.models.layers.AbstractLayer import AbstractLayer


class InputLayerImpl(AbstractLayer):

    def __init__(self):
        super().__init__()

    @staticmethod
    def get_layer(args):
        return None
