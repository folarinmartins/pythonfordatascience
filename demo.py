class TestClass(object):
	def __init__(self):
		pass
	
	def divide(self,a,b):
		try:
			return a/b
		except NameError:
			print('Variable not defined')
		except ZeroDivisionError:
			print("Division by Zero error")
		else:
			print('Code executed without errors')
		finally:
			print('Done executing code')
			
	def fileWorks(self):
		with open('./export.csv','r') as csvFile:
			print('name:',csvFile.name,'mode:',csvFile.mode)
			# content = print(csvFile.read())
			lines = csvFile.readlines()
			for i,line in enumerate(lines):
				values = line.split(',')
				sum = 0
				for value in values:
					sum += float(value)
				print('Sum of row',i,'=',sum)
	def writeLog(self):
		with open('./data.log','w') as logFile:
			logFile.write('Here is line 1\n')
			logFile.write('And here is line 2\n')
			logFile.writelines(['Here is Line 3\n','Here is line 4\n','And line 5\n'])
test = TestClass()
test.writeLog()
# print(test.divide(5.4,0))

# err5 = sum([abs(avg5[index] - sol5[index])for index in range(len(avg5))])