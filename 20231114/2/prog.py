class Num:
	def __get__(self, obj, cls):
		try:
			tmp = getattr(obj, self.__named)
		except Exception:
			tmp = 0
		return tmp

	def __set_name__(self, obj, name):
		self.__named = '_' + name

	def __set__(self, obj, val):
		try:
			setattr(obj, self.__named, val.real)
		except Exception:
			setattr(obj, self.__named, len(val))


import sys
exec(sys.stdin.read())