import ply.yacc as yacc

from syntax_lexer import tokens

start = 'program'

def p_program(p):
    '''program : global_dec Link_Start declare_statements statements Link_End functions'''
    
def p_empty(p):
    ''' empty :'''
    pass
        
def p_global_dec(p):
    ''' global_dec : struct_dec global_dec
                | declare_statements global_dec
                | empty'''
                
def p_struct_dec(p):
    ''' struct_dec : Struct id open_bracket struct_element1 struct_element2 close_bracket id_array1
                    | empty'''
    
def p_struct_element1(p):
    ''' struct_element1 : data_type id_array_dec'''
    
def p_data_type(p):
    ''' data_type : Integer
                | Decimal
                | String
                | Boolean '''

def p_id_array_dec(p):
    ''' id_array_dec : id id_array_dec2'''

def p_id_array_dec2(p):
    ''' id_array_dec2 : id_dec1
                    | open_brace lit_intposi close_brace array_dec1
                    | empty'''
        
def p_id_dec1(p):
    ''' id_dec1 : comma id id_dec1
                | empty'''
    
def p_array_dec1(p):
    ''' array_dec1 : comma id open_brace lit_intposi close_brace array_dec1
                | empty'''
    
def p_struct_element2(p):
    ''' struct_element2 : comma struct_element1 struct_element2
                        | empty'''
                        
def p_declare_statements(p):
    ''' declare_statements : Generate const_var_dec declare_statements 
                        | empty'''
                        
def p_const_var_dec(p):
    ''' const_var_dec : Fixed data_type id_array_const
                    | data_type id_array_var '''
                    
def p_id_array_const(p):
    ''' id_array_const : id id_array_const2 '''

def p_id_array_const2(p):
    ''' id_array_const2 : equal value id_const1 
                        | open_brace lit_intposi close_brace equal open_brace value1 close_brace array_const1 '''
                        
def p_id_const1(p):
    ''' id_const1 : comma id equal value id_const1 
                | empty'''

def p_array_const1(p):
    ''' array_const1 : comma id open_brace lit_intposi close_brace equal open_brace value1 close_brace array_const1 
                    | empty'''
                    
def p_id_array_var(p):
    ''' id_array_var : id id_array_var2 '''
    
def p_id_array_var2(p):
    ''' id_array_var2 : var_init id_var1
                    | open_brace lit_intposi close_brace array_init array_var1'''

def p_var_init(p):
    ''' var_init : equal value id_var1
                | empty'''
                
def p_id_var1(p):
    ''' id_var1 : comma id var_init id_var1
                | empty'''
                
def p_array_init(p):
    ''' array_init : equal open_brace value1 close_brace array_var1 
                | empty'''
                
def p_array_var1(p):
    ''' array_var1 : comma id open_brace lit_intposi close_brace array_init array_var1
                | empty'''

def p_value(p):
    ''' value : num_value
            | lit_str
            | lit_bool''' 
            
def p_num_value(p):
    ''' num_value : id_array id_struct
                | literals 
                | arithmetic_expression
                | func_call '''
                
def p_id_array(p):
    ''' id_array : id array'''
    
def p_array(p):
    ''' array : open_brace lit_intposi close_brace 
            | empty''' 

def p_id_array1(p):
    ''' id_array1 : id_array id_array2
                    | empty'''
    
def p_id_array2(p):
    ''' id_array2 : comma id_array1
                | empty'''             

def p_literals(p):
        '''literals : lit_intposi
                    | lit_intnega
                    | lit_decposi
                    | lit_decnega'''

def p_arithmetic_expression(p):
        '''arithmetic_expression : open_par arithmetic_expression close_par
                                | num_value arithmetic_operators num_value'''

def p_arithmetic_operators(p):
        '''arithmetic_operators : plus
                                | minus
                                | times
                                | divide
                                | divide_divide
                                | modulo
                                | times_times'''

def p_id_struct(p):
        '''id_struct : period id_array
                    | empty'''


def p_value1(p):
        '''value1 : value value2'''

def p_value2(p):
        '''value2 : comma value1 
                | empty'''

def p_statements(p):
        '''statements : assignment_statements statements 
                    | looping_statements statements
                    | conditional_statements statements
                    | io_statements statements
                    | func_call statements
                    | empty'''

def p_assignment_statements(p):
        '''assignment_statements : id assignment_statements2'''

def p_assignment_statements2(p):
        '''assignment_statements2 : array id_struct assignment_exp 
                                | open_brace lit_intposi close_brace more_array equal open_brace value1 close_brace'''

def p_assignment_exp(p):
        '''assignment_exp : assignment_operators num_value
                        | equal assign_value'''

def p_assign_value(p):
        '''assign_value : num_value
                        | more_id value'''

def p_more_id(p):
        '''more_id : id_array id_struct equal more_id
                | empty'''

def p_assignment_operators(p):
        '''assignment_operators : plus_equal
                                | minus_equal
                                | times_equal
                                | divide_equal
                                | divide_divide_equal
                                | modulo_equal
                                | times_times_equal'''

def p_more_array(p):
        '''more_array : equal id open_brace lit_intposi close_brace more_array
                    | empty'''

def p_looping_statements(p):
        '''looping_statements : for_statements
                            | while_statements
                            | empty'''

def p_for_statements(p):
        '''for_statements : For id In id open_brace close_brace colon open_bracket inside_statements close_bracket
                            | empty'''

def p_while_statements(p):
        '''while_statements : While open_par condition close_par colon open_bracket inside_statements close_bracket
                            | empty'''

def p_inside_statements(p):
        '''inside_statements : statements inside_statements
                            | control_statements inside_statements
                            | empty'''

def p_control_statements(p):
        '''control_statements : Break
                            | Continue
                            | Avoid'''
                            
def p_condition(p):
    ''' condition   : relational_expression
                    | logical_expression
                    | lit_bool
                    | Not open_par condition_not close_par'''
                    
def p_condition_not(p):
    ''' condition_not   : relational_expression
                        | logical_expression
                        | lit_bool'''
                        
def p_relational_expression(p):
    ''' relational_expression   : value relational_operators value'''
    
def p_relational_operators(p):
    ''' relational_operators    : greater_than
                                | less_than
                                | equal_equal
                                | not_equal
                                | great_than_equal
                                | less_than_equal'''
                                
def p_logical_expression(p):
    ''' logical_expression  : open_par logical_operand close_par logical_operators open_par logical_operand close_par'''
    
def p_logical_operand(p):
    ''' logical_operand : Not open_par logical_operand close_par
                        | relational_expression
                        | logical_expression
                        | lit_bool'''
                        
def p_logical_operators(p):
    ''' logical_operators   : And
                            | Or'''
                            
def p_conditional_statements(p):
    ''' conditional_statements  : if_statement
                                | switch_statements
                                | empty'''
                                
def p_if_statement(p):
    ''' if_statement    : If open_par condition close_par colon open_bracket inside_statements close_bracket condition_else
                        | empty'''
    
def p_condition_else(p):
    ''' condition_else  : elif_statement
                        | else_statement
                        | empty'''
                        
def p_elif_statement(p):
    ''' elif_statement  : Elif open_par condition close_par colon open_bracket inside_statements close_bracket condition_else
                        | empty'''
    
def p_else_statement(p):
    ''' else_statement  : Else colon inside_statements
                        | empty'''
    
def p_switch_statements(p):
    ''' switch_statements   : Switch id colon open_bracket execute Default colon inside_statements close_bracket End_Switch
                            | empty'''
    
def p_execute(p):
    ''' execute : Execute switch_lit colon statements Break execute1'''
    
def p_switch_lit(p):
    ''' switch_lit  : lit_str
                    | lit_intposi
                    | lit_intnega'''

def p_execute1(p):
    ''' execute1    : execute
                    | empty'''
                    
def p_io_statements(p):
    ''' io_statements   : input_statements
                        | output_statements'''
                        
def p_input_statements(p):
    ''' input_statements    : Absorb id_array id_struct'''
    
def p_output_statement(p):
    ''' output_statements   : Discharge value'''
    
def p_func_call(p):
    ''' func_call   : Sys_Call id open_par function_param close_par'''
    
def p_function_param(p):
    ''' function_param  : value1 more_param
                        | id open_brace close_brace more_param
                        | empty'''
                        
def p_more_param(p):
    ''' more_param  : comma value1 more_param
                    | comma id open_brace close_brace more_param
                    | empty'''
                    
def p_functions(p):
    ''' functions   : Sys id open_par parameters close_par open_bracket declare_statements function_body close_bracket functions
                    | empty'''
                    
def p_parameters(p):
    ''' parameters  : data_type id parameters
                    | empty'''
                    
def p_function_body(p):
    ''' function_body   : statements function_body
                        | return_statement function_body
                        | empty'''
                        
def p_return_statement(p):
    ''' return_statement    : Return value'''
    
def p_error(p):
    print("Syntax error in input")
    
parser = yacc.yacc()