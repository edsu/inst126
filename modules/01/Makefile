all: slides.html install.html

slides.html: slides.md
	pandoc --to revealjs --standalone --output slides.html slides.md

install.html: install.md
	pandoc --to revealjs --standalone --output install.html install.md

