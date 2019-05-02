import tkinter as tk
import constants as c
import time

class Timeline():
	def __init__(self):
		self.app = tk.Tk()
		self.canvas = tk.Canvas(self.app, bg="black", height=c.HEIGHT, width=c.WIDTH)
		self.canvas.pack()
		self.__start_x, self.__end_x = c.START_X, c.END_X
		self.__zoom_factor = 1
		self.__start_tick = c.START_TICK

	def go(self):
		self.app.mainloop()

	def clear(self):
		self.canvas.delete('all')
		self.app.update()

	def __length(self):
		return self.__end_x - self.__start_x

	def __tick_x(self, tick_num):
		tick_distance = self.__length() / c.num_ticks()
		return c.START_X + (tick_num - self.__start_tick) * tick_distance
		# return self.__start_x + int((tick_num - c.START_TICK) * tick_distance)

	def __set_zoom_factor(self):
		self.__zoom_factor = self.__length() / c.LENGTH

	def display_line(self):
		self.__set_zoom_factor()

		self.canvas.create_line(self.__start_x, c.Y, self.__end_x, c.Y,  fill=c.FILL_COLOR, width=self.__zoom_factor)

		for tick_num in c.TICKS:
			x = self.__tick_x(tick_num)
			y_start = c.Y
			y_end = y_start - (c.TICK_HEIGHT * self.__zoom_factor)

			self.canvas.create_line(x, y_start, x, y_end, fill=c.FILL_COLOR, width = self.__zoom_factor)
			self.canvas.create_text(x, y_end - 10, text=str(tick_num), font=("Times", 10, "bold"), fill='white')

		self.app.update()

	def __eq_x(self, current_start_x, current_end_x):
		#eq point
		goal_start_x = c.START_X
		goal_end_x = c.END_X

		a = current_start_x - goal_start_x
		b = goal_end_x - current_end_x

		d = current_end_x - current_start_x
		w = goal_end_x - goal_start_x

		x = a / (w - d)

		eq_x = a + x*d

		return eq_x

	def zoom(self, start_tick, end_tick):
		self.__start_tick = start_tick
		current_start_x = self.__tick_x(start_tick)
		current_end_x   = self.__tick_x(end_tick)

		incr_start_x = (current_start_x - self.__start_x) / c.ZOOM_SMOOTHNESS
		incr_end_x = (current_end_x - self.__end_x) / c.ZOOM_SMOOTHNESS

		print(incr_start_x, incr_end_x)

		for idx in range(c.ZOOM_SMOOTHNESS):
			self.__start_x = self.__start_x - incr_start_x
			self.__end_x = self.__end_x - incr_end_x
			print(self.__length())
			self.clear()
			self.display_line()
			time.sleep(0.1)

timeline = Timeline()
timeline.display_line()
timeline.zoom(56, 66)
#timeline.zoom(30, 40)
timeline.go()