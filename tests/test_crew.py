import unittest
from unittest.mock import patch
from nocc_fullstack_stacks_supabase.crew import NoccFullstackStacksSupabaseCrew

class TestNoccFullstackStacksSupabaseCrew(unittest.TestCase):
    def setUp(self):
        self.crew = NoccFullstackStacksSupabaseCrew()

    def test_crew_initialization(self):
        self.assertIsNotNone(self.crew)
        self.assertEqual(len(self.crew.agents), 5)  # Assuming 5 agents as per the configuration
        self.assertEqual(len(self.crew.tasks), 5)  # Assuming 5 tasks as per the configuration

    @patch('nocc_fullstack_stacks_supabase.crew.Crew.kickoff')
    def test_crew_kickoff(self, mock_kickoff):
        mock_kickoff.return_value = "Mocked crew result"
        result = self.crew.crew().kickoff(inputs={'topic': 'Test Topic'})
        self.assertEqual(result, "Mocked crew result")
        mock_kickoff.assert_called_once_with(inputs={'topic': 'Test Topic'})

if __name__ == '__main__':
    unittest.main()