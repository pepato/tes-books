# tes-books

This little project aims to scrape The Imperial Library [1] to assemble all the books from The Elder Scrolls IV: Oblivion into a single epub.

The code is just a Python script which uses BeautifulSoup to edit the files. The files will be then passed to Pandoc, which will create the epub using the following command:

	pandoc  -S -o oblivion-books.epub --epub-metadata=title.txt --epub-cover-image=images/ob-cover.jpg  --epub-chapter-level=2 content/*.html -f html-native_divs

The script is based on a Directory system which goes like this:

	by-title-oblivion.html		list of books from Oblivion
	by-title-skyrim.html		list of books from Skyrim
	./content/			the html source files for each book
	./out/				the output directory
	./out/content/			where the edited files go
	./out/images/			where images are stored (i.e. the book cover)
	./out/title.txt			the yaml metadata file for Pandoc

[1] http://imperiallibrary.info