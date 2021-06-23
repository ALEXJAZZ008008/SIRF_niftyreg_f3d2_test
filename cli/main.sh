#! /bin/bash

# Copyright University College London 2021
# Author: Alexander Whitehead, Institute of Nuclear Medicine, UCL
# For internal research only.

NIFTYREGBINPATH="/home/alex/Documents/niftyreg_install/bin/"

$NIFTYREGBINPATH"/reg_f3d" -vel -ref "./ref.nii" -flo "./flo.nii"

$NIFTYREGBINPATH"/reg_resample" -ref "./ref.nii" -flo "./flo.nii" -trans "./outputCPP.nii" -res "./outputResult_resampled.nii"
