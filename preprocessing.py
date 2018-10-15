import xml.etree.ElementTree as ET
from nltk.corpus import stopwords
import string
from nltk.stem import PorterStemmer
import glob
import os


def one_doc_preprocess(ar, list_of_arguments): 
    tree = ET.parse(ar)
    root = tree.getroot()
    stop_words = set(stopwords.words('english'))
    translator = str.maketrans('', '', string.punctuation)
    ps = PorterStemmer()
    for docid in root.iter("DOCID"): #Do I understand correctly that one XML is containing only one document (one DOCID, title, body) ? Yes
        name = docid.text.replace(" ", "")
        if docid == None:
            raise ValueError("document has invalid format")
    dest = "preprocessed_files"
    if not os.path.exists(dest):
        os.mkdir(dest)
    for argument in list_of_arguments:
        s = []
        for current_field in root.iter(argument):
            s = current_field.text.lower().replace("-", ' ').translate(translator).split() #see comment above
            if current_field == None:
                raise ValueError("document has invalid format")
        s1 = []
        for word in s:
            if word not in stop_words:
                s1.append(word)
        for w in s1:
            print(ps.stem(w), file=open(dest + '/' + name, "a"))


if __name__ == '__main__': #I think that this script should accept two parameters - directory of dataset and format of dataset and it define coverter method by format name 
                           # My main point is that this tool will be used as preprocessor for each useful dataset and producing data in uniform format
    list_of_names = glob.glob('cacm.ml/*.xml')
    list_of_fields = ["TITLE"]
    for i in list_of_names:
        one_doc_preprocess(i, list_of_fields)
