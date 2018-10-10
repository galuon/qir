import xml.etree.ElementTree as ET
from nltk.corpus import stopwords
import string
from nltk.stem import PorterStemmer
import glob
import os


def one_doc_preprocess(ar): #This is dataset-specific code. I think that you should name this method as "cacm_doc_preprocess"
    tree = ET.parse(ar)
    root = tree.getroot()
    stop_words = set(stopwords.words('english'))
    translator = str.maketrans('', '', string.punctuation)
    ps = PorterStemmer()
    a = [elem.tag for elem in root.iter()] #for what reasons you created a-variable and didn't use it?
    for docid in root.iter("DOCID"): #Do I understand correctly that one XML is containing only one document (one DOCID, title, body) ?
        name = docid.text.replace(" ", "") #what if document doesn't contain name, title or other fields? I think that you should prevent strange errors with format checking 
                                           # like if name == None then exit with message "document has invalid format"
    dest = "preprocessed_files"
    if not os.path.exists(dest):
        os.mkdir(dest)
    for title in root.iter("TITLE"):
        s = title.text.lower().replace("-", ' ').translate(translator).split() #see comment above
    s = [w for w in s if w not in stop_words] #using of list generator is not a good idea, if document will have big size then this code may fail with out of memory
                                              # you can rewrite it to for-loop with if statement in body like:
                                              # for word in s:
                                              #     if word not in stop_words:
                                              #         ...
    for w in s:
        print(ps.stem(w), file=open(dest + '/' + name, "a")) #unfortunately I haven't cacm-dataset in such format and I cannot see output of script
                                                             #but what about spaces between words? ps.stem(w) serialization gives word with spaces?


if __name__ == '__main__': #I think that this script should accept two parameters - directory of dataset and format of dataset and it define coverter method by format name 
                           # My main point is that this tool will be used as preprocessor for each useful dataset and producing data in uniform format
    list_of_names = glob.glob('cacm.ml/*.xml')
    for i in list_of_names:
        one_doc_preprocess(i)
