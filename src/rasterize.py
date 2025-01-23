from raster_types import Raster_NxM_F, Triangle_F, RasterPoint_F
import numpy as np
import matplotlib.pyplot as plt


def triangle_area(
    point_a: RasterPoint_F, point_b: RasterPoint_F, point_c: RasterPoint_F
) -> np.float32:
    return (
        point_a[0] * (point_b[1] - point_c[1])
        + point_b[0] * (point_c[1] - point_a[1])
        + point_c[0] * (point_a[1] - point_b[1])
    )


def point_in_triangle_f(point: RasterPoint_F, triangle: Triangle_F) -> bool:
    """determine if a given point is inside a triangle"""

    area_ABC: np.float32 = triangle_area(triangle[0], triangle[1], triangle[2])

    area_PBC: np.float32 = triangle_area(point, triangle[1], triangle[2])
    area_PCA: np.float32 = triangle_area(point, triangle[2], triangle[0])
    area_PAB: np.float32 = triangle_area(point, triangle[0], triangle[1])

    sign_ABC = np.sign(area_ABC)
    return (
        np.sign(area_PBC) == sign_ABC
        and np.sign(area_PCA) == sign_ABC
        and np.sign(area_PAB) == sign_ABC
    )


def update_pixel_f(
    pixel: np.float32,
    factor: np.int32,
    point: RasterPoint_F,
    triangle: Triangle_F,
) -> np.float32:
    """add color to pixel if point is in the triangle"""
    sqr_factor: np.int32 = np.int32(np.floor(np.sqrt(factor)))
    div_factor: np.float32 = 1 / factor
    for i in range(sqr_factor):
        for j in range(sqr_factor):
            point_shift: RasterPoint_F = np.array(
                [i / sqr_factor, j / sqr_factor], dtype=np.float32
            )
            if point_in_triangle_f(point + point_shift, triangle):
                pixel += div_factor
    return pixel


def rasterize_f(
    image: Raster_NxM_F,
    triangle: Triangle_F,
    factor: np.int32 = 1,
) -> Raster_NxM_F:
    """Supersample and rasterize again for higher-quality rendering"""
    updated_image: Raster_NxM_F = np.array(image, dtype=np.float32)
    for i in range(len(updated_image)):
        for j in range(len(updated_image[i])):
            updated_image[j, i] = update_pixel_f(
                updated_image[j, i],
                factor,
                np.array([i, j], dtype=np.float32),
                triangle,
            )
    return updated_image


if __name__ == "__main__":
    triangle_vertices_1: Triangle_F = np.array(
        [[22, 61], [21, 77], [96, 66]], dtype=np.float32
    )
    triangle_vertices_2: Triangle_F = np.array(
        [[21, 20], [46, 75], [88, 68]], dtype=np.float32
    )
    triangle_vertices_3: Triangle_F = np.array(
        [[5, 33], [31, 75], [45, 24]], dtype=np.float32
    )
    triangle_vertices_4: Triangle_F = np.array(
        [[10, 10], [10, 90], [90, 50]], dtype=np.float32
    )

    # generate image frame
    frame: Raster_NxM_F = np.zeros((100, 100), dtype=np.float32)

    # Rasterize without supersampling
    image: Raster_NxM_F = rasterize_f(frame, triangle_vertices_4)
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Rasterized Triangle")
    plt.imshow(image, cmap="gray", vmin=0, vmax=1)

    # Rasterize with supersampling
    supersampled_image = rasterize_f(frame, triangle_vertices_4, factor=4)

    plt.subplot(1, 2, 2)
    plt.title("Supersampled Rasterized Triangle")
    plt.imshow(supersampled_image, cmap="gray", vmin=0, vmax=1)

    plt.show()
