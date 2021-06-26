# csv-to-json-converter

A converter from CSV to JSON without using any CSV parsing libraries. Was a fun challenge!

### Challenge Considerations:
* Each new line starts with newline character (\n) which should not remain in the text
* Needs to consider that delimiter could be either a comma or a vertical pipe
* Needs to keep the contents in double quotation marks untouched
* Needs to convert numbers to integers and keep the rest of the data as a strings

### Languages used:
Python

### Python libraries used:
* Re
* json

