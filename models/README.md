# Models

`models/` builds the networks from the `--model` flag. The reversible memory-saving path lives in
`memcnn/`; `--use_naive` turns it off for comparison runs.

Adding a model means one file here plus the factory registration in `models/__init__.py`.
