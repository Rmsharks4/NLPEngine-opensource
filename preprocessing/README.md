## Pre-Processing README
### Code Structure
This is a README file for NLP PreProcessing - the first hook for Call Transcripts Analytics.
Let's look at the code structure - first and foremost:
- **bl** (Business Logic)
- **dao** (Data Access Object)
- **driver** (Service that runs the Pre-Processing routine)
- **exceptions** (Exception Classes associated with Pre-Processing)
- **resources** (Configuration Files)
- **utils** (Static Utilities required for Pre-Processing)

Now lets look at files inside each of these folders:
#### Business Logic (BL)
This contains the OOP logic for NLP Pre-processing. The following classes are present in this folder:
- **Dialogue PreProcessor**
    - **Abstract Class**: that operates on one major function:
        - **preprocess** (operation and validation included!)
    - **Abstract Class Implementations**: different versions of Abstract Class that preprocess in different ways
        - **Expand Contractions**: expands contractions in text (I'm to I am, etc.)
        - **Lowercase**: turns all characters to lowercase (CHAR to char, etc.)
        - **Porter Stemmer**: stems words to their origin stems (grows to grow, etc.)
        - **Remove Emails**: removes sensitive email info (abc@ab.com to EMAIL, etc.)
        - **Remove Numeric Characters**: remove all digits and alike (14, fourteen, sunday, etc.)
        - **Remove Punctuation**: remove all punctuation from text (a,b,c to a b c)
        - **Remove Stop Words**: remove all frequently occurring words (the, by, etc.)
        - **Spell Checker**: corrects spellings of words (cactos to cactus, etc.)
        - **Split Joint Words**: splits combination words into two (well-managed to well managed, etc.)
        - **Word Net Lemmatizer**: lemmatizes words to their roots (grew to grow, etc.)
    - **Abstract Factory**: selects which implementation should be used at a given time:
        - **get_dialogue_preprocessor** (pass in class name as argument)
    - **Abstract Handler**: selects in what flow the classes should be created and called:
        - **perform_preprocessing** (pass in configurations and data elements)  
    - **Abstract Handler Implementations**: different versions of Abstract Handler that preprocess text.
        - **Standard Flow**: It follows the following flow of pre-processing (as visible in configurations)
            - Lowercase
            - Split Joint Words
            - Contractions
            - Numbers
            - Email
            - Punctuation
            - Spell Check
            - Stop Words
            - Lemmatize
    - **Abstract Handler Factory**: selects which implementation should be used at a given time:
        - **get_dialogue_preprocessor_handler** (pass in class name as argument)

This business logic has the flexibility to add any number of implementations of a dialogue preprocessor, as well as create new types of pre-processors such as a dialogue_batch_preprocessor, etc.

#### Data Access Object (DAO)
This contains the file read and write logic for preprocessing files. The following classes are present here:
- **Config Parser Implementation**: Reads and writes config files specifically fitting for pre-processing
    - An implementation of **Abstract Config Parser** in NLP.Commons
    - Implements the following main function: **parse** (read config pattern, write in config file path)
- **Spark Data Access Object Implementation**: Reads and writes .csv files using spark dataframes for pre-processing
    - An implementation of **Abstract DAO** in NLP.Commons
    - Implements the following main functions: **load**, **create**, **save** and **query**.

This DAO Implementation helps us keep the DAO similar to the whole project as well as specific for pre-processing as well.

#### Driver
This contains one main function to run the whole routine. The following class implements it:
- **PreProcessing Service**: contains a 'run' function that runs the whole routine - starting from DAO to BL to DAO again.
    - An implementation of **Abstract Service** in NLP.commons
    - Implements the following main function: **run**

This service implementation is also universally constant, as well as unique enough to handle some pre-processing quirks.

#### Exceptions

#### Resources
This contains config files for all the files inside our business logic - and store the following information inside:
- **Class Name**
- **Class ID**
- **Class Variables**
- **Class Methods** (static, abstract and implemented)
- **Class Properties** (Required Data, Parent Classes, Child Classes, Pre-requisite Classes and Utilities)

This method of storing configurations (.ini) helps us in easy dynamic implementations of configs - instead of static ones and is also universal from NLP.commons.config.

#### Utils
This folder contains static utilities required by Business Logic files for pre-processing. The following classes are present:
- **Utils**
    - **Abstract Class**: this class operates on one static function
        - **load** (loads the static object required for preprocesing)
    - **Abstract Class Implementation**: different versions of Abstract Utils Class
        - **Contractions Dictionary**: reads a contractions dict and regex from file
        - **Emails Dictionary**: reads email regex from file
        - **Figures Dictionary**: reads numbers, digits and days from file
        - **Porter Stemmer**: downloads stemmer from nltk
        - **Punctuation Dictionary**: downloads punctuation dict from nltk
        - **Spell Checker**: downloads spell checker from Spell Checker lib
        - **Splits Dictionary**: reads splits regex from file
        - **Stop Words Dictionary**: downloads stop words from nltk
        - **Word Net Lemmatizer**: downloads lemmatizer from nltk
    - **Abstract Factory**: Selects which file implementation should be used at any given time
        - **get_utils** (takes class name as argument)
- **PreProcessing Logger**
    - Logger implementation for pre-processing logs.

This utility feature helps the whole project stay intact, overcomes overhead costs for re-loading old libraries and is a more efficient way of story constants at run-time.

### Authors

- **Ramsha Siddiqui** - *rsiddiqui@i2cinc.com*

### Acknowledgments

- **Alishan Rao** - *arao@i2cinc.com*
- **Maha Yaqub** - *myaqub@i2cinc.com* 
