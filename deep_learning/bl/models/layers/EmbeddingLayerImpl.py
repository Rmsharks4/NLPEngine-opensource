from deep_learning.bl.models.layers import AbstractLayer


class EmbeddingLayerImpl(AbstractLayer):

    def __init__(self):
        super().__init__()

    @staticmethod
    def get_layer(args):
        return None