sports_teams = ["Arsenal", "ManUnited","Chelsea","Liverpool","ManCity","Everton","Tottenham"]


'''
Creating file and printing items in the sports team list into each line 
'''
print("creating new file:\n")
with open("teams.txt", "w") as wfile:
    for team in sports_teams:
        wfile.write(f"{team}\n")




'''
Opening file to read and display the names of the 1st and the 4th
'''
print("displaying team 1 and 4:\n")
with open("./teams.txt","r") as rfile:
    read_teams = [line for line in rfile]
    print(read_teams[0])
    print(read_teams[4])
    print()

'''
Editing file to replace the top line 
and print out edited file line by line 
'''
print("replacing line 1: \n")
with open("teams.txt","w+") as wfile:
    edit_file = [line for line in wfile]
    edit_file[0] = "This is a new line \n"
    
    for line in edit_file:
        print(line)
        wfile.write(line)




'''
Open a new text file caleed teams.txt w
'''