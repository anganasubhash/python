python_dev = {"Anu", "Rahul", "Meera", "Arun", "Priya"}
sql_dev = {"Rahul", "Meera", "Arun", "Vishnu"}
powerbi_dev = {"Meera", "Arun", "Vishnu", "Asha"}
all_three = python_dev & sql_dev & powerbi_dev
only_python = python_dev - sql_dev - powerbi_dev
python_sql = (python_dev & sql_dev) - powerbi_dev
at_least_one = python_dev | sql_dev | powerbi_dev
exactly_one = (
    (python_dev - sql_dev - powerbi_dev)
    | (sql_dev - python_dev - powerbi_dev)
    | (powerbi_dev - python_dev - sql_dev)
)

print("All three skills:", all_three)
print("Only Python:", only_python)
print("Python and SQL but not Power BI:", python_sql)
print("At least one skill:", at_least_one)
print("Exactly one skill:", exactly_one)