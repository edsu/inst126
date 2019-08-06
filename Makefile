all: modules syllabus

syllabus:
	pandoc README.md -o syllabus.pdf
