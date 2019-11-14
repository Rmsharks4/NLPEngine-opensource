from deep_learning.bl.kpis.AbstractKPI import AbstractKPI
from deep_learning.bl.kpis.AppropriateToneKPIImpl import AppropriateToneKPIImpl

from data.bl.ConversationIDDataImpl import ConversationIDDataImpl
from data.bl.StartTimeDataImpl import StartTimeDataImpl
from data.bl.EndTimeDataImpl import EndTimeDataImpl
from data.bl.SpeakerDataImpl import SpeakerDataImpl

from feature_engineering.bl.NGramsDialogueFeatureEngineerImpl import NGramsDialogueFeatureEngineerImpl
from feature_engineering.bl.acts.QWhDialogueActImpl import QWhDialogueActImpl
from feature_engineering.bl.acts.QYnDialogueActImpl import QYnDialogueActImpl
from feature_engineering.bl.steps.BackwardStepsDialogueFeatureEngineerImpl import BackwardStepsDialogueFeatureEngineerImpl
from feature_engineering.bl.steps.ForwardStepsDialogueFeatureEngineerImpl import ForwardStepsDialogueFeatureEngineerImpl

from deep_learning.bl.models.CNNDeepLearningModelImpl import CNNDeepLearningModelImpl

from deep_learning.bl.models.layers.RecurrentLayerImpl import RecurrentLayerImpl
from deep_learning.bl.models.layers.DenseLayerImpl import DenseLayerImpl
from deep_learning.bl.models.layers.ActivationLayerImpl import ActivationLayerImpl
from deep_learning.bl.models.layers.ConvolutionLayerImpl import ConvolutionLayerImpl
from deep_learning.bl.models.layers.DropoutLayerImpl import DropoutLayerImpl
from deep_learning.bl.models.layers.EmbeddingLayerImpl import EmbeddingLayerImpl
from deep_learning.bl.models.layers.InputLayerImpl import InputLayerImpl
from deep_learning.bl.models.layers.OutputLayerImpl import OutputLayerImpl
from deep_learning.bl.models.layers.PoolingLayerImpl import PoolingLayerImpl
from deep_learning.bl.models.layers.AttentionLayerImpl import AttentionLayerImpl
from deep_learning.bl.models.layers.ConcatenateLayerImpl import ConcatenateLayerImpl
from deep_learning.bl.models.layers.TimeDistributedLayerImpl import TimeDistributionLayerImpl


class ActiveListeningKPIImpl(AbstractKPI):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = [[AppropriateToneKPIImpl.__name__]]
        self.config_pattern.properties.req_input = [[ConversationIDDataImpl.__name__,
                                                     SpeakerDataImpl.__name__,
                                                     StartTimeDataImpl.__name__,
                                                     EndTimeDataImpl.__name__,
                                                     NGramsDialogueFeatureEngineerImpl.__name__,
                                                     BackwardStepsDialogueFeatureEngineerImpl.__name__,
                                                     ForwardStepsDialogueFeatureEngineerImpl.__name__,
                                                     QWhDialogueActImpl.__name__,
                                                     QYnDialogueActImpl.__name__]]
        self.config_pattern.properties.req_args = [[]]
        self.cls_model = CNNDeepLearningModelImpl()

    def create_model(self, args):

        self.cls_model.layers = list()
        self.cls_model.layers.append(InputLayerImpl.get_layer(args))

        self.cls_model.layers.append(InputLayerImpl.get_layer(args))
        self.cls_model.layers.append(EmbeddingLayerImpl.get_layer(args))
        self.cls_model.layers.append(ConvolutionLayerImpl.get_layer(args))
        self.cls_model.layers.append(DenseLayerImpl.get_layer(args))

        self.cls_model.layers.append(InputLayerImpl.get_layer(args))
        self.cls_model.layers.append(EmbeddingLayerImpl.get_layer(args))
        self.cls_model.layers.append(ConvolutionLayerImpl.get_layer(args))
        self.cls_model.layers.append(DenseLayerImpl.get_layer(args))

        self.cls_model.layers.append(AttentionLayerImpl.get_layer(args))
        self.cls_model.layers.append(ConcatenateLayerImpl.get_layer(args))
        self.cls_model.layers.append(TimeDistributionLayerImpl.get_layer(args))
        self.cls_model.layers.append(DenseLayerImpl.get_layer(args))

        self.cls_model.layers.append(InputLayerImpl.get_layer(args))
        self.cls_model.layers.append(RecurrentLayerImpl.get_layer(args))
        self.cls_model.layers.append(DropoutLayerImpl.get_layer(args))

        self.cls_model.layers.append(PoolingLayerImpl.get_layer(args))
        self.cls_model.layers.append(DenseLayerImpl.get_layer(args))

        self.cls_model.layers.append(InputLayerImpl.get_layer(args))
        self.cls_model.layers.append(ConvolutionLayerImpl.get_layer(args))
        self.cls_model.layers.append(DropoutLayerImpl.get_layer(args))
        self.cls_model.layers.append(ActivationLayerImpl.get_layer(args))

        self.cls_model.layers.append(OutputLayerImpl.get_layer(args))

        self.cls_model.compile(args)

        return self.cls_model

    def run_model(self, args):
        self.cls_model.train(args)
        self.cls_model.test(args)
        self.cls_model.evaluate(args)

    def use_model(self, args):
        return self.cls_model.predict(args)
