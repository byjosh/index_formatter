# index_formatter
Take a comma separated values file (CSV) for an index and output it as file

If you don't run `git clone https://github.com/byjosh/index_formatter.git` commands as a matter of course the easiest way to get the code if you are reading this on github.com is click green Code button above & to right and you can download a ZIP file - which most folks can deal with.

## Running the script

Put your input CSV file (called test.csv in examples below) in same folder as the index_to_html.py script (so where you unzipped the files - or cloned them if you did a git clone).

index_to_html.py is the script to run in the terminal or Powershell

Command to run in Mac/Linux terminal is like: 

`python3 index_to_html.py test.csv output_file_title`

or on Windows in Powershell the command is like: 

`python3.exe .\index_to_html.py .\test.csv output_file_title`

Change `test.csv` and  `output_file_title` to appropriate values (though leave as is and it will test the script with the provided test file: test.csv.

## Input file requirements
The column layout in the CSV should be entry (e.g. "apple"), page number, book number (e.g. Book 1), notes (e.g. "often mentioned in connection with teaching the alphabet in English")

```
entry, page, book, notes
"apple", 5, "Book 1", "often mentioned when teaching letter A in English alphabet"
```

Remove any row of column labels before using the script (or modify script to have that as an option). Any lines without an entry in first column are ignored for output

The order seen in the output will currently put an entry under a term that is `Book 2 - 10` before `Book 2 - 110` (impeccable) - but will put `Book 4 - 40` before `Book 4 - 5` (a minor TODO - not usually that many pages referenced per term).


