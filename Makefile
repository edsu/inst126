all: all-modules README.md

README.md:
	pandoc README.md -o syllabus.pdf

all-modules:
	cd modules/ && $(MAKE)

