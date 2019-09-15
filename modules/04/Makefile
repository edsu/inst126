all: slides.html exercise.html ethics.html

slides.html: slides.md
	pandoc --to revealjs --standalone --output slides.html slides.md

exercise.html: exercise.md
	pandoc --standalone --output exercise.html exercise.md

ethics.html: ethics.md
	pandoc --standalone --output ethics.html ethics.md
