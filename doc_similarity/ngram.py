from collections import OrderedDict

def wordgram_analyze(contents):

	wordgram_dict = OrderedDict()

	i = 0

	while i < len(contents):
		word = ""
		jmp_count = 1
		for j in range(1, len(contents)-i):
			if contents[i+j] == ' ' or contents[i+j] == '\r' or contents[i+j] == '\n':
				jmp_oount = j
				break
			else:
				word += contents[i+j]

		if len(word) < 1:
			i += jmp_oount
			continue
		if word in wordgram_dict:
			wordgram_dict[word] += 1
		else:
			wordgram_dict[word] = 1
		i += jmp_count
	
	return wordgram_dict

