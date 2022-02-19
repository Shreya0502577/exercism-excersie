EXPECTED_BAKE_TIME = 40
PREPARATION_TIME  = 2
def bake_time_remaining(elapsed_bake_time):
     """returns how many minutes the lasagna should bake in the oven"""
     return EXPECTED_BAKE_TIME - elapsed_bake_time
    
def preparation_time_in_minutes(number_of_layers):
      """implement the bake_time_remaining() function that takes 
         the actual minutes the lasagna """
      return number_of_layers *PREPARATION_TIME 
  
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
   
    """ This function should return the total number of minutes you've been cooking, or 
        the sum of your preparation time and the time the lasagna has already 
        spent baking in the oven."""
    return ( PREPARATION_TIME*number_of_layers)+elapsed_bake_time
