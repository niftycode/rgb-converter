import io

from setuptools import setup, find_packages

with io.open('README.md', 'rt', encoding='utf8') as f:
    LONG_DESC = f.read()


setup(
    name='rgb_converter',
    version='0.0.2',
    license='MIT',
    description='Convert hex values to RGB values and vice versa',
    long_description=LONG_DESC,
    long_description_content_type='text/markdown',
    author='Bodo Schönfeld',
    author_email='bodo.schoenfeld@niftycode.de',
    url='https://github.com/niftycode/rgb-converter',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],

    packages=find_packages(exclude=('tests', 'docs')),
    python_requires='>=3.9',
    entry_points={
        'console_scripts': ['rgb_converter=rgb_converter.main:main'],
    },
    install_requires=['Pillow']
)
