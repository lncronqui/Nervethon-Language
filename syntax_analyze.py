from typing import NamedTuple
import ply.yacc as yacc

from syntax_lexer import tokens

class Output(NamedTuple):
    output: str
    tabs: int
    
class Error(NamedTuple):
    type: str
    lineno: int
    

outputs = []
errors = []
tab = 0
class Node:
    
    def __init__(self,value=">"):
        global tab
        self.value = value
        self.children = []
        tab = 0
    def add_child(self, value):
        if self.value:
            if self.children is None:
                self.children = Node(value)
            else:
                self.children.append(Node(value))
        else:
            self.value = value
        
    def traverse(self):
        global outputs
        global tab
        if self.value is not None:
            if type(self.value) is Node or isinstance(self.value, Node):
                self.value.traverse()
            if not isinstance(self.value, Node):
                outputs.append(Output(self.value,tab))
                tab+=1
            if self.children:
                for tok in self.children:
                    tok.traverse()
                    tab-=1
                    if tab < 0:
                        tab = 1
        return outputs
        
            
start = 'program'


def p_program(p):
    '''program : global_dec Link_Start declare_statements statements Link_End functions'''
    p[0] = Node("<program>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    p[0].add_child(p[3])
    p[0].add_child(p[4])
    p[0].add_child(p[5])
    p[0].add_child(p[6])
    
        
def p_global_dec(p):
    ''' global_dec : struct_dec global_dec
                | declare_statements global_dec
                |'''
    if len(p) > 1:
        p[0] = Node("<global_dec>")
        p[0].add_child(p[1])
        p[0].add_child(p[2])
    else:
        pass
                
def p_struct_dec(p):
    ''' struct_dec : Struct id open_bracket struct_element1 struct_element2 close_bracket id_array1'''
    p[0] = Node("<struct_dec>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    p[0].add_child(p[3])
    p[0].add_child(p[4])
    p[0].add_child(p[5])
    p[0].add_child(p[6])
    p[0].add_child(p[7])
    
def p_struct_element1(p):
    ''' struct_element1 : data_type id_array_dec'''
    p[0] = Node("<struct_element1>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])

    
def p_data_type(p):
    ''' data_type : Integer
                | Decimal
                | String
                | Boolean '''
    p[0] = Node("<data_type>")
    p[0].add_child(p[1])


def p_id_array_dec(p):
    ''' id_array_dec : id id_array_dec2'''
    p[0] = Node("<id_array_dec>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])

def p_id_array_dec2(p):
    ''' id_array_dec2 : id_dec1'''
    p[0] = Node("<id_array_dec2>")
    p[0].add_child(p[1])
        
def p_id_array_dec2_more(p):
    ''' id_array_dec2 : open_brace lit_intposi close_brace array_dec1'''
    p[0] = Node("<id_array_dec2>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    p[0].add_child(p[3])
    p[0].add_child(p[4])
        
def p_id_dec1(p):
    ''' id_dec1 : comma id id_dec1
                |'''
    if len(p) > 1:
        p[0] = Node("<id_dec1>")
        p[0].add_child(p[1])
        p[0].add_child(p[2])
        p[0].add_child(p[3])
    else:
        pass
    
def p_array_dec1(p):
    ''' array_dec1 : comma id open_brace lit_intposi close_brace array_dec1
                |'''
    if len(p) > 1:
        p[0] = Node("<array_dec1>")
        p[0].add_child(p[1])
        p[0].add_child(p[2])
        p[0].add_child(p[3])
        p[0].add_child(p[4])
        p[0].add_child(p[5])
        p[0].add_child(p[6])
    else:
        pass
    
def p_struct_element2(p):
    ''' struct_element2 : comma struct_element1 struct_element2
                        |'''
    if len(p) > 1:
        p[0] = Node("<struct_element2>")
        p[0].add_child(p[1])
        p[0].add_child(p[2])
        p[0].add_child(p[3])
    else:
        pass
                        
def p_declare_statements(p):
    ''' declare_statements : Generate const_var_dec declare_statements
                            |'''
    if len(p) > 1:
        p[0] = Node("<declare_statements>")
        p[0].add_child(p[1])
        p[0].add_child(p[2])
        p[0].add_child(p[3])
    else:
        pass
                        
def p_const_var_dec(p):
    ''' const_var_dec : Fixed data_type id_array_const'''
    p[0] = Node("<const_var_dec>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    p[0].add_child(p[3])
            
def p_const_var_dec_more(p):
    ''' const_var_dec : data_type id_array_var'''
    p[0] = Node("<const_var_dec>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
                    
def p_id_array_const(p):
    ''' id_array_const : id id_array_const2 '''
    p[0] = Node("<id_array_const>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])

def p_id_array_const2(p):
    ''' id_array_const2 : open_brace lit_intposi close_brace equal open_brace value1 close_brace array_const1 '''
    p[0] = Node("<id_array_const2>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    p[0].add_child(p[3])
    p[0].add_child(p[4])
    p[0].add_child(p[5])
    p[0].add_child(p[6])
    p[0].add_child(p[7])
    p[0].add_child(p[8])
    
def p_id_array_const2_more(p):
    ''' id_array_const2 : equal value id_const1'''
    p[0] = Node("<id_array_const2>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    p[0].add_child(p[3])
                        
def p_id_const1(p):
    ''' id_const1 : comma id equal value id_const1 
                |'''
    if len(p) > 1:
        p[0] = Node("<id_const1>")
        p[0].children = [p[1], p[2], p[3], p[4], p[5]]
        p[0].add_child(p[1])
        p[0].add_child(p[2])
        p[0].add_child(p[3])
        p[0].add_child(p[4])
        p[0].add_child(p[5])
    else:
        pass

def p_array_const1(p):
    ''' array_const1 : comma id open_brace lit_intposi close_brace equal open_brace value1 close_brace array_const1 
                    |'''
    if len(p) > 1:
        p[0] = Node("<array_const1>")
        p[0].add_child(p[1])
        p[0].add_child(p[2])
        p[0].add_child(p[3])
        p[0].add_child(p[4])
        p[0].add_child(p[5])
        p[0].add_child(p[6])
        p[0].add_child(p[7])
        p[0].add_child(p[8])
        p[0].add_child(p[9])
        p[0].add_child(p[10])
    else:
        pass
                    
def p_id_array_var(p):
    ''' id_array_var : id id_array_var2 '''
    p[0] = Node("<id_array_var>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    
def p_id_array_var2(p):
    ''' id_array_var2 : var_init id_var1'''
    p[0] = Node("<id_array_var2>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
        
def p_id_array_var2_more(p):
    ''' id_array_var2 : open_brace lit_intposi close_brace array_init array_var1'''
    p[0] = Node("<id_array_var2>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    p[0].add_child(p[3])
    p[0].add_child(p[4])
    p[0].add_child(p[5])

def p_var_init(p):
    ''' var_init : equal value id_var1
                |'''
    if len(p) > 1:
        p[0] = Node("<var_init>")
        p[0].add_child(p[1])
        p[0].add_child(p[2])
        p[0].add_child(p[3])
    else:
        pass
                
def p_id_var1(p):
    ''' id_var1 : comma id var_init id_var1
                |'''
    if len(p) > 1:
        p[0] = Node("<id_var1>")
        p[0].add_child(p[1])
        p[0].add_child(p[2])
        p[0].add_child(p[3])
        p[0].add_child(p[4])
    else:
        pass
                
def p_array_init(p):
    ''' array_init : equal open_brace value1 close_brace array_var1 
                |'''
    if len(p) > 1:
        p[0] = Node("<array_init>")
        p[0].children = [p[1], p[2], p[3], p[4], p[5]]
        p[0].add_child(p[1])
        p[0].add_child(p[2])
        p[0].add_child(p[3])
        p[0].add_child(p[4])
        p[0].add_child(p[5])
    else:
        pass
                
def p_array_var1(p):
    ''' array_var1 : comma id open_brace lit_intposi close_brace array_init array_var1
                |'''
    if len(p) > 1:
        p[0] = Node("<array_var1>")
        p[0].add_child(p[1])
        p[0].add_child(p[2])
        p[0].add_child(p[3])
        p[0].add_child(p[4])
        p[0].add_child(p[5])
        p[0].add_child(p[6])
        p[0].add_child(p[7])
    else:
        pass
    
def p_value_num_value(p):
    ''' value : num_value'''
    p[0] = Node("<value>")
    p[0].add_child(p[1])

def p_value(p):
    ''' value : lit_str
            | lit_bool'''
    p[0] = Node("<value>")
    p[0].add_child(p[1])
             
def p_num_value(p):
    ''' num_value : id_array id_struct'''
    p[0] = Node("<num_value>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
        
        
def p_num_value_more(p):
    ''' num_value : literals 
                | arithmetic_expression
                | func_call'''
    p[0] = Node("<num_value>")
    p[0].add_child(p[1])
                
def p_id_array(p):
    ''' id_array : id array'''
    p[0] = Node("<id_array>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    
def p_array(p):
    ''' array : open_brace lit_intposi close_brace 
            |''' 
    if len(p) > 1:
        p[0] = Node("<array>")
        p[0].children = [p[1], p[2], p[3]]
        p[0].add_child(p[1])
        p[0].add_child(p[2])
        p[0].add_child(p[3])
    else:
        pass

def p_id_array1(p):
    ''' id_array1 : id_array id_array2'''
    p[0] = Node("<id_array1>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    
def p_id_array2(p):
    ''' id_array2 : comma id_array1
                |'''
    if len(p) > 1:
        p[0] = Node("<id_array2>")
        p[0].children = [p[1], p[2]]
        p[0].add_child(p[1])
        p[0].add_child(p[2])
    else:
        pass            

def p_literals(p):
    '''literals : lit_intposi
                | lit_intnega
                | lit_decposi
                | lit_decnega'''
    p[0] = Node("<literals>")
    p[0].add_child(p[1])

def p_arithmetic_expression_group(p):
    '''arithmetic_expression : open_par arithmetic_expression close_par'''
    p[0] = Node("<arithmetic_expression>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    p[0].add_child(p[3])
    
def p_arithmetic_expression(p):
    '''arithmetic_expression : num_value arithmetic_operators num_value'''
    p[0] = Node("<arithmetic_expression>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    p[0].add_child(p[3])
    

def p_arithmetic_operators(p):
    '''arithmetic_operators : plus
                            | minus
                            | times
                            | divide
                            | divide_divide
                            | modulo
                            | times_times'''
    p[0] = Node("<arithmetic_operators>")
    p[0].add_child(p[1])

def p_id_struct(p):
    '''id_struct : period id_array
                |'''
    if len(p) > 1:
        p[0] = Node("<id_struct>")
        p[0].add_child(p[1])
        p[0].add_child(p[2])
    else:
        pass


def p_value1(p):
    '''value1 : value value2'''
    p[0] = Node("<value1>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])

def p_value2(p):
    '''value2 : comma value1 
            |'''
    if len(p) > 1:
        p[0] = Node("<value2>")
        p[0].add_child(p[1])
        p[0].add_child(p[2])
    else:
        pass

def p_statements(p):
    '''statements : assignment_statements statements 
                | looping_statements statements
                | conditional_statements statements
                | io_statements statements
                | func_call statements
                |'''
    if len(p) > 1:
        p[0] = Node("<statements>")
        p[0].add_child(p[1])
        p[0].add_child(p[2])
    else:
        pass

def p_assignment_statements(p):
    '''assignment_statements : id assignment_statements2'''
    p[0] = Node("<assignment_statements>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])

def p_assignment_statements2(p):
    '''assignment_statements2 : array id_struct assignment_exp'''
    p[0] = Node("<assignment_statements2>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    p[0].add_child(p[3])
                            
def p_assignment_statements2_more(p):
    '''assignment_statements2 : open_brace lit_intposi close_brace more_array equal open_brace value1 close_brace'''
    p[0] = Node("<assignment_statements2>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    p[0].add_child(p[3])
    p[0].add_child(p[4])
    p[0].add_child(p[5])
    p[0].add_child(p[6])
    p[0].add_child(p[7])
    p[0].add_child(p[8])

def p_assignment_exp(p):
    '''assignment_exp : assignment_operators num_value'''
    p[0] = Node("<assignment_exp>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    
def p_assignment_exp_more(p):
    '''assignment_exp : equal assign_value'''
    p[0] = Node("<assignment_exp>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])

def p_assign_value(p):
    '''assign_value : num_value'''
    p[0] = Node("<assign_value>")
    p[0].add_child(p[1])
        
def p_assign_value_more(p):
    '''assign_value : more_id value'''
    p[0] = Node("<assign_value>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])

def p_more_id(p):
    '''more_id : id_array id_struct equal more_id
            |'''
    if len(p) > 1:
        p[0] = Node("<more_id>")
        p[0].add_child(p[1])
        p[0].add_child(p[2])
        p[0].add_child(p[3])
        p[0].add_child(p[4])
    else:
        pass

def p_assignment_operators(p):
    '''assignment_operators : plus_equal
                            | minus_equal
                            | times_equal
                            | divide_equal
                            | divide_divide_equal
                            | modulo_equal
                            | times_times_equal'''
    p[0] = Node("<assignment_operators>")
    p[0].add_child(p[1])

def p_more_array(p):
    '''more_array : equal id open_brace lit_intposi close_brace more_array
                |'''
    if len(p) > 1:
        p[0] = Node("<more_array>")
        p[0].add_child(p[1])
        p[0].add_child(p[2])
        p[0].add_child(p[3])
        p[0].add_child(p[4])
        p[0].add_child(p[5])
        p[0].add_child(p[6])
    else:
        pass

def p_looping_statements(p):
    '''looping_statements : for_statements
                        | while_statements'''
    p[0] = Node("<looping_statements>")
    p[0].add_child(p[1])

def p_for_statements(p):
    '''for_statements : For id In id open_brace close_brace colon open_bracket inside_statements close_bracket'''
    p[0] = Node("<for_statements>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    p[0].add_child(p[3])
    p[0].add_child(p[4])
    p[0].add_child(p[5])
    p[0].add_child(p[6])
    p[0].add_child(p[7])
    p[0].add_child(p[8])
    p[0].add_child(p[9])
    p[0].add_child(p[10])

def p_while_statements(p):
    '''while_statements : While open_par condition close_par colon open_bracket inside_statements close_bracket'''
    p[0] = Node("<while_statements>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    p[0].add_child(p[3])
    p[0].add_child(p[4])
    p[0].add_child(p[5])
    p[0].add_child(p[6])
    p[0].add_child(p[7])
    p[0].add_child(p[8])

def p_inside_statements(p):
    '''inside_statements : statements inside_statements
                        | control_statements inside_statements
                        |'''
    if len(p) > 1:
        p[0] = Node("<inside_statements>")
        p[0].add_child(p[1])
        p[0].add_child(p[2])
    else:
        pass

def p_control_statements(p):
    '''control_statements : Break
                        | Continue
                        | Avoid'''
    p[0] = Node("<control_statements>")
    p[0].add_child(p[1])
                            
def p_condition(p):
    ''' condition   : relational_expression
                    | logical_expression'''
    p[0] = Node("<condition>")
    p[0].add_child(p[1])
        
def p_condition_more(p):
    ''' condition   : Not open_par condition_not close_par'''
    p[0] = Node("<condition>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    p[0].add_child(p[3])
    p[0].add_child(p[4])
                    
def p_condition_more1(p):
    ''' condition   : lit_bool'''
    p[0] = Node("<condition>")
    p[0].add_child(p[1])
                    
def p_condition_not(p):
    ''' condition_not   : relational_expression
                        | logical_expression'''
    p[0] = Node("<condition_not>")
    p[0].add_child(p[1])

def p_condition_not_more(p):
    ''' condition_not   : lit_bool'''
    p[0] = Node("<condition_not>")
    p[0].add_child(p[1])
                        
def p_relational_expression(p):
    ''' relational_expression   : value relational_operators value'''
    p[0] = Node("<relational_expression>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    p[0].add_child(p[3])
    
def p_relational_operators(p):
    ''' relational_operators    : greater_than
                                | less_than
                                | equal_equal
                                | not_equal
                                | great_than_equal
                                | less_than_equal'''
    p[0] = Node("<relational_operators>")
    p[0].add_child(p[1])
                                
def p_logical_expression(p):
    ''' logical_expression  : open_par logical_operand close_par logical_operators open_par logical_operand close_par'''
    p[0] = Node("<logical_expression>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    p[0].add_child(p[3])
    p[0].add_child(p[4])
    p[0].add_child(p[5])
    p[0].add_child(p[6])
    p[0].add_child(p[7])
    
def p_logical_operand(p):
    ''' logical_operand : Not open_par logical_operand close_par'''
    p[0] = Node("<logical_operand>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    p[0].add_child(p[3])
    p[0].add_child(p[4])

def p_logical_operand_more(p):
    ''' logical_operand : relational_expression
                        | logical_expression'''
    p[0] = Node("<logical_operand>")
    p[0].add_child(p[1])

def p_logical_operand_more1(p):
    ''' logical_operand : lit_bool'''
    p[0] = Node("<logical_operand>")
    p[0].add_child(p[1])
                        
def p_logical_operators(p):
    ''' logical_operators   : And
                            | Or'''
    p[0] = Node("<logical_operators>")
    p[0].add_child(p[1])
                            
def p_conditional_statements(p):
    ''' conditional_statements  : if_statement
                                | switch_statements'''
    p[0] = Node("<conditional_statements>")
    p[0].add_child(p[1])
                                
def p_if_statement(p):
    ''' if_statement    : If open_par condition close_par colon open_bracket inside_statements close_bracket condition_else'''
    p[0] = Node("<if_statement>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    p[0].add_child(p[3])
    p[0].add_child(p[4])
    p[0].add_child(p[5])
    p[0].add_child(p[6])
    p[0].add_child(p[7])
    p[0].add_child(p[8])
    
def p_condition_else(p):
    ''' condition_else  : elif_statement
                        | else_statement'''
    p[0] = Node("<condition_else>")
    p[0].add_child(p[1])
    
def p_condition_else_empty(p):
    ''' condition_else  :'''
    pass
                        
def p_elif_statement(p):
    ''' elif_statement  : Elif open_par condition close_par colon open_bracket inside_statements close_bracket condition_else'''
    p[0] = Node("<elif_statement>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    p[0].add_child(p[3])
    p[0].add_child(p[4])
    p[0].add_child(p[5])
    p[0].add_child(p[6])
    p[0].add_child(p[7])
    p[0].add_child(p[8])
    
    
def p_else_statement(p):
    ''' else_statement  : Else colon open_bracket inside_statements close_bracket'''
    p[0] = Node("<else_statement>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    p[0].add_child(p[3])
    p[0].add_child(p[4])
    p[0].add_child(p[5])
    
def p_switch_statements(p):
    ''' switch_statements   : Switch id colon open_bracket execute Default colon inside_statements close_bracket End_Switch'''
    p[0] = Node("<switch_statements>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    p[0].add_child(p[3])
    p[0].add_child(p[4])
    p[0].add_child(p[5])
    p[0].add_child(p[6])
    p[0].add_child(p[7])
    p[0].add_child(p[8])
    p[0].add_child(p[9])
    p[0].add_child(p[10])
    
def p_execute(p):
    ''' execute : Execute switch_lit colon statements Break execute1'''
    p[0] = Node("<execute>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    p[0].add_child(p[3])
    p[0].add_child(p[4])
    p[0].add_child(p[5])
    p[0].add_child(p[6])
    
def p_switch_lit(p):
    ''' switch_lit  : lit_str
                    | lit_intposi
                    | lit_intnega'''
    p[0] = Node("<switch_lit>")
    p[0].add_child(p[1])

def p_execute1(p):
    ''' execute1    : execute'''
    p[0] = Node("<execute1>")
    p[0].add_child(p[1])
    
def p_execute1_more(p):
    ''' execute1    :'''
    pass
    
                    
def p_io_statements(p):
    ''' io_statements   : input_statements
                        | output_statements'''
    p[0] = Node("<io_statements>")
    p[0].add_child(p[1])
                        
def p_input_statements(p):
    ''' input_statements    : Absorb id_array id_struct'''
    p[0] = Node("<input_statements>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    p[0].add_child(p[3])
    
def p_output_statement(p):
    ''' output_statements   : Discharge value'''
    p[0] = Node("<output_statements>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    
def p_func_call(p):
    ''' func_call   : Sys_Call id open_par function_param close_par'''
    p[0] = Node("<func_call>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    p[0].add_child(p[3])
    p[0].add_child(p[4])
    p[0].add_child(p[5])
    
def p_function_param(p):
    ''' function_param  : id open_brace close_brace more_param
                        |'''
    if len(p) > 1:
        p[0] = Node("<function_param>")
        p[0].add_child(p[1])
        p[0].add_child(p[2])
        p[0].add_child(p[3])
        p[0].add_child(p[4])
    else:
        pass
    
def p_function_param_more(p):
    ''' function_param  : value1 more_param'''
    p[0] = Node("<function_param>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
                        
def p_more_param(p):
    ''' more_param  : comma function_param
                    |'''
    if len(p) > 1:
        p[0] = Node("<more_param>")
        p[0].add_child(p[1])
        p[0].add_child(p[2])
    else:
        pass
                    
def p_functions(p):
    ''' functions   : Sys id open_par parameters close_par open_bracket declare_statements function_body close_bracket functions
                    |'''
    if len(p) > 1:
        p[0] = Node("<functions>")
        p[0].add_child(p[1])
        p[0].add_child(p[2])
        p[0].add_child(p[3])
        p[0].add_child(p[4])
        p[0].add_child(p[5])
        p[0].add_child(p[6])
        p[0].add_child(p[7])
        p[0].add_child(p[8])
        p[0].add_child(p[9])
        p[0].add_child(p[10])
    else:
        pass
                    
def p_parameters(p):
    ''' parameters  : data_type id parameters
                    |'''
    if len(p) > 1:
        p[0] = Node("<parameters>")
        p[0].add_child(p[1])
        p[0].add_child(p[2])
        p[0].add_child(p[3])
    else:
        pass
                    
def p_function_body(p):
    ''' function_body   : statements function_body
                        | return_statement function_body
                        |'''
    if len(p) > 1:
        p[0] = Node("<function_body>")
        p[0].add_child(p[1])
        p[0].add_child(p[2])
    else:
        pass
                        
def p_return_statement(p):
    ''' return_statement    : Return value'''
    p[0] = Node("<return_statement>")
    p[0].add_child(p[1])
    p[0].add_child(p[2])
    
def p_error(p):
    global errors
    if p is not None:
        errors.append(Error(p.type, p.lineno))       
    parser.errok()
    
parser = yacc.yacc()
