# runtime error troubleshooting logic - start with the suggested line and work your way above the line
# try/except/finally not used to find bugs
# used to catch things outside of your control or predictability

x = 42 
y = 0

print()
try:
    print(x / y)
except ZeroDivisionError as e:
    print("Not allowed to divide by zero")
else:
    print("Somethign else went wrong")
finally:
    print("This is my cleanup code")
print()

#exit gracefully

# try:
# except:
# finally:

#unit testing/ test driven developing inside python

# <<<Stack trace>>>
# Last calls are on the top
# Your code is likely on the bottom
# Seek out line numbers

# <<<Finding your mistake>>>
# Reread your code
# Check the documentation
# Search the internet
# Take a break
# Ask someone for help
