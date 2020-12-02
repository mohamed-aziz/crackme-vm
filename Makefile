program: code.cpp
	g++ code.cpp -oprogram

code.cpp:
	python2 scotch.py > code.cpp

clean:
	rm code.cpp
	rm program