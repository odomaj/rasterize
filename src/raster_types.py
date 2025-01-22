from typing import Annotated, Literal, Tuple
import numpy as np

Raster_NxM_F = Annotated[
    np.typing.NDArray[np.float32],
    Literal["N", "M"],
]

Raster_RGB_NxM_F = Annotated[
    np.typing.NDArray[np.float32],
    Literal["N", "M", 3],
]

Raster_NxM_I = Annotated[
    np.typing.NDArray[np.uint8],
    Literal["N", "M"],
]

Raster_RGB_NxM_I = Annotated[
    np.typing.NDArray[np.uint8],
    Literal["N", "M", 3],
]

RasterPoint_F = Annotated[np.typing.NDArray[np.float32], Literal[2]]

Triangle_F = Annotated[np.typing.NDArray[np.float32], Literal[3, 2]]
