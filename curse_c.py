from curses import wrapper

def main(stdscr):
	for i in range(0, 10):
		v = i - 10
		stdscr.addstr(i, 0, "9 divided by {} is {}" .format(v, 10/v))
	stdscr.refresh()
	stdscr.getkey()

wrapper(main)
