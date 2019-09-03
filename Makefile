all: all-modules all-homework README.md

README.md:
	pandoc README.md -o syllabus.pdf

all-modules:
	cd modules/ && $(MAKE)

all-homework:
	cd homework && $(MAKE)


