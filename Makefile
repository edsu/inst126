all: syllabus.pdf all-modules all-homework

syllabus.pdf: README.md
	pandoc README.md -o syllabus.pdf

all-modules:
	cd modules/ && $(MAKE)

all-homework:
	cd homework && $(MAKE)


