from setuptools import setup


setup(
	name='crispys_webkit',
	version='0.1.13',

	author ='Brandon Nadeau',
	author_email='brandonmnadeau@hotmail.com',

	packages=['crispys_webkit'],

	url='http://github.com/crispycret/crispys_webkit',

	license='MIT',

	description='Some common web functionalites that I use.',
	#long_description=open('README.txt').read(),

	install_requires = [
		'requests',
		'beautifulsoup4',
		'python-slugify',
	],

	zip_safe=False,
)
