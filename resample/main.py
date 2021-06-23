# Copyright University College London 2021
# Author: Alexander Whitehead, Institute of Nuclear Medicine, UCL
# For internal research only.


import matplotlib.pyplot as plt

import sirf.Reg as reg


nifty_f3d_sym = reg.NiftyF3dSym()

ref = reg.NiftiImageData3D("./ref.nii")
flo = reg.NiftiImageData3D("./flo.nii")

nifty_f3d_sym.set_reference_image(ref)
nifty_f3d_sym.set_floating_image(flo)

nifty_f3d_sym.process()

resampler = reg.NiftyResample()

dvf = nifty_f3d_sym.get_deformation_field_forward()
dvf.write("./dvf.nii")

resampler.set_reference_image(ref)
resampler.set_floating_image(flo)
resampler.add_transformation(dvf)

resampler.set_interpolation_type_to_cubic_spline()

output_volume = resampler.forward(flo)
output_volume.write("./output.nii")

plt.imshow(output_volume.as_array()[:, 100, :])
plt.savefig("./output.png")
