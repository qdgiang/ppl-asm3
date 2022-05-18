import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    # def test_undeclared_function(self):
    #     """Simple program: int main() {} """
    #     input = """
    #     Class A {
    #         foo();
    #         }
    #     """
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,400))

    # def test_diff_numofparam_stmt(self):
    #     """More complex program"""
    #     input = """
    #     Class A {
    #         foo(a, b: Int){
    #         } 
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),List())"
    #     self.assertTrue(TestChecker.test(input,expect,401))

    # def test_mismatchConstant1(self):
    #     input = """
    #     Class A {
    #         Val a : Int = 1.3;
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),List())"
    #     self.assertTrue(TestChecker.test(input,expect,402))
    
    # def test_IllegalArray(self):
    #     input = """
    #     Class A {
    #         Var a: Array[Int, 2] = Array(1.1, 2);
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),List(IntLiteral(4)))"
    #     self.assertTrue(TestChecker.test(input,expect,405))

    # def test_typeMMConstant1(self):
    #     input = """
    #     Class A {
    #         Val a: Array[Int,2] = Array(1.1,2.1);
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),ArrayType(2,IntType),[FloatLit(1.1),FloatLit(2.1)])"
    #     self.assertTrue(TestChecker.test(input,expect,406))
        
    # def test_typeMMConstant2(self):
    #     input = """
    #     Class A {
    #         Val a : Int = 1.2;
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(1.2))"
    #     self.assertTrue(TestChecker.test(input,expect,407))

    ####################### Redeclare ##################3
    def test_redeclare1(self):
        input = """
        Class Program {
            Val a : Int = 1;
            Val a: Int = 3;
            main(){}
        }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_redeclare2(self):
        input = """
        Class Program {
            main(){
                Val a : Int = 1;
                Val a: Int = 3;
            }
        }
        """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclare3(self):
        input = """
        Class Program {
            main(){
                {Val a : Int = 1;}
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclare4(self):
        input = """
        Class Program {
            main(){
                {
                Val a : Int = 1;
                Var a: Int = 3;
                }
            }
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclare5(self):
        input = """
        Class Program {
            main(){}
            get(){}
            get(){}
        }
        """
        expect = "Redeclared Method: get"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclare6(self):
        input = """
        Class Program {
            main(){}
            get(a: Int){}
            get(){}
        }
        """
        expect = "Redeclared Method: get"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redeclare7(self):
        input = """
        Class A{}
        Class A{}
        """
        expect = "Redeclared Class: A"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclare8(self):
        input = """
        Class Program {
            main(){}
            get(a : Int; b: Float; a: String){}
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redeclare9(self):
        input = """
        Class Program {
            main(){}
        }
        Class A {
            get(){}
            $get(a: Int){}
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_redeclare10(self):
        input = """
        Class Program {
            Val $a : Int = 1;
            Val a : Int = 13;
        }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_redeclare11(self):
        input = """
        Class Program {
            main(){}
            Val $a : Int = 1;
        }
        Class subProgram: Program {
            Val $a : Int = 1;
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_redeclare12(self):
        input = """
        Class Program {
            main(){}
            get(a: Int){
                Val a: String = "S";
            }
        }
        """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input,expect,411))

########################## Binary ######################## 12-20

    def test_binary1(self):
        input = """
        Class Program {
            main(){
                Var a : Boolean = 1 == 2.1;
            }
        }
        """
        expect = "Type Mismatch In Expression: FloatLit(2.1)"
        self.assertTrue(TestChecker.test(input,expect,412))

########################## Constant ######################## 21-30

    def test_constant1(self):
        input = """
        Class Program {
            main(){
                Var a : Int = 1;
                Val b : Int = 1 + a;
            }
        }
        """
        expect = "Illegal Constant Expression: BinaryOp(+,IntLit(1),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_constant2(self):
        input = """
        Class Program {
            main(){
                Val b : Int;
            }
        }
        """
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_constant3(self):
        input = """
        Class Program {
            main(){
                Val b : Int = 1 + a;
            }
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,423))
    def test_constant4(self):
        input = """
        Class Program {
            main(){
                Val b : Float = 1 + 2;
            }
        }
        """
        expect = "[None]"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_constant4(self):
        input = """
        Class Program {
            main(){
                Val b : A = 1 + a;
            }
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_constant5(self):
        input = """
        Class Program {
            main(){
                Var a: Int = 1;
                Val b : Array[Int, 2] = Array(a, 1); 
            }
        }
        """
        expect = "Illegal Constant Expression: [Id(a),IntLit(1)]"
        self.assertTrue(TestChecker.test(input,expect,426))
    def test_constant6(self):
        input = """
        Class Program {
            main(){
                Val a: Int = Null;
            }
        }
        """
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_constant7(self):
        input = """
        Class Program {
            main(){
                Var a: Int = 1;
                Val b : Array[Array[Int, 1], 2] = Array(Array(a), Array(1)); 
            }
        }
        """
        expect = "Illegal Constant Expression: [[Id(a)],[IntLit(1)]]"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_constant8(self):
        input = """
        Class A {Val $x: Int = 1;}
        Class Program {
            main(){
                A::$x = 1;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(A),Id($x)),IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_constant9(self):
        input = """
        Class A {
            Val $x: Int = 1;
            Var $y: Int = 2;
        }
        Class Program {
            main(){
                A::$x = A::$y;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(A),Id($x)),FieldAccess(Id(A),Id($y)))"
        self.assertTrue(TestChecker.test(input,expect,430))

    ######################### Stmt #################### 31-40

    def test_callStmt1(self):
        input = """
        Class Program { main(){} }
        Class B{ $getA(a: Int){ } }
        Class A{ method(b: Int){ B::$getA(b,1); } }
        """
        expect = "Type Mismatch In Statement: Call(Id(B),Id($getA),[Id(b),IntLit(1)])"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_callStmt2(self):
        input = """
        Class Program { main(){} }
        Class B{ $getA(a: Int){} }
        Class A{
            method(b: Int){ b::$getA(b,1); }
        }
        """
        expect = "Type Mismatch In Statement: Call(Id(b),Id($getA),[Id(b),IntLit(1)])"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_callStmt4(self):
        input = """
        Class Program {
            main(){Return;}
        }
        Class B{
            $getA(a: Int){
                Return a;
            }
        }
        Class A{
            method(b: B){
                b::$getA(b,1);
            }
        }
        """
        expect = "Illegal Member Access: Call(Id(b),Id($getA),[Id(b),IntLit(1)])"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_callStmtReturnMethod(self):
        input = """
        Class Program {
            main(){Return;}
        }
        Class B{
            $getA(a: Int){
                Return a;
            }
        }
        Class A{
            method(b: Int){
                B::$getA(b,1);
            }
        }
        """
        expect = "Type Mismatch In Statement: Call(Id(B),Id($getA),[Id(b),IntLit(1)])"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_callStmt5(self):
        input = """
        Class Program {
            main(){Return;}
        }
        Class B{
            getA(a: Int){
                Return;
            }
        }
        Class A{
            method(){
                Var b: B;
                b.getA(c);
            }
        }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_callStmt6(self):
        input = """
        Class Program {
            main(){Return;}
        }
        Class A{
            $getA(a: Int){
                Return a;
            }
            method(b: Int){
                Self.getA(b,1);
            }
        }
        """
        expect = "Undeclared Method: getA"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_callStmt7(self):
        input = """
        Class Program {
            main(){Return;}
            getA(a,b : Int){}
        }
        Class A{
            method(b: Int){
                Self.getA(b,1);
            }
        }
        """
        expect = "Undeclared Method: getA"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_callStmt8(self):
        input = """
        Class Program {
            main(){Return;}
            getA(a,b : Int){}
        }
        Class A{
            $method(b: Int){
                Self.getA(b,1);
            }
        }
        """
        expect = "Illegal Member Access: Call(Self(),Id(getA),[Id(b),IntLit(1)])"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_callStmt9(self):
        input = """
        Class Program {
            main(){Return;}
        }
        Class B{$getA(a,b : Int){}}
        Class A{
            $method(b: Int){
                Var c: B;
                c.getA(b,1);
            }
        }
        """
        expect = "Undeclared Method: getA"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_callStmt10(self):
        input = """
        Class Program {main(){Return;}}
        Class B{getA(a,b : Int){}}
        Class A{
            $method(b: Int){
                Var c: B;
                Var d: B = c;
                d.getA(b,c);
            }
        }
        """
        expect = "Type Mismatch In Statement: Call(Id(d),Id(getA),[Id(b),Id(c)])"
        self.assertTrue(TestChecker.test(input,expect,440))

        ################## Expr ################# 441-450

    def test_callExpr1(self):
        input = """
        Class Program {main(){Return;}}
        Class B{getA(a: Int){Return a;}}
        Class A{
            method(b: B){
                Return b.getA(b);
            }
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(b),Id(getA),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_callExpr2(self):
        input = """
        Class Program {main(){Return;}}
        Class B{$getA(a: Int){Return ;}}
        Class A{
            method(b: Int){
                Return B::$getA(b);
            }
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(B),Id($getA),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_callExpr3(self):
        input = """
        Class Program {main(){Return;}}
        Class B{$getA(a: Int){Return ;}}
        Class A{
            method(b: B){
                Return b::$getA(1);
            }
        }
        """
        expect = "Illegal Member Access: CallExpr(Id(b),Id($getA),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_callExpr4(self):
        input = """
        Class Program { main(){Return;} }
        Class B{ $getA(a: Int){ Return a; } }
        Class A{
            method(b: Int){ Return 1 + B::$getA(b, 1); }
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(B),Id($getA),[Id(b),IntLit(1)])"
        self.assertTrue(TestChecker.test(input,expect,444))


    def test_callExpr5(self):
        input = """
        Class Program { main(){Return;} }
        Class B{ $getA(a: Int){ Return a/2; } }
        Class A{ method(b: Int){ Return 1.0 % B::$getA(b); } }
        """
        expect = "Type Mismatch In Expression: FloatLit(1.0)"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_callExpr6(self):
        input = """
        Class Program { main(){Return;} }
        Class A{
            getA(a: Int){ Return a/2; } 
            method(b: Int){ Return 1.0 % Self.getA(b); } }
        """
        expect = "Type Mismatch In Expression: FloatLit(1.0)"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_callExpr7(self):
        input = """
        Class Program { main(){Return;} }
        Class A{
            getA(a: Int){ Return a/2; } 
            method(b: Int){ 
                Return 1.0 % Self.getA(b); 
            } 
        }
        """
        expect = "Type Mismatch In Expression: FloatLit(1.0)"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_callExpr8(self):
        input = """
        Class Program { main(){Return;} }
        Class A{
            getA(a: Int){ Return a/2; } 
            $method(b: Int){ Return 1.0 % Self.getA(b); } }
        """
        expect = "Illegal Member Access: CallExpr(Self(),Id(getA),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_callExpr9(self):
        input = """
        Class Program { main(){Return;} }
        Class B{$getA(a,b : Int){}}
        Class A{
            $method(b: Int){
                Var c: B;
                Return c.getA(b,1);
            }
        }
        """
        expect = "Undeclared Method: getA"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_callExpr10(self):
        input = """
        Class Program {main(){Return;}}
        Class B{getA(a,b : Int){}}
        Class A{
            $method(b: Int){
                Var c: B;
                Var d: B = c;
                Return d.getA(b,c);
            }
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(d),Id(getA),[Id(b),Id(c)])"
        self.assertTrue(TestChecker.test(input,expect,450))

    ####################### FieldAccess ##################### 451 - 460

    ########################## ArrayCell ################## 461 - 470


    def test_callArrayCell1(self):
        input = """
        Class Program {main(){Return;}}
        Class B{getA(a,b : Int){}}
        Class A{
            $method(b: Int){
                Val c: Array[Array[Int, 2], 2] = Array(Array(2,1), Array(1,4));
                Return c[0][1][1];
            }
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(c),[IntLit(0),IntLit(1),IntLit(1)])"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_callArrayCell2(self):
        input = """
        Class Program {main(){Return;}}
        Class A{
            method(){
                Val c: Array[Array[Int, 2], 2] = Array(Array(2,1), Array(1,4));
                Return c[0.1];
            }
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(c),[FloatLit(0.1)])"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_callArrayCell3(self):
        input = """
        Class Program {main(){Return;}}
        Class A{
            method(b: Float){
                Var c: Array[Array[Int, 2], 2];
                Return c[0.1];
            }
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(c),[FloatLit(0.1)])"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_callArrayCell4(self):
        input = """
        Class Program {main(){Return;}}
        Class B{getA(a,b : Int){}}
        Class A{
            $method(b: Int){
                Val c: Array[Array[Int, 2], 2] = Array(Array(2,1), Array(1,4));
                Val x : Int = c[b][b+1];
                Return x[0];
            }
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(x),[IntLit(0)])"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_callArrayCell5(self):
        input = """
        Class A{
            method(c: Array[Array[Int, 2], 2]){
                Var x: Array[Int, 1];
                x = c[0];
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x),ArrayCell(Id(c),[IntLit(0)]))"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_callArrayCell6(self):
        input = """
        Class B{ Val g: Int = 1;}
        Class A{
            $method(x,y,z : Int){
                Var b: B;
                Val k: Array[Int, 1] = b.g(x + y + z);
            }
        }
        Class Program {main(){ A::$method(1,2,3); } }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(b),Id(g),[BinaryOp(+,BinaryOp(+,Id(x),Id(y)),Id(z))])"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_if1(self):
        input = """
        Class A{
            $method(x: Int){
                If (x) {
                    x = 1;
                }
            }
        }
        Class Program {main(){ A::$method(1); } }
        """
        expect = "Type Mismatch In Statement: If(Id(x),Block([AssignStmt(Id(x),IntLit(1))]))"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_if2(self):
        input = """
        Class A{
            $method(x: Int){
                If (x > 1) {
                    x = 1;
                }
                Elseif(x % 2 - 0){
                    x = 0;
                }
            }
        }
        Class Program {main(){ A::$method(1); } }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(-,BinaryOp(%,Id(x),IntLit(2)),IntLit(0)),Block([AssignStmt(Id(x),IntLit(0))]))"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_if3(self):
        input = """
        Class A{
            $method(x: Int){
                If (x > 1) {
                    x = 1;
                }
                Elseif(x % 2 == 0){
                    x = 0;
                    If (x) {
                        x = 1;
                    }
                }
            }
        }
        Class Program {main(){ A::$method(1); } }
        """
        expect = "Type Mismatch In Statement: If(Id(x),Block([AssignStmt(Id(x),IntLit(1))]))"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_if4(self):
        input = """
        Class A{
            $method(x: Int){
                If (x > 1) {}
                Elseif(x % 2 == 0){}
                Else{
                    If (x){}
                }
            }
        }
        Class Program {main(){ A::$method(1); } }
        """
        expect = "Type Mismatch In Statement: If(Id(x),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,470))

    #################### FOR/IN ####################### 471 - 480

    def test_for1(self):
        input = """
        Class A{
            $method(x: Float){
                Foreach (i In x .. 100 By 2) {
                    x = i + x;
                }
            }
        }
        Class Program {main(){ A::$method(1); } }
        """
        expect = "Type Mismatch In Statement: For(Id(i),Id(x),IntLit(100),IntLit(2),Block([AssignStmt(Id(x),BinaryOp(+,Id(i),Id(x)))])])"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_for2(self):
        input = """
        Class A{
            $method(x: Int){
                Foreach (x In 5.1 .. 2){}
                Return 1;
            }
        }
        Class Program {main(){} submain(){ Return A::$method(1); } }
        """
        expect = "Type Mismatch In Statement: For(Id(x),FloatLit(5.1),IntLit(2),IntLit(1),Block([])])"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_for3(self):
        input = """
        Class A{
            $method(x: String){
                Foreach (i In x .. 100 By 2) {
                    x = i + x;
                }
            }
        }
        Class Program {main(){ A::$method(1); } }
        """
        expect = "Type Mismatch In Statement: For(Id(i),Id(x),IntLit(100),IntLit(2),Block([AssignStmt(Id(x),BinaryOp(+,Id(i),Id(x)))])])"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_for4(self):
        input = """
        Class A{
            $method(x: Int){
                Foreach (x In 5 .. 2.1){}
                Return x;
            }
        }
        Class Program {main(){} submain(){ Return A::$method(1); } }
        """
        expect = "Type Mismatch In Statement: For(Id(x),IntLit(5),FloatLit(2.1),IntLit(1),Block([])])"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_for5(self):
        input = """
        Class A{
            $method(x: Int){
                Foreach (x In 5 .. 2 By x){
                    Foreach (x In 1 .. 2 By y){}
                }
                Return x;
            }
        }
        Class Program {main(){} submain(){ Return A::$method(1); } }
        """
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_break1(self):
        input = """
        Class A{
            $method(x: Int){
                Foreach (x In 5 .. 2 By x){
                }
                Break;
                Return 1;
            }
        }
        Class Program {main(){} submain(){ Return A::$method(1); } }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,476))


    def test_continue1(self):
        input = """
        Class A{
            $method(x: Int){
                Continue;
                Return 1;
            }
        }
        Class Program {main(){} submain(){ Return A::$method(1); } }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_continue2(self):
        input = """
        Class A{
            $method(x: Int){
                Foreach (x In 5 .. 2 By x){
                    Break;
                }
                Continue;
                Return 1;
            }
        }
        Class Program {main(){} submain(){ Return A::$method(1); } }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_continue3(self):
        input = """
        Class A{
            $method(x: Int){
                Foreach (x In 5 .. 2 By x){
                    {{Continue;}}
                    Foreach (x In 5 .. 2 By x){
                        Break;
                    }
                }
                {{Continue;}}
            }
        }
        Class Program {main(){} submain(){ Return A::$method(1); } }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_continue4(self):
        input = """
        Class A{
            $method(x: Int){
                If (x > 1) {
                    Continue;
                }
                Return 1;
            }
        }
        Class Program {main(){} submain(){ Return A::$method(1); } }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,480))

    ################ No entry Point ################ 481 - 490
    
    def test_noEntryPoint1(self):
        input = """
        Class Program {main(x: Int){Return;}}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_noEntryPoint2(self):
        input = """
        Class Program {main(){Return 1;}}
        """
        expect = "Type Mismatch In Statement: MethodDecl(Id(main),Static,[],Block([Return(IntLit(1))]))"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_noEntryPoint3(self):
        input = """
        Class Program {noMain(t: Int){Return;}}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_noEntryPoint4(self):
        input = """
        Class Program {
            Var x: Int;
            main(x: Int){ If (Self.x == 1){ Return 1; } }
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,484))

    ############## Illegal Member Access ###############3 491 - 450

    def test_illMemAccess1(self):
        input = """
        Class A{
            Val $x: Int = 1;
        }
        Class B{
            method(a: A){
                Return a::$x;
            }
        }

        Class Program {main(){}}
        """
        expect = "Illegal Member Access: FieldAccess(Id(a),Id($x))"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_illMemAccess2(self):
        input = """
        Class A{
            Val x: Int = 1;
        }
        Class B{
            method(a: A){
                Return A.x;
            }
        }
        Class Program {main(){}}
        """
        expect = "Illegal Member Access: FieldAccess(Id(A),Id(x))"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_illMemAccess3(self):
        input = """
        Class A{
            Val $x: Int = 1;
        }
        Class B{
            method(a: A){
                Return E::$x;
            }
        }

        Class Program {main(){}}
        """
        expect = "Undeclared Class: E"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_illMemAccess4(self):
        input = """
        Class A{
            Val $x: Int = 1;
        }
        Class B{
            method(a: A){
                Return v.x;
            }
        }

        Class Program {main(){}}
        """
        expect = "Undeclared Identifier: v"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_illMemAccess5(self):
        input = """
        Class A{
            Val $x: Int = 1;
        }
        Class B{
            method(a: String){
                Return a.x;
            }
        }

        Class Program {main(){}}
        """
        expect = "Type Mismatch In Expression: FieldAccess(Id(a),Id(x))"
        self.assertTrue(TestChecker.test(input,expect,495))
    
    def test_methodConst1(self):
        input = """
        Class A{
            Val $x: Int = 1;
            $method(a: Int){
                Return 1 + a;
            }
            
        }
        Class B{
            method(){
                Val x: Int = A::$method(2);
            }
        }

        Class Program {main(){}}
        """
        expect = "Illegal Constant Expression: CallExpr(Id(A),Id($method),[IntLit(2)])"
        self.assertTrue(TestChecker.test(input,expect,496))
    
    def test_assignStmt1(self):
        input = """
        Class A{
            Var $y: Int = 1;
        }
        Class B{
            method(){
                Val x: Int = 1;
                x = A::$y;
            }
        }

        Class Program {main(){}}
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(x),FieldAccess(Id(A),Id($y)))"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_assignStmt2(self):
        input = """
        Class A{
            Var $y: Int = 1;
        }
        Class B{
            method(){
                Var y : Int = A::$y;
                Val a : Int = y;
            }
        }

        Class Program {main(){}}
        """
        expect = "Illegal Constant Expression: Id(y)"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_main1(self):
        input = """
        Class Program {main(x: Int){}}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_main2(self):
        input = """
        Class Program {main(){Return 1;}}
        """
        expect = "Type Mismatch In Statement: MethodDecl(Id(main),Static,[],Block([Return(IntLit(1))]))"
        self.assertTrue(TestChecker.test(input,expect,500))

    def test_constructor1(self):
        input = """
        Class A{
            Var x: Int;
            Val y: Float = 1.1;
            Constructor(a: Int; b: Float){
                Self.x = a;
                Self.y = b;
            }
        }
        Class Program {main(){}}
        """
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(y)),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,501))

    def test_constructor2(self):
        input = """
        Class A{
            Destructor(){Return 1;}
        }
        Class Program {main(){}}
        """
        expect = "Type Mismatch In Statement: MethodDecl(Id(Destructor),Instance,[],Block([Return(IntLit(1))]))"
        self.assertTrue(TestChecker.test(input,expect,502))

    # def test_assignStmt(self):
    #     input = """
    #     Class A{
    #         Var $y: Int = 1;
    #     }
    #     Class B{
    #         method(){
    #             Val x: Int = 1;
    #             x = A::$y;
    #         }
    #     }

    #     Class Program {main(){}}
    #     """
    #     expect = "Cannot Assign To Constant: AssignStmt(Id(x),FieldAccess(Id(A),Id($y)))"
    #     self.assertTrue(TestChecker.test(input,expect,497))

    # def test_assignStmt(self):
    #     input = """
    #     Class A{
    #         Var $y: Int = 1;
    #     }
    #     Class B{
    #         method(){
    #             Val x: Int = 1;
    #             x = A::$y;
    #         }
    #     }

    #     Class Program {main(){}}
    #     """
    #     expect = "Cannot Assign To Constant: AssignStmt(Id(x),FieldAccess(Id(A),Id($y)))"
    #     self.assertTrue(TestChecker.test(input,expect,497))

    # def test_break4(self):
    #     input = """
    #     Class A{
    #         $method(x: Int){
    #             Foreach (x In 5 .. 2 By x){
    #             }
    #             Break;
    #             Return 1;
    #         }
    #     }
    #     Class Program {main(){} submain(){ Return A::$method(1); } }
    #     """
    #     expect = "Break Not In Loop"
    #     self.assertTrue(TestChecker.test(input,expect,476))
    # def test_returnStmt1(self):
    #     input = """
    #     Class Program {
    #         main(){
    #             Var a: Int = 1;
    #             Var b: Int = 1;
    #             Return 1 + a + b;
    #         }
    #     }
    #     """
    #     expect = "[None]"
    #     self.assertTrue(TestChecker.test(input,expect,441))
    # def test_FieldAccess1(self):
    #     input = """ #     Class Program {
    #         main(){}
    #     }
    #     Class A{
    #         Val get: Int = 1;
    #     }
    #     Class B : A{
    #         main(){
    #             Var x: Int = B.get;
    #         }
    #     }

    #     """
    #     expect = "Redeclared Attribute: a"
    #     self.assertTrue(TestChecker.test(input,expect,411))
    # def test_Arr1(self):
    #     input = """
    #     Class A {
    #         Var a: Array[Int, 2] = Array(1.1, 2.1);
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),List(IntLiteral(4)))"
    #     self.assertTrue(TestChecker.test(input,expect,407))

    # def test_Int2(self):
    #     input = """
    #     Class A {
    #         Var a: Int = 1;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),List(IntLiteral(4)))"
    #     self.assertTrue(TestChecker.test(input,expect,408))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: int main() {} """
    #     input = Program([FuncDecl(Id("main"),[],IntType(),Block([],[
    #         CallExpr(Id("foo"),[])]))])
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([],[
    #                 CallExpr(Id("putIntLn"),[
    #                     CallExpr(Id("getInt"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),List(IntLiteral(4)))"
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_diff_numofparam_stmt_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([],[
    #                 CallExpr(Id("putIntLn"),[])]))])
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),List())"
    #     self.assertTrue(TestChecker.test(input,expect,405))
    