import sys
import PyPDF2

file_name = sys.argv[1]
template = PyPDF2.PdfFileReader(f'{file_name}')

watermark = PyPDF2.PdfFileReader(open('watermark.pdf','rb'))

output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
	page = template.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)

	with open('newwatermarkedfile.pdf', 'wb') as file:
		output.write(file)



