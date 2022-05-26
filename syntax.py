import ply.yacc as yacc
from lexer import (
    Tokens,
    Lexer
)

tokens = Lexer.tokens

class Parser:
    def p_program(self, p):
        '''program : global_dec Link.Start declare_statements statements Link.End functions'''
        
    def p_null(self, p):
        ''' null : empty '''
            
    def p_global_dec(self, p):
        ''' global_dec : struct_dec global_dec
                    | declare_statements global_dec
                    | comments_statements global_dec 
                    | null'''
                    
    def p_struct_dec(self, p):
        ''' struct_dec : Struct id [ struct_element1 struct_element2 ] id_array1'''
        
    def p_struct_element1(self, p):
        ''' struct_element1 : data_type id_array_dec'''
        
    def p_data_type(self, p):
        ''' data_type : Integer
                    | Decimal
                    | String
                    | Boolean '''

    def p_id_array_dec(self, p):
        ''' id_array_dec : id id_array_dec2'''

    def p_id_array_dec2(self, p):
        ''' id_array_dec2 : id_dec1
                        | { lit_intposi } array_dec1
                        | null '''
            
    def p_id_dec1(self, p):
        ''' id_dec1 : , id id_dec1
                    | null '''
        
    def p_array_dec1(self, p):
        ''' array_dec1 : , id { lit_intposi } array_dec1
                    | null '''
        
    def p_struct_element2(self, p):
        ''' struct_element2 : , struct_element1 struct_element2
                            | null'''
                            
    def p_declare_statements(self, p):
        ''' declare_statements : Generate const_var_dec declare_statements 
                            | null '''
                            
    def p_const_var_dec(self, p):
        ''' const_var_dec : Fixed data_type id_array_const
                        | data_type id_array_var '''
                        
    def p_id_array_const(self, p):
        ''' id_array_const : id id_array_const2 '''

    def p_id_array_const2(self, p):
        ''' id_array_const2 : = value id_const1 
                            | { lit_intposi } = { value1 } array_const1 '''
                            
    def p_id_const1(self, p):
        ''' id_const1 : , id = value id_const1 
                    | null '''

    def p_array_const1(self, p):
        ''' array_const1 : , id { lit_intposi } = { value1 } array_const1 
                        | null '''
                        
    def p_id_array_var(self, p):
        ''' id_array_var : id id_array_var2 '''
        
    def p_id_array_var2(self, p):
        ''' id_array_var2 : var_init id_var1
                        | { lit_intposi } array_init array_var1'''

    def p_var_init(self, p):
        ''' var_init : = value id_var1
                    | null '''
                    
    def p_id_var1(self, p):
        ''' id_var1 : , id var_init id_var1
                    | null '''
                    
    def p_array_init(self, p):
        ''' array_init : = { value1 } array_var1 
                    | null '''
                    
    def p_array_var1(self, p):
        ''' array_var1 : , id { lit_intposi } array_init array_var1
                    | null'''
    
    def p_value(self, p):
        ''' value : num_value
                | lit_str
                | lit_bool''' 
                
    def p_num_value(self, p):
        ''' num_value : id_array id_struct
                    | literals 
                    | arithmetic_expression
                    | func_call '''
                    
    def p_id_array(self, p):
        ''' id_array : id_array'''
        
    def p_array(self, p):
        ''' array : { lit_intposi } 
                | null ''' 

    def p_id_array1(self, p):
        ''' id_array1 : id_array id_array2'''
        
    def p_id_array2(self, p):
        ''' id_array2 : , id_array1
                    | null '''             

    def p_literals(self, p):
            '''literals : lit_intposi
                        | lit_intnega
                        | lit_decposi
                        | lit_decnega'''

    def p_arithmetic_expression(self, p):
            '''arithmetic_expression : ( arithmetic_expression )
                                    | num_value arithmetic_operators num_value'''

    def p_arithmetic_operators(self, p):
            '''arithmetic_operators : +
                                    | -
                                    | *
                                    | /
                                    | //
                                    | %
                                    | **'''

    def p_id_struct(self, p):
            '''id_struct : . id_array
                        | null'''


    def p_value1(self, p):
            '''value1 : value value2'''

    def p_value2(self, p):
            '''value2 : , value1 
                    | null'''

    def p_comments(self, p):
            '''comments : /* ascii */'''

    def p_statements(self, p):
            '''statements : assignment_statements statements 
                        | looping_statements statements
                        | conditional_statements statements
                        | io_statements statements
                        | comments statements 
                        | func_call statements
                        | null'''

    def p_assignment_statements(self, p):
            '''assignment_statements : id assignment_statements2'''

    def p_assignment_statements2(self, p):
            '''assignment_statements2 : array id_struct assignment_exp 
                                    | { lit_intposi } more_array = { value1 }'''

    def p_assignment_exp(self, p):
            '''assignment_exp : assignment_operators num_value
                            | = assign_value'''

    def p_assign_value(self, p):
            '''assign_value : num_value
                            | more_id value'''

    def p_more_id(self, p):
            '''more_id : id_array id_struct = more_id
                    | null'''

    def p_assignment_operators(self, p):
            '''assignment_operators : +=
                                    | -=
                                    | *=
                                    | /=
                                    | //=
                                    | %=
                                    | **='''

    def p_more_array(self, p):
            '''more_array : = id { lit_intposi } more_array
                        | null'''

    def p_looping_statements(self, p):
            '''looping_statements : for_statements
                                | while_statements'''

    def p_for_statements(self, p):
            '''for_statements : For id In id { } : [ inside_statements ]'''

    def p_while_statements(self, p):
            '''while_statements : While ( condition ): [ inside_statements ]'''

    def p_inside_statements(self, p):
            '''inside_statements : statements inside_statements
                                | control_statements inside_statements'''

    def p_control_statements(self, p):
            '''control_statements : Break
                                | Continue
                                | Avoid'''
                                
    def p_condition(self, p):
        ''' condition   : relational_expression
                        | logical_expression
                        | lit_bool
                        | Not ( condition_not )'''
                        
    def p_condition_not(self, p):
        ''' condition_not   : relational_expression
                            | logical_expression
                            | lit_bool'''
                            
    def p_relational_expression(self,p):
        ''' relational_expression   : value relational_operators value'''
        
    def p_relational_operators(self, p):
        ''' relational_operators    : >
                                    | <
                                    | ==
                                    | !=
                                    | >=
                                    | <='''
                                    
    def p_logical_expression(self, p):
        ''' logical_expression  : ( logical_operand ) logical_operator ( logical_operand )'''
        
    def p_logical_operand(self, p):
        ''' logical_operand : Not ( logical_operand )
                            | relational_expression
                            | logical_expression
                            | lit_bool'''
                            
    def p_logical_operators(self, p):
        ''' logical_operators   : And
                                | Or'''
                                
    def p_conditional_statements(self,p):
        ''' conditional_statements  : if_statement
                                    | switch_statements'''
                                    
    def p_if_statement(self, p):
        ''' if_statement    : If ( condition ) : [ inside_statements ] condition_else'''
        
    def p_condition_else(self,p):
        ''' condition_else  : elif_statement
                            | else_statement
                            | null'''
                            
    def p_elif_statement(self, p):
        ''' elif_statement  : Elif ( condition ) : [ inside_statements ] condition_else'''
        
    def p_else_statement(self, p):
        ''' else_statement  : Else: inside_statements'''
        
    def p_switch_statements(self, p):
        ''' switch_statements   : Switch ID: [ execute Default : inside_statements ] End.Switch'''
        
    def p_execute(self, p):
        ''' execute : Execute switch_lit: statements Break execute1'''
        
    def p_switch_lit(self, p):
        ''' switch_lit  : lit_str
                        | lit_intposi
                        | lit_intnega'''

    def p_execute1(self, p):
        ''' execute1    : execute
                        | null'''
                        
    def p_io_statements(self, p):
        ''' io_statements   : input_statements
                            | output_statements'''
                            
    def p_input_statements(self, p):
        ''' input_statements    : Absorb id_array id_struct'''
        
    def p_output_statement(self, p):
        ''' output_statements   : Discharge value'''
        
    def p_func_call(self, p):
        ''' func_call   : Sys.Call ID ( function_param )'''
        
    def p_function_param(self, p):
        ''' function_param  : value1 more_param
                            | ID { } more_param
                            | null'''
                            
    def p_more_param(self, p):
        ''' more_param  : , value1 more_param
                        | , ID { } more_param
                        | null'''
                        
    def p_functions(self, p):
        ''' functions   : Sys ID ( parameters ) [ declare_statements function_body ] functions
                        | comments functions
                        | null'''
                        
    def p_parameters(self, p):
        ''' parameters  : data_type ID parameters
                        | null'''
                        
    def p_function_body(self, p):
        ''' function_body   : statements function_body
                            | return_statement function_body
                            | null'''
                            
    def p_return_statement(self, p):
        ''' return_statement    : Return value'''
        
    def p_error(self,p):
        print("Syntax error in input")
        
    def __init__(self):
        self.parser = yacc.yacc(start=self.start ,module=self)
        
    def run(self, data):
        result = yacc.yacc(start=self.start ,module=self)
        return result
    
    

def run(data):
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        if not s: continue
        result = yacc.yacc(data)
        print(result)



# parser = yacc.yacc()

# while True:
#     try:
#         s = raw_input('calc > ')
#     except EOFError:
#         break
#     if not s: continue
#     result = parser.parse(s)
#     print(result)