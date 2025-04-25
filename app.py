import kivy
import math
from kivy.properties  import ObjectProperty
from kivy.app import App
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.widget import Widget



class home(Widget):
		def __init__(self,**kwargs):
			super(home,self).__init__(**kwargs)

#function to concantinate input depending on situation		
		def digit(self,num):
			num_s = self.ids.display.text
			if num_s == '0':
				self.ids.display.text = ''
				self.ids.display.text = num

			# checking if inpuylts are math operators
			elif num == '/' or num == '*' or num == '+' or num =='-' : 

				#check if last character is an operator if it is do not repeat either operator if not concantinate operator to form math expression
				if num_s[-1] == '/' or num_s[-1] == '*' or num_s[-1] == '+' or num_s[-1] =='-':
					pass
				
				else:
					#concantinate operator
					self.ids.display.text = '%s%s'%(num_s,num) 
#checking dot 
			elif  num == '.':
				if '.' in num_s[-1]:
					pass
				else:
					self.ids.display.text = '%s%s'%(num_s,num)
									
#if digit value is available concantinate more values
			elif num_s  != '0':
				text = '%s%s'%(self.ids.display.text,num)
				self.ids.display.text = text

#######################################function_below
#check if number if negative or positive to change sign
		def abs(self):
			num_s = self.ids.display.text
			if num_s[0] == '-':
				self.ids.display.text = num_s[1:]
			elif num_s == '0':
				pass
			else:
				self.ids.display.text = '%s%s'%('-',num_s)

#########################function_below
#delete last string content function
		def remove(self):
			if self.ids.display.text != 'error':
				self.ids.display.text = self.ids.display.text[:-1]
			else:
				self.ids.display.text = '0'
			
##########################function_below		
#function to evaluate the expression
		def evaluate(self):
			try:
				ans = str(eval(self.ids.display.text))
				self.ids.count.text = ans
				self.ids.display.text = ans
			except:
				self.ids.count.text = 'error'
				self.ids.display.text = '0'
		
		
Builder.load_file('home.kv')
		
		
class application(App):
	def build(self):
		return home()
		
		


application().run()