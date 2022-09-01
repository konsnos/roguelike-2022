from setuptools import setup

setup(
    name='roguelike-2022',
    version='1.0.0',
    packages=['components'],
    url='https://github.com/konsnos/roguelike-2022',
    license='',
    classifiers=[
        'Development Status :: - Alpha',

        'Programming Language :: Python :: 3.8',
    ],
    author='Konstantinos Egkarchos',
    author_email='konsnosl@gmail.com',
    description='',
    install_requires=[
        'tcod>=11.15',
        'numpy>=1.18',
    ],
    python_requires='>=3.7'
)
