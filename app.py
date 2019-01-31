#!/usr/bin/env python3
from newsdb import get_articles, get_popular_author, get_errors
import datetime

print("Please choose from these questions:")
print("1 - What are the most popular three articles of all time?")
print("2 - Who are the most popular article authors of all time?")
print("3 - On which days did more than 1% of requests lead to errors?")
print("Enter q or quit to exit.\n")

while True:
    selection = input("Enter your selection (num): ").strip().lower()
    if selection == "q" or selection == "quit":
        print("Goodbye.")
        break
    else:
        if selection == "1":
            try:
                articles = get_articles()
                for article in articles:
                    print("%s - %s views" % (article[0], article[1]))
            except Exception as e:
                print("Error. Unable to answer your question.")
            print()
        elif selection == "2":
            try:
                authors = get_popular_author()
                for author in authors:
                    print("%s - %s views" % (author[0], author[1]))
            except Exception as e:
                print("Error. Unable to answer your question.")
            print()
        elif selection == "3":
            try:
                errorDay = get_errors()
                percentage = "{:.1f}".format((errorDay[0][1] * 100)/errorDay[0][2])
                print(errorDay[0][0].strftime("%B %d, %Y") + " - " +
                percentage + "% errors\n")
            except Exception as e:
                print("Error. Unable to answer your question.")
            print()
        else:
            print("Sorry, I didn't get your question. Try again.\n")
