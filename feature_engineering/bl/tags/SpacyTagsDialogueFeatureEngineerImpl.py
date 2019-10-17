from feature_engineering.bl.tags.AbstractTagsDialogueFeatureEngineerImpl import AbstractTagsDialogueFeatureEngineerImpl
import spacy
import neuralcoref


class SpacyTagsDialogueFeatureEngineerImpl(AbstractTagsDialogueFeatureEngineerImpl):

    def tags(self, args):
        nlp = spacy.load('en_core_web_sm')
        neuralcoref.add_to_pipe(nlp)

        doc = nlp(args)

        return {'Sentences': [sent for sent in doc.sents],
                'Noun Chunks': [chunk for chunk in doc.noun_chunks],
                'Co-reference': [coref for coref in doc._.coref_clusters],
                'Tokens': ({
                    'Word': token.text,
                    'Lemma': token.lemma_,
                    'Punct': token.is_alpha,
                    'Stop': token.is_stop,
                    'POS': token.pos_,
                    'Tags': token.tag_,
                    'Type': token.ent_type_,
                    'Dep': token.dep_,
                    'Shape': token.shape_,
                    'IOB': token.ent_iob_} for token in doc.text)}
