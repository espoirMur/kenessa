from setuptools import setup

setup(
      name='kenessa',
      version='0.1.5',
      description='Rwanda Administrative Location',
      classifiers=[
      ],
      keywords= 'rwanda administrative location',
      url='https://github.com/rmuhire/kenessa',
      author='Remy Muhire',
      author_email='rmuhire@exuus.com',
      license='MIT',
      packages=['kenessa'],
      entry_points={
          'console_scripts': ['kenessa-province=kenessa.command_line:main'],
      },
      package_data = {'kenessa': ['json/*.json']},
      zip_safe=False
)



