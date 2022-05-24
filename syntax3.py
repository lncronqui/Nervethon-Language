def p_condition(self, p):
    ''' condition   : relational_expression
                    | logical_expression
                    | LIT_BOOL
                    | Not ( condition_not )'''
                    
def p_condition_not(self, p):
    ''' condition_not   : relational_expression
                        | logical_expression
                        | LIT_BOOL'''
                        
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
                        | LIT_BOOL'''
                        
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
    ''' switch_lit  : LIT_STR
                    | LIT_INTPOSI
                    | LIT_INTNEGA'''

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
    
