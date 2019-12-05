import json

with open('input.json') as f:
    data = json.load(f)
    for entry in data['results']:
        for alt in entry['alternatives']:
            print('transcript', alt['transcript'])
            for word in alt['timestamps']:
                print('word', word[0])
                print('start', word[1])
                print('end', word[2])
    for entry in data['speaker_labels']:
        print('start', entry['from'])
        print('end', entry['to'])
        print('speaker', entry['speaker'])


# QUESTIONS: HOW DO I READ IN THIS DATA?
# MAKE OUR DAO DEPENDANT ON JSON? AND THEN CONVERT IT INTO PANDAS DATAFRAME?
# MAKE A DATAFRAME CONSTRUCTION CLASS IN PREPROCESSING?

# MERGE ON SPEAKER LABELS
# WHEN SPEAKER LABEL CHANGES, NEW DIALOGUE

# MERGE ON HOLD TIME
# WHEN HOLD TIME EXCEEDS THRESHOLD: 3 SECONDS, NEW DIALOGUE

# THEN REMOVE NULLS - EMPTY STRINGS
# AND LIMIT SPEAKERS - LABEL SPEAKERS IN THIS STAGE
# DEFINE SCENARIOS - WHEN TO LIMIT A SPEAKER AND WHERE

# SPEAKER PRE-PROCESSING
# LABEL CSR AND CALLER

# LABEL START TIME
# LABEL END TIME

# CLEAN NUMBERS, DATES, EMAILS, LOCATIONS, LEMMAS AND STOP WORDS
# THEN SEND FORWARD

