import pandas as pd
import spacy


def qwhat(doc):
    a = iter(doc)
    prev = None
    for t in a:
        if t.lower_ in ['what'] and t.dep_ in ['attr', 'nsubj', 'dobj', 'pobj', 'det', 'dep', 'nsubjpass', 'dative']:
            token = next(a, None)
            if token is None or token.tag_ in ['VBZ', 'VBD', 'VBP', 'MD', 'NN', 'NNS', 'CD', 'IN']:
                if prev is None or prev.tag_ not in ['VBZ', 'VB']:
                    print(doc)
        elif t.lower_ in ['what'] and t.dep_ in ['conj', 'ROOT', 'appos']:
            print(doc)
        prev = t


def qwhere(doc):
    a = iter(doc)
    prev = None
    for t in a:
        if t.lower_ in ['where'] and t.dep_ in ['pcomp', 'advmod']:
            token = next(a, None)
            if token is None or token.tag_ in ['VBP', 'VBD', 'VBZ', 'MD', 'IN', 'TO'] or (prev is None or prev.tag_ in ['IN']):
                    if prev is None or prev.tag_ not in ['NN']:
                        print(doc)
        prev = t


def qwho(doc):
    a = iter(doc)
    prev = None
    for t in a:
        if t.lower_ in ['who'] and t.dep_ in ['nsubj', 'pobj', 'dep']:
            token = next(a, None)
            if token is not None and token.tag_ in ['VBZ', 'VBD', 'VBP', 'MD', 'NN', 'NNP', 'NNS', 'CD', 'IN']:
                if prev is None or prev.tag_ not in ['NN', 'NNP', 'NNS', 'WDT', 'VBZ', 'VB', 'PRP', 'JJR']:
                    print(doc)
        prev = t


def qwhen(doc):
    a = iter(doc)
    prev = None
    for t in a:
        if t.lower_ in ['when'] and t.dep_ in ['advmod']:
            token = next(a, None)
            if token is not None and token.tag_ in ['VBZ', 'VBD', 'VBP', 'MD', 'NN', 'NNP', 'NNS', 'CD', 'IN']:
                if prev is None or prev.tag_ not in ['NN', 'NNP', 'NNS', 'WDT', 'VBZ', 'VB', 'PRP', 'JJR']:
                    print(doc)
        prev = t


def qwhy(doc):
    a = iter(doc)
    prev = None
    for t in a:
        if t.lower_ in ['why'] and t.dep_ in ['advmod']:
            token = next(a, None)
            if token is not None and token.tag_ in ['VBZ', 'VBD', 'VBP', 'MD', 'NN', 'NNP', 'NNS', 'CD', 'IN']:
                if prev is None or prev.tag_ not in ['NN', 'NNP', 'NNS', 'WDT', 'VBZ', 'VB', 'PRP', 'JJR']:
                    print(doc)
        prev = t


def qhow(doc):
    a = iter(doc)
    prev = None
    for t in a:
        if t.lower_ in ['how'] and t.dep_ in ['advmod']:
            token = next(a, None)
            if token is not None and token.tag_ in ['VBZ', 'JJ', 'RB', 'TO', 'VBD', 'VBP', 'VBN', 'MD', 'NN', 'NNP', 'NNS', 'CD', 'IN']:
                if prev is None or prev.tag_ not in ['NN', 'NNP', 'NNS', 'WDT', 'VBZ', 'VB', 'VBP', 'PRP', 'JJR']:
                    print(doc, [(d.lower_, d.tag_, d.dep_) for d in doc])
        prev = t


def has_words(doc):
    a = iter(doc)
    prev = None
    for t in a:
        if t.lower_ in ['what', 'when', 'where', 'who', 'why', 'how'] and \
                t.dep_ in ['advmod', 'attr', 'nsubj', 'dobj', 'pobj', 'det', 'dep', 'nsubjpass', 'dative', 'pcomp', 'nsubj', 'pobj', 'dep']:
            token = next(a, None)
            if token is not None and token.tag_ in ['VBZ', 'JJ', 'RB', 'TO', 'VBD', 'VBP', 'VBN', 'MD', 'NN', 'NNP', 'NNS', 'CD', 'IN'] or \
                    (prev is None or prev.tag_ in ['IN']):
                if prev is None or prev.tag_ not in ['NN', 'NNP', 'NNS', 'WDT', 'VBZ', 'VB', 'VBP', 'PRP', 'JJR']:
                    print(doc)
            elif t.lower_ in ['what'] and t.dep_ in ['conj', 'ROOT', 'appos']:
                print(doc)
        prev = t


def check_others(doc):
    a = iter(doc)
    prev = None
    for t in a:
        if t.lower_ in ['how']:
            token = next(a, None)
            if token is not None:
                print((t.tag_, t.dep_), (token.lower_, token.tag_, token.dep_), doc)
            #print(doc, [(d.lower_, d.tag_, d.dep_) for d in doc])
        prev = t


df = pd.read_csv('FeatureEngineeringService.csv', sep=',', encoding='utf-8')

nlp = spacy.load('en_core_web_sm')

df['PlainTextDataImpl'].apply(lambda x: has_words(nlp(str(x))))
