# Checking disk usage: total number of bites - the amount used - the amount free
import shutil

du = shutil.disk_usage("/")
print(du)

# Calculating percentage of available disk space
print("Percentage of free disk space: " + str(du.free/du.total * 100))
