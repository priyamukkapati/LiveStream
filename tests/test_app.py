import importlib.util
import pathlib
import unittest


def load(name):
    path = pathlib.Path(__file__).resolve().parents[1] / "app.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ProjectTests(unittest.TestCase):
    def test_chat_delivery_moderation_and_backpressure(self):
        room = load("livestream").Community()
        host = room.join("coding", "host")
        viewer = room.join("coding", "viewer")
        for i in range(105):
            room.publish("coding", "host", str(i))
        self.assertEqual(viewer.qsize(), 100)
        self.assertEqual(viewer.get_nowait()["text"], "5")
        room.ban("viewer")
        with self.assertRaises(ValueError):
            room.publish("coding", "viewer", "hello")
        self.assertEqual(host.qsize(), 100)

