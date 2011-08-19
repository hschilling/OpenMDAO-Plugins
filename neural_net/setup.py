

#
# This file is autogenerated during plugin_quickstart and overwritten during
# plugin_makedist. DO NOT CHANGE IT if you plan to use plugin_makedist to update 
# the distribution.
#

from setuptools import setup, find_packages

kwargs = {'author': '',
 'author_email': '',
 'classifiers': ['Intended Audience :: Science/Research',
                 'Topic :: Scientific/Engineering'],
 'description': '',
 'download_url': '',
 'entry_points': '[openmdao.surrogatemodel]\nNeuralNet=neraul_net:NeuralNet',
 'include_package_data': True,
 'install_requires': ['openmdao.main'],
 'keywords': ['openmdao'],
 'license': '',
 'maintainer': '',
 'maintainer_email': '',
 'name': 'neural_net',
 'package_data': {'neural_net': ['sphinx_build/html/.buildinfo',
                                 'sphinx_build/html/genindex.html',
                                 'sphinx_build/html/index.html',
                                 'sphinx_build/html/objects.inv',
                                 'sphinx_build/html/pkgdocs.html',
                                 'sphinx_build/html/py-modindex.html',
                                 'sphinx_build/html/search.html',
                                 'sphinx_build/html/searchindex.js',
                                 'sphinx_build/html/srcdocs.html',
                                 'sphinx_build/html/usage.html',
                                 'sphinx_build/html/_downloads/NN_Sin.py',
                                 'sphinx_build/html/_images/NNTutorial.png',
                                 'sphinx_build/html/_modules/index.html',
                                 'sphinx_build/html/_modules/neural_net/neural_net.html',
                                 'sphinx_build/html/_sources/index.txt',
                                 'sphinx_build/html/_sources/pkgdocs.txt',
                                 'sphinx_build/html/_sources/srcdocs.txt',
                                 'sphinx_build/html/_sources/usage.txt',
                                 'sphinx_build/html/_static/basic.css',
                                 'sphinx_build/html/_static/default.css',
                                 'sphinx_build/html/_static/doctools.js',
                                 'sphinx_build/html/_static/file.png',
                                 'sphinx_build/html/_static/jquery.js',
                                 'sphinx_build/html/_static/minus.png',
                                 'sphinx_build/html/_static/plus.png',
                                 'sphinx_build/html/_static/pygments.css',
                                 'sphinx_build/html/_static/searchtools.js',
                                 'sphinx_build/html/_static/sidebar.js',
                                 'sphinx_build/html/_static/underscore.js',
                                 'test/test_neural_net.py']},
 'package_dir': {'': 'src'},
 'packages': ['neural_net'],
 'url': '',
 'version': '0.1',
 'zip_safe': False}


setup(**kwargs)

