all: index.html cws_model.html 中文句法现象.html

%.html: %.md
	markdown <$*.md > $*.html

