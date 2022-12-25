CXX ?= g++
.PHONY: clean

main: main.cpp factorial.o
	$(CXX) -o $@ -g -O0 $^

%.o: %.cpp
	$(CXX) -o $@ -g -O0 -c $<

clean:
	rm -f main *.o
