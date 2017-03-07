import ngram
import analyze
import os
import fileio


doc_path = '../text1/'

file_list = os.listdir(doc_path)

print('start')

for item in file_list:
	extension = os.path.splitext(item)[1]
	if extension != '.txt':
		continue
	analyzed_dict = analyze.tfidf_analyze(doc_path, doc_path + item)

	for cmp_file in file_list:
		print(item + ' and ' + cmp_file)
		cmp_dict = analyze.tfidf_analyze(doc_path, doc_path + cmp_file)

		cos_dict = analyze.cosine_similarity_analyze(analyzed_dict, cmp_dict)
		print('analyze['+str(item.replace(os.path.splitext(item)[1],'')) + ', ' + str(cmp_file) + '] : ' + str(cos_dict))

	item = item.replace(os.path.splitext(item)[1], '.csv')
	fileio.write_file('./analyze/'+item, analyzed_dict)
