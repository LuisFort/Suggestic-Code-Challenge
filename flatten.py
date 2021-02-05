from time import time

a = [1, 2, [3, 4, [5, 6], 7], 8]
#a = [[1,2,[3,4,5], [6,7]],[8,9],10,[11,[12,13,14,[15,16,17,[18,19]],20]]]


def flatten(nestedArray):
	flattenArray = []
	for element in nestedArray :
		if type(element) is list:
			flattenArray += flatten(element)
		else :
			flattenArray.append(element)

	return flattenArray

start = time()
print(flatten(a))
print('Tiempo de ejecución: ', time()-start)
