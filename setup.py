from setuptools import setup, find_packages

version = '1.0b3'

tests_require = ['collective.testcaselayer']

setup(name='plonetheme.sunburst',
      version=version,
      description="New theme for Plone 4.0",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='web zope plone theme',
      author='Plone Foundation',
      author_email='product-developers@lists.plone.org',
      url='http://pypi.python.org/pypi/plonetheme.sunburst',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      tests_require=tests_require,
      extras_require={'tests': tests_require},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
