from setuptools import setup, find_packages

setup(name='pysdaza',
      version='0.1.0',
      description='My python functions for data analysis',
      url='http://github.com/sdaza/pysdaza',
      author='Sebastian Daza',
      author_email='sebastian.daza@gmail.com',
      license='MIT',
      packages=['pysdaza'],
      install_requires=['pandas', 'numpy'],
      zip_safe=False)
