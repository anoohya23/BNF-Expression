"""
<expression>  ::=  <factor>  * <expression>   |   <factor>  /  <expression>   |   <factor>
<factor>  :==  <term> + <factor>  |  <term> - <factor>  |  <term>
<term>  ::=  {  <expression>  }  |  <literal>
<literal>  ::=  0|1|2|3|4|5|6|7|8|9
"""

class ExpTree:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class RecursiveDescent:

    #Returns the current token if bool=True if False return current token and increments token pointing to next charachter
    def getToken(self,bool=False):
        global token
        global str
        if (bool):
            if(token<len(str)): # The token won't be incremented if bool = True
                return str[token] # Will just return thr current token
            else:
                return
        if (token<len(str)): # IF bool=False then token will be incremented and it will be pointing to next token
            if(str[token].isdigit()):
                ch = ''
                while (True): ##IF number is more than 1 digit
                    if (token<len(str) and str[token].isdigit()):
                        ch = ch + str[token]
                        token += 1
                    else:
                        return ch
            else:
                token = token + 1
                return str[token-1]

    #functions returns Exptree to term having root as digit/Number and left and rigtht pointer as None/Null
    def literal(self):
        rd = RecursiveDescent()
        global str
        lit = rd.getToken()
        if(lit.isdigit()):
            return ExpTree(lit)
        else:
            return None

    #This Function check for whether the token is having {} or literal and calls the respective functions accordingly..
    def term(self):
        rd = RecursiveDescent()
        x=rd.getToken(True)
        #If token has {} then expression is called..
        if (x=='{'):
            rd.getToken()
            ex = rd.expression()
            if(ex!=None):
                r = rd.getToken()
                if(r=='}'):
                    return ex
                else:
                    return None
            else:
                return None
        # else it must have literal
        else:
            literal= rd.literal()
            if(literal!=None):
                return literal
            else:
                return None

    # This Function checks if token is having + or - if not it means its a term 
    def factor(self):
        rd = RecursiveDescent()
        global str
        ter = rd.term()
        if(ter!=None):
            oper=rd.getToken(True)
            #if token does not have + or - it means its a term.
            if(oper != '+' and oper!='-'):
                return ter
            #if it contains + or - then call factor function
            else:
                rd.getToken()
                fact=rd.factor()
                if(fact!=None):
                    return ExpTree(oper,ter,fact)
                else:
                    return None

    # This Function checks if token is having * or / if not it means its a factor 
    def expression(self):
        rd=RecursiveDescent()
        global str
        fact=rd.factor()
        if(fact==None):
            return None
        oper = rd.getToken(True)
        # if token does not have * or / it means its a factor..
        if(oper!='*' and oper!='/'):
            return fact
        else:
            rd.getToken()
            expr = rd.expression()
            if (expr!=None):
                return ExpTree(oper,fact,expr)
            else:
                return None
        return None

    def Evaluate(self,root):
        rd = RecursiveDescent()
        if (rd.leaf(root)):
            return int(root.val)

        #Recursive Function to evaluate the Exptree
        else:
            if (root.val == '+'):
                return rd.Evaluate(root.left) + rd.Evaluate(root.right)
            if (root.val == '-'):
                return rd.Evaluate(root.left) - rd.Evaluate(root.right)
            if (root.val == '*'):
                return rd.Evaluate(root.left) * rd.Evaluate(root.right)
            if (root.val == '/'):
                return rd.Evaluate(root.left) / rd.Evaluate(root.right)

    #if a node is leaf return True else returns False
    def leaf(self,root):
        if (root.left == None and root.right == None):
            return True
        else:
            return False

    def Inorder(self,head):
        if(head==None):
            return
        rd = RecursiveDescent()

        rd.Inorder(head.left)
        print(head.val,end="")
        rd.Inorder(head.right)

    def preOrder(self,head):
        if(head==None):
            return
        rd = RecursiveDescent()

        print(head.val, end="")
        rd.preOrder(head.left)
        rd.preOrder(head.right)

    def postOrder(self,head):
        if(head==None):
            return
        rd = RecursiveDescent()

        rd.postOrder(head.left)
        rd.postOrder(head.right)
        print(head.val, end="")


str=input("Enter String \n")
str=list(str)
#Remove White Spaces if any
for i in (str[:]):
    if (i==" "):
        str.remove(i)
token=0
rd=RecursiveDescent()
exptree=rd.expression()

print("Inorder is =>",end="")
rd.Inorder(exptree)
print()
print("Preorder is =>",end="")
rd.preOrder(exptree)
print()
print("Postorder is =>",end="")
rd.postOrder(exptree)
print()
print("Value of the Expression Tree is =>",round(rd.Evaluate(exptree),2))
