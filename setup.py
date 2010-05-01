from setuptools import setup, find_packages

version = '1.0b4'

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
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/plonetheme.sunburst',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      extras_require={'test': ['collective.testcaselayer']},
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
