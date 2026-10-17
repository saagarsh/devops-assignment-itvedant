import unittest
import json
from main import Handler
from http.server import HTTPServer
from threading import Thread
from urllib.request import urlopen

class AppTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.url = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def test_home(self):
        with urlopen(self.url) as response:
            self.assertEqual(response.status, 200)
            self.assertEqual(
                json.load(response)["message"],
                "Hello from the DevOps assignment!"
            )

    def test_health(self):
        with urlopen(self.url + "/health") as response:
            self.assertEqual(
                json.load(response)["status"], "healthy"
            )

if __name__ == "__main__":
    unittest.main()
