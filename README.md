# transphone

`transphone` is a grapheme-to-phoneme conversion toolkit. It provides approximation G2P model for 8000 languages.

This repo contains our code and pretrained models roughly following our paper accepted at `Findings of ACL 2022`

`Zero-shot Learning for Grapheme to Phoneme Conversion with Language Ensemble`

It is a multilingual G2P (grapheme-to-phoneme) model that can be applied to all 8k languages registered in the [Glottolog database](https://glottolog.org/glottolog/language). You can read our papers at [Open Review](https://openreview.net/pdf?id=dKTTArRu8G2)

Our approach:
- We first trained our supervised multilingual model with ~900 languages using lexicons from [Wikitionary](https://en.wiktionary.org/wiki/Wiktionary:Main_Page)
- if the target language (any language from the 8k languages) does not have any training set, we approximate its g2p model by using similar lanuguages from the supervised language sets and ensemble their inference results to obtain the target g2p.


## Install

Transphone is available from pip

```bash
pip install transphone
```
You can also clone this repository and install

```bash
python setup.py install
```

## Usage

A simple python usage is as follows:

```python
In [1]: from transphone.g2p import read_g2p                                                                                                     

# read a pretrained model. It will download the pretrained model automatically into repo_root/data/model
In [2]: model = read_g2p()                                                                                                                      

# to infer pronunciation for a word with ISO 639-3 id
# For any pretrained languages (~900 languages), it will use the pretrained model without approximation
In [3]: model.inference('transphone', 'eng')                                                                                                    
Out[3]: ['t', 'ɹ', 'æ', 'n', 's', 'f', 'ə', 'ʊ', 'n']

# If the specified language is not available, then it will approximate it using nearest languages
# in this case, aaa (Ghotuo language) is not one of the training languages, we fetch 10 nearest languages to approximate it 
In [4]: model.inference('transphone', 'aaa')                                                                                                    
lang  aaa  is not available directly, use  ['bin', 'bja', 'bkh', 'bvx', 'dua', 'eto', 'gwe', 'ibo', 'kam', 'kik']  instead
Out[4]: ['t', 'l', 'a', 'n', 's', 'f', 'o', 'n', 'e']

# To gain deeper insights, you can also specify debug flag to see output of each language
In [5]: model.inference('transphone', 'aaa', debug=True)                                                                                        
bin   ['s', 'l', 'a', 'n', 's', 'f', 'o', 'n', 'e']
bja   ['s', 'l', 'a', 'n', 's', 'f', 'o', 'n']
bkh   ['t', 'l', 'a', 'n', 's', 'f', 'o', 'n', 'e']
bvx   ['t', 'r', 'a', 'n', 's', 'f', 'o', 'n', 'e']
dua   ['t', 'r', 'n', 's', 'f', 'n']
eto   ['t', 'l', 'a', 'n', 's', 'f', 'o', 'n', 'e']
gwe   ['t', 'l', 'a', 'n', 's', 'f', 'o', 'n', 'e']
ibo   ['t', 'l', 'a', 'n', 's', 'p', 'o', 'n', 'e']
kam   ['t', 'l', 'a', 'n', 's', 'f', 'o', 'n', 'e']
kik   ['t', 'l', 'a', 'n', 's', 'f', 'ɔ', 'n', 'ɛ']
Out[5]: ['t', 'l', 'a', 'n', 's', 'f', 'o', 'n', 'e']
```

## Models

| model | # supported languages |       description        |
| :----: |:---------------------:|:------------------------:|
| latest |          ~8k          | based on our work at [1] |

## Reference

- [1] Li, Xinjian, et al. "Zero-shot Learning for Grapheme to Phoneme Conversion with Language Ensemble." Findings of the Association for Computational Linguistics: ACL 2022. 2022.
- [2] Li, Xinjian, et al. "Phone Inventories and Recognition for Every Language" LREC 2022. 2022