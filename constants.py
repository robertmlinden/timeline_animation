HEIGHT = 750
WIDTH = 2500
BUFFER = 50

START_X = BUFFER
Y = HEIGHT - BUFFER
END_X = WIDTH - BUFFER
LENGTH = END_X - START_X

START_TICK = 6
END_TICK = 100
ROUNDS = END_TICK - START_TICK + 1

TICKS = range(START_TICK, END_TICK + 1)

TICK_HEIGHT = 10

FILL_COLOR = '#00bfff'

def num_ticks():
	return len(TICKS) - 1

def line_width(zoom_length):
	return (WIDTH - 2*BUFFER)  / zoom_length

TICK_WIDTH = LENGTH / num_ticks()