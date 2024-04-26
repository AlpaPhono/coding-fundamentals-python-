# Make a dictionary of books, with 3 authors and multple books per author
# Use an input asking for an author name.
# Print a STRING of books by that author. (not a list).
# Use a join method. (",".join)
# Use direct access and then dedo using the get method

books = {
    "Rebecca Yarros" : ["Onyx Storm", "Fourth Wing"],
 "Liz Truss": ["After the Coalition: Aconservative Agenda for Britain","Ten Years To Save The West: Lessons from the only conservative in the room"],
"Agatha Christie": ["Marple: Twelve New Stories","Sinister Spring"],
"J.R.R. TolKien": ["The Two Towers","The Lord of the Rings"]
}

author = input("Please enter an authors name").lower()
flag = True
while flag:

    if author in books:

        print(author.join(books[author]))
        flag = False



    else:
        print("This is not an available author try again")

