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

import ANN
import numpy as np

from info import __doc__

from numpy.testing import Tester
test = Tester().test

from scikits.ann.version import __version__

class kdtree(ANN._kdtree):
    """Immutable kd-tree wrapper for the Approximate Nearest Neighbor library kd-tree implementation"""
    
    def __init__(self, *args):
        """kdtree(arr, bs=1, split=ANN_KD_SUGGEST)
        
        Construct a new ANN Kd-tree wrapper.
            
        *Parameters *
            arr : {array_like; 2D}
                Array of [observations x dimensions]
            bs : {integer; default=1}
                See ANN documentation
            split : {integer; default=ANN_KD_SUGGEST}
                ANN split rule. See ANN documentation
        """
        
        super(kdtree, self).__init__(*args)
        self.nDim = args[0].shape[1]
    
    
    def knn(self, pts, k=1, eps=0.0):
        """(idx,d2) = knn(pts, k=1, eps=0.0)
        
        Find k-nearest neighbors of one (or more) points.
        
        * Parameters *
            pts : numpy.ndarray
                [nPts x nDimensions]
                nDimensions must be the same as the number of dimensions of the points
                that initialized this kdtree.
            k : int
                Number of nearest neighbors to find
            eps : double
                eps of approximate nearest neighbor search. Use eps=0.0 to find exact
                nearest neighbors.
                Default = 0.0.
                
        * Returns *
            idx : numpy.ndarray
                [nPts x k]
                Each row corresponds to the same row in parameter `pts`. Row gives index into
                kdtree's initialized points of nearest neighbors.
            d2 : numpy.ndarray
                [nPts x k]
                Array of squared distances to the points given in idx.
                
        * Example *
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
        
        pts = np.atleast_2d(pts)
        assert(pts.shape[1] == self.nDim)
        
        idx = np.empty((pts.shape[0], k), dtype='i')
        d2 = np.empty_like(idx).astype(np.float_)

        self._knn2(pts, idx, d2, eps)
        
        return (idx, d2)
    
