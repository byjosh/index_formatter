# index_formatter
Take a comma separated values file (CSV) for an index and output it as file

If you don't run `git clone https://github.com/byjosh/index_formatter.git` commands as a matter of course the easiest way to get the code if you are reading this on github.com is click green Code button above & to right and you can download a ZIP file - which most folks can deal with.

## Running the script

Put your input CSV file (called `test_book_before_page.csv` or `test_page_before_book.csv` in examples below depending on whether input file has book before page number column or vice versa) in same folder as the index_to_html.py script (so where you unzipped the files - or cloned them if you did a git clone).

index_to_html.py is the script to run in the terminal or Powershell

Command to run in Mac/Linux terminal is like: 

`python3 index_to_html.py test_book_before_page.csv output_file_title`

or on Windows in Powershell the command is like: 

`python3.exe .\index_to_html.py .\test_book_before_page.csv output_file_title`

Change `test_book_before_page.csv` and  `output_file_title` to appropriate values (though leave as is and it will test the script with the provided test file: test_book_before_page.csv.

## Input file requirements

The column layout in the CSV for using it simply as`python3 index_to_html.py test_book_before_page.csv output_file_title` or `python3.exe .\index_to_html.py .\test_book_before_page.csv output_file_title` should be book number then page number:-
```
entry,  book, page, notes
"apple","Book 1", 5,  "often mentioned when teaching letter A in English alphabet"
```
### Input with page number column before book column
Run with `page` as a final argument as `python3 index_to_html.py test_page_before_book.csv output_file_title  page` or `python3.exe .\index_to_html.py .\test_page_before_book.csv output_file_title  page` the column layout in the CSV can be entry (e.g. "apple"), page number, book number (e.g. Book 1), notes (e.g. "often mentioned in connection with teaching the alphabet in English")



```
entry, page, book, notes
"apple", 5, "Book 1", "often mentioned when teaching letter A in English alphabet"
```

Remove any row of column labels before using the script (or modify script to have that as an option). Any lines without an entry in first column are ignored for output

The order seen for the page numbers for each entry will work best if all book references end so last character is a number (whether `book 3`, `volume 3`, `101.3`) and the page number is a number with no other characters (so: `100` ; not `100-102`) - but the comparison function uses strings to make the comparison - just in case you don't follow these rules. But unless an entry has a half a dozen or more pages referenced one can probably spot the correct order at a glance even if your input data does not play nice with the comparison function.

### Test files
`test_book_before_page.csv` and `test_page_before_book.csv` are provided as test files. With the latter the optional `page` argument is needed as final argument like `python3 index_to_html.py test_page_before_book.csv output_file_title  page` or `python3.exe .\index_to_html.py .\test_page_before_book.csv output_file_title  page` - with `test_book_before_page.csv` that final argument can and indeed should be omitted (as the default column order is `entry,  book, page, notes`).
##
