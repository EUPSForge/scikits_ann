#!/bin/bash

export ANN_DIR="$PREFIX"
export ANN_LIB="$ANN_DIR/lib"
export ANN_INCLUDE="$ANN_DIR/include"

$PYTHON setup.py install
