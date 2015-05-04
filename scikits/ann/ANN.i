// -*- c++ -*-

/* 
SWIG interface file for ANN library

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

/* TODO
    - wrap std::istream/std::ostream - use typemaps -> loads/dumps
*/


%module ANN
%{
    #define SWIG_FILE_WITH_INIT
    #include "ANN/ANN.h"
    #include "kdtree.h"
    #include <sstream>
%}

%include "numpy.i"
%include "constraints.i"

%init %{
    import_array();
%}


//knn1
%apply (double* IN_ARRAY2, int DIM1, int DIM2) {(double* pa, int n, int m)}
%apply (double* IN_ARRAY1, int DIM1) {(double* q, int qd)}
%apply (int DIM1, int* ARGOUT_ARRAY1) {(int k, int* nn_idx)}
%apply (int DIM1, double* ARGOUT_ARRAY1) {(int k2, double* dd)}

//knn2
%apply (double* IN_ARRAY2, int DIM1, int DIM2) {(double* q, int qd1, int qd2)}
%apply (int DIM1, int DIM2, int* INPLACE_ARRAY2) {(int idx1, int idx2, int* nn_idx)}
%apply (int DIM1, int DIM2, double* INPLACE_ARRAY2) {(int dd1, int dd2, double* dd)}


//constraints
%apply int NONNEGATIVE {int n}
%apply int NONNEGATIVE {int dd}
%apply int NONNEGATIVE {int bs}
%apply int NONNEGATIVE {int k}
%apply int NONNEGATIVE {int qd}
%apply int NONNEGATIVE {int k2}
%apply double NONNEGATIVE {double eps}

//%import "ANN.h"
%include "kdtree.h"
