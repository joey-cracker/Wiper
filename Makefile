wiper: wiper.py
	pyinstaller -F --clean --distpath . wiper.py
install: wiper
	cp wiper ~/bin
    
