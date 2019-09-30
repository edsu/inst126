all: slides.html exercise.html reflection.html

slides.html: slides.md
	pandoc --to revealjs --standalone --output slides.html slides.md

exercise.html: exercise.md
	pandoc --standalone --output exercise.html exercise.md

reflection.html: reflection.md
	pandoc --standalone --output reflection.html reflection.md