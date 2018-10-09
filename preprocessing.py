import xml.etree.ElementTree as ET
from nltk.corpus import stopwords
import string
from nltk.stem import PorterStemmer
import glob
import os


def one_doc_preprocess(ar):
    tree = ET.parse(ar)
    root = tree.getroot()
    stop_words = set(stopwords.words('english'))
    translator = str.maketrans('', '', string.punctuation)
    ps = PorterStemmer()
    a = [elem.tag for elem in root.iter()]
    for docid in root.iter("DOCID"):
        name = docid.text.replace(" ", "")
    dest = "preprocessed_files"
    if not os.path.exists(dest):
        os.mkdir(dest)
    for title in root.iter("TITLE"):
        s = title.text.lower().replace("-", ' ').translate(translator).split()
    s = [w for w in s if w not in stop_words]
    for w in s:
        print(ps.stem(w), file=open(dest + '/' + name, "a"))


if __name__ == '__main__':
    list_of_names = glob.glob('cacm.ml/*.xml')
    for i in list_of_names:
        one_doc_preprocess(i)
