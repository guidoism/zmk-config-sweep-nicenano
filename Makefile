all:
	python pretty.py && open /tmp/aaa.html
	/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --headless --disable-gpu --screenshot --window-size=460,1100 /tmp/aaa.html
