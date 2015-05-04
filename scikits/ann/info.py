#!/usr/bin/env python
# encoding: utf-8

# info.py
# 
# Created by Barry Wark on 2007-11-07.
# Copyright (c) 2007 Barry Wark. All rights reserved.
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

__doc_title__ = """The Approximate Nearest Neighbor library"""

__doc__ = """The ANN module provides a numpy-compatible python wrapper around the Approximate Nearest Neighbor library.

The Approximate Nearest Neighbor library is available from http://www.cs.umd.edu/~mount/ANN/.

* Installation *
Download and build the Approximate Nearest Neighbor library. Modify the line in this package's setup.py file so that ANN_ROOT is the path to the root of the Approximate Nearest Neighbor library source tree.

Run ::

    python setup.py build
    python setup.py test
    sudo python setup.py install

from within the source directory.

* Usage *
scikits.ann exposes a single class, kdtree that wraps the Approximate Nearest Neighbor library's kd-tree implementation. kdtree has a single (non-constructor) method, knn that finds the indecies (of the points used to construct the kdtree) of the k-nearest neighbors and the squared distances to those points. A little example will probably be much more enlightening::
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

