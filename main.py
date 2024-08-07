#
# TITLE:
# AUTHOR: Hyunseung Yoo
# PURPOSE:
# REVISION:
# REFERENCE: https://www.youtube.com/watch?v=l8Imtec4ReQ&t=1486s
#
#


from kivy.app import App
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button


#
class PageLayoutExample(PageLayout):
	pass


#
class ScrollViewExample(ScrollView):
	pass


#
class StackLayoutExample(StackLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.orientation = "lr-tb"
		for cnt in range(1, 101):
			size = dp(80)
			b = Button(text="Z"+str(cnt), size_hint=(None, None), size=(size, size))
			self.add_widget(b)	


#
class GridLayoutExample(GridLayout):
	pass


#
class AnchorLayoutExample(AnchorLayout):
	pass
	# def __init__(self, **kwargs):


#
class BoxLayoutExample(BoxLayout):
	pass
	#def __init__(self, **kwargs):
		# super().__init__(**kwargs)
		# self.orientation = 'vertical'
		# b1 = Button(text='Gray')
		# b2 = Button(text='Gom')
		# b3 = Button(text='Family')
		# self.add_widget(b1)
		# self.add_widget(b2)
		# self.add_widget(b3)


#
class MainWidget(Widget):
	pass


# 
class TheLabApp(App):
	pass


#
# MAIN
#

TheLabApp().run()	
