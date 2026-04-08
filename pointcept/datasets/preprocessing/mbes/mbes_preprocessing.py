from pathlib import Path
import numpy as np


src_path = Path(r"C:\Users\OWNER\Desktop\ptv3_testi\0_txt")
dst_path = Path(r"C:\Users\OWNER\Desktop\ptv3_testi\1_npy\train")

for index, point_cloud in enumerate(src_path.glob("*.txt")):
    point_cloud_data = np.loadtxt(point_cloud, delimiter=",")

    segment = point_cloud_data[:, 0].astype(np.int32)
    coord = point_cloud_data[:, 1:4].astype(np.float32)
    intensity = point_cloud_data[:, 4:5].astype(np.float32)
    line = point_cloud_data[:, 5].astype(np.int32)
    distance = point_cloud_data[:, 6:7].astype(np.float32)

    sample_path = dst_path / f"sample_{index}"
    sample_path.mkdir(parents=True, exist_ok=True)

    np.save(sample_path / "segment", segment)
    np.save(sample_path / "coord", coord)
    np.save(sample_path / "intensity", intensity)
    np.save(sample_path / "line", line)
    np.save(sample_path / "distance", distance)
