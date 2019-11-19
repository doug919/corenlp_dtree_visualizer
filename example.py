
import spacy
from spacy import displacy


# Input text
text = 'Jim killed John with a joke.'

# Get a dependency tree from a Stanford CoreNLP pipeline
with CoreNLPClient(annotators=['tokenize','ssplit','pos','lemma','ner','parse','depparse'],
        timeout=60000, memory='8G', output_format='json') as client:
    # submit the request to the server
    ann = client.annotate(text)


# Convert dependency tree formats
tree = _corenlp_dep_tree_to_spacy_dep_tree(sent['tokens'], sent['enhancedPlusPlusDependencies'])

# Visualize with Spacy
nlp = spacy.load("en_core_web_sm")
displacy.serve(tree, style="dep", manual=True)
