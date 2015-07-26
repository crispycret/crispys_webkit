

def get_class(obj): 
	return obj.__class__

def get_class_name(obj): 
	return obj.__class__.__name__



def get_methods_on_class(cls):
	""" 
	Returns a list of tuples containing of all the method names and methods in a class 
	i.e [(method_name1, method1), (method_name2, method2), ...]
	"""
	methods = []
	methods_to_ignore = object.__dict__.keys() # __init__, __str__, etc.

	for attr_name, attr_value in cls.__dict__.items():
		match_str = '<function %s at' % attr_name

		if match_str in str(attr_value):
			if attr_name not in methods_to_ignore:
				methods += [(attr_name, attr_value)]
	return methods




