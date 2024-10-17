CC=gcc
FLAGS=-Wall

mtliani: longest_line.c
# .PHONY: mtliani
	@echo
	$(CC) $(FLAGS) -o lon_lin longest_line.c
	@echo

debug: longest_line.c
# .PHONY: debug
	$(CC) $(FLAGS) -g -o glon_lin longest_line.c
	gdb -tui glon_lin

obieqturi: lon_lin.o
	$(CC) $(FLAGS) -o lon_lin lon_lin.o

lon_lin.o: longest_line.c
	$(CC) $(FLAGS) -c -o lon_lin.o

didi: main.c longest.h copy.c get_line.c
	$(CC) $(FLAGS) -o udidesi main.c longest.h copy.c get_line.c
# CC=gcc
# CFLAGS=-Wall
#
#
# #all : longest_line
# #.PHONY : all
# #
# #erTi faili
# longest : longest_line.o
# 	$(CC) $(CFLAGS) -o udidesi longest_line.o
#
# longest_line.o : longest_line.c
# 	$(CC) $(CFLAGS) -c -o longest_line.o longest_line.c
