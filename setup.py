# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='CaviClean',
      version='5.13',
      description='Convert cavit files',
      author='Xavier Bouteiller',
      author_email='xavier.bouteiller@u-bordeaux.fr',
      packages=['CaviClean'],
      install_requires=['pytz>=2020.1',
                        'python-dateutil==2.8.1',
                        'numpy>=1.19.2',
                        'six==1.15.0',
                        'pandas>=1.1.3'])
