import pandas as pd
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
	def usePandas(self):
		df = pd.read_csv('./export.csv')
		set = {'name':['Akin','Adebayo','Debola'],'age':[10,20,30],'gender':['m','f','o']}
		df2 = pd.DataFrame(set)

		print(df[['2.5','2.1'][0]])
		# print(df.iloc[0].unique())
		# print(df['2.5'].unique())
		# print(df['2.1']>=1.1)
		# print(df[df['2.1']>=1.1])
		# print(df['2.5'][df['2.1']>=1.1])
		# df.to_csv('filtered.csv')
		# print(df[['2.1','2.5']])

		# print(df2.iloc[:,:])
		# print(df2.loc[0:1,'name':'age'])

		# print(df.head())		
		
	def useNumpy(self):
		import numpy as np
		import matplotlib.pyplot as plt
		a = np.array([1,2,3,5,7,10,15,21])
		x = np.linspace(0,np.pi*2,100)
		y = np.sin(x)
		plt.plot(x,y)
		# print(type(a))
		# print(a.dtype)
		# print(a)
test = TestClass()
test.useNumpy()


# print(test.divide(5.4,0))

# err5 = sum([abs(avg5[index] - sol5[index])for index in range(len(avg5))])