# Student ID: 1952044
# Student name: Quach Dang Giang
# 13/5

import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_bkel1(self):
        input = Program(
    [
        ClassDecl(
            Id("Program"),
            [
                MethodDecl(
                    Static(),
                    Id("main"),
                    [],
                    Block([])
                ),
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        Id("myVar"),
                        StringType(),
                        StringLiteral("Hello World")
                    )
                ),
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        Id("myVar"),
                        IntType()
                    )
                )
            ]
        )
    ]
)
        expect = "Redeclared Attribute: myVar"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_bkel2(self):
        input = Program(
    [
        ClassDecl(
            Id("Program"),
            [
                MethodDecl(
                    Static(),
                    Id("main"),
                    [],
                    Block(
                        [
                            Assign(
                                Id("myVar"),
                                IntLiteral(10)
                            )
                        ]
                    )
                )
            ]
        )
    ]
)
        expect = "Undeclared Identifier: myVar"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_bkel3(self):
        input = Program(
    [
        ClassDecl(
            Id("Program"),
            [
                MethodDecl(
                    Static(),
                    Id("main"),
                    [],
                    Block([
                        ConstDecl(
                            Id("myVar"),
                            IntType(),
                            IntLiteral(5)
                        ),
                        Assign(
                            Id("myVar"),
                            IntLiteral(10)
                        )]
                    )
                )
            ]
        )
    ]
)
        expect = "Cannot Assign To Constant: AssignStmt(Id(myVar),IntLit(10))"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_bkel4(self):
        input = Program(
    [
        ClassDecl(
            Id("Program"),
            [
                MethodDecl(
                    Static(),
                    Id("main"),
                    [],
                    Block(
                        [
                            Break()
                        ]
                    )
                )
            ]
        )
    ]
)
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_bkel5(self):
        input = Program(
    [
        ClassDecl(
            Id("Program"),
            [
                MethodDecl(
                    Static(),
                    Id("main"),
                    [],
                    Block(
                        [
                            ConstDecl(
                                Id("myVar"),
                                IntType(),
                                FloatLiteral(1.2)
                            )
                        ]
                    )
                )
            ]
        )
    ]
)
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(myVar),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input,expect,404))

## TestNoEntry
    def test_1(self):
        input = """Class A{
            Var a:Int;
            }"""

        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_2(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 1;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_3(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 1;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_4(self):
        input = """Class B: Program{
            Var a: Int;
            main(){
                Self.a = 1;
                }
            }"""
        expect = "Undeclared Class: Program"
        self.assertTrue(TestChecker.test(input,expect,408))
    
    def test_5(self):
        input = """Class A{
            Var a: Int;
            Val b: Int;
            main(){
                Self.a = 1;
                }
            }"""
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_6(self):
        input = """Class A{
            Var a: Int;
            main(x,y,z: Int; x: String){
                Self.a = 1;
                }
            }"""
        expect = "Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_7(self):
        input = """Class A{
            Var a: Int;
            main(){
                Var a: String = "Inner Var";
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_8(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 1;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_9(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 1;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_10(self):
        input = """Class A{
            Var a:Int;
            }"""

        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_11(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 5;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_12(self):
        input = """Class A{
            main(){
                a = 1;
                }
            }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_13(self):
        input = """Class A{
            Var a: Int = 1;
            main(){
                Self.a = 1.5;
                }
            }"""
        expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Self(),Id(a)),FloatLit(1.5))"
        self.assertTrue(TestChecker.test(input,expect,417))
    
    def test_14(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 1;
                {
                    Self.a = 2;
                    {
                        Self.a = 3;
                    }
                }
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_15(self):
        input = """Class A{
            Val a: Int;
            main(){
                Self.a = 1;
                }
            }"""
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_16(self):
        input = """Class A{
            Val a: Int = 2;
            main(){
                Self.a = 1;
                }
            }"""
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(a)),IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_17(self):
        input = """Class A{
            Var b: Int;
            main(){
                Self.a = 1;
                }
            }
            Class B{
                Var a: A = New A();
                main(){
                    Self.a.b = 2;
                }
            }
                """
        expect = "Undeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_18(self):
        input = """Class A{
            Var a: Int = True;
            main(){
                Self.a = 1;
                }
            }"""
        expect = "Type Mismatch In Statement: AttributeDecl(Instance,VarDecl(Id(a),IntType,BooleanLit(True)))"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_19(self):
        input = """Class A{
            Val a:Int = 5.5;
            }"""

        expect = "Type Mismatch In Statement: AttributeDecl(Instance,ConstDecl(Id(a),IntType,FloatLit(5.5)))"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_20(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 5.5;
                }
            }"""
        expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Self(),Id(a)),FloatLit(5.5))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_21(self):
        input = """Class A{
            Var a: Int;
            Var b: Float = 5.5;
            main(){
                Self.a = Self.b;
                }
            }"""
        expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Self(),Id(a)),FieldAccess(Self(),Id(b)))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_22(self):
        input = """Class A{
            Var a: Int;
            main(){
                Var b: Float = 5.5;
                Self.a = b;
                }
            }"""
        expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Self(),Id(a)),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,426))
    
    def test_23(self):
        input = """Class A{
            Var a: Int;
            main(){
                Var b: Float = 5.5;
                Self.a = b;
                }
            }"""
        expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Self(),Id(a)),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_24(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 5;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_25(self):
        input = """Class A{
            Var a: Float;
            main(){
                Self.a = 1;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_26(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 1;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_27(self):
        input = """Class A{
            Var a: Int;
            method(){
                Self.a = 1;
            }}"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_28(self):
        input = """Class A{
            Var a:Int;
            $main(){}
            }
            Class B{
                main(){
                    A::$main();
}
                }"""

        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_29(self):
        input = """Class A{
            Var a: Int;
            $method(){}
            main(ba: Int){
                Foreach (ba In 1 .. 100 By 2){
                    A::$method();
                }
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_30(self):
        input = """Class A{}
            Class B: A{}
            Class C: B{}"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_31(self):
        input = """Class A{
            Var $cdef: Int;
            main(){
                A::$cdef = 1;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,435))
    
    def test_32(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 1;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_33(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 1;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_34(self):
        input = """Class A{
            Var a: Boolean;
            main(){
                Self.a = True;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_35(self):
        input = """Class A{
            Var a: Boolean;
            main(){
                Self.a = (1 == 2);
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_36(self):
        input = """Class C{
            Var a: Int;
            main(){
                Self.a = 9999 + (2-3);
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_37(self):
        input = """Class A{
            Var a:Int;
            }"""

        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_38(self):
        input = """
        Class Program {
            Val a : Int = 1;
            Val a: Int = 3;
            main(){}
        }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_39(self):
        input = """
        Class A{
            $method(x: String){
               Break;
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_40(self):
        input = """Class A{
            Var a: Int;
            main(){
                Break;
                }
            }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,444))
    
    def test_41(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 1;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_42(self):
        input = """
        Class Program {
            main(){}
            get(a : Int; b: Float; a: String){}
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_43(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 1;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_44(self):
        input = """
        Class Program {
            main(){}
            get(a: Int){
                Val a: String = "S";
            }
        }
        """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_45(self):
        input = """
        Class Program {
            mai(){
                Var a : Boolean = 1 == 2;
            }
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_46(self):
        input = """Class A{
            Var a:Int;
            }"""

        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_47(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 1;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_48(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 1;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_49(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.b = 1;
                }
            }"""
        expect = "Undeclared Attribute: b"
        self.assertTrue(TestChecker.test(input,expect,453))
    
    def test_50(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 1;
                {
                    Self.a = 2;
                    {
                        Self.a = 3;
                    }
                }
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_51(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 1;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_52(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 134765;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_53(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 4+2;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_54(self):
        input = """Class A{
            Var a: String;
            main(){
                Self.a = "Bruh";
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_55(self):
        input = """Class A{
            Var a:Int;
            }"""

        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_56(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 1;
                {
                    Self.a = 2;
                    {
                        Self.a = 3;
                    }
                }
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_57(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 1;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_58(self):
        input = """
        Class A{}
        Class A{}
        """
        expect = "Redeclared Class: A"
        self.assertTrue(TestChecker.test(input,expect,462))
    
    def test_59(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 1;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_60(self):
        input = """
        Class Program {
            main(){}
            get(a : Int; b: Float; a: String){}
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_61(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 1;
                {
                    Self.a = 2;
                    {
                        Self.a = 3;
                    }
                }
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_62(self):
        input = """
        Class Program {
            main(){}
            get(){}
            get(){}
        }
        """
        expect = "Redeclared Method: get"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_63(self):
        input = """Class A{
            Var $a: Int;
            main(){
                A::$a = 1;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_64(self):
        input = """
        Class Program {
            Val a : Int = 1;
            Val a : Int = 12;
        }
        """

        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_65(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 1;
                {
                    Self.a = 2;
                    {
                        Self.a = 3;
                    }
                }
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_66(self):
        input = """Class A{
            Var a,b,c,a: Int;
            main(){
                Self.a = 1;
                }
            }"""
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_67(self):
        input = """Class A{
            Var $a: Int;
            main(){
                A::$a = 3%4;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,471))
    
    def test_68(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 1;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_69(self):
        input = """Class A{
            Var $a: Boolean;
            main(){
                A::$a = "test" ==. "String";
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_70(self):
        input = """
        Class A{
            Var x: Int = 1;
            method(b: Int){
                Var y: Int = Self.x;
            }
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_71(self):
        input = """Class A{
            Var a: Int;
            main(a,b,c: Int){
                a = 1;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_72(self):
        input = """
        Class B{ Var $x: Int = 1; }
        Class A{
            Var x: Int = 1;
            method(b: Int){ Var y: Int = Self.x + A::$x; }
        }
        """
        expect = "Undeclared Attribute: $x"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_73(self):
        input = """Class A{
            Var a:Int;
            }"""

        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_74(self):
        input = """
        Class B{ Var x: Int = 1; }
        Class A{
            Var x: Int = 1;
            method(b: Int){
                Var y: Int = B::$x;
            }
        }
        """
        expect = "Undeclared Attribute: $x"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_75(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 1;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_76(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 1;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,480))
    
    def test_77(self):
        input = """Class A{
            main(a,b,c,d: Float){
                a=b;
                b=c;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_78(self):
        input = """Class A{
            Var a: String;
            main(){
                Self.a = "No ENtry";
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_79(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 1-5-4-3;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_80(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 2341;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_81(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 2;
                {
                    Self.a = 23;
                    {
                        Self.a = 3;
                    }
                }
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_82(self):
        input = """Class A{
            Var a: A = New A();
            }"""

        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_83(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 1%4;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_84(self):
        input = """Class A{
            Var a: Float;
            main(){
                Self.a = 1+3.5;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_85(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 23/6%4;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,489))
    
    def test_86(self):
        input = """Class A{
            Var a: Boolean;
            main(){
                Self.a = "Hello" ==. "World";
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_87(self):
        input = """Class A{
            Var a: Float;
            main(){
               Self.a = 123;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_88(self):
        input = """
        Class Program {
            main(){}
            get(a: Int){}
            get(){}
        }
        """
        expect = "Redeclared Method: get"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_89(self):
        input = """Class A{
            Var a: String;
            main(){
                Self.a = "Hello" +. "World";
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_90(self):
        input = """Class A{
            Var a: Boolean;
            main(){
                Self.a = True && False || False;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_91(self):
        input = """Class A{
            Var a: Float;
            }"""

        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_92(self):
        input = """Class A{
            Var a: Int;
            main(){
                Self.a = 1*5;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_93(self):
        input = """Class A{
            Var a: Int = 5;
            main(){
                Self.a = 2+3*4-5;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_94(self):
        input = """Class A{
            Var $a: Int;
            main(){
                Self.a = 1;
                }
            }"""
        expect = "Undeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,498))
    
    def test_95(self):
        input = """Class A{
            Var a: Float;
            main(){
                Self.a = 2+3.5;
                }
            }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,499))

 