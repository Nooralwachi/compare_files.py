def compare_files(filename1,filename2):
	file1_gen=(line.strip() for line in open(filename1))
	file2_gen=(line.strip() for line in open(filename2))
	for line1, line2 in zip(file1_gen,file2_gen):
		if line1 != line2:
			return False
	return True

print(compare_files('file1.txt', 'file2.txt'))