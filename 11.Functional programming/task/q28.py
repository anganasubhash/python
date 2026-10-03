installed = ("Python", "Chrome", "Excel", "Word")
required = ("Python", "Chrome", "Excel", "Word", "PowerPoint")
missing = []
for software in required:
    if software not in installed:
        missing.append(software)
print("Missing software:", missing)