from flexx import app,ui,event
from pyfiglet import Figlet

class Example(ui.Widget):
	
	def init(self):
		self.count = 0
		with ui.HBox():
			self.button = ui.Button(text='Click me',flex=0)
			self.label = ui.Label(flex=1)
	
	@event.connect('button.mouse_down')
	def _handle_click(self,down):
		if down:
			self.count += 1
			f = Figlet(font='slant')
			self.label.text = f.renderText(str(self.count))

if __name__ == '__main__':
	
	main = app.launch(Example)
	app.run()
