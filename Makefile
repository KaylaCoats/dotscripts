BINSRCS = ~/bin/check_links.py ~/bin/replace.py

link:
	rm -f ${BINSRCS}
	ln -s ~/.scripts/check_links.py ~/bin/check_links.py
	ln -s ~/.scripts/replace.py ~/bin/replace.py

unlink:
	unlink ~/bin/check_links.py
	unlink ~/bin/replace.py
	cp ~/.scripts/check_links.py ~/bin/check_links.py
	cp ~/.scripts/replace.py ~/bin/replace.py
