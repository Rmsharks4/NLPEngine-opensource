
import xml.etree.ElementTree as ET
import pandas as pd
import json
from collections import OrderedDict

tree = ET.parse('../data/spaadia_data.xml')
xml_data = tree.getroot()
xml_str = ET.tostring(xml_data, encoding='utf8', method='xml')


class Dialogue:

    id = None
    turns = []

    def __init__(self, id):
        self.id = id

    def add_turns(self, turn):
        self.turns.append(turn)

    class Turn:

        n = None
        speaker = None
        talks = []

        def __init__(self, speaker, n):
            self.n = n
            self.speaker = speaker

        def add_talks(self, talk):
            self.talks.append(talk)

        class Talk:

            n = None
            name = None
            sp_act = None
            text = None
            polarity = None
            topic = None
            mode = None
            acts = []

            def __init__(self, n, name, sp_act, text):
                self.n = n
                self.name = name
                self.sp_act = sp_act
                self.text = text

            def add_acts(self, act):
                self.acts.append(act)

            class Act:

                name = None
                act_dict = dict()

                def __init__(self, name):
                    self.name = name


def iterate_xml(data):
    rows = []
    dialogues = []
    for child in data:
        dialogue = Dialogue(child.attrib['id'])
        if len(child) == 0:
            rows.append({
                'DialogueID': dialogue.id,
                'Turn-N': None,
                'Speaker': None,
                'Talk': None,
                'Talk-N': None,
                'Sp-Act': None,
                'Text': None,
                'Mode': None,
                'Topic': None,
                'Polarity': None,
                'Act': None,
                'Key': None,
                'Value': None
            })
        for gchild in child:
            turn = Dialogue.Turn(gchild.attrib['speaker'], gchild.attrib['n'])
            if len(gchild) == 0:
                rows.append({
                    'DialogueID': dialogue.id,
                    'Turn-N': turn.n,
                    'Speaker': turn.speaker,
                    'Talk': None,
                    'Talk-N': None,
                    'Sp-Act': None,
                    'Text': None,
                    'Mode': None,
                    'Topic': None,
                    'Polarity': None,
                    'Act': None,
                    'Key': None,
                    'Value': None
                })
            for ggchild in gchild:
                talk = Dialogue.Turn.Talk(ggchild.attrib['n'], ggchild.tag, ggchild.attrib['sp-act'], ggchild.text)
                if 'mode' in ggchild.attrib:
                    talk.mode = ggchild.attrib['mode']
                if 'topic' in ggchild.attrib:
                    talk.topic = ggchild.attrib['topic']
                if 'polarity' in ggchild.attrib:
                    talk.polarity = ggchild.attrib['polarity']
                if len(ggchild) == 0:
                    rows.append({
                            'DialogueID': dialogue.id,
                            'Turn-N': turn.n,
                            'Speaker': turn.speaker,
                            'Talk': talk.name,
                            'Talk-N': talk.n,
                            'Sp-Act': talk.sp_act,
                            'Text': talk.text,
                            'Mode': talk.mode,
                            'Topic': talk.topic,
                            'Polarity': talk.polarity,
                            'Act': None,
                            'Key': None,
                            'Value': None
                        })
                for gggchild in ggchild:
                    act = Dialogue.Turn.Talk.Act(gggchild.tag)
                    if len(gggchild.attrib.items()) == 0:
                        rows.append({
                                'DialogueID': dialogue.id,
                                'Turn-N': turn.n,
                                'Speaker': turn.speaker,
                                'Talk': talk.name,
                                'Talk-N': talk.n,
                                'Sp-Act': talk.sp_act,
                                'Text': talk.text,
                                'Mode': talk.mode,
                                'Topic': talk.topic,
                                'Polarity': talk.polarity,
                                'Act': act.name,
                                'Key': None,
                                'Value': None
                            })
                    for key, value in gggchild.attrib.items():
                        act.act_dict[key] = value
                        rows.append({
                                'DialogueID': dialogue.id,
                                'Turn-N': turn.n,
                                'Speaker': turn.speaker,
                                'Talk': talk.name,
                                'Talk-N': talk.n,
                                'Sp-Act': talk.sp_act,
                                'Text': talk.text,
                                'Mode': talk.mode,
                                'Topic': talk.topic,
                                'Polarity': talk.polarity,
                                'Act': act.name,
                                'Key': key,
                                'Value': value
                            })
                    talk.add_acts(act)
                turn.add_talks(talk)
            dialogue.add_turns(turn)
        dialogues.append(dialogue)
    df = pd.DataFrame(rows, columns=['DialogueID', 'Turn-N', 'Speaker', 'Talk', 'Talk-N', 'Sp-Act', 'Text', 'Mode', 'Topic', 'Polarity',
                                     'Act', 'Key', 'Value'])
    df.to_csv('data.csv')
    return dialogues


dialogues = iterate_xml(xml_data)

