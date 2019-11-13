from vectorization.bl.StandardFlowVectorizerHandlerImpl import StandardFlowVectorizerHandlerImpl


class AbstractVectorizerHandlerFactory:

    def __init__(self):
        pass

    @staticmethod
    def get_vectorizer_handler(handler_type):
        switcher = {
            StandardFlowVectorizerHandlerImpl.__name__: StandardFlowVectorizerHandlerImpl()
        }
        return switcher.get(handler_type, None)
