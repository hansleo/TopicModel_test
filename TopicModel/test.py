# -*- coding:utf-8 -*-

import numpy as np
from konlpy.corpus import kobill
from konlpy.tag import Twitter
from gensim import corpora
from gensim import models


docs_ko = [kobill.open('test.txt').read()]
t = Twitter()
pos = lambda d: ['/'.join(p) for p in t.pos(d, stem=True, norm=True)]
texts_ko = [pos(doc) for doc in docs_ko]
test_ko = list()
for item in texts_ko[0]:
    if item.find('Punctuation') > -1: continue
    elif item.find('Number') > -1: continue
    elif item.find('Verb') > -1: continue
    elif item.find('Josa') > -1: continue
    elif item.find('Adjective') > -1: continue
    elif item.find('Conjunction') > -1: continue
    elif item.split('/')[0] is '': continue
    elif len(item.split('/')[0]) is 1: continue
    else: test_ko.append(item)
test_ko = [test_ko]
dict_ko = corpora.Dictionary(test_ko)
dict_ko.save('ko.dict')

tf_ko = [dict_ko.doc2bow(text) for text in test_ko]
tfidf_model_ko = models.TfidfModel(tf_ko)
tfidf_ko = tfidf_model_ko[tf_ko]
corpora.MmCorpus.serialize('ko.mm', tfidf_ko)

# print(tfidf_ko.corpus[0][:10])
print(sorted(tfidf_ko.corpus[0], key=lambda x: x[1], reverse=True)[:10])
for i in range(0,11):
    print(dict_ko.get(sorted(tfidf_ko.corpus[0], key=lambda x: x[1], reverse=True)[i][0]))
# print(dict_ko.get(11))

np.random.seed(42)
ntopics, nwords = 3, 5


lsi_ko = models.LsiModel(tfidf_ko, id2word=dict_ko, num_topics=ntopics)
print('--------------')
print(lsi_ko.print_topics(num_topics=ntopics, num_words=nwords))

lda_ko = models.LdaModel(tfidf_ko, id2word=dict_ko, num_topics=ntopics)
print('--------------')
print(lda_ko.print_topics(num_topics=ntopics, num_words=nwords))

hdp_ko = models.HdpModel(tfidf_ko, id2word=dict_ko)
print('--------------')
print(hdp_ko.print_topics(num_topics=ntopics, num_words=nwords))

