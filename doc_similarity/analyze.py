import os
import math
import fileio
import ngram
from collections import OrderedDict
import operator

def tf_value(dictionary, word):
	
	return dictionary[word] / len(dictionary)


def tf_analyze(path):
	
	text = fileio.read_file(path)
	dictionary = ngram.wordgram_analyze(text)
	tf_dict = OrderedDict()

	for k, v in dictionary.items():
		tf_dict[str(k)] = tf_value(dictionary, str(k))
	sorted_tf_dict = OrderedDict(sorted(tf_dict.items(), key=operator.itemgetter(1), reverse=True))
	return sorted_tf_dict

def wordgram_map(dirpath):
	file_list = os.listdir(dirpath)
	dict_map = []
	for item in file_list:
		extension = os.path.splitext(item)[1]
		if extension != '.txt':
			continue
		item = dirpath + item
		file_contents = fileio.read_file(item)
		file_dict = ngram.wordgram_analyze(file_contents)
		dict_map.append(file_dict)
	return dict_map

def idf_value(dirpath, dict_map, word):
	file_list = os.listdir(dirpath)
	word_count = 0
	for dict_elem in dict_map:
		if word in dict_elem:
			word_count += 1
	if word_count is 0:
		word_count = 1
	return math.log(len(file_list)/word_count)

def idf_analyze(dirpath, path):
	dict_map = wordgram_map(dirpath)
	contents = fileio.read_file(path)
	dict_file = ngram.wordgram_analyze(contents)
	dict_idf = OrderedDict()
	for dict_elem in dict_file.keys():
		dict_idf[dict_elem] = idf_value(dirpath, dict_map, dict_elem)
	sorted_idf_dict = OrderedDict(sorted(dict_idf.items(), key=operator.itemgetter(1), reverse=True))
	return sorted_idf_dict

def tfidf_analyze(dirpath, path):
	dict_tf = tf_analyze(path)
	dict_idf = idf_analyze(dirpath, path)

	tf_idf_dict = OrderedDict()
	for tf_elem in dict_tf.keys():
		tf_idf_dict[tf_elem] = dict_tf[tf_elem] * dict_idf[tf_elem]

	sorted_tf_idf_dict = OrderedDict(sorted(tf_idf_dict.items(), key=operator.itemgetter(1), reverse=True))
	return sorted_tf_idf_dict

def cosine_similarity_analyze(document_dict_a, document_dict_b):
	cmp_len = len(document_dict_a)
	if len(document_dict_b) < cmp_len:
		cmp_len = len(document_dict_b)
	
	import similarity

	vector_a = []
	vector_b = []
	vector_dot = []

	for v in document_dict_a.values():
		vector_a.append(v)

	for v in document_dict_b.values():
		vector_b.append(v)

	for a_k, a_v in document_dict_a.items():
		if a_k in document_dict_b:
			vector_dot.append(a_v * document_dict_b[a_k])
	
	return similarity.cosine_similarity(vector_a, vector_b, vector_dot)


