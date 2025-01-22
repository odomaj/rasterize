from raster_types import Raster_NxM_F, Triangle
import numpy as np
import matplotlib.pyplot as plt


def supersample_rasterization(
    image: Raster_NxM_F,
    triangle: Triangle,
    factor: np.int32 = 1,
) -> Raster_NxM_F:
    """Supersample and rasterize again for higher-quality rendering"""
    return image


def rasterization(
    image: Raster_NxM_F,
    triangle: Triangle,
) -> Raster_NxM_F:
    """Rasterize the triangle using barycentric coordinates"""
    return supersample_rasterization(image, triangle)


if __name__ == "__main__":
    triangle_vertices_1: Triangle = np.array(
        [[22, 61], [21, 77], [96, 66]], dtype=np.float32
    )
    triangle_vertices_2: Triangle = np.array(
        [[21, 20], [46, 75], [88, 68]], dtype=np.float32
    )
    triangle_vertices_3: Triangle = np.array(
        [[5, 33], [31, 75], [45, 24]], dtype=np.float32
    )
    triangle_vertices_4: Triangle = np.array(
        [[10, 10], [10, 90], [90, 50]], dtype=np.float32
    )

    # generate image frame
    frame: Raster_NxM_F = np.zeros((100, 100), dtype=np.float32)

    # Rasterize without supersampling
    image: Raster_NxM_F = rasterization(frame, triangle_vertices_1)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Rasterized Triangle")
    plt.imshow(image, cmap="gray")

    # Rasterize with supersampling
    supersampled_image = supersample_rasterization(
        frame, triangle_vertices_1, factor=4
    )

    plt.subplot(1, 2, 2)
    plt.title("Supersampled Rasterized Triangle")
    plt.imshow(supersampled_image, cmap="gray")

    plt.show()
