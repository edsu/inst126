all: slides.html

slides.html: slides.md
	pandoc --to revealjs --standalone --output slides.html slides.md

exercise.html: exercise.md
	pandoc --to html --standalone --output exercise.html exercise.md


