import tkinter as tk
import constants as c
import time

class Timeline():
	def __init__(self):
		self.app = tk.Tk()
		self.canvas = tk.Canvas(self.app, bg="black", height=c.HEIGHT, width=c.WIDTH)
		self.canvas.pack()
		self.__zoom_factor = 1
		self.__start_tick = c.START_TICK
		self.__eq_x = 0

	def go(self):
		self.app.mainloop()

	def clear(self):
		self.canvas.delete('all')
		self.app.update()

	def __length(self):
		pass
		#return self.__end_x - self.__start_x

	def __tick_x(self, tick_num, zoom_factor):
		tick_distance = LENGTH / c.num_ticks()
		return c.START_X + (tick_num)

	def __tick_x(self, tick_num):
		tick_distance = self.__length() / c.num_ticks()
		return c.START_X + (tick_num - self.__start_tick) * tick_distance

	def __set_eq_x(current_start_x, current_end_x):
		#eq point
		goal_start_x = c.START_X
		goal_end_x = c.END_X

		a = current_start_x - goal_start_x
		b = goal_end_x - current_end_x

		d = current_end_x - current_start_x
		w = goal_end_x - goal_start_x

		x = a / (w - d)

		self.__eq_x = a + x*d


	def display_line(self, zoom_factor=1):
		start_x = self.__eq_x - (self.__eq_x - c.START_X) * zoom_factor
		end_x = self.__eq_x + (c.END_X - self.__eq_x) * zoom_factor

		length = end_x - start_x

		self.canvas.create_line(start_x, c.Y, end_x, c.Y,  fill=c.FILL_COLOR, width=zoom_factor)

		# for tick_num in c.TICKS:
		# 	x = self.__tick_x(tick_num)
		# 	y_start = c.Y
		# 	y_end = y_start - (c.TICK_HEIGHT * zoom_factor)

		# 	self.canvas.create_line(x, y_start, x, y_end, fill=c.FILL_COLOR, width = zoom_factor)
		# 	self.canvas.create_text(x, y_end - 10, text=str(tick_num), font=("Times", 10, "bold"), fill='white')

		self.app.update()

	def zoom(self, start_tick, end_tick):
		self.__start_tick = start_tick
		current_start_x = self.__tick_x(start_tick)
		current_end_x   = self.__tick_x(end_tick)

		self.__set_eq_x(current_start_x, current_end_x)

		final_zoom_factor = (current_end_x - current_start_x) / (c.END_X - c.START_X)

		for zoom_idx in range(c.ZOOM_SMOOTHNESS):
			self.clear()

			zoom_factor = zoom_idx / c.ZOOM_SMOOTHNESS * final_zoom_factor
			self.display_line(zoom_factor)
			time.sleep(0.1)

timeline = Timeline()
timeline.display_line()
timeline.zoom(56, 66)
#timeline.zoom(30, 40)
timeline.go()