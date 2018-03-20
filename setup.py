import sys,os

main_dependencies = [
    "setuptools"
]

for dep in main_dependencies:
    try:
        __import__(dep)
    except ImportError:
        print(
            "Error: You do not have %s installed, please\n"
            "       install it. For example doing\n"
            "\n"
            "       pip3 install %s\n" % (dep, dep)
        )
        sys.exit(1)


from setuptools import setup
import reportex


setup(
    name='reportex',
    version=reportex.__version__,
    maintainer=reportex.__maintainer__,
    maintainer_email='sebastien.popoff@espci.fr',
    author=reportex.__author__,
    author_email=reportex.__email__,
    license=reportex.__license__,
    url='https://github.com/wavefrontshaping/reportex',
    install_requires=[
        "matplotlib"
    ],
    python_requires='>=2.7',
#    classifiers=[
#        'Development Status :: 3 - Alpha',
#        'Environment :: Console',
#        'Environment :: Console :: Curses',
#        'Intended Audience :: Developers',
#        'Intended Audience :: End Users/Desktop',
#        'Intended Audience :: System Administrators',
#        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
#        'Operating System :: MacOS',
#        'Operating System :: POSIX',
#        'Operating System :: Unix',
#        'Programming Language :: Python :: 3.3',
#        'Programming Language :: Python :: 3.4',
#        'Programming Language :: Python :: 3.5',
#        'Programming Language :: Python :: 3.6',
#        'Topic :: Utilities',
#    ],
    extras_require=dict(
        # List additional groups of dependencies here (e.g. development
        # dependencies). You can install these using the following syntax,
        # for example:
        # $ pip install -e .[develop]
        optional=[

        ],
        develop=[
#            "sphinx",
#            'sphinx-argparse',
#            'sphinx_rtd_theme',
#            'pytest',
        ]
    ),
    description='Simple tool to create quick pdf report with figures using latex.',
    long_description='',
    keywords=[
        'latex',
        'report',
        'pdf',
        'matplotlib'
    ],
    data_files=[

        (os.path.join(os.path.expanduser("~"),".reportex/templates/default/"), [
            "templates/default/template.tex"
        ])
    ],
    packages=[
        "reportex"
    ],
    platforms=['linux', 'osx'],
)
