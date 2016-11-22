from setuptools import setup

setup(name='myrw',
      version='0.1',
      description='Rwanda Administrative Location',
      classifiers=[
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2.7',
            'Topic :: Rwanda Administrative Location :: Linguistic',
      ],
      keywords= 'rwanda map administration package',
      url='https://github.com/rmuhire/myrw',
      author='Remy Muhire, Dieume Hirwa',
      author_email='rmuhire@exuus.com, dhirwa@exuus.com',
      license='MIT',
      packages=['myrw'],
      install_requires = [

      ],
      entry_points={
          'console_scripts': ['myrw-province=myrw.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)