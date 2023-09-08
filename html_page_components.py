#!/usr/bin/env python3
# This file is from
# https://github.com/byjosh/index_formattter
# licensed under https://www.gnu.org/licenses/gpl-3.0.html
def get_html_header(title: str = None) -> str:
    if title is None:
        title = "My_index"

    header = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">"""

    title = f'<title>{title}</title>'

    style = """   <style type="text/css">
        /* This is an inline stylesheet so */
            .entrycontainer {
                /* This is space between each entry term*/
                 margin-top: 0px;
                }
            .moredetails {
                display: block;
                /* This is how far the notes are indented to right */
                 padding-left: 60px;
                }
                :nth-child(-n + 1 of .moredetails) span.location { 
                /* This is how far the first entry is pushed away from the entry term */
                margin-left: 10px;
            } 
    
            span.location { 
                /* The following is how far the page numbers are pulled left*/
                margin-left: -20px;
                font-style: italic;
                font-weight: bold;
                
                }
            .entry {
                /* This allows the moredetails container with page number and notes to float up to right */
                float: left; 
                font-weight: bold;}
            .notes,.location,.entry {
                margin-left: 10px; 
                
            }
            
            
            .entrycontainer:nth-child(-n + 1 of .moredetails) {
                color: green;
            } 
    
             
    
            </style>"""

    end_header = """</head><body>"""
    return header + title + style + end_header
def get_html_footer() -> str:
    footer = """</body></html>"""
    return footer