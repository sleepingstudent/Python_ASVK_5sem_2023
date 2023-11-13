class InvalidInput(Exception): pass

class BadTriangle(Exception): pass

def triangleSquare(inStr):
	try:
		(x1, y1), (x2, y2), (x3, y3) = eval(inStr)
	except:
		raise InvalidInput
	
	try:
		y1, y2, y3 = float(y1), float(y2), float(y3)
		x1, x2, x3 = float(x1), float(x2), float(x3)
		res = abs((x1 - x3) * (y2 - y3) - (y1 - y3) * (x2 - x3)) * 0.5
		return res
	except:
		raise BadTriangle


res = 0
fl = True
while fl:
	try:
		res = triangleSquare(input())
	except InvalidInput:
		print("Invalid input")
	except BadTriangle:
		print("Not a triangle")
	else:
		fl = False
		print(f"{res:.2f}")
		
