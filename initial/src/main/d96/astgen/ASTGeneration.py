# Student ID: 1952044
# Student name: Quach Dang Giang

from functools import reduce
from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *

def flatten(lst):
    res = []
    if (not isinstance(lst, list)):
        return lst
    elif (any(isinstance(el, list) for el in lst)):
        #return [item for sublist in lst for item in sublist]
        for sublist in lst:
            if (isinstance(sublist, list)):
                for item in sublist:
                    res.append(item)
            else:
                res.append(sublist)
        return res
    else:
        return lst

def toInt(text):
    if ('x' in text or 'X' in text):
        return int(text, 16)
    elif ('b' in text or 'B' in text):
        return int(text, 2)
    elif (text[0] == '0'):
        return int(text, 8)
    else:
        return int(text)


# program: classdecl* EOF;
class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        res = []
        for x in ctx.classdecl():
            res += [x.accept(self)]
        return Program(res)


    def visitClassdecl(self, ctx: D96Parser.ClassdeclContext):
        if (ctx.getChildCount() == 7):
            cname = Id(ctx.ID(0).getText())
            pname = Id(ctx.ID(1).getText())
        else:
            cname = Id(ctx.ID(0).getText())
            pname = None
        res = ClassDecl(cname, self.visit(ctx.member_list()), pname)
        if (cname.name == "Program"):
            for x in res.memlist:
                if (isinstance(x, MethodDecl) and x.name.name == "main" and x.param == []):
                    x.kind = Static()
        return res
    #member_list: member*;
    def visitMember_list(self, ctx: D96Parser.Member_listContext):
        res = []
        if (isinstance(ctx.member(), list)):
            for member in ctx.member():
                res += [member.accept(self)]
        else:
            res += [ctx.member().accept(self)]
        return flatten(res)
        #return res

    # member: attribute | method;
    def visitMember(self, ctx: D96Parser.MemberContext):
        if (ctx.attribute()):
            return self.visit(ctx.attribute())
        else:
            return self.visit(ctx.method())
    # attribute: (VAL | VAR) id_list COLON (typename | ID) (ASSIGNOP expr_list)? SEMI;
    def visitAttribute(self, ctx:D96Parser.AttributeContext):
        id_list = self.visit(ctx.id_list())
        type_name = self.visit(ctx.typename()) #if ctx.typename() else Id(ctx.ID().getText())
        kind = lambda id: Static() if '$' in str(id) else Instance()
        decl = lambda is_immutable, id, type_name, expr: ConstDecl(id, type_name, expr) if is_immutable else VarDecl(id ,type_name, expr)
        if (ctx.ASSIGNOP()):  #initialization
            expr_list = self.visit(ctx.expr_list())
            res = [AttributeDecl(kind(id),decl(ctx.VAL(),id,type_name,expr)) for id, expr in zip(id_list, expr_list)]
            return res
        else:   #no initialization
            if (isinstance(self.visit(ctx.typename()),ClassType)):  #initialization for ClassType
                if (ctx.VAL()): #immutable => None
                    return [AttributeDecl(kind(id),ConstDecl(id,type_name,None)) for id in id_list]
                else:   #mutable => NullLiteral
                    return [AttributeDecl(kind(id),decl(ctx.VAL(),id,type_name,NullLiteral())) for id in id_list]
            else:   #initialization for other types
                res = [AttributeDecl(kind(id),decl(ctx.VAL(),id,type_name,None)) for id in id_list]
                return res
        
    # id_list: (ID | DOLLARID) (CM (ID | DOLLARID))*;
    def visitId_list(self, ctx: D96Parser.Id_listContext):
        res = []
        for i in range(ctx.getChildCount()):
            if (i % 2 == 0):
                res += [Id(ctx.getChild(i).getText())]
        return res 
    # return [Id(a),[Id(b)]]
    
    def visitMethod(self, ctx: D96Parser.MethodContext):
        if(ctx.cons_method()):
            return self.visit(ctx.cons_method())
        elif(ctx.dest_method()):
            return self.visit(ctx.dest_method())
        else:
            tmp = Instance() if ctx.ID() else Static()
            paralist = self.visit(ctx.paralist()) if (ctx.paralist()) else []
            #if (ctx.getChild(0).getText() == 'main'):
                #return [MethodDecl(
                    #Static(),
                    #Id("main"),
                    #[],
                    #self.visit(ctx.block_statement()))]            
            return [MethodDecl(
                tmp,
                Id(ctx.getChild(0).getText()),
                paralist,
                self.visit(ctx.block_statement()))] 

    def visitCons_method(self, ctx: D96Parser.Cons_methodContext):
        paralis = self.visit(ctx.paralist()) if (ctx.paralist()) else []
        return MethodDecl(
            Instance(),
            Id('Constructor'),
            paralis,
            self.visit(ctx.block_statement()))


    def visitDest_method(self, ctx: D96Parser.Dest_methodContext):
        return MethodDecl(
            Instance(),
            Id('Destructor'),
            [],
            self.visit(ctx.block_statement()))

    def visitParalist(self, ctx: D96Parser.ParalistContext):
        return flatten(list(map(lambda x: x.accept(self), ctx.parameter())))
    
    def visitParameter(self, ctx: D96Parser.ParameterContext):
        kind = lambda id: Static() if '$' in str(id) else Instance()
        res = []
        #if (ctx.typename()):
        for x in self.visit(ctx.id_list()):
            res += [VarDecl(x, self.visit(ctx.typename()), None)]
        return res
        #else:
        #    for x in self.visit(ctx.id_list()):
        #        res += [VarDecl(x, Id(ctx.ID().getText()), None)]
        #    return res

    def visitBlock_statement(self, ctx: D96Parser.Block_statementContext):
        if (ctx.statement_list()):
            #return Block(flatten(self.visit(ctx.statement_list()))) 
            return Block(flatten(self.visit(ctx.statement_list())))
        else:
            return Block([])

    def visitStatement_list(self, ctx: D96Parser.Statement_listContext):
        
        res = []
        if (isinstance(ctx.statement(),list)):
            for x in ctx.statement():
                res += [self.visit(x)]
        else:
            res += [self.visit(ctx.statement())]
        return res
        #single list of statement class
    
    def visitStatement(self, ctx: D96Parser.StatementContext):
        return ctx.getChild(0).accept(self)
    
    def visitVar_dec(self, ctx: D96Parser.Var_decContext):
        id_list = self.visit(ctx.id_list())
        type_name = self.visit(ctx.typename()) #if ctx.typename() else ClassType(Id(ctx.ID().getText()))
        decl = lambda is_immutable, id, type_name, expr: ConstDecl(id, type_name, expr) if is_immutable else VarDecl(id ,type_name, expr)
        if (ctx.ASSIGNOP()):
            expr_list = self.visit(ctx.expr_list())
            res = [decl(ctx.VAL(),id,type_name,expr) for id, expr in zip(id_list, expr_list)]
            return res
        else:
            if (isinstance(self.visit(ctx.typename()),ClassType)):
                if (ctx.VAL()):
                    return [ConstDecl(id,type_name,None) for id in id_list]
                else:
                    res = [decl(ctx.VAL(),id,type_name,NullLiteral()) for id in id_list]
                    return res
            else: 
                res = [decl(ctx.VAL(),id,type_name,None) for id in id_list]
                return res
    def visitAssign_sta(self, ctx: D96Parser.Assign_staContext):
        """if (ctx.getChildCount() == 4):
            if(ctx.ID()):
                return Assign(Id(ctx.ID().getText()), ctx.expr().accept(self))
            elif(ctx.DOLLARID()):
                
                return Assign(Id(ctx.DOLLARID().getText()), ctx.expr().accept(self))
        elif (ctx.getChildCount() == 5):
            expr = self.visit(ctx.index_operator())
            temp = [self.visit(x) for x in expr] if isinstance(expr,List) else self.visit(expr)
            res = ArrayCell(ctx.getChild(0).accept(self),temp)
            return res
        else:"""
        lhs = ctx.getChild(0).accept(self)
        rhs = ctx.getChild(2).accept(self)
        return Assign(lhs, rhs)
    
    def visitIf_statement(self, ctx: D96Parser.If_statementContext):
        expr_list = []
        block_list = []
        if_expr, if_block = self.visit(ctx.if_clause())
        expr_list += [if_expr]
        block_list += [if_block]
        if (ctx.elseif_clause()):
            elseif_expr, elseif_block = self.visit(ctx.elseif_clause()) 
            if (isinstance(elseif_expr, list)):
                expr_list += elseif_expr
                block_list += elseif_block
            else:
                expr_list += [elseif_expr]
                block_list += [elseif_block]

            if (ctx.else_clause()):
                block_list += [self.visit(ctx.else_clause())]
                temp = If(
                    expr_list[-1].accept(self), 
                    block_list[-2].accept(self), 
                    block_list[-1].accept(self))

                for e,b in zip(expr_list[:-1][::-1], block_list[:-2][::-1]):
                    temp = If(self.visit(e), self.visit(b), temp)
                return temp
            else:
                temp = None 
                for e,b in zip(expr_list[::-1], block_list[::-1]):
                    temp = If(self.visit(e), self.visit(b), temp)
                return temp
        if (ctx.else_clause()):
            else_block = self.visit(ctx.else_clause())
            return If(if_expr.accept(self),if_block.accept(self),else_block.accept(self))
        
        return If(if_expr.accept(self),if_block.accept(self),None)  
        
        
    def visitIf_clause(self, ctx: D96Parser.If_clauseContext):
        return ctx.expr(),ctx.block_statement()
    
    def visitElseif_clause(self, ctx: D96Parser.Elseif_clauseContext):
        return ctx.expr(),ctx.block_statement()
    
    def visitElse_clause(self, ctx: D96Parser.Else_clauseContext):
        return ctx.block_statement()

    def visitFor_in_statement(self, ctx: D96Parser.For_in_statementContext):
        id = Id(ctx.ID().getText()) if (ctx.ID()) else Id(ctx.DOLLARID().getText())
        expr1 = ctx.expr(0).accept(self)
        expr2 = ctx.expr(1).accept(self)
        expr3 = ctx.expr(2).accept(self) if (ctx.expr(2)) else IntLiteral(1)
        return For(
            id, 
            expr1, 
            expr2, 
            self.visit(ctx.block_statement()),
            expr3)
    def visitBreak_statement(self, ctx: D96Parser.Break_statementContext):
        return Break()
    
    def visitContinue_statement(self, ctx: D96Parser.Continue_statementContext):
        return Continue()
    def visitReturn_statement(self, ctx: D96Parser.Return_statementContext):
        return Return(ctx.expr().accept(self)) if (ctx.expr()) else Return(None)


    def visitMethod_statement(self, ctx: D96Parser.Method_statementContext):
        methodname = Id(ctx.getChild(2).getText())
        exprlist = self.visit(ctx.expr_list()) if (ctx.expr_list()) else []
        return CallStmt(
            ctx.expr().accept(self), 
            methodname,
            exprlist)
    
    def visitIndexedarray(self, ctx: D96Parser.IndexedarrayContext):
        #if(isinstance(ctx.lit(),list)):
            #return ArrayLiteral([self.visit(x) for x in ctx.lit()])
        #else:
            #return ArrayLiteral([self.visit(ctx.lit())])
        if (ctx.expr_list()):
            return ArrayLiteral(self.visit(ctx.expr_list()))
        else:
            return ArrayLiteral([])
    def visitMultiarray(self, ctx: D96Parser.MultiarrayContext):
        return ArrayLiteral([x for x in self.visit(ctx.arr_list())])

    def visitArr_list(self, ctx: D96Parser.Arr_listContext):
        if (ctx.arr_list()):
            return [ctx.getChild(0).accept(self)] + self.visit(ctx.arr_list())
        else:
            return [ctx.getChild(0).accept(self)]     
    def visitExpr_list(self, ctx: D96Parser.Expr_listContext):
        res = []
        if (isinstance(ctx.expr(),list)):
            for x in ctx.expr():
                res += [x.accept(self)]
            return res
        else:
            return [ctx.expr().accept(self)]   
    #return list of class
    
    def visitExpr(self, ctx: D96Parser.ExprContext):
        if (ctx.getChildCount() == 1):
            if (ctx.SELF()):
                return SelfLiteral()
            elif (ctx.NULL()):
                return NullLiteral()
            elif(ctx.ID()):
                return Id(ctx.ID().getText())
            elif(ctx.DOLLARID()):
                return Id(ctx.DOLLARID().getText())
            else:
                return ctx.getChild(0).accept(self)
        elif (ctx.getChildCount() == 2):
            if (ctx.index_operator()):
                expr = self.visit(ctx.index_operator())
                temp = [self.visit(x) for x in expr] if isinstance(expr,list) else self.visit(expr)
                res = ArrayCell(ctx.getChild(0).accept(self),temp)
                return res
            return UnaryOp(ctx.getChild(0).getText(), ctx.getChild(1).accept(self))
        elif (ctx.getChildCount() == 3):
            if (ctx.LP()):
                return ctx.getChild(1).accept(self)
            elif(ctx.DOT() or ctx.DOUBLECOLON()):
                return FieldAccess(
                    ctx.getChild(0).accept(self),
                    Id(ctx.getChild(2).getText()))
            else:
                return BinaryOp(
                    ctx.getChild(1).getText(), 
                    ctx.getChild(0).accept(self), 
                    ctx.getChild(2).accept(self))
        else:
            exprs = ctx.expr_list().accept(self) if (ctx.expr_list()) else []
            return CallExpr(
                ctx.getChild(0).accept(self),
                Id(ctx.getChild(2).getText()),
                exprs)
    #return single class

    def visitCreate_object(self, ctx: D96Parser.Create_objectContext):
        ID = Id(ctx.ID().getText())
        return NewExpr(ID, self.visit(ctx.expr_list())) if (ctx.expr_list()) else NewExpr(ID,[])
        #return single class

    def visitIndex_operator(self, ctx: D96Parser.Index_operatorContext):
        return ctx.expr()

    def visitLit(self, ctx: D96Parser.LitContext):
        if (ctx.INTLIT()):
            return IntLiteral(toInt(ctx.INTLIT().getText()))
        elif(ctx.FLOATLIT()):
            if (ctx.FLOATLIT().getText()[0] == '.'):
                res = '0' + ctx.FLOATLIT().getText()
                return FloatLiteral(float(res))
            else:
                return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif(ctx.STRINGLIT()):
            return StringLiteral(ctx.STRINGLIT().getText())    
        else:
            if (ctx.BOOLLIT().getText() == "True"):
                return BooleanLiteral(True)
            else:
                return BooleanLiteral(False)
        
    def visitTypename(self, ctx: D96Parser.TypenameContext):
        if (ctx.INTTYPE()):
            return IntType()
        elif (ctx.FLOATTYPE()):
            return FloatType()
        elif (ctx.BOOLTYPE()):
            return BoolType()
        elif (ctx.STRINGTYPE()):
            return StringType()
        elif (ctx.ID()):
            return ClassType(Id(ctx.ID().getText()))
        else:
            return self.visit(ctx.arr_decl())

    def visitArr_decl(self, ctx: D96Parser.Arr_declContext):
        return ArrayType(toInt(ctx.INTLIT().getText()), ctx.typename().accept(self))
