from defaults import DefaultDataset
from builder import DATASETS


@DATASETS.register_module()
class MBESDataset(DefaultDataset):
    VALID_ASSETS = ["segment", "coord", "intensity", "line", "distance"]

    def __init__(self):
        super().__init__()

