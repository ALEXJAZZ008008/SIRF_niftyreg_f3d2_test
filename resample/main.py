# Copyright University College London 2021
# Author: Alexander Whitehead, Institute of Nuclear Medicine, UCL
# For internal research only.


import sirf.Reg as reg


nifty_f3d_sym = reg.NiftyF3dSym()

nifty_f3d_sym.set_reference_image(reg.NiftiImageData3D("./ref.nii"))
nifty_f3d_sym.set_floating_image(reg.NiftiImageData3D("./flo.nii"))

nifty_f3d_sym.process()

resampler = reg.NiftyResample()

nifty_f3d_sym.get_deformation_field_forward().write("./dvf.nii")

resampler.set_reference_image(reg.NiftiImageData3D("./ref.nii"))
resampler.set_floating_image(reg.NiftiImageData3D("./flo.nii"))
resampler.add_transformation(nifty_f3d_sym.get_deformation_field_forward())

resampler.set_interpolation_type_to_cubic_spline()

resampler.forward(reg.NiftiImageData3D("./flo.nii")).write("./output.nii")
