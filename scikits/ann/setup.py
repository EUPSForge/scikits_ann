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
setup.py

Created by Barry Wark on 2007-11-07.
Copyright (c) 2007 Barry Wark. All rights reserved.
"""

import os
import os.path

from numpy.distutils.core import setup
from numpy.distutils.misc_util import Configuration

def configuration(parent_package='', top_path=None):
    
    config = Configuration('ann', parent_package, top_path)
    
    assert('ANN_LIB' in os.environ)
    assert('ANN_INCLUDE' in os.environ)
    
    ann_library_dir = os.environ['ANN_LIB']
    ann_include_dir = os.environ['ANN_INCLUDE']
    
    #TODO: add flags to statically link libANN
    config.add_extension('_ANN',
                        sources = ['ANN.i'],
                        include_dirs = ['.', ann_include_dir],
                        library_dirs = [ann_library_dir],
                        libraries = ['ANN'],
                        language='c++',
#                        swig_opts='-c++',
                        )
    config.add_subpackage('tests')
    
    return config

if __name__ == '__main__':
    setup(configuration=configuration)