import re
from multiprocessing import Queue
def reduce_file_path(path):
	q = Queue()
	temp= path.split("/")
	stay="."
	back=".."
	stack=[]
	jump=True
	for i in temp:
		if i==stay:
			continue
		elif i==back:
			stack.pop()
		else:
			if i!='':
				stack.append('/')
				stack.append(i)
	final=[]
	final.append("/")
	for i in stack:
		if i!='/':
			final.append(i)
	return final

print(reduce_file_path("/etc/../etc/../etc/../"))
