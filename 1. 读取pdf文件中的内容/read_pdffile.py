import PyPDF2

#  python读取pdf文件
# https://blog.csdn.net/m0_56636447/article/details/127539726
# ok https://www.post.japanpost.jp/zipcode/dl/bangobo/02.pdf
pdfFileObj = open("02.pdf","rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
for item in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(item)
    print(pageObj.extractText())