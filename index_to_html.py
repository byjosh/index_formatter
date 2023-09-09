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
import html
import argparse

# if you want to see the master dictionary created change logging.FATAL to logging.DEBUG
logging.basicConfig(level=logging.DEBUG)

"""have Location tuple with book and page, then list of tuples consisting of (book, page num, entry)"""
Location = namedtuple('Location', 'book page')
Entry = namedtuple('Entry', 'location notes taglist chapter')
tagseparator = ": "
outputseparator = '--'
csv_input_filename = None
title = None
order = 'ebpnt'
""" The inputs that we want are 
inputfile [required]
title [optional]
field order [optional]
output [optional ]
tags [optional]

The default is it takes a CSV, outputs an HTML file, does not add entries based on tags, 
and has a field order of entry, book, page, notes, tags

possible orders are (grounds for using a switch case perhaps)
"""
field_orders = ['ebpnt',
                'ebcpnt',
                'enbcpt',
                'enbpt',
                'bpent',
                'bcpent',
                ]


parser = argparse.ArgumentParser(prog="index_as_html.py",
                                 description="takes a CSV file with columns for entry, book #, [chapter#] , page#, description and tags fields (not necessarily in that order and outputs order HTML or a CSV with tags prepended to the entry")

parser.add_argument('inputCSVfile',
                    help='input CSV file to be processed - see README and help below re: order of columns needed')
parser.add_argument('-o', '--outputtitle', action='store', help="title used in naming output document and in HTML head")
parser.add_argument('-f', '--fields', action='store',choices=field_orders,
                    help=f'specify order of columns (fields) in your CSV file where each letter is initial letter of following (might call your columns slightly differently but this make clear function of each column):\nEntry (what you look up in index e.g. apple),\nBook (or volume e.g. vol 1) , \nChapter [optional], Notes (notes or description on Entry item e.g. popular fruit), \nTags [optional in sense program will check if this is empty column] - comma separated list of classifications that might apply to the entry e.g. for apple depending on context: fruit, tree, cooking, literacy, physics, Abrahamic religion (those are just examples - in botanical context just fruit and tree would be relevant)')
parser.add_argument('-t', '--tags', action='store_true',
                    help=f'process tags so that entries are added with the tag prepended to the entry - using tag separator (defaults to {tagseparator} )')
parser.add_argument('-ts','--tagseparator',action='store',help=f'The separator between a tag and an entry when adding an entry of tag tagseparator entry default set to { tagseparator} - likely a colon followed by a space')
parser.add_argument('-c', '--csv', action='store_true', help='output file as CSV - if used in conjunctions')
parser.add_argument('-os','--outputseparator',action='store',help='when outputting HTML the book, chapter, page numbers will be concatenated and joined this seperator is between them')



args = parser.parse_args()
print(args)
# set various fields away from defaults
csv_input_filename = html.escape(args.inputCSVfile)
if args.outputtitle:
    title = html.escape(args.outputtitle)
if args.fields:
    order = html.escape(args.fields)
if args.tagseparator:
    tagseparator = html.escape(args.tagseparator)
if args.outputseparator:
    outputseparator = html.escape(args.outputseparator)
def not_file(file):
    """Test file is missing"""
    if path.isfile(file):
        return False
    else:
        return True


def not_csv(file):
    """Tests that file misses a .csv extension"""
    if file.split(".")[-1].casefold() == 'csv'.casefold():
        return False
    else:
        return True


logging.debug(sys.argv)


if not_file(csv_input_filename) or not_csv(csv_input_filename):
    print("first argument does not exist as file or is not a .csv file")
    exit()

elif len(sys.argv) == 4 and isinstance(sys.argv[1], str):

    logging.info(sys.argv)
    logging.info(sys.argv[3])
    if isinstance(sys.argv[3], str) and sys.argv[3] in ["page", 'book']:
        order = sys.argv[3]

    else:
        print('arguments are inputfilename, output title,  page')
        print('page indicate if the entry, page, book, notes is order rather than entry, book, page, notes')
        exit()

logging.info(f'Order is {order} first')


# Export your index as a comma separated values file (CSV format)
# have the strings quoted in double quotes like "this"
# filename - rename this to your CSV file


def create_master_dict(csv_input_filename: str) -> dict:  #
    """Given a CSV file with columns for entry, book number, page number, notes - in that order - return a dictionary with
    entries as keys and value is list of named tuples of Entry(Location(book,page),notes) format"""
    master_dict = {}
    global order
    with open(csv_input_filename, encoding='utf-8') as csvfile:

        index_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        entry = order.find('e')
        book = order.find('b')
        chapter = order.find('c')
        page = order.find('p')
        notes = order.find('n')
        tags = order.find('t')
        chapter_no = None
        taglist = None

        for row in index_reader:
            if chapter != -1:
                chapter_no = row[chapter]
            else:
                chapter_no = None
            if len(row) == len(order):
                taglist = row[tags]
            else:
                taglist = None
            logging.debug(f'Current row is {row}')
            if row[entry] in master_dict.keys():
                master_dict[row[entry]].append(Entry(Location(row[book], row[page]), row[notes],taglist,chapter_no))
            elif row[entry] not in master_dict.keys() and row[entry].strip() != '':
                # the row[entry].strip() != '' means ignore line if no entry
                master_dict[row[entry]] = [Entry(Location(row[book], row[page]), row[notes],taglist,chapter_no)]
            if args.tags is True and taglist is not None:
                for current_tag in taglist.split(','):
                    current_tag = current_tag.strip()
                    current_tag_entry = f'{current_tag}{tagseparator}{row[entry]}'
                    if current_tag_entry in master_dict.keys():
                        master_dict[current_tag_entry].append(
                                Entry(Location(row[book], row[page]), row[notes], taglist, chapter_no))
                    elif current_tag_entry not in master_dict.keys() and row[entry].strip() != '':
                        # the row[entry].strip() != '' means ignore line if no entry
                        master_dict[current_tag_entry] = [Entry(Location(row[book], row[page]), row[notes], taglist, chapter_no)]
        logging.debug(f'dictionary of entries generated is {master_dict}')
    return master_dict


def html_item_output(item):
    return f'<div class="moredetails"><span class="location">{html.escape(item.location.book, quote=True)} -- {html.escape(item.location.page, quote=True)}</span>\
    <span class="notes">{html.escape(item.notes, quote=True)}</span></div>'


def create_page_html():
    entries = create_master_dict(csv_input_filename)
    sorted_keys = sorted(entries.keys(), key=str.casefold)
    output = html_page_components.get_html_header(title)

    def tuple_string(entry_tuple):
        """Function used to get key for ordering book - relies on last char of book sting being a digit"""
        book_num = entry_tuple.location.book.strip()[-1:]
        page_num = entry_tuple.location.page
        if book_num.isdigit() and page_num.isdigit():
            # so book 4 page 40 is not more than book 6 page 7 use x 1000
            float_value = (int(book_num) * 1000) + int(page_num)
            # use a string anyway so results are comparable
            return str(float_value)
        elif not book_num.isdigit() or not page_num.isdigit():
            # it went wrong - use a string
            print(
                f'For better ordering have last character of {entry_tuple.location.book} as number not {book_num} and {page_num} as number')
            return html.escape(f'{book_num}-{page_num}', quote=True)

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
    #write_page_to_file()
    create_master_dict(csv_input_filename)