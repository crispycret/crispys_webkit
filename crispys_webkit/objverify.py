import requests
from bs4 import BeautifulSoup as BS

from urls import LazyUrl
from objprope import get_class, get_class_name


__doc__ = \
""" 
Wrapping the isinstance method, verify an objects type.
If an object is not of the specified type raise a TypeError.
Ignoring the error is possible by providing a True value to the optional
ignore parameter in the function calls.  
"""


def is_type_of(obj, cls, ignore=False):
	""" Checks if an object is/of a specified class """
	# print obj, get_class_name(obj)
	if isinstance(obj, cls):
		return True
	elif ignore: 
		return False
	raise TypeError('%r is not of type %r' % (get_class(obj), cls))


def has_attr_of_type(obj, attrname, cls, ignore=False): 
	"""
	Checks if an object has a specified attribute, and checks if the
	attribute is of a specified type.
	"""
	type_error = False	
	if hasattr(obj, attrname):
		attr = getattr(obj, attrname)
		if is_type_of(attr, cls, ignore=True): 
			return True
		type_error = True
	
	elif ignore: 
		return False
	elif type_error:
		raise TypeError('%s is of type %r, expected type %r' %\
			('%s.%s' % (get_class_name(obj), attrname), get_class(attr), cls))
	raise AttributeError('%r has no attribute `%s`' % (get_class(obj), attrname))




def is_dict(obj, ignore=False):
	""" Checks if an object is type dict """
	return is_type_of(obj, dict, ignore)

def is_lazy_url(obj, ignore=False):

	""" Check if an object is type LazyUrl """
	return is_type_of(obj, LazyUrl, ignore)

def is_soup(obj, ignore=False):
	""" Checks if an object is type BeautifulSoup """
	return is_type_of(obj, BS, ignore)

def is_response(obj, ignore=False):
	""" Checks if an object is of type requests.Response """
	return is_type_of(obj, requests.Response, ignore)



def has_soup(obj, ignore=False):
	return has_attr_of_type(obj, 'soup', BS, ignore)

def has_response(obj, ignore=False):
	return has_attr_of_type(obj, 'response', requests.Response, ignore)

def has_headers(obj, ignore=False):
	return has_attr_of_type(obj, 'headers', requests.structures.CaseInsensitiveDict, ignore)

