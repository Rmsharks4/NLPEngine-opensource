from deep_learning.bl.models.layers import AbstractLayer


class DenseLayerImpl(AbstractLayer):

    def __init__(self):
        super().__init__()

    @staticmethod
    def get_layer(args):
        return None