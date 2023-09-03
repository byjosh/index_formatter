# index_formatter
Take a comma separated values file (CSV) for an index and output it as file

## Running the script

Put your input CSV file (called input.csv in examples below) in same folder as the index_to_html.py script.

index_to_html.py is the script to run in the terminal or Powershell

command in Mac/Linux terminal is like: 

`python3 index_to_html.py input.csv output_file_title`

or on Windows in Powershell is like: 

`python3.exe .\index_to_html.py .\input.csv output_file_title`

## Input file requirements
The column layout in the CSV should be entry (e.g. "apple"), page number, book number (e.g. Book 1), notes (e.g. "often mentioned in connection with teaching the alphabet in English")

```
entry, page, book, notes
"apple", 5, "Book 1", "often mentioned when teaching letter A in English alphabet"
```

Remove any row of column labels before using the script (or modify script to have that as an option). Any lines without an entry in first column are ignored for output

The order seen in the output will currently put an entry under a term that is `Book 2 - 10` before `Book 2 - 110` (impeccable) - but will put `Book 4 - 40` before `Book 4 - 5` (a minor TODO - not usually that many pages referenced per term).


