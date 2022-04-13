from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charamander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
#
# print(table)


table = PrettyTable()
table.add_column("Language", ["Python", "C", "SQL"])
table.add_column("Field Of Usage", ["Machine Learning\n Data Science\n Automation", "Machine Interface\n Robotics",
                                    "Data Science"])
table.align = "r"
print(table)

