# Student ID: 1952044
# Student name: Quach Dang Giang

import unittest
from TestUtils import TestChecker
from TestUtils import TestAST
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_25(self):
        input = """
        Class B{
            Var x: String = "Hello";
            Val y: String = "HMM"
        }
        Class A{
            Var a: Float;
            main(){
                Self.a = 4;
            }
        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,1))