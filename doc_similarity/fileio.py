
def read_file(path):
	file = open(path, 'r', encoding = 'utf-8')
	contents = ''
	while True:
		line = file.readline()
		if (not line):
			break
		contents += line
	return contents

def write_file(path, dict):
	file = open(path, 'w', encoding = 'utf-8')
	for k, v in dict.items():
		text = str(k) + ',' + str(v) + '\n'
		file.write(text)
	file.close()
