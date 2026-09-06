# test_trackbeacon.py
"""
Tests for TrackBeacon module.
"""

import unittest
from trackbeacon import TrackBeacon

class TestTrackBeacon(unittest.TestCase):
    """Test cases for TrackBeacon class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TrackBeacon()
        self.assertIsInstance(instance, TrackBeacon)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TrackBeacon()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
