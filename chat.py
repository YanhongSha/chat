# Chat format change

def read_file(filename):
	lines = []
	with open (filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			lines.append((line).strip())
	return lines

def convert(lines):
	new = []
	person = None

	for line in lines:
		if line == 'Customer':
			person = 'Cusotmer '
			continue
		elif line == 'Service':
			person = 'Service'
			continue
		if person:                #只有person有值，才会执行
			new.append(person + ': ' + line)
	return new

def write_file(filename,lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()    #进入点
