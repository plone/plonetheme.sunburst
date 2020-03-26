import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.5.5.dev0'

long_description = (
    read('README.rst') + '\n' +
    read('plonetheme', 'sunburst', 'README.rst') + '\n' +
    read('CHANGES.rst') + '\n'
    )

setup(name='plonetheme.sunburst',
      version=version,
      description="The default theme for Plone 4.",
      long_description=long_description,
      classifiers=[
          "Development Status :: 6 - Mature",
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Plone :: 5.0",
          "Framework :: Plone :: 5.1",
          "Framework :: Plone :: 5.2",
          "Framework :: Plone :: Core",
          "Framework :: Zope2",
          "Framework :: Zope :: 4",
          "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
        ],
      keywords='web zope plone theme',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='https://pypi.org/project/plonetheme.sunburst',
      license='GPL version 2',
      packages=find_packages(),
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFCore',
          'plone.theme',
          'zope.component',
          'zope.interface',
      ],
      extras_require={
          'test': [
              'plone.app.testing',
          ]
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
