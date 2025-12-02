import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from data.image_folder import is_image_file, make_dataset  # noqa: E402


class ImageDiscoveryTests(unittest.TestCase):
    def test_extensions_are_case_insensitive_and_include_webp_and_tiff(self):
        for name in ("a.PNG", "b.WebP", "c.Tif", "d.TIFF", "e.jpeg"):
            self.assertTrue(is_image_file(name), name)
        self.assertFalse(is_image_file("notes.txt"))

    def test_missing_directory_raises_value_error(self):
        with self.assertRaises(ValueError):
            make_dataset(os.path.join(tempfile.gettempdir(), "revgan-does-not-exist"))

    def test_walk_is_deterministic(self):
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "b.PNG").write_bytes(b"x")
            Path(tmp, "a.WEBP").write_bytes(b"x")
            Path(tmp, "skip.txt").write_text("x", encoding="utf-8")
            names = [os.path.basename(p) for p in make_dataset(tmp)]
            self.assertEqual(names, ["a.WEBP", "b.PNG"])


if __name__ == "__main__":
    unittest.main()
