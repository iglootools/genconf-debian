"""
   Copyright 2011 Sami Dalouche

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import unittest
from tests.genconftests import samples

class ManifestTestCase(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
    
    def test_should_get_all_concrete_profiles(self):
        assert set([p.name for p in samples.simple_manifest.concrete_profiles()]) == set(["development"]) 
    
    def test_should_have_project(self):
        assert samples.simple_manifest.project == 'simple'
    
    
    

