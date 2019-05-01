import tkinter as tk
import constants as c
import time

class Timeline():
	def __init__(self):
		self.app = tk.Tk()
		self.canvas = tk.Canvas(self.app, bg="black", height=c.HEIGHT, width=c.WIDTH)
		self.canvas.pack()
		self.start_x, self.end_x = c.START_X, c.END_X
		self.pre_zoom_start_x, self.pre_zoom_end_x = self.start_x, self.end_x

	def go(self):
		self.app.mainloop()

	def clear(self):
		self.canvas.delete('all')
		self.app.update()

	def __length(self):
		return self.end_x - self.start_x

	def __tick_x(self, tick_num):
		tick_distance = self.__length() / c.num_ticks()
		return self.start_x + int((tick_num - c.START_TICK) * tick_distance)

	def __zoom_factor(self):
		pre_zoom_length = self.pre_zoom_end_x - self.pre_zoom_start_x
		zoom_factor = self.__length() / pre_zoom_length
		return zoom_factor

	def display_line(self):
		zoom_factor = self.__zoom_factor()

		self.canvas.create_line(self.start_x, c.Y, self.end_x, c.Y,  fill=c.FILL_COLOR, width=zoom_factor)

		for tick_num in c.TICKS:
			x = self.__tick_x(tick_num)
			y_start = c.Y
			y_end = y_start - (c.TICK_HEIGHT * zoom_factor)

			self.canvas.create_line(x, y_start, x, y_end, fill=c.FILL_COLOR, width = zoom_factor)

		self.app.update()

	def zoom(self, start_tick, end_tick):
		goal_start_x = self.__tick_x(start_tick)
		goal_end_x   = self.__tick_x(end_tick)

		incr_start_x = (goal_start_x - self.start_x) / c.ZOOM_SMOOTHNESS
		incr_end_x = (goal_end_x - self.end_x) / c.ZOOM_SMOOTHNESS

		self.pre_zoom_start_x = self.start_x
		self.pre_zoom_end_x = self.end_x

		for idx in range(c.ZOOM_SMOOTHNESS):
			self.start_x = self.start_x - incr_start_x
			self.end_x = self.end_x - incr_end_x
			self.clear()
			self.display_line()
			time.sleep(0.1)

timeline = Timeline()
timeline.display_line()
timeline.zoom(20, 30)
timeline.go()