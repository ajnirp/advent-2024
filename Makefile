1.out: 1.cpp
	g++ 1.cpp --std=c++1z -o 1.out

2.out: 2.cpp 2.hpp
	g++ 2.cpp 2.hpp -o 2.out

clean:
	rm -f *.gch *.out