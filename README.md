# index_formatter
Take a comma separated values file (CSV) for an index and output it as file

The column layout in the CSV should be entry (e.g. "apple"), page number, book number (e.g. Book 1), notes (e.g. "often mentioned in connection with teaching the alphabet in English")
Remove any column labels before using the script (or modify script to have that as an option)

The order seen in the output will currently put an entry under a term that is Book 2 - 10 before Book 2 110 (impeccable) - but will put Book 4 - 40 before Book 4 - 5 (a minor TODO - not usually that many pages referenced per term)


