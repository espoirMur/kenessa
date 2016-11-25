from setuptools import setup

setup(
      name='myrw',
      version='0.1.1',
      description='Rwanda Administrative Location',
      classifiers=[
      ],
      keywords= 'rwanda map administration package',
      url='https://github.com/rmuhire/myrw',
      author='Remy Muhire, Dieume Hirwa',
      author_email='rmuhire@exuus.com, dhirwa@exuus.com',
      license='MIT',
      packages=['myrw'],
      entry_points={
          'console_scripts': ['myrw-province=myrw.command_line:main'],
      },
      package_data = {'myrw': ['json/*.json']},
      zip_safe=False
)



