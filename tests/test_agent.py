import unittest
from agents.agent import DarwinAgent

class TestDarwinAgent(unittest.TestCase):
    def test_initialization(self):
        agent = DarwinAgent(id="test", attribution_model=None, bo_controller=None, memory_graph=None)
        self.assertEqual(agent.id, "test")
        self.assertIsNone(agent.model)

if __name__ == '__main__':
    unittest.main()
