#######FUNCTIONS WITH OUTPUTS #######################

# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"{formatted_f_name} {formatted_l_name}"  # everything after return keyword replaces where
#                                                      # that function is called
#
# formatted_string = format_name("niTHin" ,"NAZaR")
# print(formatted_string)


######MULTIPLE RETURN VALUES#############
def format_name(f_name, l_name):
    if f_name == "" or l_name =="":
        return "You didn't provide any input"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Return:{formatted_f_name} {formatted_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))

