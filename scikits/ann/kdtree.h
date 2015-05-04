/*
kdtree.h
Wrapper for the ANN library
Copyright 2007, Barry Wark. All rights reserved.
Copyright (c) 2007, Barry Wark

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
*/

#include "ANN/ANN.h"
#include <sstream>

class _kdtree {
    
    ANNpointArray pts;
    ANNkd_tree *tree;
    
    public:
        /**
            Construct a new ANN Kd-tree wrapper.
            kdtree(arr, bs=1, split=ANN_KD_SUGGEST)
            
            *Parameters *
                arr : {array_like; 2D}
                    Array of [observations x dimensions]
                bs : {integer; default=1}
                    See ANN documentation
                split : {integer; default=ANN_KD_SUGGEST}
                    ANN split rule. See ANN documentation
        */
        _kdtree(double *pa, int n, int  m, int bs=1, int split=ANN_KD_SUGGEST) {
            pts = annAllocPts(n, m);
            
            
            for(int i=0; i<n; i++) {
                for(int j=0; j<m; j++) {
                     pts[i][j] = pa[i*m+j];
                }
            }
            
            tree = new ANNkd_tree(pts, n, m, bs, (ANNsplitRule)split);
        }
        
        ~_kdtree() {
            annDeallocPts(pts);
            delete tree;
        }
        
        void _knn2(double* q, int qd1, int qd2,
                int idx1, int idx2, int* nn_idx,
                int dd1, int dd2, double* dd,
                double eps=0.0) const {
                    
                    assert(qd1 == dd1);
                    assert(dd1 == idx1);
                    assert(dd2 == idx2);
                    
                    for(unsigned int i=0; i < (unsigned)qd1; i++) {
                        tree->annkSearch(q + (i*qd2), 
                                        dd2,
                                        nn_idx + (i*idx2),
                                        dd + (i*dd2),
                                        eps);
                    }
                    
                }
        
        
        /**
        Provide a __repr__ for python
        */
        const char* __repr__() const {
            return stringRep(true);
    	}
    	
    	/**
    	Provide a __str__ for python
    	*/
    	const char* __str__() const {
            return stringRep(false);
    	}
    	
	private:
	    const char* stringRep(bool includePoints) const {
	        std::ostringstream outstream;
    		tree->Dump(includePoints?ANNtrue:ANNfalse, outstream);
    		return outstream.str().c_str();
	    }
};