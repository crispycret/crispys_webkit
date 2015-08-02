import os, unittest

from crispys_webkit import LazyUrl, LazyPath


class LazyPathCreationTests(unittest.TestCase):

	def test_create_lazy_path(self):
		url = LazyUrl('stackoverflow.com')
		path = LazyPath(url)
		self.assertIn(path.rel, 'stackoverflow.com')
		self.assertTrue(os.path.exists(path.getpath()))





if __name__ == '__main__':
	unittest.main()