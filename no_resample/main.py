# Copyright University College London 2021
# Author: Alexander Whitehead, Institute of Nuclear Medicine, UCL
# For internal research only.


import matplotlib.pyplot as plt

import sirf.Reg as reg


nifty_f3d_sym = reg.NiftyF3dSym()

nifty_f3d_sym.set_reference_image(reg.NiftiImageData3D("./ref.nii"))
nifty_f3d_sym.set_floating_image(reg.NiftiImageData3D("./flo.nii"))

nifty_f3d_sym.process()

nifty_f3d_sym.get_deformation_field_forward().write("./dvf.nii")

output_volume = nifty_f3d_sym.get_output()
output_volume.write("./output.nii")

plt.imshow(output_volume.as_array()[:, 100, :])
plt.savefig("./output.png")
