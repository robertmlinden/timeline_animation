import tkinter as tk
import constants as c
import time

class Timeline():
	def __init__(self):
		self.app = tk.Tk()
		self.canvas = tk.Canvas(self.app, bg="black", height=c.HEIGHT, width=c.WIDTH)
		self.start_x, self.end_x = c.START_X, c.END_X

	def go(self):
		self.canvas.pack()
		self.app.mainloop()

	def clear(self):
		self.canvas.delete('all')

	def __tick_x(self, tick_num):
		return c.BUFFER + int((tick_num - c.START_TICK) * c.TICK_WIDTH)


	def __line_width(self, zoom_length):
		return (c.WIDTH - 2*c.BUFFER)  / zoom_length

	def display_line(self):
		line_width = self.__line_width(self.end_x - self.start_x)

		self.canvas.create_line(self.start_x, c.Y, self.end_x, c.Y,  fill=c.FILL_COLOR, width=line_width)

		for tick_num in c.TICKS:
			x = self.__tick_x(tick_num)
			y_start = c.Y
			y_end = y_start - c.TICK_HEIGHT

			self.canvas.create_line(x, y_start, x, y_end, fill=c.FILL_COLOR)

	def zoom(self, start_tick, end_tick):
		pass

timeline = Timeline()
timeline.display_line()
timeline.go()