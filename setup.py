#!/usr/bin/env python

from distutils.core import setup

setup(
    name='pyffprobe',
    version='1.0.0',
    description="A wrapper around ffprobe command to extract metadata from media files.",
    author='Simon Hargreaves',
    author_email='simon@simon-hargreaves.com',
    maintainer='Vereniging Campus Kabel',
    maintainer_email='info@vck.utwente.nl',
    url='https://github.com/VerenigingCampusKabel/ffprobe3',
    packages=['pyffprobe3'],
    keywords='ffmpeg, ffprobe, mpeg, mp4',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Natural Language :: English',
        'Topic :: Multimedia :: Video',
        'Topic :: Software Development :: Libraries'
    ])
