#!/usr/bin/env python
# encoding: utf-8
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
"""
untitled.py

Created by  on 2007-10-24.
Copyright (c) 2007 Barry Wark. All rights reserved.
"""

import numpy as N
from numpy.testing import NumpyTestCase
from numpy.testing import assert_equal, assert_almost_equal, assert_array_almost_equal

from scikits.ann import kdtree

def checkReturnNumber(k, i):
    """check k returns i from knn"""
    
    pt = N.random.rand(3)
    assert_equal(k.knn(pt, i)[0].size,i)
    assert_equal(k.knn(pt, i)[1].size,i)


def distanceFromOrigin(pts):
    """pts is [observations x dimensions]"""
    
    return N.apply_along_axis(lambda (arr) : N.sqrt(N.power(arr,2).sum()),1,pts)


def checkReturnNN(pts,distances):
    
    pt = N.zeros(pts.shape[1])
    tree = kdtree(pts)
    nn,nn_distances = tree.knn(pt,1)
    nn_distances = N.sqrt(nn_distances)
    
    sorted_distances = N.sort(distances)
    
    for j in xrange(nn.size):
        assert_almost_equal(distanceFromOrigin(N.atleast_2d(pts[nn[j]])), nn_distances[j])
        assert_almost_equal(nn_distances[j],sorted_distances[j])
        assert_almost_equal(nn[j], N.where(distances==sorted_distances[j])[0][0])


class TestANNWrapper(object):
    """Unit tests for ANN wrapper"""
    
    def test_knn_returns_corrent_number_of_neighbors(self):
        
        pts = N.random.rand(10,3)
        
        k = kdtree(pts)
        
        for i in xrange(10):
            yield checkReturnNumber,k,i
    
    
    def test_knn_returns_nearest_neighbor(self):
        
        for nObs in [1,3,10]:
            pts = N.random.rand(nObs,2)
            distances = distanceFromOrigin(pts)
            
            for i in xrange(nObs):
                yield checkReturnNN,pts,distances
            
    
                





if __name__ == '__main__':
    import nose
    nose.run(argv=[__file__,__file__])

