# index_formatter
Take a comma separated values file (CSV) containing your index and output it as HTML file (default), CSV (use `-c` option), or DOCX (use `-d` - requires installing python-docx with pip - see **venv and pip install instructions** section but can be used for HTML and CSV without using pip). Skips first row of your input CSV file assuming it has a header row of column labels - if it lacks a header use `-n` option (`--noheader`) to ensure all rows are included in output.

Default column order assumed in your CSV is Entry (what you look up), Book (book or volume number), Page (page number), Notes (further notes about the entry), Tags (column containing comma separated list of tags - prepended to Entry to make new entries when `-t` is used). That order as used for `-f` option would be `-f ebpnt` - see **Input file column order** section below for more explanation and column orders.


If you don't run `git clone https://github.com/byjosh/index_formatter.git` commands as a matter of course the easiest way to get the code if you are reading this on github.com is click green Code button above & to right and you can download a ZIP file - which most folks can deal with. 
This gets you everything but the `-d` or `--docx` option for .docx file output (for use in word processing software such as Microsoft Word or LibreOffice) - if you need docx output see venv and pip install instructions.

## venv and pip install instructions
To get the docx export functionality one needs [python-docx](https://github.com/python-openxml/python-docx) - so best install this in a [Python virtual environment](https://docs.python.org/3/library/venv.html)

Windows (in PowerShell) - with `your_username` and `your_code_folder` as fields that will change according to your choices - if you unzipped rather than cloned into `your_code_folder` simply start on line 2 not line 1 (assuming you have Python 3 installed)
```
PS C:\Users\your_username\Documents> git clone https://github.com/byjosh/index_formatter.git your_code_folder
PS C:\Users\your_username\Documents> python3.exe -m venv .\your_code_folder\
PS C:\Users\your_username\Documents> cd .\your_code_folder\
PS C:\Users\your_username\Documents\your_code_folder> .\Scripts\Activate.ps1
(your_code_folder) PS C:\Users\your_username\Documents\your_code_folder>  python3.exe -m pip install python-docx
```
**Important note re: last line of `python3.exe -m pip install python-docx` - if not preceded by the  `.\Scripts\Activate.ps1` on previous line this would not install in the virtual environment and if run as `pip install python-docx` it would appear to run - but the docx module would not be available for the script in the correct manner so one needs the `python3.exe -m` prefix i.e. use the full `python3.exe -m pip install python-docx` as shown**

You would now be ready to run the script on Windows - with docx export enabled.

On Linux in a terminal (where `your_username@yourcomputer:~/Documents$` is the prompt and what comes after the `$` is what you enter) you could use the following commands (again if you unzipped the code into `your_code_folder` rather than using a `git clone` command then proceed from the 2nd line presuming the terminal is open in the folder that contains `your_code_folder`.
```
your_username@yourcomputer:~/Documents$  git clone https://github.com/byjosh/index_formatter.git your_code_folder
your_username@yourcomputer:~/Documents$ python3 -m venv your_code_folder/
your_username@yourcomputer:~/Documents$ cd your_code_folder/
your_username@yourcomputer:~/Documents/your_code_folder$ source bin/activate
(your_code_folder) your_username@yourcomputer:~/Documents/your_code_folder$ pip install python-docx
```
Continuing this Linux example the next command to run to take advantage of the new docx export option is:-
```
(your_code_folder) your_username@yourcomputer:~/Documents/your_code_folder$ python3 index_formatter.py test_book_before_page.csv -d -t
```
The `-t` option at the end of preceding command uses any tags present to construct new entries prefixed with the tags.
## Running the script

Put your input CSV file (called `test_book_before_page.csv` or `test_page_before_book.csv` in examples below depending on whether input file has book before page number column or vice versa) in same folder as the index_formatter.py script (so where you unzipped the files - or cloned them if you did a git clone).

index_formatter.py is the script to run in the terminal or PowerShell. The default input CSV column order is Entry, Book, Page, Notes, Tags (see **Input file column order** section below)

Command to run in Mac/Linux terminal is like: 

`python3 index_formatter.py test_book_before_page.csv -o "output_file_title"`

or on Windows in PowerShell the command is like: 

`python3.exe .\index_formatter.py .\test_book_before_page.csv -o "output_file_title"`

Change `test_book_before_page.csv` and  `output_file_title` to appropriate values (though leave as is and it will test the script with the provided test file: test_book_before_page.csv.
### A couple of options
 `-t` processes the tags so each tag in tag column is prefixed to the main index term to create a new entry. This allows one to index a book by noting an entry and a list of words as tags in one column of a spreadsheet and then have this script use those words as prefixes for duplicate entries. If the words in the tag list are subjects, themes or topics this means the script is automatically making a separate entry but under the subject/theme/topic. E.g. putting `apple` as the entry with a tag column of `cooking,fruit,tree` would result in entries for `apple, cooking: apple, fruit: apple, tree: apple` etc.
 
`-c` outputs a CSV (if one does not use `-c` then it outputs an HTML file)  - as the `-t` option will necessary produce a large number of new entries if tags are much used one may wish to manually prune some of those entries - and a CSV file open in a spreadsheet where one can right click and delete irrelevant rows - might be a good way to do that - hence the option of CSV output via the `-c` option.

On Windows in PowerShell the command using those options is like: 

`python3.exe .\index_formatter.py .\test_book_before_page.csv -o "output_file_title" -c -t`

It comes with built in help - so experiment.

## Builtin help

Any options that have `-o OUTPUTTITLE` format are best written with the supplied string put in quotes if there are any characters in string that could mess with terminal (the capitalized OUTPUTTITLE indicates you have to supply a string in place of the capitalized option - here OUTPUTTITLE - if using the option) e.g. `-o "Today's index test"`. 

`-f {ebpnt,epbnt,ebcpnt,enbcpt,enbpt,enbcpt,bpent,bcpent,entbp,entbcp}` also needs input after the `-f` option e.g. `-f ebcpnt`  (see **Input file column order** section below).

Thanks to use of argparse library there is builtin help like the following:

> usage: index_formatter.py [-h] [-o OUTPUTTITLE] [-f {ebpnt,epbnt,ebcpnt,enbcpt,enbpt,enbcpt,bpent,bcpent,entbp,entbcp}] [-t] [-ts TAGSEPARATOR] [-c] [-os OUTPUTSEPARATOR] [-v] [-vv] [-d] inputCSVfile\
>takes a CSV file with columns for entry, book #, [chapter#] , page#, description and tags fields (not necessarily in that order and outputs order HTML or a CSV with tags prepended to the entry\
positional arguments:\
  inputCSVfile          input CSV file to be processed - see README and help below re: order of columns needed\
options:\
  -h, --help            show this help message and exit
> 
> -o OUTPUTTITLE, --outputtitle OUTPUTTITLE\
                        title used in naming output document and in HTML head\
 > \
> -f {ebpnt,epbnt,ebcpnt,enbcpt,enbpt,enbcpt,bpent,bcpent,entbp,entbcp}, --fields {ebpnt,epbnt,ebcpnt,enbcpt,enbpt,enbcpt,bpent,bcpent,entbp,entbcp}\
                        specify order of columns (fields) in your CSV file where each letter is initial letter of following (might call your columns slightly differently but this make clear function of each column): Entry      
                        (what you look up in index e.g. apple), Book (or volume e.g. vol 1) , Chapter [optional], Notes (notes or description on Entry item e.g. popular fruit), Tags [optional in sense program will check if     
                        this is empty column] - comma separated list of classifications that might apply to the entry e.g. for apple depending on context: fruit, tree, cooking, literacy, physics, Abrahamic religion (those are  
                        just examples - in botanical context just fruit and tree would be relevant)\
> \
>  -t, --tags            process tags so that entries are added with the tag prepended to the entry that had tags in the tags column - using tag separator (defaults to : ) - e.g. for an entry of "apple" with tags column of "fruit,cooking" the result would be an entry for "apple" plus entries for "cooking: apple" & "fruit: apple" with notes the same as in the row that had the tags - if you have 6 apple entries but tags only found on row of first apple entry then only that row will be used to make further entries - use tags in tags column on each row you want processed by this option
\
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
> 
> -d, --docx            you can set this option to export a docx file - docx files can be used in
                        wordprocessing software (congratulations on using pip to enable this
                        option)
> 
> -n, --noheader        process all rows of CSV as there is no header row - default is to ignore 1st row assuming it is a header with column labels






## Input file column order

The input file column order by default is `ebpnt`. The default is also to assume that the first line of input CSV is a header row of column labels (if first row is data use the `-n` or `--noheader` option)

The possible columns are:
* Entry (e) - what you look up in an index
* Book (b) - the book or volume it is found in
* Chapter (c) - optional chapter
* Page (p) - page number
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

Trademark footnote: Microsoft, PowerShell, Windows, Microsoft Word, are trademarks of the Microsoft group of companies. Linux is a trademark of Linus Torvalds. The Document Foundation and 
LibreOffice are trademarks of The Document Foundation. Any other trademarks are property of their owners. The mention of the trademarks is solely for the proper acknowledgement of their ownership - no linkage to this project or endorsement of it is implied by the mention of the trademarks.
