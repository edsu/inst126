all: all-modules syllabus

syllabus:
	pandoc README.md -o syllabus.pdf

all-modules:
	cd modules/ && $(MAKE)

