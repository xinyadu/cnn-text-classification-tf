import argparse
import json
import codecs

parser = argparse.ArgumentParser()
parser.add_argument('--file_path', default="../proced2/dev.txt", type=str)

args = parser.parse_args()

if __name__ == '__main__':
	with open(args.file_path, 'r') as infile:
		paragraphs = json.load(infile)	

	pos_sents = []
	neg_sents = []
	for para in paragraphs:
		for sent in para['text']:
		
			# label y
			if sent['ans_num'] > 0:
				pos_sents.append(sent['tokenized_sentence'])
			else:
				neg_sents.append(sent['tokenized_sentence'])

	out_file_name = args.file_path.rsplit('/')[-1].split('.')[0] + '-pos'
	with codecs.open(out_file_name, 'w', 'utf-8') as outfile:
		for s in pos_sents:
			outfile.write(s + '\n')

	out_file_name = args.file_path.rsplit('/')[-1].split('.')[0] + '-neg'
	with codecs.open(out_file_name, 'w', 'utf-8') as outfile:
		for s in neg_sents:
			outfile.write(s + '\n')

	print len(pos_sents)

