# index_formatter
Take a comma separated values file (CSV) for an index and output it as file

If you don't run `git clone https://github.com/byjosh/index_formatter.git` commands as a matter of course the easiest way to get the code if you are reading this on github.com is click green Code button above & to right and you can download a ZIP file - which most folks can deal with.

## Running the script

Put your input CSV file (called `test_book_before_page.csv` or `test_page_before_book.csv` in examples below depending on whether input file has book before page number column or vice versa) in same folder as the index_formatter.py script (so where you unzipped the files - or cloned them if you did a git clone).

index_formatter.py is the script to run in the terminal or Powershell. The default input CSV column order is Entry, Book, Page, Notes, Tags (see **Input file column order** section below)

Command to run in Mac/Linux terminal is like: 

`python3 index_formatter.py test_book_before_page.csv -o "output_file_title"`

or on Windows in Powershell the command is like: 

`python3.exe .\index_formatter.py .\test_book_before_page.csv -o "output_file_title"`

Change `test_book_before_page.csv` and  `output_file_title` to appropriate values (though leave as is and it will test the script with the provided test file: test_book_before_page.csv.
### A couple of options
 `-t` processes the tags so each tag in tag column is prefixed to the main index term to create a new entry. This allows one to index a book by noting an entry and a list of words as tags in one column of a spreadsheet and then have this script use those words as prefixes for duplicate entries. If the words in the tag list are subjects, themes or topics this means the script is automatically making a separate entry but under the subject/theme/topic. E.g. putting `apple` as the entry with a tag column of `cooking,fruit,tree` would result in entries for `apple, cooking: apple, fruit: apple, tree: apple` etc.
 
`-c` outputs a CSV (if one does not use `-c` then it outputs an HTML file)  - as the `-t` option will necessary produce a large number of new entries if tags are much used one may wish to manually prune some of those entries - and a CSV file open in a spreadsheet where one can right click and delete irrelevant rows - might be a good way to do that - hence the option of CSV output via the `-c` option.

On Windows in Powershell the command using those options is like: 

`python3.exe .\index_formatter.py .\test_book_before_page.csv -o "output_file_title" -c -t`

It comes with built in help - so experiment.

## Builtin help

Any options that have `-o OUTPUTTITLE` format are best written quotes if there are any characters in string that could mess with terminal (the capitalized OUTPUTTITLE indicates you have to supply a string if using the option) e.g. `-o "Today's index test"`. 

`-f {ebpnt,ebcpnt,enbcpt,enbpt,bpent,bcpent}` also needs input after the `-f` option e.g. `-f ebcpnt`  (see **Input file column order** section below).

Thanks to use of argparse library there is builtin help like the following:

> usage: index_formatter.py [-h] [-o OUTPUTTITLE] [-f {ebpnt,ebcpnt,enbcpt,enbpt,bpent,bcpent}] [-t] [-ts TAGSEPARATOR] [-c] [-os OUTPUTSEPARATOR] [-v] [-vv] inputCSVfile\
>takes a CSV file with columns for entry, book #, [chapter#] , page#, description and tags fields (not necessarily in that order and outputs order HTML or a CSV with tags prepended to the entry\
positional arguments:\
  inputCSVfile          input CSV file to be processed - see README and help below re: order of columns needed\
options:\
  -h, --help            show this help message and exit
> 
> -o OUTPUTTITLE, --outputtitle OUTPUTTITLE\
                        title used in naming output document and in HTML head\
 > \
> -f {ebpnt,ebcpnt,enbcpt,enbpt,bpent,bcpent}, --fields {ebpnt,ebcpnt,enbcpt,enbpt,bpent,bcpent}\
                        specify order of columns (fields) in your CSV file where each letter is initial letter of following (might call your columns slightly differently but this make clear function of each column): Entry      
                        (what you look up in index e.g. apple), Book (or volume e.g. vol 1) , Chapter [optional], Notes (notes or description on Entry item e.g. popular fruit), Tags [optional in sense program will check if     
                        this is empty column] - comma separated list of classifications that might apply to the entry e.g. for apple depending on context: fruit, tree, cooking, literacy, physics, Abrahamic religion (those are  
                        just examples - in botanical context just fruit and tree would be relevant)\
> \
> -t, --tags            process tags so that entries are added with the tag prepended to the entry - using tag separator (defaults to : )\
>\
> -ts TAGSEPARATOR, --tagseparator TAGSEPARATOR\
                        The separator between a tag and an entry when adding an entry of tag tagseparator entry default set to : - likely a colon followed by a space 
> 
> -c, --csv             output file as CSV - if used in conjunctions\ 
-os OUTPUTSEPARATOR, --outputseparator OUTPUTSEPARATOR\
                        when outputting HTML the book, chapter, page numbers will be concatenated and joined this seperator is between them
> 
>  -v                    logging.INFO level of log verbosity
> 
>   -vv                   logging.DEBUG level of logging verbosity





## Input file column order

The input file column order by default is `ebpnt`.

The possible columns are:
* Entry (e) - what you look up in an index
* Book (b) - the book or volume it is found in
* Chapter (c) - optional chapter
* Notes (n) - the longer notes or description regarding an index entry
* Tags (t) - a comma separated list of tags

Possible orders are `ebpnt`, `epbnt`, `ebcpnt`,`enbcpt`,`enbpt`,`bpent`,`bcpent`,`entbp`,`entbcp` (see `field_orders` list in code).
### Example input column orders
```
entry,  book, page, notes, tags
"apple","Book 1", 5,  "often mentioned when teaching letter A in English alphabet","fruit,tree,cooking"
```
The above seen in `test_book_before_page.csv` would be specified `-f=ebpnt` on the command line - but is the default anyway
The below seeen in `test_page_before_book.csv` would be specified `-f=epbnt` on the command line.
```
entry, page, book, notes, tags
"apple", 5, "Book 1", "often mentioned when teaching letter A in English alphabet","education, cooking"
```
## Misc notes
Remove any row of column labels before using the script (or modify script to have that as an option). Any lines without an entry in first column are ignored for output

The order seen for the page numbers for each entry will work best if all book references end so last character is a number (whether `book 3`, `volume 3`, `101.3`) and the page number is a number with no other characters (so: `100` ; not `100-102`) - but the comparison function uses strings to make the comparison - just in case you don't follow these rules. But unless an entry has a half a dozen or more pages referenced one can probably spot the correct order at a glance even if your input data does not play nice with the comparison function.

## Test files
`test_book_before_page.csv` and `test_page_before_book.csv` are provided as test files. With the latter the optional `-f=epbnt` argument is needed as final argument like `python3 index_formatter.py test_page_before_book.csv output_file_title  -f=epbnt` or `python3.exe .\index_formatter.py .\test_page_before_book.csv output_file_title  -f=epbnt`.
