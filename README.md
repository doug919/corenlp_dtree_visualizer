# visualize_dependency_tree
Visualize dependency trees for Stanford CoreNLP outputs with Spacy

# Motivation
I just found that Spacy has an amazing visualizer that we should explore more and this project bridges the gap between the CoreNLP parsing output and it.

# Examples
```python
import spacy
from spacy import displacy
from stanfordnlp.server import CoreNLPClient

from corenlp_dtree_visualizer.converters import _corenlp_dep_tree_to_spacy_dep_tree


# Input text
text = 'Jim killed John with a joke.'

# Get a dependency tree from a Stanford CoreNLP pipeline
with CoreNLPClient(annotators=['tokenize','ssplit','pos','lemma','ner','parse','depparse'],
        timeout=60000, memory='8G', output_format='json') as client:
    # submit the request to the server
    ann = client.annotate(text)

# Convert dependency tree formats
sent = ann['sentences'][0]
tree = _corenlp_dep_tree_to_spacy_dep_tree(sent['tokens'], sent['enhancedPlusPlusDependencies'])

# Visualize with Spacy
nlp = spacy.load("en_core_web_sm")
displacy.render(tree, style="dep", manual=True)

# could also save to a file
# svg = displacy.render(tree, style="dep", manual=True)
# with open('tmp.svg', 'w', encoding='utf-8') as fw:
    # fw.write(svg)
```


![Alt text](./example.svg)
<img src="./example.svg">
