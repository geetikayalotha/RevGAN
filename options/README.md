# Options

`base_options.py` declares the shared flags; `train_options.py` and `test_options.py` add the mode
specific ones. Every flag is printed at startup unless `--mute_optprint` is passed, and the parsed
options are saved next to the checkpoints so a run can be reproduced.

`--gpu_ids` accepts a comma list (`0,1`), a single id, or `-1` for CPU.
