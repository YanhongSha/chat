# Chat format change

def read_file(filename):
	lines = []
	with open (filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			lines.append((line).strip())
	return lines

# 进行统计
def convert(lines):
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_pic_count = 0
	viki_pic_count = 0
	for line in lines:
		s = line.split(' ')   #成为清单
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_pic_count += 1				
			else:
				for msg in s[2:]:   #清单的分割
					allen_word_count += len(msg)	
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_pic_count += 1	
			else:
				for msg in s[2:]:
					viki_word_count += len(msg)			
	print('Allen speaks', allen_word_count, 'words.')
	print('Viki speaks', viki_word_count, 'words.')
	print('Allen puts', allen_sticker_count, 'sticker.')
	print('Viki puts', viki_sticker_count, 'sticker.')
	print('Allen puts', allen_pic_count, 'pics.')
	print('Viki puts', viki_pic_count, 'pics.')


def write_file(filename,lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	# write_file('output.txt', lines)

main()    #进入点
