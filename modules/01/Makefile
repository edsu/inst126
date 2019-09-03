all: slides.html install.html exercise.html

slides.html: slides.md
	pandoc --to revealjs --standalone --output slides.html slides.md

install.html: install.md
	pandoc --to html --standalone --output install.html install.md

exercise.html: exercise.md
	pandoc --to html --standalone --output exercise.html exercise.md

