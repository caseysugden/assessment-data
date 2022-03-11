log_file = open("um-server-01.txt") # opens a file and assigns it to log_file


def sales_reports(log_file): # creates a function called [sales_report] that takes [log_file] as an argument
    for line in log_file: # loops over each line
        line = line.rstrip() # removes any trailing characters (spaces by default)
        day = line[0:3] # assigns first three characters of line to [day]
        # if day == "Mon": # checks if day is equal to "Mon"
        #     print(line) # if day is equal to "Mon", prints the line
        quantity = line[16:18]
        if int(quantity) >= 10:
            print(line)


sales_reports(log_file) # calls [sales_report] function passing in [log_file] as parameter
