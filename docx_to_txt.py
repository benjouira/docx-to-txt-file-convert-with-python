import docx2txt


text = docx2txt.process("file name.docx")


with open("new txt file name.txt", "w") as text_file:
	print(text, file=text_file)
