def _corenlp_dep_tree_to_spacy_dep_tree(tokens, dep_tree, attach_root=True):
    '''convert a dependency tree from Stanford Corenlp's JSON output format
        to Spacy's visualizer format
    params:
    '''
    words = [{'text': t['word'], 'tag': t['pos']} for t in sent['tokens']]
    if attach_root:
        words = [{'text': '[ROOT]', 'tag': 'ROOT'}] + words

        arcs = []
        for dep in sent['enhancedPlusPlusDependencies']:
            if attach_root:
                arc = {'start': dep['governor'], 'end': dep['dependent'], 'label': dep['dep'],
                        'dir': 'left' if dep['governor'] > dep['dependent'] else 'right'}
            else:
                if dep['governor'] != 0:
                    arc = {'start': dep['governor']-1, 'end': dep['dependent']-1, 'label': dep['dep'],
                            'dir': 'left' if dep['governor'] > dep['dependent'] else 'right'}
                    arcs.append(arc)
    tree = {'words': words, 'arcs': arcs}
    return tree
