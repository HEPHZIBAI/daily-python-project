'''

Project Brief
Have a look at the following Python script. The script exports the webpage of a given URL to a PDF file.

import pdfkit

# Define the URL and the output file path
url = 'https://en.wikipedia.org/wiki/Elephant'
output_file = 'output.pdf'

# Convert the URL to a PDF
pdfkit.from_url(url, output_file)

print(f'Webpage saved as PDF: {output_file}')
Your task for today’s project to improve the above program by enabling it to convert multiple webpages to PDF. Specifically, your new program should:

Read multiple URLs from a text file. Here is a sample text file.

Save the webpage of each URL into a separate PDF file.

Name the PDF files according to the URL. For example, https___en_wikipedia_org_wiki_Elephant.pdf

Project Learning Benefits
'''