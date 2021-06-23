# Copyright University College London 2021
# Author: Alexander Whitehead, Institute of Nuclear Medicine, UCL
# For internal research only.


import math
import numpy as np
import matplotlib.pyplot as plt

import sirf.Reg as reg


nifty_f3d_sym = reg.NiftyF3dSym()

ref = reg.NiftiImageData3D("./ref.nii")
ref.crop([1, -1, -1], [-1, -1, -1])

flo = reg.NiftiImageData3D("./flo.nii")
flo.crop([1, -1, -1], [-1, -1, -1])

nifty_f3d_sym.set_reference_image(ref)
nifty_f3d_sym.set_floating_image(flo)

nifty_f3d_sym.process()

resampler = reg.NiftyResample()

dvf = nifty_f3d_sym.get_deformation_field_forward()
dvf.write("./dvf.nii")

dvf = reg.NiftiImageData3DDeformation.compose_single_deformation([dvf, reg.AffineTransformation(np.asarray([[math.cos(math.radians(180.0)),  0.0, math.sin(math.radians(180.0)),  0.0],
                                                                                                            [0.0,                            1.0, 0.0,                            0.0],
                                                                                                            [-math.sin(math.radians(180.0)), 0.0, math.cos(math.radians(180.0)),  -220.0],
                                                                                                            [0.0,                            0.0, 0.0,                            1.0]])).get_as_deformation_field(ref)], ref)

resampler.set_reference_image(ref)
resampler.set_floating_image(flo)
resampler.add_transformation(dvf)

resampler.set_interpolation_type_to_cubic_spline()

output_volume = resampler.forward(flo)
output_volume.write("./output.nii")

plt.imshow(output_volume.as_array()[:, 100, :])
plt.savefig("./output.png")
