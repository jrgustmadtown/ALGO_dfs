all: build run

build:
	javac DFS.java
run: 
	java DFS

clean:
	rm *.class