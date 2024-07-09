from prettytable import PrettyTable

table=PrettyTable(["Pokemon Name","Type"])
table.add_row(["Pikachue","Electric"])
table.add_row(["Squirtle","Water"])
table.add_row(["Charmander","Fire"])

table.align="l"
print(table)
