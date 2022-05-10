# Student ID: 1952044
# Student name: Quach Dang Giang

import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_bkel1(self):
        """Simple program: int main() {} """
        input = """Class Program {}"""
        expect = "Program([ClassDecl(Id(Program),[])])"
        self.assertTrue(TestAST.test(input,expect,396))

    def test_bkel2(self):
        """More complex program"""
        input = """Class Rectangle : Shape {}"""
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[])])"
        self.assertTrue(TestAST.test(input,expect,397))
    
    def test_bkel3(self):
        """More complex program"""
        input = """Class Rectangle {
    Var length: Int;
}"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(length),IntType))])])"
        self.assertTrue(TestAST.test(input,expect,398))

    def test_bkel4(self):
        """More complex program"""
        input = """Class Rectangle {
        Val $x: Int = 10;
}"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(10)))])])"
        self.assertTrue(TestAST.test(input,expect,399))


    def test_bkel5 (self):
        input = """
        Class main{}
        """
        output = """Program([ClassDecl(Id(main),[])])"""
        num = 393
        self.assertTrue(TestAST.test(input,output,num))  
    def test_bkel6 (self):
        input = """
Class Rectangle: Shape {
    getArea() {
        Return Self.length * Self.width;
    }
}
"""
        output = """Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"""
        num = 394
        self.assertTrue(TestAST.test(input,output,num))  
    def test_bkel7 (self):
        input = """
    Class Shape {
        $getNumOfShape() {
            Return Self.length * Self.width;
        }
    }
"""
        output = """Program([ClassDecl(Id(Shape),[MethodDecl(Id($getNumOfShape),Static,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"""
        num = 395
        self.assertTrue(TestAST.test(input,output,num))

    def test_type(self):
        input = """
        Class Child {
            foo_method(a:Int;b:Boolean;c:String){}
            }
        """
        expect = 'Program([ClassDecl(Id(Child),[MethodDecl(Id(foo_method),Instance,[param(Id(a),IntType),param(Id(b),BoolType),param(Id(c),StringType)],Block([]))])])' 

        self.assertTrue(TestAST.test(input,expect,391))

    def test_type2(self):
        input = """
        Class A {
            foo(a:Int;b:Boolean;c:String){
                Var d:abc;
                Var e:String = "abc";
            }
            }"""
        expect = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(b),BoolType),param(Id(c),StringType)],Block([VarDecl(Id(d),ClassType(Id(abc)),NullLiteral()),VarDecl(Id(e),StringType,StringLit(abc))]))])])"""
        self.assertTrue(TestAST.test(input,expect,300))

    def test_random_1(self):
        input = """Class Rectangle: Shape {
    Constructor(a,b: Int) {
        Self.length = a;
        Self.width = b;
    }
}
        """
        output = "Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(length)),Id(a)),AssignStmt(FieldAccess(Self(),Id(width)),Id(b))]))])])"
        self.assertTrue(TestAST.test(input,output,301))
   
    def test_random_2(self):
        input = """Class Rectangle: Shape {
            Constructor(a: Int) {
                Self.length = a;
                }
                }"""
        output = """Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(length)),Id(a))]))])])"""
        self.assertTrue(TestAST.test(input,output,302))

    def test_random_3(self):
        input = """Class Rectangle: Shape {
            Destructor() {
                Self.print(area);
                }
                }"""
        output = """Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(Destructor),Instance,[],Block([Call(Self(),Id(print),[Id(area)])]))])])"""
        self.assertTrue(TestAST.test(input,output,303))

    def test_random_4(self):
        input = """
       Class A {
           Var a:Int;
           Var b:Int;
       }
       """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType))])])'
        self.assertTrue(TestAST.test(input,expect,304))

    def test_random_5(self):
        input = """
       Class A {
           Var a:Int;
           Var b:Int;
           }
           """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType))])])'
        self.assertTrue(TestAST.test(input,expect,305))

    def test_random_6(self):
        input = """
       Class A {
           Var a:Int;
           Var b:Int;
           }
           """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType))])])'
        self.assertTrue(TestAST.test(input,expect,306))

    def test_random_7(self):
        input = """
       Class A {
           Var a:Int;
           Var b:Int;
           }
           """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType))])])'
        self.assertTrue(TestAST.test(input,expect,307))

    def test_random_8(self):
        input = """
       Class A {
           Var a:Int;
           Var b:Int;
           }
           """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType))])])'
        self.assertTrue(TestAST.test(input,expect,308))

    def test_random_9(self):
        input = """
       Class A {
           Var a:Int;
           Var b:Int;
           }
           """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType))])])'
        self.assertTrue(TestAST.test(input,expect,309))

    def test_random_10(self):
        input = """
       Class A {
           Var a:Int;
           Var b:Int;
           }
           """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType))])])'
        self.assertTrue(TestAST.test(input,expect,392))

    def test_0(self):
        input = """Class Programm {
        main() {
            Out.printInt(Shape::$numOfShape);
        }
    }
"""
        output = """Program([ClassDecl(Id(Programm),[MethodDecl(Id(main),Instance,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))])]))])])"""
        num = 310
        self.assertTrue(TestAST.test(input,output,num)) 

    def test_1(self):
        input = """Class Shape {
Val $numOfShape: Int = 0;
Val immutableAttribute: Int = 0;
Var length, width: Int;
$getNumOfShape() {
Return $numOfShape;
}
}
"""
        output = """Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(Id($numOfShape))]))])])"""
        num = 311
        self.assertTrue(TestAST.test(input,output,num)) 
    def test_2(self):
        input = """Class Rectangle: Shape {
getArea() {
Return Self.length * Self.width;
} }
"""
        output = """Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"""
        num = 312
        self.assertTrue(TestAST.test(input,output,num)) 

    def test_3(self):
        input = """Class Program {
main() {
Out.printInt(Shape::$numOfShape);
} }
"""
        output = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))])]))])])"""
        num = 313
        self.assertTrue(TestAST.test(input,output,num)) 

    def test_4(self):
        input = """Class Programm {
        main() {
            Out.printInt(Shape::$numOfShape);
        }
    }
"""
        output = """Program([ClassDecl(Id(Programm),[MethodDecl(Id(main),Instance,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))])]))])])"""
        num = 314
        self.assertTrue(TestAST.test(input,output,num)) 

    def test_5(self):
        input = """Class Rectangle: Shape {
    getArea() {
        Return Self.length * Self.width;
    }

    Val a: Int;
}
"""
        output = """Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))])),AttributeDecl(Instance,ConstDecl(Id(a),IntType,None))])])"""
        num = 315
        self.assertTrue(TestAST.test(input,output,num)) 

    def test_6(self):
        input = """Class Parent{
    Val a: Int;
    Constructor(){a = 5;}
}
"""
        output = """Program([ClassDecl(Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(Id(a),IntLit(5))]))])])"""
        num = 316 
        self.assertTrue(TestAST.test(input,output,num)) 

    def test_7(self):
        input = """Class Parent{
            Val a: Int;
            getA(){
                Return Self.a;
            }
            Constructor(){
                a=5;
            }
        }
"""
        output = """Program([ClassDecl(Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),MethodDecl(Id(getA),Instance,[],Block([Return(FieldAccess(Self(),Id(a)))])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(Id(a),IntLit(5))]))])])"""
        num = 317 
        self.assertTrue(TestAST.test(input,output,num)) 

    def test_8(self):
        input = """Class Parent{
            Val a: Int;
            Var $b, $c: Int = 1 + 6, 2;
            getA(){
                Return Self.a;
            }
            getBplusC(){
                Return Self.b + Self.c;
            }
            Constructor(){
                a=5;
            }
        }
"""
        output = """Program([ClassDecl(Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Static,VarDecl(Id($b),IntType,BinaryOp(+,IntLit(1),IntLit(6)))),AttributeDecl(Static,VarDecl(Id($c),IntType,IntLit(2))),MethodDecl(Id(getA),Instance,[],Block([Return(FieldAccess(Self(),Id(a)))])),MethodDecl(Id(getBplusC),Instance,[],Block([Return(BinaryOp(+,FieldAccess(Self(),Id(b)),FieldAccess(Self(),Id(c))))])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(Id(a),IntLit(5))]))])])"""
        num = 318 
        self.assertTrue(TestAST.test(input,output,num)) 

    def test_9(self):
        input = """Class Parent{
            Val a: Int;
            Var $b, $c: Int = 1 + 6, 2;
            getA(){
                Return Self.a;
            }
            getBplusCplusD(D: Int){
                D = 5;
                Return Self.b + Self.c + D;
            }
            Constructor(){
                a=5;
            }
        }
"""
        output = """Program([ClassDecl(Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Static,VarDecl(Id($b),IntType,BinaryOp(+,IntLit(1),IntLit(6)))),AttributeDecl(Static,VarDecl(Id($c),IntType,IntLit(2))),MethodDecl(Id(getA),Instance,[],Block([Return(FieldAccess(Self(),Id(a)))])),MethodDecl(Id(getBplusCplusD),Instance,[param(Id(D),IntType)],Block([AssignStmt(Id(D),IntLit(5)),Return(BinaryOp(+,BinaryOp(+,FieldAccess(Self(),Id(b)),FieldAccess(Self(),Id(c))),Id(D)))])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(Id(a),IntLit(5))]))])])"""
        num = 319 
        self.assertTrue(TestAST.test(input,output,num)) 

    def test_10(self):
        input = """Class Parent{
            Val a: Int;
            Var $b, $c: Int = 1 + 6, 2;
            getA(){
                Return Self.a;
            }
            getBplusCplusD(D: Int){
                D = 5;
                Return Self.b + Self.c + D;
            }
            Constructor(){
                Self.a=5;
            }
        }
        Class Child: Parent{
            Val child: String;
            Constructor(){
                Self.child = "Child class";
            }
        }
"""
        output = """Program([ClassDecl(Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Static,VarDecl(Id($b),IntType,BinaryOp(+,IntLit(1),IntLit(6)))),AttributeDecl(Static,VarDecl(Id($c),IntType,IntLit(2))),MethodDecl(Id(getA),Instance,[],Block([Return(FieldAccess(Self(),Id(a)))])),MethodDecl(Id(getBplusCplusD),Instance,[param(Id(D),IntType)],Block([AssignStmt(Id(D),IntLit(5)),Return(BinaryOp(+,BinaryOp(+,FieldAccess(Self(),Id(b)),FieldAccess(Self(),Id(c))),Id(D)))])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(a)),IntLit(5))]))]),ClassDecl(Id(Child),Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(child),StringType,None)),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(child)),StringLit(Child class))]))])])"""
        num = 320
        self.assertTrue(TestAST.test(input,output,num)) 

    def test_11(self):
        input = """
        Class Parent{
            Val a: Int;
            Var $b, $c: Int = 1 + 6, 2;
            getA(){
                RandomClass.print();
            }
            getBplusCplusD(D: Int){
                D = 5;
                Return Self.b + Self.c + D;
            }
            Constructor(){
                Self.a=5;
            }
        }
        Class Child: Parent{
            Val child: String;
            Constructor(){
                Self.child = "Child class";
            }
        }
"""
        output = """Program([ClassDecl(Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Static,VarDecl(Id($b),IntType,BinaryOp(+,IntLit(1),IntLit(6)))),AttributeDecl(Static,VarDecl(Id($c),IntType,IntLit(2))),MethodDecl(Id(getA),Instance,[],Block([Call(Id(RandomClass),Id(print),[])])),MethodDecl(Id(getBplusCplusD),Instance,[param(Id(D),IntType)],Block([AssignStmt(Id(D),IntLit(5)),Return(BinaryOp(+,BinaryOp(+,FieldAccess(Self(),Id(b)),FieldAccess(Self(),Id(c))),Id(D)))])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(a)),IntLit(5))]))]),ClassDecl(Id(Child),Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(child),StringType,None)),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(child)),StringLit(Child class))]))])])"""
        self.assertTrue(TestAST.test(input,output,321)) 

    def test_12(self):
        input = """
        Class Parent{
            Val a: Int;
            Var $b, $c: Int = 1 + 6, 2;
            getRandom(){
                RandomClass.print();
            }
            getDoubleA(){
                RandomClass.print(a*a);
            }
            getBplusCplusD(D: Int){
                D = 5;
                Return Self.b + Self.c + D;
            }
            Constructor(){
                Self.a=5;
            }
        }
        Class Child: Parent{
            Val child: String;
            Constructor(){
                Self.child = "Child class";
            }
        }
"""
        output = """Program([ClassDecl(Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Static,VarDecl(Id($b),IntType,BinaryOp(+,IntLit(1),IntLit(6)))),AttributeDecl(Static,VarDecl(Id($c),IntType,IntLit(2))),MethodDecl(Id(getRandom),Instance,[],Block([Call(Id(RandomClass),Id(print),[])])),MethodDecl(Id(getDoubleA),Instance,[],Block([Call(Id(RandomClass),Id(print),[BinaryOp(*,Id(a),Id(a))])])),MethodDecl(Id(getBplusCplusD),Instance,[param(Id(D),IntType)],Block([AssignStmt(Id(D),IntLit(5)),Return(BinaryOp(+,BinaryOp(+,FieldAccess(Self(),Id(b)),FieldAccess(Self(),Id(c))),Id(D)))])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(a)),IntLit(5))]))]),ClassDecl(Id(Child),Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(child),StringType,None)),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(child)),StringLit(Child class))]))])])"""
        self.assertTrue(TestAST.test(input,output,322))
    def test_13(self):
        input = """
        Class Parent{
            Val a: Int;
            Var $b, $c: Int = 1 + 6, 2;
            getRandom(){
                RandomClass.print();
            }
            getDoubleA(){
                RandomClass.print(a*a);
            }
            getBplusCplusD(D: Int){
                D = 5;
                Return Self.b + Self.c + D;
            }
            Constructor(){
                Self.a=5;
            }
        }
        Class Child: Parent{
            Val child: String;
            $testStatic(str: String){
                str = "Hello";
                RandomClass.print(str);
            }
            Constructor(){
                Self.child = "Child class";
            }
        }
"""
        output = """Program([ClassDecl(Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Static,VarDecl(Id($b),IntType,BinaryOp(+,IntLit(1),IntLit(6)))),AttributeDecl(Static,VarDecl(Id($c),IntType,IntLit(2))),MethodDecl(Id(getRandom),Instance,[],Block([Call(Id(RandomClass),Id(print),[])])),MethodDecl(Id(getDoubleA),Instance,[],Block([Call(Id(RandomClass),Id(print),[BinaryOp(*,Id(a),Id(a))])])),MethodDecl(Id(getBplusCplusD),Instance,[param(Id(D),IntType)],Block([AssignStmt(Id(D),IntLit(5)),Return(BinaryOp(+,BinaryOp(+,FieldAccess(Self(),Id(b)),FieldAccess(Self(),Id(c))),Id(D)))])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(a)),IntLit(5))]))]),ClassDecl(Id(Child),Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(child),StringType,None)),MethodDecl(Id($testStatic),Static,[param(Id(str),StringType)],Block([AssignStmt(Id(str),StringLit(Hello)),Call(Id(RandomClass),Id(print),[Id(str)])])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(child)),StringLit(Child class))]))])])"""
        self.assertTrue(TestAST.test(input,output,323)) 

    def test_14(self):
        input = """
        Class Parent{
            Val a: Int;
            Var $b, $c: Int = 1 + 6, 2;
            getRandom(){
                RandomClass.print();
            }
            getDoubleA(){
                RandomClass.print(a*a);
            }
            getBplusCplusD(D: Int){
                D = 5;
                Return Self.b + Self.c + D;
            }
            Constructor(){
                Self.a=5;
            }
        }
        Class Child: Parent{
            Val child: String;
            $testStatic(str: String){
                str = "Hello";
                RandomClass.print(str);
            }
            Val My1stCons, My2ndCons: Int = 1 + 5, 2;
            Var $x, $y : Int = 0, 0;
            Constructor(){
                Self.child = "Child class";
            }
        }
"""
        output = """Program([ClassDecl(Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Static,VarDecl(Id($b),IntType,BinaryOp(+,IntLit(1),IntLit(6)))),AttributeDecl(Static,VarDecl(Id($c),IntType,IntLit(2))),MethodDecl(Id(getRandom),Instance,[],Block([Call(Id(RandomClass),Id(print),[])])),MethodDecl(Id(getDoubleA),Instance,[],Block([Call(Id(RandomClass),Id(print),[BinaryOp(*,Id(a),Id(a))])])),MethodDecl(Id(getBplusCplusD),Instance,[param(Id(D),IntType)],Block([AssignStmt(Id(D),IntLit(5)),Return(BinaryOp(+,BinaryOp(+,FieldAccess(Self(),Id(b)),FieldAccess(Self(),Id(c))),Id(D)))])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(a)),IntLit(5))]))]),ClassDecl(Id(Child),Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(child),StringType,None)),MethodDecl(Id($testStatic),Static,[param(Id(str),StringType)],Block([AssignStmt(Id(str),StringLit(Hello)),Call(Id(RandomClass),Id(print),[Id(str)])])),AttributeDecl(Instance,ConstDecl(Id(My1stCons),IntType,BinaryOp(+,IntLit(1),IntLit(5)))),AttributeDecl(Instance,ConstDecl(Id(My2ndCons),IntType,IntLit(2))),AttributeDecl(Static,VarDecl(Id($x),IntType,IntLit(0))),AttributeDecl(Static,VarDecl(Id($y),IntType,IntLit(0))),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(child)),StringLit(Child class))]))])])""" 
        self.assertTrue(TestAST.test(input,output,324)) 

    def test_15(self):
        input = """
        Class Parent{
            Val a: Int;
            Var $b, $c: Int = 1 + 6, 2;
            getRandom(){
                RandomClass.print();
            }
            getDoubleA(){
                RandomClass.print(a*a);
            }
            getBplusCplusD(D: Int){
                D = 5;
                Return Self.b + Self.c + D;
            }
            Constructor(){
                Self.a=5;
            }
        }
        Class Child: Parent{
            Val child: String;
            $testStatic(str: String){
                str = "Hello";
                RandomClass.print(str);
            }
            Val My1stCons, My2ndCons: Int = 1 + 5, 2;
            Var $x, $y : Int = 0, 0;
            Constructor(){
                Self.child = "Child class";
            }
            printChild(){
                Foreach (i In 1 .. 100 By 1){
                    Out.print(Self.child);
                }
            }
        }
"""
        output = """Program([ClassDecl(Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Static,VarDecl(Id($b),IntType,BinaryOp(+,IntLit(1),IntLit(6)))),AttributeDecl(Static,VarDecl(Id($c),IntType,IntLit(2))),MethodDecl(Id(getRandom),Instance,[],Block([Call(Id(RandomClass),Id(print),[])])),MethodDecl(Id(getDoubleA),Instance,[],Block([Call(Id(RandomClass),Id(print),[BinaryOp(*,Id(a),Id(a))])])),MethodDecl(Id(getBplusCplusD),Instance,[param(Id(D),IntType)],Block([AssignStmt(Id(D),IntLit(5)),Return(BinaryOp(+,BinaryOp(+,FieldAccess(Self(),Id(b)),FieldAccess(Self(),Id(c))),Id(D)))])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(a)),IntLit(5))]))]),ClassDecl(Id(Child),Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(child),StringType,None)),MethodDecl(Id($testStatic),Static,[param(Id(str),StringType)],Block([AssignStmt(Id(str),StringLit(Hello)),Call(Id(RandomClass),Id(print),[Id(str)])])),AttributeDecl(Instance,ConstDecl(Id(My1stCons),IntType,BinaryOp(+,IntLit(1),IntLit(5)))),AttributeDecl(Instance,ConstDecl(Id(My2ndCons),IntType,IntLit(2))),AttributeDecl(Static,VarDecl(Id($x),IntType,IntLit(0))),AttributeDecl(Static,VarDecl(Id($y),IntType,IntLit(0))),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(child)),StringLit(Child class))])),MethodDecl(Id(printChild),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([Call(Id(Out),Id(print),[FieldAccess(Self(),Id(child))])])])]))])])"""
        self.assertTrue(TestAST.test(input,output,325)) 

    def test_16(self):
        input = """        
        Class Child: Parent{
            Val child: String;
            foreach_test(){
                Foreach (i In 1 .. 100 By 1){
                    Out.print(Self.child);
                }
            }
        }
"""
        output = """Program([ClassDecl(Id(Child),Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(child),StringType,None)),MethodDecl(Id(foreach_test),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([Call(Id(Out),Id(print),[FieldAccess(Self(),Id(child))])])])]))])])"""
        self.assertTrue(TestAST.test(input,output,326)) 

    def test_17(self):
        input = """        
        Class Child: Parent{
            Val child: String;
            foreach_test(){
                Foreach (i In 1 .. 100 By 2){
                    Out.print(arr[x]);
                }
            }
        }
"""
        output = """Program([ClassDecl(Id(Child),Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(child),StringType,None)),MethodDecl(Id(foreach_test),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(print),[ArrayCell(Id(arr),[Id(x)])])])])]))])])"""
        self.assertTrue(TestAST.test(input,output,327)) 

    def test_18(self):
        input = """  Class France:Rec{
                         Drawing(k,d,f: Int; k: String){
                             If (k.s == f.j){
                                 Break ;
                             }
                             Elseif (o.m() != x::$mj(3,4,5)){
                                 Break;
                             }
                             Else {
                                 Return nothing;
                             }
                         }
        }
                   """
        output = """Program([ClassDecl(Id(France),Id(Rec),[MethodDecl(Id(Drawing),Instance,[param(Id(k),IntType),param(Id(d),IntType),param(Id(f),IntType),param(Id(k),StringType)],Block([If(BinaryOp(==,FieldAccess(Id(k),Id(s)),FieldAccess(Id(f),Id(j))),Block([Break]),If(BinaryOp(!=,CallExpr(Id(o),Id(m),[]),CallExpr(Id(x),Id($mj),[IntLit(3),IntLit(4),IntLit(5)])),Block([Break]),Block([Return(Id(nothing))])))]))])])"""
        self.assertTrue(TestAST.test(input,output,328)) 

    def test_19(self):
        input = """        
        Class Child: Parent{
            Val child: String;
            foreach_test(){
                Foreach (i In 1 .. 5 By 2){
                    Out.print(arr[x]);
                }
            }
        }
"""
        output = """Program([ClassDecl(Id(Child),Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(child),StringType,None)),MethodDecl(Id(foreach_test),Instance,[],Block([For(Id(i),IntLit(1),IntLit(5),IntLit(2),Block([Call(Id(Out),Id(print),[ArrayCell(Id(arr),[Id(x)])])])])]))])])""" 
        self.assertTrue(TestAST.test(input,output,329)) 

    def test_20(self):
        input = """Class Programm {
        Val child: String;
        foreach_test(){
            Foreach (i In 2 .. 3 By 4){
                Out.print(arr[x]);
            }
        }
    }
"""
        output = """Program([ClassDecl(Id(Programm),[AttributeDecl(Instance,ConstDecl(Id(child),StringType,None)),MethodDecl(Id(foreach_test),Instance,[],Block([For(Id(i),IntLit(2),IntLit(3),IntLit(4),Block([Call(Id(Out),Id(print),[ArrayCell(Id(arr),[Id(x)])])])])]))])])"""
        self.assertTrue(TestAST.test(input,output,330)) 

    def test_21(self):
        input = """        
        Class Child: Parent{
            Val child: String;
            if_test(){
                If (a == 5){
                    out.print("Bruh");
                }
            }
        }
"""
        output = """Program([ClassDecl(Id(Child),Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(child),StringType,None)),MethodDecl(Id(if_test),Instance,[],Block([If(BinaryOp(==,Id(a),IntLit(5)),Block([Call(Id(out),Id(print),[StringLit(Bruh)])]))]))])])"""
        self.assertTrue(TestAST.test(input,output,331)) 

    def test_22(self):
        input = """  Class test {
                             Val $f,$t,$_j : String = True, False, 98 ;
                              nn(){
                                  print.out();
                              }
                     } 
                    """
        output = """Program([ClassDecl(Id(test),[AttributeDecl(Static,ConstDecl(Id($f),StringType,BooleanLit(True))),AttributeDecl(Static,ConstDecl(Id($t),StringType,BooleanLit(False))),AttributeDecl(Static,ConstDecl(Id($_j),StringType,IntLit(98))),MethodDecl(Id(nn),Instance,[],Block([Call(Id(print),Id(out),[])]))])])"""
        self.assertTrue(TestAST.test(input,output,332)) 
    def test_23(self):
        input = """Class IP  {
                          Val g : Int ;
                          Var o,l,j : String = "as\t" , "ion'"" , "3172" ;
                    }
"""
        output = """Program([ClassDecl(Id(IP),[AttributeDecl(Instance,ConstDecl(Id(g),IntType,None)),AttributeDecl(Instance,VarDecl(Id(o),StringType,StringLit(as	))),AttributeDecl(Instance,VarDecl(Id(l),StringType,StringLit(ion'"))),AttributeDecl(Instance,VarDecl(Id(j),StringType,StringLit(3172)))])])"""
        self.assertTrue(TestAST.test(input,output,333)) 

    def test_24(self):
        input = """        
        Class Child: Parent{
            Val i: Int;
            if_test(){
                If (i*2 == 5){
                    out.print("Bruh2");
                }
            }
        }
"""
        output = """Program([ClassDecl(Id(Child),Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(i),IntType,None)),MethodDecl(Id(if_test),Instance,[],Block([If(BinaryOp(==,BinaryOp(*,Id(i),IntLit(2)),IntLit(5)),Block([Call(Id(out),Id(print),[StringLit(Bruh2)])]))]))])])""" 
        self.assertTrue(TestAST.test(input,output,334)) 

    def test_25(self):
        input = """        
        Class Child: Parent{
            Val i: Int;
            if_test(){
                If ((i+3)/2 == 5){
                    out.print("Bruh2");
                }
            }
        }
"""
        output = """Program([ClassDecl(Id(Child),Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(i),IntType,None)),MethodDecl(Id(if_test),Instance,[],Block([If(BinaryOp(==,BinaryOp(/,BinaryOp(+,Id(i),IntLit(3)),IntLit(2)),IntLit(5)),Block([Call(Id(out),Id(print),[StringLit(Bruh2)])]))]))])])"""
        self.assertTrue(TestAST.test(input,output,335)) 

    def test_26(self):
        input = """        
        Class Child: Parent{
            Val i: Int;
            if_test(){
                If ((i+3)/2 == 5){
                    out.print("Bruh2");
                }
                Elseif (i%2 != 0){
                    out.print("Elseif");
                }
            }
        }
"""
        output = """Program([ClassDecl(Id(Child),Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(i),IntType,None)),MethodDecl(Id(if_test),Instance,[],Block([If(BinaryOp(==,BinaryOp(/,BinaryOp(+,Id(i),IntLit(3)),IntLit(2)),IntLit(5)),Block([Call(Id(out),Id(print),[StringLit(Bruh2)])]),If(BinaryOp(!=,BinaryOp(%,Id(i),IntLit(2)),IntLit(0)),Block([Call(Id(out),Id(print),[StringLit(Elseif)])])))]))])])"""
        self.assertTrue(TestAST.test(input,output,336)) 

    def test_27(self):
        input = """        
        Class Child: Parent{
            Val i: Int;
            if_test(){
                If ((i+3)/2 == 5){
                    out.print("Bruh2");
                }
                Elseif (i%2 != 0){
                    out.print("Elseif");
                }
                Else{
                    out.print("Bruh3");
                    Return 0;
                }
            }
        }
"""
        output = """Program([ClassDecl(Id(Child),Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(i),IntType,None)),MethodDecl(Id(if_test),Instance,[],Block([If(BinaryOp(==,BinaryOp(/,BinaryOp(+,Id(i),IntLit(3)),IntLit(2)),IntLit(5)),Block([Call(Id(out),Id(print),[StringLit(Bruh2)])]),If(BinaryOp(!=,BinaryOp(%,Id(i),IntLit(2)),IntLit(0)),Block([Call(Id(out),Id(print),[StringLit(Elseif)])]),Block([Call(Id(out),Id(print),[StringLit(Bruh3)]),Return(IntLit(0))])))]))])])"""
        self.assertTrue(TestAST.test(input,output,337)) 

    def test_28(self):
        input = """        
        Class Child: Parent{
            Val i: Int;
            if_test(){
                If ((i+3)/2 == 5){
                    out.print("Bruh2");
                    Return 2;
                }
                Elseif (i%2 != 0){
                    out.print("Elseif");
                    Return 1;
                }
                Else{
                    out.print("Bruh3");
                    Return 0;
                }
            }
        }
"""
        output = """Program([ClassDecl(Id(Child),Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(i),IntType,None)),MethodDecl(Id(if_test),Instance,[],Block([If(BinaryOp(==,BinaryOp(/,BinaryOp(+,Id(i),IntLit(3)),IntLit(2)),IntLit(5)),Block([Call(Id(out),Id(print),[StringLit(Bruh2)]),Return(IntLit(2))]),If(BinaryOp(!=,BinaryOp(%,Id(i),IntLit(2)),IntLit(0)),Block([Call(Id(out),Id(print),[StringLit(Elseif)]),Return(IntLit(1))]),Block([Call(Id(out),Id(print),[StringLit(Bruh3)]),Return(IntLit(0))])))]))])])"""
        self.assertTrue(TestAST.test(input,output,338)) 

    def test_29(self):
        input = """        
        Class Child: Parent{
            Val i: Int;
            if_test(){
                If (Child.i == 5){
                    out.print("Bruh2");
                }
                Elseif (i%2 != 0){
                    out.print("Elseif");
                }
                Else{
                    out.print("Bruh3");
                    Return 0;
                }
            }
        }
"""
        output = """Program([ClassDecl(Id(Child),Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(i),IntType,None)),MethodDecl(Id(if_test),Instance,[],Block([If(BinaryOp(==,FieldAccess(Id(Child),Id(i)),IntLit(5)),Block([Call(Id(out),Id(print),[StringLit(Bruh2)])]),If(BinaryOp(!=,BinaryOp(%,Id(i),IntLit(2)),IntLit(0)),Block([Call(Id(out),Id(print),[StringLit(Elseif)])]),Block([Call(Id(out),Id(print),[StringLit(Bruh3)]),Return(IntLit(0))])))]))])])""" 
        self.assertTrue(TestAST.test(input,output,339)) 

    def test_30(self):
        input = """        
        Class Child: Parent{
            Val i: Int;
            if_test(){
                If (Self.i == 5){
                    out.print("Bruh2");
                }
                Elseif (i%2 != 0){
                    out.print("Elseif");
                }
                Else{
                    out.print("Bruh3");
                    Return 0;
                }
            }
        }
"""
        output = """Program([ClassDecl(Id(Child),Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(i),IntType,None)),MethodDecl(Id(if_test),Instance,[],Block([If(BinaryOp(==,FieldAccess(Self(),Id(i)),IntLit(5)),Block([Call(Id(out),Id(print),[StringLit(Bruh2)])]),If(BinaryOp(!=,BinaryOp(%,Id(i),IntLit(2)),IntLit(0)),Block([Call(Id(out),Id(print),[StringLit(Elseif)])]),Block([Call(Id(out),Id(print),[StringLit(Bruh3)]),Return(IntLit(0))])))]))])])"""
        self.assertTrue(TestAST.test(input,output,340)) 
    

    def test_31(self):
        input = """        
        Class A {
           Var $b:Float=6.3;
       }
"""
        output = """Program([ClassDecl(Id(A),[AttributeDecl(Static,VarDecl(Id($b),FloatType,FloatLit(6.3)))])])"""
        self.assertTrue(TestAST.test(input,output,341)) 

    def test_32(self):
        input = """  Class A {
           foo(){
               a.b.c="abc";
           }
       } 
                    """
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),StringLit(abc))]))])])"""
        self.assertTrue(TestAST.test(input,output,342)) 
    def test_33(self):
        input = """Class A {
           foo(){
               Break;
               Continue;
               Return a==.!b;
               {}
           }
       }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([Break,Continue,Return(BinaryOp(==.,Id(a),UnaryOp(!,Id(b)))),Block([])]))])])"""
        self.assertTrue(TestAST.test(input,output,343)) 

    def test_34(self):
        input = """        
Class Child:Par{
           Foo(){
               If(1){}
               If(2){}Else{}
               If(3){}Elseif(4){}Else{a=1;}
           }
       }
"""
        output = """Program([ClassDecl(Id(Child),Id(Par),[MethodDecl(Id(Foo),Instance,[],Block([If(IntLit(1),Block([])),If(IntLit(2),Block([]),Block([])),If(IntLit(3),Block([]),If(IntLit(4),Block([]),Block([AssignStmt(Id(a),IntLit(1))])))]))])])""" 
        self.assertTrue(TestAST.test(input,output,344)) 

    def test_35(self):
        input = """        
        Class Chi:Par{
           Foo(){
               If(1){}
           }
       }
"""
        output = """Program([ClassDecl(Id(Chi),Id(Par),[MethodDecl(Id(Foo),Instance,[],Block([If(IntLit(1),Block([]))]))])])"""
        self.assertTrue(TestAST.test(input,output,345)) 

    def test_36(self):
        input = """        
        Class Ex8n  {
                          E__(){
                              Var o : Int = (21+3)-(Self.ock) ;
                              Return b   ## random comment ##; 
                          }
                    }
"""
        output = """Program([ClassDecl(Id(Ex8n),[MethodDecl(Id(E__),Instance,[],Block([VarDecl(Id(o),IntType,BinaryOp(-,BinaryOp(+,IntLit(21),IntLit(3)),FieldAccess(Self(),Id(ock)))),Return(Id(b))]))])])"""
        self.assertTrue(TestAST.test(input,output,346)) 

    def test_37(self):
        input = """        
        Class son: _Child{
            Val a,c,b,d: Int;
            if_test(){
                If (a + b == c + d){
                    out.print("Bruh");
                }
            }
        }
"""
        output = """Program([ClassDecl(Id(son),Id(_Child),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(c),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(b),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(d),IntType,None)),MethodDecl(Id(if_test),Instance,[],Block([If(BinaryOp(==,BinaryOp(+,Id(a),Id(b)),BinaryOp(+,Id(c),Id(d))),Block([Call(Id(out),Id(print),[StringLit(Bruh)])]))]))])])"""
        self.assertTrue(TestAST.test(input,output,347)) 

    def test_38(self):
        input = """        
        Class son: _Child{
            Val asdss: String;
            if_test(){
                If (class::$asd +. Parent.asd ==. "String"){
                    out.print("Bruh");
                }
            }
        }
"""
        output = """Program([ClassDecl(Id(son),Id(_Child),[AttributeDecl(Instance,ConstDecl(Id(asdss),StringType,None)),MethodDecl(Id(if_test),Instance,[],Block([If(BinaryOp(==.,BinaryOp(+.,FieldAccess(Id(class),Id($asd)),FieldAccess(Id(Parent),Id(asd))),StringLit(String)),Block([Call(Id(out),Id(print),[StringLit(Bruh)])]))]))])])"""
        self.assertTrue(TestAST.test(input,output,348)) 

    def test_39(self):
        input = """        
        Class Parent{
            Val a: Int;
            getA(){
                Return a;
            }
            Constructor(){
                a=5_45467.43;
            }
        }
"""
        output = """Program([ClassDecl(Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),MethodDecl(Id(getA),Instance,[],Block([Return(Id(a))])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(Id(a),FloatLit(545467.43))]))])])""" 
        self.assertTrue(TestAST.test(input,output,349)) 

    def test_40(self):
        input = """        
        Class Child{
        test() {
            Out.printin(1);
            Out.print("Hello");
            Out.print(1.5);
            Return 5;
        }
    }
"""
        output = """Program([ClassDecl(Id(Child),[MethodDecl(Id(test),Instance,[],Block([Call(Id(Out),Id(printin),[IntLit(1)]),Call(Id(Out),Id(print),[StringLit(Hello)]),Call(Id(Out),Id(print),[FloatLit(1.5)]),Return(IntLit(5))]))])])"""
        self.assertTrue(TestAST.test(input,output,350)) 

    def test_51(self): 
        input = """        
        Class A{
            foo(){
                Return 071;
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([Return(IntLit(57))]))])])"""
        self.assertTrue(TestAST.test(input,output,351))

    def test_52(self): 
        input = """        
        Class A{
            foo(){
                Return 0xABC;
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([Return(IntLit(2748))]))])])"""
        self.assertTrue(TestAST.test(input,output,352))

    def test_53(self): 
        input = """        
        Class A{
            foo(){
                Return 0b1010100010101;
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([Return(IntLit(5397))]))])])"""
        self.assertTrue(TestAST.test(input,output,353))

    def test_54(self):
        input = """        
        Class A{
            foo(){
                Return .5e-2;
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([Return(FloatLit(0.005))]))])])"""
        self.assertTrue(TestAST.test(input,output,354))

    def test_55(self):
        input = """        
        Class A{
            foo(){
                Return 10e+2;
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([Return(FloatLit(1000.0))]))])])"""
        self.assertTrue(TestAST.test(input,output,355))

    def test_56(self):
        input = """        
        Class A{
            foo(){
                Return 15e-2;
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([Return(FloatLit(0.15))]))])])"""
        self.assertTrue(TestAST.test(input,output,356))

    def test_57(self):
        input = """        
        Class A{
            foo(){
                Return 1.5e+2;
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([Return(FloatLit(150.0))]))])])"""
        self.assertTrue(TestAST.test(input,output,357))

    def test_58(self):
        input = """        
        Class A{
            foo(){
                Return 1.678;
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([Return(FloatLit(1.678))]))])])"""
        self.assertTrue(TestAST.test(input,output,358))

    def test_59(self):
        input = """        
        Class A{
            foo(){
                Return "abcdefg";
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([Return(StringLit(abcdefg))]))])])"""
        self.assertTrue(TestAST.test(input,output,359))

    def test_60(self):
        input = """        
        Class A{
            foo(){
                Return "abcd\\b";
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([Return(StringLit(abcd\\b))]))])])"""
        self.assertTrue(TestAST.test(input,output,360))

    def test_61(self): 
        input = """        
        Class A{
            foo(a,b,c,d: Int;b:ABC){
                Return 071;
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),IntType),param(Id(b),ClassType(Id(ABC)))],Block([Return(IntLit(57))]))])])"""
        self.assertTrue(TestAST.test(input,output,361))

    def test_62(self): 
        input = """        
        Class A{
            foo(a: Boolean){
                Return 052;
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[param(Id(a),BoolType)],Block([Return(IntLit(42))]))])])"""
        self.assertTrue(TestAST.test(input,output,362))

    def test_63(self): 
        input = """        
        Class A{
            foo(){
                Return 0b1010100010101;
            }
            foo2(){
                If(a>b){
                    Self.print("hello");
                    }
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([Return(IntLit(5397))])),MethodDecl(Id(foo2),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(hello)])]))]))])])"""
        self.assertTrue(TestAST.test(input,output,363))

    def test_64(self):
        input = """        
        Class A{
            foo(){
                Foreach ( a In 1 .. 100 By 2)
                {
                    Out.printInt(i);
                }
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([For(Id(a),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)])])])]))])])"""
        self.assertTrue(TestAST.test(input,output,364))

    def test_65(self):
        input = """        
        Class A{
            foo(){
                Foreach (a In 1 .. 100)
                {
                    Out.printInt(arr[x]);
                    Return i;
                }
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([For(Id(a),IntLit(1),IntLit(100),IntLit(1),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(arr),[Id(x)])]),Return(Id(i))])])]))])])"""
        self.assertTrue(TestAST.test(input,output,365))

    def test_66(self):
        input = """        
Class Parent{
            Val a: Int;
            getA(){
                Return Self.a;
            }
            Constructor(){
                a=5;
            }
        }
"""
        output = """Program([ClassDecl(Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),MethodDecl(Id(getA),Instance,[],Block([Return(FieldAccess(Self(),Id(a)))])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(Id(a),IntLit(5))]))])])"""
        self.assertTrue(TestAST.test(input,output,366))

    def test_67(self):
        input = """        
       Class Child: Parent{
            Val child: String;
            foreach_test(){
                Foreach (i In 1 .. 100 By 1){
                    Out.print(Self.child);
                }
            }
        }
"""
        output = """Program([ClassDecl(Id(Child),Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(child),StringType,None)),MethodDecl(Id(foreach_test),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([Call(Id(Out),Id(print),[FieldAccess(Self(),Id(child))])])])]))])])"""
        self.assertTrue(TestAST.test(input,output,367))

    def test_68(self):
        input = """Class test {
            Var f,$t,_j : String = True, False, 98 ;
            nn(a: Int; b,c: String){
                print.out();
                    }
            } 
"""
        output = """Program([ClassDecl(Id(test),[AttributeDecl(Instance,VarDecl(Id(f),StringType,BooleanLit(True))),AttributeDecl(Static,VarDecl(Id($t),StringType,BooleanLit(False))),AttributeDecl(Instance,VarDecl(Id(_j),StringType,IntLit(98))),MethodDecl(Id(nn),Instance,[param(Id(a),IntType),param(Id(b),StringType),param(Id(c),StringType)],Block([Call(Id(print),Id(out),[])]))])])"""
        self.assertTrue(TestAST.test(input,output,368))

    def test_69(self):
        input = """        
       Class A:B{
           foo(){
               Return Self.foo();
           }
           Constructor (a,b:J){}
           Destructor (){}
       }
"""
        output = """Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(foo),Instance,[],Block([Return(CallExpr(Self(),Id(foo),[]))])),MethodDecl(Id(Constructor),Instance,[param(Id(a),ClassType(Id(J))),param(Id(b),ClassType(Id(J)))],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(input,output,369))

    def test_70(self):
        input = """        
        Class A{
            foo(a:Int; b:Float; c:String; d:Boolean; e: randomclass){
                Return 5;
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(b),FloatType),param(Id(c),StringType),param(Id(d),BoolType),param(Id(e),ClassType(Id(randomclass)))],Block([Return(IntLit(5))]))])])"""
        self.assertTrue(TestAST.test(input,output,370))

    def test_71(self): 
        input = """        
        Class A{
            foo(a,e:Int; b,f:Float; c,g:String; d:Boolean; e: randomclass){
                Return 5+3+Self.a+e;
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(e),IntType),param(Id(b),FloatType),param(Id(f),FloatType),param(Id(c),StringType),param(Id(g),StringType),param(Id(d),BoolType),param(Id(e),ClassType(Id(randomclass)))],Block([Return(BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(5),IntLit(3)),FieldAccess(Self(),Id(a))),Id(e)))]))])])"""
        self.assertTrue(TestAST.test(input,output,371))

    def test_72(self): 
        input = """        
       Class Child:B{
           Var $a:Array[Int,3] = Array(1,1,1);
       }
"""
        output = """Program([ClassDecl(Id(Child),Id(B),[AttributeDecl(Static,VarDecl(Id($a),ArrayType(3,IntType),[IntLit(1),IntLit(1),IntLit(1)]))])])"""
        self.assertTrue(TestAST.test(input,output,372))

    def test_73(self): 
        input = """        
       Class Child:B{
           Var a, b, c:Int;
           Foo(){
               Var a, b, c:Int;
           }
       }
"""
        output = """Program([ClassDecl(Id(Child),Id(B),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Instance,VarDecl(Id(c),IntType)),MethodDecl(Id(Foo),Instance,[],Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType)]))])])"""
        self.assertTrue(TestAST.test(input,output,373))

    def test_74(self):
        input = """        
        Class Child: Parent{
            Val asd: String;
            if_test(){
                If (class.what ==. "String"){
                    out.print("Bruh");
                }
            }
        }
"""
        output = """Program([ClassDecl(Id(Child),Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(asd),StringType,None)),MethodDecl(Id(if_test),Instance,[],Block([If(BinaryOp(==.,FieldAccess(Id(class),Id(what)),StringLit(String)),Block([Call(Id(out),Id(print),[StringLit(Bruh)])]))]))])])"""
        self.assertTrue(TestAST.test(input,output,374))

    def test_75(self):
        input = """        
        Class Parent{
            Val a: Int;
            Var $b, $c: Int = 1 + 6, 2;
            getA(){
                RandomClass.print();
            }
            getBplusCplusD(D: Int){
                D = 5;
                Return Self.b + Self.c + D;
            }
            Constructor(){
                Self.a=5;
            }
        }
        Class Child: Parent{
            Val child: String;
            Constructor(){
                Self.child = "Child class";
            }
        }
"""
        output = """Program([ClassDecl(Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Static,VarDecl(Id($b),IntType,BinaryOp(+,IntLit(1),IntLit(6)))),AttributeDecl(Static,VarDecl(Id($c),IntType,IntLit(2))),MethodDecl(Id(getA),Instance,[],Block([Call(Id(RandomClass),Id(print),[])])),MethodDecl(Id(getBplusCplusD),Instance,[param(Id(D),IntType)],Block([AssignStmt(Id(D),IntLit(5)),Return(BinaryOp(+,BinaryOp(+,FieldAccess(Self(),Id(b)),FieldAccess(Self(),Id(c))),Id(D)))])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(a)),IntLit(5))]))]),ClassDecl(Id(Child),Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(child),StringType,None)),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(child)),StringLit(Child class))]))])])"""
        self.assertTrue(TestAST.test(input,output,375))

    def test_76(self):
        input = """        
        Class A{
            foo(){
                Return 15e-2;
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([Return(FloatLit(0.15))]))])])"""
        self.assertTrue(TestAST.test(input,output,376))

    def test_77(self):
        input = """        
        Class Parent{
            Val a: Int;
            Var $b, $c: Int = 1 + 6, 2;
            getRandom(){
                RandomClass.print();
            }
            getDoubleA(){
                RandomClass.print(a*a);
            }
            getBplusCplusD(D: Int){
                D = 5;
                Return Self.b + Self.c + D;
            }
            Constructor(){
                Self.a=5;
            }
        }
        Class Child: Parent{
            Val child: String;
            $testStatic(str: String){
                str = "Hello";
                RandomClass.print(str);
            }
            Val My1stCons, My2ndCons: Int = 1 + 5, 2;
            Var $x, $y : Int = 0, 0;
            Constructor(){
                Self.child = "Child class";
            }
        }
"""
        output = """Program([ClassDecl(Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Static,VarDecl(Id($b),IntType,BinaryOp(+,IntLit(1),IntLit(6)))),AttributeDecl(Static,VarDecl(Id($c),IntType,IntLit(2))),MethodDecl(Id(getRandom),Instance,[],Block([Call(Id(RandomClass),Id(print),[])])),MethodDecl(Id(getDoubleA),Instance,[],Block([Call(Id(RandomClass),Id(print),[BinaryOp(*,Id(a),Id(a))])])),MethodDecl(Id(getBplusCplusD),Instance,[param(Id(D),IntType)],Block([AssignStmt(Id(D),IntLit(5)),Return(BinaryOp(+,BinaryOp(+,FieldAccess(Self(),Id(b)),FieldAccess(Self(),Id(c))),Id(D)))])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(a)),IntLit(5))]))]),ClassDecl(Id(Child),Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(child),StringType,None)),MethodDecl(Id($testStatic),Static,[param(Id(str),StringType)],Block([AssignStmt(Id(str),StringLit(Hello)),Call(Id(RandomClass),Id(print),[Id(str)])])),AttributeDecl(Instance,ConstDecl(Id(My1stCons),IntType,BinaryOp(+,IntLit(1),IntLit(5)))),AttributeDecl(Instance,ConstDecl(Id(My2ndCons),IntType,IntLit(2))),AttributeDecl(Static,VarDecl(Id($x),IntType,IntLit(0))),AttributeDecl(Static,VarDecl(Id($y),IntType,IntLit(0))),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(child)),StringLit(Child class))]))])])"""
        self.assertTrue(TestAST.test(input,output,377))

    def test_78(self):
        input = """        
Class Programm {
        Val My1stCons, My2ndCons: Int = 1 + 5, 2;
        Val My1stCons, My2ndCons: Int = 1 + 5, 2;
        main() {
            Out.printInt(Shape::$numOfShape);
        }
    }
"""
        output = """Program([ClassDecl(Id(Programm),[AttributeDecl(Instance,ConstDecl(Id(My1stCons),IntType,BinaryOp(+,IntLit(1),IntLit(5)))),AttributeDecl(Instance,ConstDecl(Id(My2ndCons),IntType,IntLit(2))),AttributeDecl(Instance,ConstDecl(Id(My1stCons),IntType,BinaryOp(+,IntLit(1),IntLit(5)))),AttributeDecl(Instance,ConstDecl(Id(My2ndCons),IntType,IntLit(2))),MethodDecl(Id(main),Instance,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))])]))])])"""
        self.assertTrue(TestAST.test(input,output,378))

    def test_79(self):
        input = """        
        Class Parent{
            Val a: Int;
            Var $b, $c: Int = 1 + 6, 2;
            getRandom(){
                RandomClass.print();
            }
            getDoubleA(){
                RandomClass.print(a*a);
            }
            getBplusCplusD(D: Int){
                D = 5;
                Return Self.b + Self.c + D;
            }
            Constructor(){
                Self.a=5;
            }
        }
        Class Child: Parent{
            Val child: String;
            $testStatic(str: String){
                str = "Hello";
                RandomClass.print(str);
            }
            Val My1stCons, My2ndCons: Int = 1 + 5, 2;
            Var $x, $y : Int = 0, 0;
            Constructor(){
                Self.child = "Child class";
            }
            printChild(){
                Foreach (i In 1 .. 100 By 1){
                    Out.print(Self.child);
                }
            }
        }
"""
        output = """Program([ClassDecl(Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Static,VarDecl(Id($b),IntType,BinaryOp(+,IntLit(1),IntLit(6)))),AttributeDecl(Static,VarDecl(Id($c),IntType,IntLit(2))),MethodDecl(Id(getRandom),Instance,[],Block([Call(Id(RandomClass),Id(print),[])])),MethodDecl(Id(getDoubleA),Instance,[],Block([Call(Id(RandomClass),Id(print),[BinaryOp(*,Id(a),Id(a))])])),MethodDecl(Id(getBplusCplusD),Instance,[param(Id(D),IntType)],Block([AssignStmt(Id(D),IntLit(5)),Return(BinaryOp(+,BinaryOp(+,FieldAccess(Self(),Id(b)),FieldAccess(Self(),Id(c))),Id(D)))])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(a)),IntLit(5))]))]),ClassDecl(Id(Child),Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(child),StringType,None)),MethodDecl(Id($testStatic),Static,[param(Id(str),StringType)],Block([AssignStmt(Id(str),StringLit(Hello)),Call(Id(RandomClass),Id(print),[Id(str)])])),AttributeDecl(Instance,ConstDecl(Id(My1stCons),IntType,BinaryOp(+,IntLit(1),IntLit(5)))),AttributeDecl(Instance,ConstDecl(Id(My2ndCons),IntType,IntLit(2))),AttributeDecl(Static,VarDecl(Id($x),IntType,IntLit(0))),AttributeDecl(Static,VarDecl(Id($y),IntType,IntLit(0))),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(child)),StringLit(Child class))])),MethodDecl(Id(printChild),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([Call(Id(Out),Id(print),[FieldAccess(Self(),Id(child))])])])]))])])"""
        self.assertTrue(TestAST.test(input,output,379))

    def test_80(self):
        input = """        
        Class Child: Parent{
            Val i: Int;
            if_test(){
                If (Self.if_test() == 5){
                    out.print("Bruh2");
                }
                Elseif (i%2 != 0){
                    out.print("Elseif");
                }
                Else{
                    out.print("Bruh3");
                    Return 0;
                }
            }
        }
"""
        output = """Program([ClassDecl(Id(Child),Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(i),IntType,None)),MethodDecl(Id(if_test),Instance,[],Block([If(BinaryOp(==,CallExpr(Self(),Id(if_test),[]),IntLit(5)),Block([Call(Id(out),Id(print),[StringLit(Bruh2)])]),If(BinaryOp(!=,BinaryOp(%,Id(i),IntLit(2)),IntLit(0)),Block([Call(Id(out),Id(print),[StringLit(Elseif)])]),Block([Call(Id(out),Id(print),[StringLit(Bruh3)]),Return(IntLit(0))])))]))])])"""
        self.assertTrue(TestAST.test(input,output,380))

    def test_81(self): 
        input = """        
        Class A{
            foo(){
                Shape::$getNumOfShape();
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([Call(Id(Shape),Id($getNumOfShape),[])]))])])"""
        self.assertTrue(TestAST.test(input,output,381))

    def test_82(self): 
        input = """        
        Class A{
            foo(){
                Shape::$getNumOfShape();
                Shape.getNumOfShape();
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([Call(Id(Shape),Id($getNumOfShape),[]),Call(Id(Shape),Id(getNumOfShape),[])]))])])"""
        self.assertTrue(TestAST.test(input,output,382))

    def test_83(self): 
        input = """        
        Class A{
            foo(){
                Shape::$getNumOfShape();
                Shape.getNumOfShape();
                Shape.getNumOfShape(A.number);
                Shape.getNumOfShape(A.number, A.getNum());
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([Call(Id(Shape),Id($getNumOfShape),[]),Call(Id(Shape),Id(getNumOfShape),[]),Call(Id(Shape),Id(getNumOfShape),[FieldAccess(Id(A),Id(number))]),Call(Id(Shape),Id(getNumOfShape),[FieldAccess(Id(A),Id(number)),CallExpr(Id(A),Id(getNum),[])])]))])])"""
        self.assertTrue(TestAST.test(input,output,383))

    def test_84(self):
        input = """        
        Class A{
            foo(){
                Shape::$getNumOfShape();
                Shape.getNumOfShape();
                Shape.getNumOfShape(A.number);
                Shape.getArr(b[5][6]);
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([Call(Id(Shape),Id($getNumOfShape),[]),Call(Id(Shape),Id(getNumOfShape),[]),Call(Id(Shape),Id(getNumOfShape),[FieldAccess(Id(A),Id(number))]),Call(Id(Shape),Id(getArr),[ArrayCell(Id(b),[IntLit(5),IntLit(6)])])]))])])"""
        self.assertTrue(TestAST.test(input,output,384))

    def test_85(self):
        input = """        
        Class A{
            foo(){
                Shape.getArr(b[5][6],(a+1)[5]);
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([Call(Id(Shape),Id(getArr),[ArrayCell(Id(b),[IntLit(5),IntLit(6)]),ArrayCell(BinaryOp(+,Id(a),IntLit(1)),[IntLit(5)])])]))])])"""
        self.assertTrue(TestAST.test(input,output,385))

    def test_86(self):
        input = """        
        Class A{
            foo(){
                Shape.call(method);
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([Call(Id(Shape),Id(call),[Id(method)])]))])])"""
        self.assertTrue(TestAST.test(input,output,386))

    def test_87(self):
        input = """        
        Class A{
            foo(){
                Shape::$callmethod();
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([Call(Id(Shape),Id($callmethod),[])]))])])"""
        self.assertTrue(TestAST.test(input,output,387))

    def test_88(self):
        input = """        
        Class A{
            foo(para1,para2,$para3: Int; $para4,para5,par6:Float){
                Return para1;
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[param(Id(para1),IntType),param(Id(para2),IntType),param(Id($para3),IntType),param(Id($para4),FloatType),param(Id(para5),FloatType),param(Id(par6),FloatType)],Block([Return(Id(para1))]))])])"""
        self.assertTrue(TestAST.test(input,output,388))

    def test_89(self):
        input = """        
        Class Program{
            main(){
                Self.print("this is a special static method");
            }
            main(para:Int){
                Self.print("this is not a static method");
            }
        }
        Class nonProgram{
            main(){
                Self.print("also non static method");
            }
            main(para1,para2:Float){
                Self.print("also non static method");
            }
        }
"""
        output = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Self(),Id(print),[StringLit(this is a special static method)])])),MethodDecl(Id(main),Instance,[param(Id(para),IntType)],Block([Call(Self(),Id(print),[StringLit(this is not a static method)])]))]),ClassDecl(Id(nonProgram),[MethodDecl(Id(main),Instance,[],Block([Call(Self(),Id(print),[StringLit(also non static method)])])),MethodDecl(Id(main),Instance,[param(Id(para1),FloatType),param(Id(para2),FloatType)],Block([Call(Self(),Id(print),[StringLit(also non static method)])]))])])"""
        self.assertTrue(TestAST.test(input,output,389))

    def test_90(self):
        input = """        
        Class A{
            Constructor(para1,para2,$para3: Int; $para4,para5,par6:Float){
                Var a,b,c: Int = 5,6,0xBC;
                Shape.getArr(b,a,c,Self.d);
            }
        }
"""
        output = """Program([ClassDecl(Id(A),[MethodDecl(Id(Constructor),Instance,[param(Id(para1),IntType),param(Id(para2),IntType),param(Id($para3),IntType),param(Id($para4),FloatType),param(Id(para5),FloatType),param(Id(par6),FloatType)],Block([VarDecl(Id(a),IntType,IntLit(5)),VarDecl(Id(b),IntType,IntLit(6)),VarDecl(Id(c),IntType,IntLit(188)),Call(Id(Shape),Id(getArr),[Id(b),Id(a),Id(c),FieldAccess(Self(),Id(d))])]))])])"""
        self.assertTrue(TestAST.test(input,output,390))

    def test_91(self):
        input = """
        Class A: B{
            Val a: ABC;
            Val b,c,d: ABC;
            }"""

        output = """Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Instance,ConstDecl(Id(a),ClassType(Id(ABC)),None)),AttributeDecl(Instance,ConstDecl(Id(b),ClassType(Id(ABC)),None)),AttributeDecl(Instance,ConstDecl(Id(c),ClassType(Id(ABC)),None)),AttributeDecl(Instance,ConstDecl(Id(d),ClassType(Id(ABC)),None))])])"""
        self.assertTrue(TestAST.test(input,output,400))

    def test_92(self):
        input = """
        Class A: C{
            Var a: Int;
            Var $b: String = "Hello\\n";
            Var c,$d,e,s: Float = 5.0,2e-4,.5e-3,1.5e3;
            Var bruh: Float = 25.2;
            Var x,y: RandomClass;
            Var z: RandomClass = Null;
            Val $f: Int;
            Val g: String = "World\\b";
            Val h,$i,j: Float = 1.0,2e-4,.5e-3;
            Val k,$l: RandomClass;
            Val m: RandomClass2 = Null;
            Val $n,p: Boolean = True, False;
            foo(){
                Var a: ABC;
                Val b: ABC;
                Val c: ABC = Null;
                Var d,e,f,g: Int = 0575 ,0xAB75, 0b1110010101, 757;
                {}
                }
            }"""

        output = """Program([ClassDecl(Id(A),Id(C),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Static,VarDecl(Id($b),StringType,StringLit(Hello\\n))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(5.0))),AttributeDecl(Static,VarDecl(Id($d),FloatType,FloatLit(0.0002))),AttributeDecl(Instance,VarDecl(Id(e),FloatType,FloatLit(0.0005))),AttributeDecl(Instance,VarDecl(Id(s),FloatType,FloatLit(1500.0))),AttributeDecl(Instance,VarDecl(Id(bruh),FloatType,FloatLit(25.2))),AttributeDecl(Instance,VarDecl(Id(x),ClassType(Id(RandomClass)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(y),ClassType(Id(RandomClass)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(z),ClassType(Id(RandomClass)),NullLiteral())),AttributeDecl(Static,ConstDecl(Id($f),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(g),StringType,StringLit(World\\b))),AttributeDecl(Instance,ConstDecl(Id(h),FloatType,FloatLit(1.0))),AttributeDecl(Static,ConstDecl(Id($i),FloatType,FloatLit(0.0002))),AttributeDecl(Instance,ConstDecl(Id(j),FloatType,FloatLit(0.0005))),AttributeDecl(Instance,ConstDecl(Id(k),ClassType(Id(RandomClass)),None)),AttributeDecl(Static,ConstDecl(Id($l),ClassType(Id(RandomClass)),None)),AttributeDecl(Instance,ConstDecl(Id(m),ClassType(Id(RandomClass2)),NullLiteral())),AttributeDecl(Static,ConstDecl(Id($n),BoolType,BooleanLit(True))),AttributeDecl(Instance,ConstDecl(Id(p),BoolType,BooleanLit(False))),MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),ClassType(Id(ABC)),NullLiteral()),ConstDecl(Id(b),ClassType(Id(ABC)),None),ConstDecl(Id(c),ClassType(Id(ABC)),NullLiteral()),VarDecl(Id(d),IntType,IntLit(381)),VarDecl(Id(e),IntType,IntLit(43893)),VarDecl(Id(f),IntType,IntLit(917)),VarDecl(Id(g),IntType,IntLit(757)),Block([])]))])])"""
        self.assertTrue(TestAST.test(input,output,401))