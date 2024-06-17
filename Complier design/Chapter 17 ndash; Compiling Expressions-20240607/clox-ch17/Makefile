CC = clang 
FLAGS = 
SRC = src
OUTPUT = bin
MAIN = clox
SOURCES := $(wildcard $(SRC)/*.c)
HEADERS := $(wildcard $(SRC)/*.h)
OBJECTS := $(patsubst %.c,%.o,$(SOURCES))
OUTPUTMAIN := $(OUTPUT)/$(MAIN)

all: $(OUTPUT) $(MAIN)
	@echo Executing 'all' complete! 

$(OUTPUT): 
	mkdir -p $(OUTPUT)

$(MAIN) : $(OBJECTS)
	$(CC) $(FLAGS) -o $(OUTPUTMAIN) $(OBJECTS) 

.c.o :
	$(CC) $(FLAGS) -c $< -o $@

.PHONY: clean 
clean: 
	rm -rf $(OUTPUTMAIN)
	rm -rf $(OBJECTS)
	@echo Cleanup complete! 

run: all 
	./$(OUTPUTMAIN)
