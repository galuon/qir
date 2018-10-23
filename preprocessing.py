import xml.etree.ElementTree as ET
from nltk.corpus import stopwords
import string
from nltk.stem import PorterStemmer
import glob
import os
import sys


def one_doc_preprocess(ar, list_of_arguments):
    tree = ET.parse(ar)
    root = tree.getroot()
    stop_words = set(stopwords.words('english'))
    translator = str.maketrans('', '', string.punctuation)
    ps = PorterStemmer()
    for docid in root.iter("DOCID"):
        if docid is None:
            raise ValueError("document has invalid format")
        name = docid.text.replace(" ", "")

    dest = "preprocessed_files"
    if not os.path.exists(dest):
        os.mkdir(dest)
    for argument in list_of_arguments:
        s = []
        for current_field in root.iter(argument):
            if current_field is None:
                raise ValueError("document has invalid format")
            s = current_field.text.lower().replace("-", ' ')\
                .translate(translator).split()
        with open(dest + '/' + name, "a") as output_file:
            for word in s:
                if word not in stop_words:
                    print(ps.stem(word), file=output_file)


if __name__ == '__main__':
    path = 'cacm.ml/*.xml'
    # path = sys.argv[1]
    # is above a good way of reading path?
    list_of_names = glob.glob(path)
    list_of_fields = ["TITLE"]
    for i in list_of_names:
        one_doc_preprocess(i, list_of_fields)
