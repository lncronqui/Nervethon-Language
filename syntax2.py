
import ply.yacc as yacc

def p_literals(self, p):
        '''literals : lit_intposi
                    | lit_intnega
                    | lit_decposi
                    | lit_decnega'''

def p_arithmetic_expression(self, p):
        '''arithmetic_expression : (arithmetic_expression)
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
        '''id_struct : .id_array
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
                                  | {lit_intposi} more_array = { value1 }'''

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
        '''more_array : = id {lit_intposi} more_array
                      | null'''

def p_looping_statements(self, p):
        '''looping_statements : for_statements
                              | while_statements'''

def p_for_statements(self, p):
        '''for_statements : For id In id{}: [inside_statements]'''

def p_while_statements(self, p):
        '''while_statements : While(condition): [inside_statements]'''

def p_inside_statements(self, p):
        '''inside_statements : statements inside_statements
                             | control_statements inside_statements'''

def p_control_statements(self, p):
        '''control_statements : Break
                              | Continue
                              | Avoid'''