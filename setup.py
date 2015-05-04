#! /usr/bin/env python

# Copyright (c) 2007, Barry Wark
# 
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

import setuptools

long_description = """
The ANN module provides a numpy-compatible python wrapper around the 
Approximate Nearest Neighbor library (http://www.cs.umd.edu/~mount/ANN/).

* Installation *
Download and build the Approximate Nearest Neighbor library. Modify the ANN section of 
site.cfg so that ANN_ROOT is the path to the root of the Approximate Nearest Neighbor 
library include/lib tree.
If /usr/local/include contains the ANN/ include directory and /usr/local/lib contains 
libANN.a, then
ANN_ROOT = /usr/local

Run ::

    python setup.py build_ext --inplace build test
    sudo python setup.py install

from within the source directory.

* Usage *
scikits.ann exposes a single class, kdtree that wraps the Approximate Nearest Neighbor 
library's kd-tree implementation. kdtree has a single (non-constructor) method, knn that 
finds the indecies (of the points used to construct the kdtree) of the k-nearest neighbors
 and the squared distances to those points. A little example will probably be much 
 more enlightening::
    >>> import scikits.ann as ann
        
    >>> import numpy as np

    >>> k=ann.kdtree(np.array([[0.,0],[1,0],[1.5,2]]))

    >>> k.knn([0,.2],1)
    (array([[0]]), array([[ 0.04]]))

    >>> k.knn([0,.2],2)
    (array([[0, 1]]), array([[ 0.04,  1.04]]))

    >>> k.knn([[0,.2],[.1,2],[3,1],[0,0]],2)
    (array([[0, 1],
           [2, 0],
           [2, 1],
           [1, 2]]), array([[ 0.04,  1.04],
           [ 1.96,  4.01],
           [ 3.25,  5.  ],
           [ 1.  ,  6.25]]))

    >>> k.knn([[0,.2],[.1,2],[3,1],[0,0]],3)
    (array([[ 0,  1,  2],
           [ 2,  0,  1],
           [ 2,  1,  0],
           [ 1,  2, -1]]), array([[  4.00000000e-002,   1.04000000e+000,   5.49000000e+000],
           [  1.96000000e+000,   4.01000000e+000,   4.81000000e+000],
           [  3.25000000e+000,   5.00000000e+000,   1.00000000e+001],
           [  1.00000000e+000,   6.25000000e+000,   1.79769313e+308]]))
    
"""

classifiers = ['Development Status :: 4 - Beta',
                'Intended Audience :: Developers',
                'Intended Audience :: Science/Research',
                'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                'Programming Language :: Python',
                'Topic :: Scientific/Engineering',
                'Topic :: Software Development :: Libraries :: Python Modules']

DISTNAME = 'scikits.ann'
VERSION = '0.2'

import os
import os.path
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('site.cfg')

if('ANN_LIB' not in os.environ):
    os.environ['ANN_LIB'] = config.get('ANN', 'ANN_LIB')

if('ANN_INCLUDE' not in os.environ):
    os.environ['ANN_INCLUDE'] = config.get('ANN', 'ANN_INCLUDE')


def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    
    config = Configuration(None, parent_package, top_path,
                            namespace_packages=['scikits'])
    
    config.set_options(
        ignore_setup_xxx_py=True,
        assume_default_configuration=True,
        delegate_options_to_subpackages=True,
        quiet=True,
    )
    
    config.add_subpackage('scikits')
    config.add_subpackage(DISTNAME)
    
    config.add_data_files('scikits/__init__.py')

    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    
    setup(
        configuration = configuration,
        name = DISTNAME,
        version = VERSION,
        description = "Approximate Nearest Neighbor library wrapper for Numpy",
        long_description = long_description,
        author      = "Barry Wark",
        author_email = "barrywark@gmail.com",
        install_requires = ['configobj'],
        requires = ['numpy'],
        classifiers = classifiers,
        license = 'GNU Library or Lesser General Public License (LGPL)',
        url = 'http://scipy.org/scipy/scikits/wiki/AnnWrapper',
        test_suite = 'nose.collector',
    )
