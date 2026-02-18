# Datasets

RevGAN reads an image folder per split. `make_dataset` walks the directory in sorted order and keeps
files whose lower-cased extension is one of `.jpg .jpeg .png .ppm .bmp .webp .tif .tiff .npy`.

A missing directory is a `ValueError` naming the path, under normal and `python -O` runs alike, so a
typo cannot turn into an empty training set.

Pair the folders with the `--dataroot` option; the aligned and unaligned loaders expect the
`trainA/trainB/valA/valB` layout described in the README.
