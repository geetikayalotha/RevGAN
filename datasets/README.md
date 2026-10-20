# Dataset helpers

`combine_A_and_B.py` builds paired training data from two folders. `download_cyclegan_dataset.sh` and
`download_pix2pix_dataset.sh` fetch the public datasets, and `make_dataset_aligned.py` produces the
aligned layout. Output belongs in `datasets/<name>` and stays out of git.

The loader itself (see `docs/datasets.md`) walks each split in sorted order and accepts the
lower-cased extensions `.jpg .jpeg .png .ppm .bmp .webp .tif .tiff .npy`.
