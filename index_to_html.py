#!/usr/bin/env python3
# This file is from
# https://github.com/byjosh/index_formattter
# licensed under https://www.gnu.org/licenses/gpl-3.0.html
import csv
from collections import namedtuple
import html_page_components
import time
import sys
from os import path
import logging
# if you want to see the master dictionary created change logging.FATAL to logging.DEBUG
logging.basicConfig(level=logging.FATAL)

"""have Location tuple with book and page, then list of tuples consisting of (book, page num, entry)"""
Location = namedtuple('Location', 'book page')
Entry = namedtuple('Entry', 'location notes')

csv_input_filename = None
title = None


def print_usage():
    """Usage notes for this script"""
    script_name_not_windows = sys.argv[0].lstrip(".\\")
    script_name_windows = ".\\" + sys.argv[0].lstrip(".\\")
    print("please supply the name of a CSV file as first argument and optionally as second argument a title for your output file ")
    print(f'So command on Mac/Linux like: python3 {script_name_not_windows} input.csv output_file_title ')
    print(f'or on Windows like: python3.exe {script_name_windows} .\input.csv output_file_title')
    print('With output_file_title of "my index"  (surround with quotes if it contains spaces) ')
    print("& at 2pm 1st Sept 2030 the output file is my index_as_html_20300901-140000.html")
    return


if len(sys.argv) < 2:
    print_usage()
elif len(sys.argv) == 2 and path.isfile(sys.argv[1]) and sys.argv[1].split[-1].casefold() == 'csv'.casefold():
    csv_input_filename = sys.argv[1]
elif len(sys.argv) == 3 and isinstance(sys.argv[1], str):
    csv_input_filename = sys.argv[1]
    title = sys.argv[2]


# Export your index as a comma separated values file (CSV format)
# have the strings quoted in double quotes like "this"
# filename - rename this to your CSV file


def create_master_dict(csv_input_filename: str) -> dict:  #
    """Given a CSV file with columns for entry, book number, page number, notes - in that order - return a dictionary with
    entries as keys and value is list of named tuples of Entry(Location(book,page),notes) format"""
    master_dict = {}
    with open(csv_input_filename, encoding='utf-8') as csvfile:

        index_reader = csv.reader(csvfile, delimiter=',', quotechar='"')

        for row in index_reader:
            logging.debug(f'Current row is {row}')
            if row[0] in master_dict.keys():
                master_dict[row[0]].append(Entry(Location(row[2], row[1]), row[3]))
            elif row[0] not in master_dict.keys() and row[0].strip() != '':
                # the row[0].strip() != '' condition means if there is no entry in first column line is ignored
                master_dict[row[0]] = [Entry(Location(row[2], row[1]), row[3])]
        logging.debug(f'dictionary of entries generated is {master_dict}')
    return master_dict


def html_item_output(item):
    return f'<div class="moredetails"><span class="location">{item.location.book} -- {item.location.page}</span><span class="notes">{item.notes}</span></div>'


def create_page_html():
    entries = create_master_dict(csv_input_filename)
    sorted_keys = sorted(entries.keys(), key=str.casefold)
    output = html_page_components.get_html_header(title)
    
    def tuple_string(entry_tuple):
        """Function used to get key for ordering book - relies on last char of book sting being a digit"""
        book_num = entry_tuple.location.book.strip()[-1:]
        page_num = entry_tuple.location.page
        if book_num.isdigit() and page_num.isdigit():
            #so book 4 page 40 is not more than book 6 page 7 use x 1000
            float_value =(int(book_num)*1000)+int(page_num)
            # use a string anyway so results are comparable
            return str(float_value)
        elif not book_num.isdigit() or not page_num.isdigit():
            # it went wrong - use a string
            print(f'For better ordering have last character of {entry_tuple.location.book} as number not {book_num} and {page_num} as number')
            return f'{book_num}-{page_num}'  

    for key in sorted_keys:
        list_of_Entry_tuples = sorted(entries[key], key=tuple_string)
        output += f'<div class="entrycontainer"><div class="entry">{key}</div>'
        for item in list_of_Entry_tuples:
            output += html_item_output(item)
        output += '</div>'

    output += html_page_components.get_html_footer()
    return output


def write_page_to_file():
    # write the html output to a file
    now = time.strftime('%Y%m%d-%H%M%S')
    output_name = f'{title}_as_html_{now}.html'
    with open(output_name, mode='w', encoding='utf-8') as file:
        file.write(create_page_html())
    print(f'Created {output_name} as a file in the same folder as this script')
    logging.debug(f'The arguments provided to script were {sys.argv[1:]}')


if csv_input_filename is not None:
    write_page_to_file()
