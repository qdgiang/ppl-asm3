
"""
 * @author nhphung
"""
#from numpy import block
#from re import A
# 13/5
#from attr import field
from AST import * 
from Visitor import *
from StaticError import *

class MType:
    def __init__(self, partype: list, rettype: Type):
        self.partype = partype
        self.rettype = rettype

    def __str__(self) -> str:
        res = "\n"
        for par in self.partype:
            res += str(par) + ", "
        res = res[:-2]
        res += "-> " + str(self.rettype)
        res += "\n"
        return res

class AttributeEntry:
    def __init__(self, name: str, typ: Type, isStatic: bool = False, isConstant: bool = False, value = None) -> None:
        self.name = name
        self.typ = typ # value is IntType or FloatType... NOT an object of the class like IntType()
        self.isStatic = isStatic
        self.isConstant = isConstant
        self.value = value

    def __str__(self) -> str:
        return "Attribute: " + self.name + ", " + str(self.typ) + ", isStatic: " + str(self.isStatic) + ", isConst: " + str(self.isConstant) + ", " + str(self.value) + "\n"

    # to get class template name when attribute.typ is a ClassType()
    # clâss X{}
    # Var x: X
    # For exmaple: x.a, we use this method to get the name of classtype of x, which is X, else return None
    def get_class_type(self) -> str:
        if isinstance(self.typ, ClassType):
            return self.typ.classname.name
        else:
            return None
class MethodManager:
    def __init__(self, name: str, typ: MType, isStatic: bool = False, isConstant: bool = False, value = None) -> None:
        self.name = name
        self.typ = typ
        self.isStatic = isStatic
        self.isConstant = isConstant
        self.value = value
        self.declDict = {}
        # key: level - str, value: AttributeEntry

    def __str__(self) -> str:
        res = "Method: " + self.name + ", " + str(self.typ) + "isStatic: " + str(self.isStatic) + ", isConst: " + str(self.isConstant) + ", " + str(self.value) + "\n"
        res += "Local var and val declared:\n"
        for _, val in self.declDict.items():
            res += str(val)
        return res



    def add_decl(self, entry: AttributeEntry):
        self.declDict[entry.name] = entry
    
    # if declared already, return true
    def check_decl(self, name: str) -> bool:
        return name in self.declDict

    def get_decl(self, name: str) -> AttributeEntry:
        return self.declDict.get(name, None)

class ClassManger:
    def __init__(self, name : str) -> None:
        self.name = name
        self.attributeDict = {}
        # key: attribute name, value: AttributeEntry

        self.methodDict = {}
        # key: method name, value: MethodManager
        # use for both method scope

        self.blockDict = {}
        # key: block name, value: Method Manager
        # use for block scope

        self.inClass = True # in class scope
        self.inMethod = False # in method scope, if both false => use blocklevel, since method and block are at same place here
        self.currentMethod = "0not_in_method0"
        self.blockLevel = 0

    def __str__(self) -> str:
        res = "ATTRIBUTE DECLARED:\n"
        for _, value in self.attributeDict.items():
            res += str(value)
        res += "METHOD DECLARED:\n"
        for _, value in self.methodDict.items():
            res += str(value)
        res += "BLOCK DECLARED:\n"
        for _, value in self.blockDict.items():
            res += str(value)
        return res
    def add_attribute(self, entry: AttributeEntry):
        if self.inClass:
            self.attributeDict[entry.name] = entry
        else:
            if self.inMethod:
                self.methodDict[self.currentMethod].add_decl(entry)
            else:
                self.blockDict[str(self.blockLevel) + "block"].add_decl(entry)
        
    
    def add_method(self, entry: MethodManager):
        self.methodDict[entry.name] = entry

    # check if attribute is already defined
    def check_attribute(self, name: str) -> bool:
        if self.inClass:
            return name in self.attributeDict
        else:
            if self.inMethod:
                return self.methodDict[self.currentMethod].check_decl(name)
            else:
                for i in range(self.blockLevel, 0, -1):
                    if self.blockDict[str(i) + "block"].check_decl(name) is True:
                        return True
                if self.methodDict[self.currentMethod].check_decl(name) is True:
                    return True

                #if name in self.attributeDict:
                #    return True
                #if self.methodDict[self.currentMethod].check_decl(name) is True:
                    #return True
                #for i in range (1, self.blockLevel + 1):
                    #if self.blockDict[str(i) + "block"].check_decl(name) is True:
                        #return True
        return False
                        # in method decl and and block
    def check_method(self, name: str) -> bool:
        return name in self.methodDict

    def get_attribute(self, name: str) -> AttributeEntry:
        if self.inClass:
            return self.attributeDict.get(name, None)
        else:
            if self.inMethod:
                return self.methodDict[self.currentMethod].get_decl(name)
            else:
                #if self.attributeDict.get(name, None) is not None:
                #    return self.attributeDict.get(name, None)
                if self.methodDict[self.currentMethod].get_decl(name) is not None:
                    return self.methodDict[self.currentMethod].get_decl(name)
                else:
                    for i in range (self.blockLevel, 0, -1):
                        if self.blockDict[str(i) + "block"].get_decl(name) is not None:
                            return self.blockDict[str(i) + "block"].get_decl(name)

                    if self.methodDict[self.currentMethod].get_decl(name) is not None:
                        return self.methodDict[self.currentMethod].get_decl(name)
            return None

    def get_attribute_only_in_class(self, name: str) -> AttributeEntry:
        return self.attributeDict.get(name, None)

    def check_attribute_only_in_class(self, name: str) -> bool:
        return name in self.attributeDict

    def get_method(self, name: str) -> AttributeEntry:
        method_manager = self.methodDict[name]
        entry = AttributeEntry(method_manager.name, method_manager.typ.rettype, method_manager.isStatic, method_manager.isConstant, method_manager.value)
        return entry

    def check_attribute_only_current_scope(self, name: str):
        if self.inClass:
            return name in self.attributeDict
        else:
            if self.inMethod:
                return self.methodDict[self.currentMethod].check_decl(name)
            else:
                return self.blockDict[str(self.blockLevel) + "block"].check_decl(name)

    def check_attribute_only_current_scope_and_method(self, name: str):
        if self.inClass:
            return name in self.attributeDict
        else:
            if self.inMethod:
                return self.methodDict[self.currentMethod].check_decl(name)
            else:
                if self.methodDict[self.currentMethod].check_decl(name) is True:
                    return True
                else:
                    for i in range(self.blockLevel, 0, -1):
                        if self.blockDict[str(i) + "block"].check_decl(name) is True:
                            return True
                return False

    def get_attribute_only_current_scope(self, name: str):
        if self.inClass:
            return self.attributeDict.get(name, None)
        else:
            if self.inMethod:
                return self.methodDict[self.currentMethod].get_decl(name)
            else:
                return self.blockDict[str(self.blockLevel) + "block"].get_decl(name)

    def enter_method(self, name: str):
        self.inClass = False
        self.inMethod = True
        self.currentMethod = name

    def exit_method(self):
        self.inClass = True
        self.inMethod = False
        self.currentMethod = "0not_in_method0"

    def enter_block(self):
        self.inClass = False
        self.inMethod = False
        self.blockLevel += 1
        block_name = str(self.blockLevel) + "block"
        new_block = MethodManager(block_name, MType([], VoidType()))
        self.blockDict[block_name] = new_block

    def exit_block(self):
        if self.blockLevel < 2: # if block >= 2, it is a block within block. Exiting it doesn't auto mean we are in method now
            self.inClass = False
            self.inMethod = True
        self.blockDict.pop(str(self.blockLevel) + "block", None)
        self.blockLevel -= 1

    def log(self):
        print("Class: " + self.name)
        print("inClass: " + str(self.inClass))
        print("inMethod: " + str(self.inMethod))
        print("currentMethod: " + self.currentMethod)
        print("blockLevel: " + str(self.blockLevel))

class GlobalManager:
    def __init__(self):
        self.classdict = {}
        # key: class name
        # value: a ClassManger object
        self.currentScope = "0NotInClass"

    def __str__(self) -> str:
        res = ""
        for nam, value in self.classdict.items():
            res += "-" * 30
            res += " Class: " + nam + " "
            res += "-" * 30 + "\n"
            res += str(value) 
            res += "\n"
        return res
        

    def add_class(self, name: str):
        self.classdict[name] = ClassManger(name)

    def check_class(self, name: str):
        return name in self.classdict
        
    def add_attribute(self, entry: AttributeEntry):
        self.classdict[self.currentScope].add_attribute(entry)

    def add_method(self, entry: MethodManager):
        self.classdict[self.currentScope].add_method(entry)

    def check_attribute(self, name: str) -> bool:
        return self.classdict[self.currentScope].check_attribute(name)

    def check_method(self, name: str) -> bool:
        return self.classdict[self.currentScope].check_method(name)

    def get_attribute(self, name: str):
        return self.classdict[self.currentScope].get_attribute(name)

    def enter_class(self, name: str):
        self.currentScope = name

    def exit_class(self):
        self.currentScope = "0NotInClass"

    def enter_method(self, name: str):
        self.classdict[self.currentScope].enter_method(name)

    def exit_method(self):
        self.classdict[self.currentScope].exit_method()

    def enter_block(self):
        self.classdict[self.currentScope].enter_block()

    def exit_block(self):
        self.classdict[self.currentScope].exit_block()

    def log(self):
        self.classdict[self.currentScope].log()

    def get_attribute_from_class(self, class_name: str, name: str) -> AttributeEntry:
        return self.classdict[class_name].get_attribute_only_in_class(name)

    def get_method_from_class(self, class_name: str, name: str) -> MethodManager:
        return self.classdict[class_name].get_method(name)

    def check_attribute_from_class(self, class_name: str, name: str) -> bool:
        return self.classdict[class_name].check_attribute_only_in_class(name)

    def check_method_from_class(self, class_name: str, name: str) -> bool:
        return self.classdict[class_name].check_method(name)

    def check_attribute_only_current_scope(self, name: str) -> bool:
        return self.classdict[self.currentScope].check_attribute_only_current_scope(name)

    def check_attribute_only_current_scope_and_method(self, name: str) -> bool:
        return self.classdict[self.currentScope].check_attribute_only_current_scope_and_method(name)

    def get_attribute_only_current_scope(self, name) -> bool:
        return self.classdict[self.currentScope].get_attribute_only_current_scope(name)
class UtilityInfo:
    def __init__(self):
        self.inLoop = False
        self.hasEntryPoint = False
        self.consDeclared = 0
        self.inConstructor = False
        self.inDestructor = False
        self.inEntryMethod = False
        self.inParameterDecl = False
        self.binTypeList = {
            ("+", IntType, IntType): IntType(),
            ("+", FloatType, FloatType): FloatType(),
            ("-", IntType, IntType): IntType(),
            ("-", FloatType, FloatType): FloatType(),
            ("*", IntType, IntType): IntType(),
            ("*", FloatType, FloatType): FloatType(),
            ("/", IntType, IntType): IntType(),
            ("/", FloatType, FloatType): FloatType(),
            ("%", IntType, IntType): IntType(),
            ("&&", BoolType, BoolType): BoolType(),
            ("||", BoolType, BoolType): BoolType(),
            ("==.", StringType, StringType): BoolType(),
            ("+.", StringType, StringType): StringType(),
            ("==", IntType, IntType): BoolType(),
            ("==", BoolType, BoolType): BoolType(),
            ("!=", IntType, IntType): BoolType(),
            ("!=", BoolType, BoolType): BoolType(),
            ("<", IntType, IntType): BoolType(),
            ("<", FloatType, FloatType): BoolType(),
            ("<=", IntType, IntType): BoolType(),
            ("<=", FloatType, FloatType): BoolType(),
            (">", IntType, IntType): BoolType(),
            (">", FloatType, FloatType): BoolType(),
            (">=", IntType, IntType): BoolType(),
            (">=", FloatType, FloatType): BoolType(),
        }

        self.unaryTypeList = {
            ("-", IntType): IntType(),
            ("-", FloatType): FloatType(),
            ("!", BoolType): BoolType(),
        }

    def enter_loop(self):
        self.inLoop = True
    
    def get_bin_type(self, op: str, left: type, right: type) -> Type:
        return self.binTypeList.get((op, left, right), None)

    def get_unary_type(self, op: str, right: type) -> Type:
        return self.unaryTypeList.get((op, right), None)

    def exit_loop(self):
        self.inLoop = False

    def enter_special_method(self, name: str, classname: str, isPotentialEntry: bool):
        if name == "Constructor":
            self.inConstructor = True
        if name == "Destructor":
            self.inDestructor = True
        if name == "main" and classname == "Program" and isPotentialEntry:
            self.hasEntryPoint = True
            self.inEntryMethod = True
        self.inParameterDecl = True

    def exit_paremeter_decl(self):
        self.inParameterDecl = False

    def exit_special_method(self):
        self.inConstructor = False
        self.inDestructor = False
        self.inEntryMethod = False
        self.inMethodDecl = False
    
    def exit_constructor(self):
        self.inConstructor = False

    def enter_destructor(self):
        self.inDestructor = True

    def exit_destructor(self):
        self.inDestructor = False
    
    def check_in_loop(self) -> bool:
        return self.inLoop

class StaticChecker(BaseVisitor):

    """
    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType()))
    ]"""
            
    
    def __init__(self,ast):
        self.ast = ast
        self.manager = GlobalManager()
        self.helper = UtilityInfo()
    
    def check(self): 
        return self.visit(self.ast, None)

    def visit(self, ast, c):
        if isinstance(ast, Id):
            return self.visitId(ast, c)
        elif isinstance(ast, BinaryOp):
            return self.visitBinaryOp(ast, c)
        elif isinstance(ast, UnaryOp):
            return self.visitUnaryOp(ast, c)
        elif isinstance(ast, CallExpr):
            return self.visitCallExpr(ast, c)
        elif isinstance(ast, NewExpr):
            return self.visitNewExpr(ast, c)
        elif isinstance(ast, ArrayCell):
            return self.visitArrayCell(ast, c)
        elif isinstance(ast, FieldAccess):
            return self.visitFieldAccess(ast, c)
        elif isinstance(ast, IntLiteral):
            return self.visitIntLiteral(ast, c)
        elif isinstance(ast, FloatLiteral):
            return self.visitFloatLiteral(ast, c)
        elif isinstance(ast, StringLiteral):
            return self.visitStringLiteral(ast, c)
        elif isinstance(ast, BooleanLiteral):
            return self.visitBooleanLiteral(ast, c)
        elif isinstance(ast, NullLiteral):
            return self.visitNullLiteral(ast, c)
        elif isinstance(ast, SelfLiteral):
            return self.visitSelfLiteral(ast, c)
        elif isinstance(ast, ArrayLiteral):
            return self.visitArrayLiteral(ast, c)
        elif isinstance(ast, Assign):
            self.visitAssign(ast, c)
        elif isinstance(ast, If):
            self.visitIf(ast, c)
        elif isinstance(ast, For):
            self.visitFor(ast, c)
        elif isinstance(ast, Break):
            self.visitBreak(ast, c)
        elif isinstance(ast, Continue):
            self.visitContinue(ast, c)
        elif isinstance(ast, Return):
            self.visitReturn(ast, c)
        elif isinstance(ast, CallStmt):
            self.visitCallStmt(ast, c)
        elif isinstance(ast, VarDecl):
            self.visitVarDecl(ast, c)
        elif isinstance(ast, Block):
            self.visitBlock(ast, c)
        elif isinstance(ast, ConstDecl):
            self.visitConstDecl(ast, c)
        elif isinstance(ast, ClassDecl):
            self.visitClassDecl(ast, c)
        elif isinstance(ast, Instance):
            self.visitInstance(ast, c)
        elif isinstance(ast, Static):
            self.visitStatic(ast, c)
        elif isinstance(ast, MethodDecl):
            self.visitMethodDecl(ast, c)
        elif isinstance(ast, AttributeDecl):
            self.visitAttributeDecl(ast, c)
        elif isinstance(ast, IntType):
            self.visitIntType(ast, c)
        elif isinstance(ast, FloatType):
            self.visitFloatType(ast, c)
        elif isinstance(ast, BoolType):
            self.visitBoolType(ast, c)
        elif isinstance(ast, StringType):
            self.visitStringType(ast, c)
        elif isinstance(ast, ArrayType):
            self.visitArrayType(ast, c)
        elif isinstance(ast, ClassType):
            self.visitClassType(ast, c)
        elif isinstance(ast, VoidType):
            self.visitVoidType(ast, c)
        elif isinstance(ast, Program):
            return self.visitProgram(ast, c)
        
    def visitProgram(self, ast: Program, c):
        for decl in ast.decl:
            self.visit(decl, c)
        if self.helper.hasEntryPoint is False:
            raise NoEntryPoint()
        return []

    def visitClassDecl(self, ast: ClassDecl, c):
        name = ast.classname.name

        if ast.parentname is not None:
            parname = ast.parentname.name
            if self.manager.check_class(parname) is False:
                raise Undeclared(Class(), parname)
        
        if self.manager.check_class(name) is True:
            raise Redeclared(Class(), name)

        self.manager.add_class(name)
        self.manager.enter_class(name)
        for decl in ast.memlist:
            self.visit(decl, c)
        self.manager.exit_class()

    def visitAttributeDecl(self, ast: AttributeDecl, c):
        isStatic = True if isinstance(ast.kind, Static) else False
        if isinstance(ast.decl, VarDecl):
            name = ast.decl.variable.name
            typ = ast.decl.varType #IntType(), FloatType(), StringType(), ArrayType, ClassType
            if isinstance(ast.decl.varType, ClassType) and isinstance(ast.decl.varInit, NewExpr):
                if ast.decl.varType.classname.name != ast.decl.varInit.classname.name:
                    raise TypeMismatchInStatement(ast)
            isConstant = False
            if ast.decl.varInit is not None:
                expr_entry = self.visit(ast.decl.varInit, c)
                expr_type = expr_entry.typ #IntType() ..
                if type(typ) is FloatType:
                    if type(expr_type) is IntType:
                        expr_type = FloatType()
                if type(typ) is not type(expr_type):
                    raise TypeMismatchInStatement(ast)

        else: #is ConstDecl
            name = ast.decl.constant.name
            typ = ast.decl.constType
            if isinstance(ast.decl.constType, ClassType) and isinstance(ast.decl.value, NewExpr):
                if ast.decl.constType.classname.name != ast.decl.value.classname.name:
                    raise TypeMismatchInStatement(ast)
            isConstant = True
            if ast.decl.value is None:
                raise IllegalConstantExpression(None)
            expr_entry = self.visit(ast.decl.value, c)
            expr_type = expr_entry.typ
            if type(typ) is FloatType:
                if type(expr_type) is IntType:
                    expr_type = FloatType()
            if type(typ) is not type(expr_type):
                raise TypeMismatchInStatement(ast)

        if self.manager.check_attribute(name) is True:
            raise Redeclared(Attribute(), name)
        entry = AttributeEntry(name, typ, isStatic, isConstant)
        self.manager.add_attribute(entry)

    def visitMethodDecl(self, ast: MethodDecl, c):
        isStatic = True if isinstance(ast.kind, Static) else False
        name = ast.name.name
        if self.manager.check_method(name) is True:
            raise Redeclared(Method(), name)

        entry = MethodManager(name, MType([], VoidType()), isStatic, False)
        self.manager.add_method(entry)
        isPotentialEntry = False if ast.param != [] else True

        self.helper.enter_special_method(name, self.manager.currentScope, isPotentialEntry)
        self.manager.enter_method(name)

        for par in ast. param:
            self.visit(par, c)
        self.helper.exit_paremeter_decl()
        self.visit(ast.body,c)

        self.helper.exit_special_method()
        self.manager.exit_method()

    def visitVarDecl(self, ast: VarDecl, c):
        name = ast.variable.name
        if self.helper.inParameterDecl is True:
            if self.manager.check_attribute_only_current_scope_and_method(name) is True:
                raise Redeclared(Parameter(), name)
        #if self.manager.check_attribute(name) is True:
            #if self.helper.inParameterDecl:
                #raise Redeclared(Parameter(), name)
            #else:
                #raise Redeclared(Variable(), name)
        if self.manager.check_attribute_only_current_scope_and_method(name) is True:
            raise Redeclared(Variable(), name)
        typ = ast.varType #IntType(), FloatType(), StringType(), ArrayType(), ClassType()


        if isinstance(ast.varType, ClassType) and isinstance(ast.varInit, NewExpr):
            if ast.varType.classname.name != ast.varInit.classname.name:
                raise TypeMismatchInStatement(ast)
        if ast.varInit is not None:
            expr = self.visit(ast.varInit,c)
            expr_type = expr.typ #IntType() ..
            if type(typ) is FloatType:
                if type(expr_type) is IntType:
                    expr_type = FloatType()

            if type(typ) is not type(expr_type): # init value is not of same type as declared
                raise TypeMismatchInStatement(ast)
        self.manager.add_attribute(AttributeEntry(name, typ, False, False))


    def visitConstDecl(self, ast: ConstDecl, c):
        name = ast.constant.name
        if self.manager.check_attribute_only_current_scope_and_method(name) is True:
            raise Redeclared(Constant(), name)
        typ = ast.constType #IntType(), FloatType(), StringType(), ArrayType(), ClassType()
        if isinstance(ast.value, NullLiteral):
            raise IllegalConstantExpression(ast.value)

        if ast.value is None: # no init value
            raise IllegalConstantExpression(None)
        else:
            if isinstance(ast.constType, ClassType) and isinstance(ast.value, NewExpr):
                if ast.constType.classname.name != ast.value.classname.name:
                    raise TypeMismatchInStatement(ast)
            expr = self.visit(ast.value, c)
            expr_type = expr.typ
            if type(typ) is FloatType:
                if type(expr_type) is IntType:
                    expr_type = FloatType()

            if type(typ) is not type(expr_type): # init value is not of same type as declared
                raise TypeMismatchInConstant(ast)

            if expr.value is None: # init as a NullLiteral
                raise IllegalConstantExpression(None)
        
        self.manager.add_attribute(AttributeEntry(name, typ, False, True))

    def visitBlock(self, ast: Block, c):
        self.manager.enter_block()
        for inst in ast.inst:
            self.visit(inst, c)

        self.manager.exit_block()
        
            
    def visitId(self, ast: Id, c):
        isStatic = True if ast.name[0] == "$" else False
        return AttributeEntry(ast.name, IntType(), isStatic)
        """
        if self.manager.check_attribute(ast.name) is not True:
            raise Undeclared(Identifier(), ast.name)
        else:
            entry = self.manager.get_attribute(ast.name)
        return entry"""

        
    def visitBinaryOp(self, ast: BinaryOp, c):
        left_entry = self.visit(ast.left, c)
        right_entry = self.visit(ast.right,c)

        left_type = type(left_entry.typ)
        right_type = type(right_entry.typ)
        if (left_type is IntType) and (right_type is FloatType):
            left_type = FloatType
        if (left_type is FloatType) and (right_type is IntType):
            right_type = FloatType
        if left_type is not right_type:
            raise TypeMismatchInExpression(ast)
        else:
            ret_type = self.helper.get_bin_type(ast.op, left_type, right_type)
            return AttributeEntry("temp_binary_expression", ret_type, False, False)
    def visitUnaryOp(self, ast: UnaryOp, c):
        entry = self.visit(ast, c)
        ret_type = self.helper.get_unary_type(ast.op, entry.typ)
        if ret_type is None:
            raise TypeMismatchInExpression(ast)
        else:
            return AttributeEntry("temp_unary_expression", entry.typ, False, False)


    def visitCallExpr(self, ast: CallExpr, c):
        method_name = ast.method.name
        if method_name[0] == "$": # static method
            class_entry = self.visit(ast.obj, c)
            class_name = class_entry.name
            if self.manager.check_class(class_name) is False:
                raise Undeclared(Class(), class_name)
            
            if self.manager.check_method_from_class(class_name, method_name) is False:
                raise Undeclared(Method(), method_name)

            method_entry = self.manager.get_method_from_class(class_name, method_name)
            return method_entry
        
        else: # instance method
            obj_temp_entry = self.visit(ast.obj, c) # actually only need the name
            if self.manager.check_attribute(obj_temp_entry.name) is False:
                raise Undeclared(Identifier(), obj_temp_entry.name)

            obj_entry_declared = self.manager.get_attribute(obj_temp_entry.name)
            classtype_of_obj = obj_entry_declared.get_class_type()
            
            if classtype_of_obj is None:
                raise TypeMismatchInConstant(ast)

            if self.manager.check_method_from_class(classtype_of_obj, method_name) is False:
                raise Undeclared(Method(), method_name)

            method_entry = self.manager.get_attribute_from_class(classtype_of_obj, method_name)
            return method_entry


    def visitNewExpr(self, ast: NewExpr, c):
        entry = AttributeEntry(ast.classname.name, ClassType(ast.classname), False, False)
        return entry

    def visitArrayCell(self, ast: ArrayCell, c):
        arr_tmp_entry = self.visit(ast.arr, c) #get name
        arr_entry = self.manager.get_attribute(arr_tmp_entry.name)
        if arr_entry is None:
            raise Undeclared(Identifier(), arr_tmp_entry.name)
        if type(arr_entry.typ) is not ArrayType:
            raise TypeMismatchInExpression(ast)

        else: #It is indeed an array
            for i in ast.idx:
                idx_tmp_entry = self.visit(i, c)
                if type(idx_tmp_entry.typ) is not IntType:
                    raise TypeMismatchInExpression(ast)

        return AttributeEntry("temp_array_cell", arr_entry.typ.eleType, False, False)


    def visitFieldAccess(self, ast: FieldAccess, c) -> AttributeEntry: 
        #If visitId, only can get the name
        class_obj = self.visit(ast.obj, c) # return attributeEntry
        #if type(ast.obj) is Id:
        #    obj_name = class_obj.name
        field_name = ast.fieldname.name #return a string

        if isinstance(ast.obj, SelfLiteral):
            if self.manager.check_attribute_from_class(self.manager.currentScope, field_name) is False:
                raise Undeclared(Attribute(), field_name)
            else:
                entry = self.manager.get_attribute_from_class(self.manager.currentScope, field_name)
                if entry is None:
                    raise Undeclared(Attribute(), field_name)
                return entry

        if field_name[0] != "$": # access instance attribute
            if isinstance(ast.obj, FieldAccess):
                class_obj = self.visit(ast.obj, c)
                class_name_of_obj = class_obj.get_class_type()
                if self.manager.check_attribute_from_class(class_name_of_obj, field_name) is False:
                    raise Undeclared(Attribute(), field_name)
            else:
                if self.manager.check_attribute_only_current_scope(class_obj.name) is True:
                    true_class_obj = self.manager.get_attribute_only_current_scope(class_obj.name)
                else:
                    true_class_obj = self.manager.get_attribute(class_obj.name)
                class_name_of_true_obj = true_class_obj.get_class_type() # get from class_obj.typ.classname.name
                if class_name_of_true_obj is not None: #if the class_obj is indeed of ClassType, get a string of classdecl name
                    if self.manager.check_class(class_name_of_true_obj) is False:
                        raise Undeclared(Class(), class_name_of_true_obj)
                else:
                    raise IllegalMemberAccess(ast)
                if self.manager.check_attribute_from_class(class_name_of_true_obj, field_name) is False:
                    raise Undeclared(Attribute(), field_name)
                return self.manager.get_attribute_from_class(class_name_of_true_obj, field_name) # return attributeEntry that we are trying to access

        else: # access static attribute
            class_name = class_obj.name  # get from class_obj.name
            if self.manager.check_class(class_name) is False:
                raise Undeclared(Class(), class_name)

            if self.manager.check_attribute_from_class(class_name, field_name) is False:
                raise Undeclared(Attribute(), field_name) 

            return self.manager.get_attribute_from_class(class_name, field_name) # return attributeEntry that we are trying to access



    def visitIntLiteral(self, ast: IntLiteral, c):
        return AttributeEntry("temp_int_literal", IntType(), False, False, ast.value)

    def visitFloatLiteral(self, ast: FloatLiteral, c):
        return AttributeEntry("temp_float_literal", FloatType(), False, False, ast.value)

    def visitStringLiteral(self, ast: StringLiteral, c):
        return AttributeEntry("temp_string_literal", StringType(), False, False, ast.value)

    def visitBooleanLiteral(self, ast: BooleanLiteral, c):
        return AttributeEntry("temp_boolean_literal", BoolType(), False, False, ast.value)

    def visitNullLiteral(self, ast: NullLiteral, c):
        return AttributeEntry("temp_null_literal", VoidType(), False, False, None)

    # return a temporary attributeEntry that helps pointing to curent class by using the first attribute
    def visitSelfLiteral(self, ast: SelfLiteral, c):
        return AttributeEntry("temp_self_literal", ClassType(Id(self.manager.currentScope)), False, False)

    def visitArrayLiteral(self, ast: ArrayLiteral, c):
        #member_type = type(self.visit(ast.value[0], c).typ) # .typ return an OBJECT of IntType or ... so cast type to get the type
        member_type = self.visit(ast.value[0], c).typ
        for mem in ast.value:
            temp = self.visit(mem, c)
            if temp.typ is not member_type:
                raise IllegalArrayLiteral(ast)

        return AttributeEntry("temp_array_literal", ArrayType(len(ast.value), member_type), False, False)

    # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=158471#p491277
    def visitAssign(self, ast: Assign, c):
        lhs = self.visit(ast.lhs, c)
        if isinstance(ast.lhs, FieldAccess):
            lhs_entry = lhs
        else:
            if self.manager.check_attribute(lhs.name) is False:
                raise Undeclared(Identifier(), lhs.name)
            lhs_entry = self.manager.get_attribute(lhs.name)
        if isinstance(lhs_entry, AttributeEntry):
            if lhs_entry.isConstant is True:
                raise CannotAssignToConstant(ast)

        rhs = self.visit(ast.exp, c)
        if isinstance(ast.exp, Id):
            if self.manager.check_attribute(ast.exp.name) is False:
                raise Undeclared(Identifier(), ast.exp.name)
            rhs_entry = self.manager.get_attribute(rhs.name)
        else:
            rhs_entry = rhs
        left_type = lhs_entry.typ
        expr_type = rhs_entry.typ

        if type(left_type) is IntType and type(expr_type) is not IntType:
            raise TypeMismatchInStatement(ast)

        if type(left_type) is FloatType:
            if (type(expr_type) is not IntType) and (type(expr_type) is not FloatType):
                raise TypeMismatchInStatement(ast)
            else:
                expr_type = FloatType()


        if type(left_type) is not type(expr_type):
            raise TypeMismatchInStatement(ast)

        if type(left_type) is ArrayType and type(expr_type) is ArrayType:
            if (left_type.size != expr_type.size) or (type(left_type.eleType) is not type(expr_type.eleType)):
                raise TypeMismatchInStatement(ast)
        
    def visitIf(self, ast: If, c):
        expr = self.visit(ast.expr, c)
        if type(expr.typ) is not BoolType:
            raise TypeMismatchInStatement(ast)
        else:
            self.visit(ast.thenStmt, c)
            if ast.elseStmt is not None:
                self.visit(ast.elseStmt, c)

    def visitFor(self, ast: For, c):
        id_entry = self.visit(ast.id, c) # get name

        if self.manager.check_attribute(id_entry.name) is False:
            raise Undeclared(Identifier(), id_entry.name)
            #self.manager.add_attribute(AttributeEntry(id_entry.name, IntType(), False, False, 0))
        # TODO fix this
        #if type(id_entry.typ) is not IntType:
        #    raise TypeMismatchInStatement(ast)

        expr1_entry = self.visit(ast.expr1, c)
        if type(expr1_entry.typ) is not IntType:
            raise TypeMismatchInStatement(ast)

        if id_entry.isConstant is True:
            raise CannotAssignToConstant(Assign(Id(id_entry.name), IntLiteral(expr1_entry.value)))
        
        expr2_entry = self.visit(ast.expr2, c)
        if type(expr2_entry.typ) is not IntType:
            raise TypeMismatchInStatement(ast)
        self.helper.enter_loop
        self.visit(ast.loop, c)
        self.helper.exit_loop

    def visitBreak(self, ast: Break, c):
        if self.helper.check_in_loop() is False:
            raise MustInLoop(ast)

    def visitContinue(self, ast: Continue, c):
        if self.helper.check_in_loop() is False:
            raise MustInLoop(ast)

    def visitReturn(self, ast: Return, c):
        if self.helper.inConstructor or self.helper.inDestructor:
            raise TypeMismatchInStatement(ast)

        if self.helper.inEntryMethod:
            if ast.expr is not None:
                raise TypeMismatchInStatement(ast)

    def visitCallStmt(self, ast: CallStmt, c):
        method_name = ast.method.name
        if method_name[0] == "$": # static method
            class_entry = self.visit(ast.obj, c)
            class_name = class_entry.name
            if self.manager.check_class(class_name) is False:
                raise Undeclared(Class(), class_name)
            
            if self.manager.check_method_from_class(class_name, method_name) is False:
                raise Undeclared(Method(), method_name)

            method_entry = self.manager.get_method_from_class(class_name, method_name)
            return method_entry
        
        else: # instance method
            obj_temp_entry = self.visit(ast.obj, c) # actually only need the name
            if self.manager.check_attribute(obj_temp_entry.name) is False:
                raise Undeclared(Identifier(), obj_temp_entry.name)

            obj_entry_declared = self.manager.get_attribute(obj_temp_entry.name)
            classtype_of_obj = obj_entry_declared.get_class_type()
            
            if classtype_of_obj is None:
                raise TypeMismatchInConstant(ast)

            if self.manager.check_method_from_class(classtype_of_obj, method_name) is False:
                raise Undeclared(Method(), method_name)

            method_entry = self.manager.get_attribute_from_class(classtype_of_obj, method_name)
            return method_entry

    def visitIntType(self, ast: IntType, c):
        pass

    def visitFloatType(self, ast: FloatType, c):
        pass

    def visitBoolType(self, ast: BoolType, c):
        pass

    def visitStringType(self, ast: StringType, c):
        pass

    def visitArrayType(self, ast: ArrayType, c):
        pass

    def visitClassType(self, ast: ClassType, c):
        pass

    def visitVoidType(self, ast: VoidType, c):
        pass

    def visitInstance(self, ast: Instance, c):
        pass

    def visitStatic(self, ast: Static, c):
        pass



        
    

