all: index.html cws_model.html

%.html: %.md
	markdown <$*.md > $*.html

