def my_function(p_var):
    if 42 <= p_var <= 48:
        my_var = int(p_var / 7)
        my_var -= 4
        return my_var
    else:
        new_var = p_var % 9
        new_var = new_var ** 2
        return new_var
print(my_function(57))