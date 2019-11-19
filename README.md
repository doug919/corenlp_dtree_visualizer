# Convert Stanford CoreNLP's Dependency Tree to Spacy's for Visualization
This module provides a format converter from Stanford CoreNLP's dependency trees to Spacy's such that the visualation can be done using Spacy's visualizer.

# Motivation
I just found that Spacy has an amazing visualizer that we should explore more and this project bridges the gap between the CoreNLP parsing outputs and it.

# Pre-requisite
Install Spacy and stanfordnlp. The versions we have tested are Spacy 2.2.2 and stanfordnlp 0.2.0
```
pip install spacy stanfordnlp
```

Download Stanford CoreNLP (tested on 3.9.2) Java library: https://stanfordnlp.github.io/CoreNLP/

Set the env variable for stanfordnlp:
```
export CORENLP_HOME=/yourhome/stanford-corenlp-full-2018-10-05
```

# Installation
```
pip install corenlp-vdep
```


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


![svg](./example.svg)
