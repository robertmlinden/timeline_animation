import tkinter as tk
import constants as c
import time

class Timeline():
	def __init__(self):
		self.app = tk.Tk()
		self.canvas = tk.Canvas(self.app, bg="black", height=c.HEIGHT, width=c.WIDTH)
		self.canvas.pack()
		self.__eq_x = 0
		self.__last_start_x = c.START_X
		self.__last_end_x   = c.END_X
		self.__zoom_factor = 1

	def go(self):
		self.app.mainloop()

	def clear(self):
		self.canvas.delete('all')
		self.app.update()

	def __length(self):
		return c.LENGTH * self.__zoom_factor

	def __set_eq_x(self):
		#eq point
		goal_start_x = c.START_X
		goal_end_x = c.END_X

		a = self.__last_start_x - goal_start_x
		b = goal_end_x - self.__last_end_x

		d = self.__last_end_x - self.__last_start_x
		w = goal_end_x - goal_start_x

		x = a / (w - d)

		self.__eq_x = a + x*d + c.START_X

	def __tick_x(self, tick_num, start_x=c.START_X):
		tick_distance = self.__length() / c.num_ticks()
		return start_x + (tick_num - c.START_TICK) * tick_distance

	def display_line(self):
		start_x = self.__eq_x - (self.__eq_x - c.START_X) * self.__zoom_factor
		end_x = self.__eq_x + (c.END_X - self.__eq_x) * self.__zoom_factor

		# import pdb; pdb.set_trace()

		length = end_x - start_x

		self.canvas.create_line(start_x, c.Y, end_x, c.Y,  fill=c.FILL_COLOR, width=self.__zoom_factor)

		for tick_num in c.TICKS:
			x = self.__tick_x(tick_num, start_x)
			y_start = c.Y
			y_end = y_start - (c.TICK_HEIGHT * self.__zoom_factor)

			self.canvas.create_line(x, y_start, x, y_end, fill=c.FILL_COLOR, width = self.__zoom_factor)
			self.canvas.create_text(x, y_end - 5*self.__zoom_factor, text=str(tick_num), font=("Times", int(5*self.__zoom_factor), "bold"), fill='white')

		self.app.update()

	def zoom(self, start_tick, end_tick):
		self.__last_start_x = self.__tick_x(start_tick)
		self.__last_end_x   = self.__tick_x(end_tick)

		print(self.__last_start_x, self.__last_end_x)

		# print(self.__last_start_x, self.__last_end_x)
		# import pdb; pdb.set_trace()

		self.__set_eq_x()

		final_zoom_factor = (c.END_X - c.START_X) / (self.__last_end_x - self.__last_start_x)
		print(final_zoom_factor)

		# print(final_zoom_factor)

		# import sys; sys.exit(0)

		# import pdb; pdb.set_trace()

		for zoom_idx in range(c.ZOOM_SMOOTHNESS):
			self.clear()

			self.__zoom_factor = 1 + (zoom_idx + 1) / c.ZOOM_SMOOTHNESS * (final_zoom_factor - 1)
			print(self.__zoom_factor)
			# print(self.__eq_x)
			self.display_line()
			time.sleep(c.ZOOM_TIME_LENGTH / (c.ZOOM_SMOOTHNESS - 1))

timeline = Timeline()
timeline.display_line()
time.sleep(c.ZOOM_TIME_LENGTH / (c.ZOOM_SMOOTHNESS - 1))
# timeline.zoom(6, 16)
timeline.zoom(16, 26)
#timeline.zoom(30, 40)
timeline.go()