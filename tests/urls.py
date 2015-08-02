import unittest

from crispys_webkit.urls import LazyUrl


stackoverflow_url = 'http://stackoverflow.com/'

def create_stackoverflow_lazyurl():
	return LazyUrl(stackoverflow_url)

class LazyUrlMixin(object):

	def check_stackoverflow_url(self, url):
		self.assertEqual(url.scheme, 'http')
		self.assertEqual(url.host, 'stackoverflow.com')
		self.assertEqual(url.path, '/')
		self.assertEqual(str(url), 'http://stackoverflow.com/')

class LazyUrlCreationTests(LazyUrlMixin, unittest.TestCase):

	#### Object Instantiation ################################
	def test_create_lazy_url(self):
		""" Create a normal LazyUrl """
		url = LazyUrl('http://stackoverflow.com/')
		self.check_stackoverflow_url(url)

	def test_create_lazy_url_with_bad_scheme(self):
		""" use a scheme that is not allowed """ 
		url = LazyUrl('ftp://stackoverflow.com')
		self.check_stackoverflow_url(url)

	def test_create_lazy_url_with_no_scheme(self):
		""" don't use a scheme """ 
		url = LazyUrl('stackoverflow.com')
		self.check_stackoverflow_url(url)
	##########################################################


class LazyUrlGetSetTests(LazyUrlMixin, unittest.TestCase):

	#### Set Methods #########################################
	def test_set_scheme_with_bad_scheme(self):
		url = create_stackoverflow_lazyurl()
		self.check_stackoverflow_url(url)
		url.set_scheme('ssh')
		self.assertEqual(url.scheme, 'http')
		self.assertEqual(str(url), 'http://stackoverflow.com/')

	def test_set_scheme_with_good_scheme(self):
		url = create_stackoverflow_lazyurl()
		self.check_stackoverflow_url(url)
		url.set_scheme('https')
		self.assertEqual(url.scheme, 'https')
		self.assertEqual(str(url), 'https://stackoverflow.com/')

	def test_set_host(self):
		url = create_stackoverflow_lazyurl()
		self.check_stackoverflow_url(url)
		url.set_host('news.ycombinator.com')
		self.assertEqual(str(url), 'http://news.ycombinator.com/')

	def test_set_path(self):
		url = create_stackoverflow_lazyurl()
		self.check_stackoverflow_url(url)
		url.set_path('/user/1234/crispycret')
		self.assertIn(stackoverflow_url, str(url))
		self.assertEqual(url.path, '/user/1234/crispycret')
		self.assertEqual(str(url), 'http://stackoverflow.com/user/1234/crispycret')

	def test_set_params(self):
		url = create_stackoverflow_lazyurl()
		self.check_stackoverflow_url(url)
		url.set_params('price')
		self.assertEqual(str(url), 'http://stackoverflow.com/;price')

	def test_set_query(self):
		url = create_stackoverflow_lazyurl()
		self.check_stackoverflow_url(url)
		url.set_query('id=123')
		self.assertEqual(str(url), 'http://stackoverflow.com/?id=123')

	def test_set_fragment(self):
		url = create_stackoverflow_lazyurl()
		self.check_stackoverflow_url(url)
		url.set_fragment('someLabel')
		self.assertIn(stackoverflow_url, str(url))
		self.assertEqual(url.fragment, 'someLabel')
		self.assertEqual(str(url), 'http://stackoverflow.com/#someLabel')
	##########################################################


class LazyUrlMethodTests(LazyUrlMixin, unittest.TestCase):

	def test_get_full_path(self):
		url = create_stackoverflow_lazyurl()
		self.check_stackoverflow_url(url)
		url.set_path('question/55555/SomeQuestion')
		url.set_fragment('bookmark')
		self.assertEqual(url.get_full_path(), '/question/55555/SomeQuestion#bookmark')

	def test_clear_full_path(self):
		url = create_stackoverflow_lazyurl()
		self.check_stackoverflow_url(url)
		url.set_scheme('https')
		url.set_path('question/55555/SomeQuestion')
		url.set_params('details')
		url.set_query('id=1')
		url.set_fragment('bookmark')
		self.assertEqual(str(url), 'https://stackoverflow.com/question/55555/SomeQuestion;details?id=1#bookmark')
		url.clear_full_path()
		self.assertEqual(str(url), 'https://stackoverflow.com/')




if __name__ == '__main__':
	unittest.main()