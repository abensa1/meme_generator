# Quote Engine

The modules in this folder read data from various files (csv, docx, pdf, txt), process it and return a list of quotes and authors.

## How to use

- Import the 'Ingestor' module class
- Define the path to a document and call the 'Ingestor' class 'parse' method

## Librarires
The modules use the following open source libraries:
- [pandas]
- [python-docx]
- [pdftotext]

## Modules

### CSVImport
Reads the CSV file using 'pandas' library, extracts the lines and returns a list of quotes.

### DOCXImport
Reads the docx file using 'python-docx' library, extracts the lines and returns a list of quotes.

### TXTImport
Reads the txt file, extracts the lines and returns a list of quotes.

### PDFImport
Reads the pdf file using a subprocess to call the 'pdftotext' library and covert the pdf to text. Once PDF converted, it calls the TXTimport class to read the tempt text file extracts the lines and returns a list of quotes.

### IngestorInterface
Abstract class that defines the structure of the Import subclasses

### DogQuotes
Uses the outputs of the Import classes to create a quote object that is used to display quotes



