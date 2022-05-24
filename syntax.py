import ply.yacc as yacc

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
                      | { lit_intposi }array_init array_var1'''

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
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   