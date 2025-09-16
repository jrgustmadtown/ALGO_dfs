all: build run

build:
	javac HelloWorld.java
run: 
	java HelloWorld

clean:
	rm *.class