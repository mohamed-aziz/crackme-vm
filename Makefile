program: code.cpp
	clang++ code.cpp -O2 -oprogram
	strip program

code.cpp:
	python2 scotch.py > code.cpp

clean:
	rm code.cpp
	rm program