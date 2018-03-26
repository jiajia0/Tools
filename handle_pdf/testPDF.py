# @Time    : 2018/3/26 20:07
# @Author  : Leafage
# @File    : handlePDF.py
# @Software: PyCharm
# @Describe: 测试处理PDF文件，参考文档：https://pythonhosted.org/PyPDF2/

from PyPDF2 import PdfFileWriter, PdfFileReader,PdfFileMerger


def get_info_pdf(filename):
    # 打开文件
    file_stream = open(filename, 'rb')

    # 创建一个实例用来读取pdf文件
    pdf_reader = PdfFileReader(file_stream)

   # 获取pdf文件的信息
    document_info = pdf_reader.getDocumentInfo()

    # 获取pdf文件的总页数
    pdf_page_nums = pdf_reader.getNumPages()

    # 获取单页pdf文件数据，得到一个PageObject对象
    single_page = pdf_reader.getPage(1)

    # 获取页面布局
    pdf_layout = pdf_reader.getPageLayout()

    # 检索指定PageObject的页码
    page_num = pdf_reader.getPageNumber(single_page)


def write_pdf():
    # 初始化一个对pdf写操作实例
    pdf_writer = PdfFileWriter()

    # 初始化一个读pdf实例
    pdf_reader = PdfFileReader('ex1.pdf')

    # 将reader中的内容拷贝到writer中，并且可以设置一个参数，当页面添加到writer中会调用该参数，也就是会回掉下面的after_page_append函数，并将writer中的内容传入作为参数
    # pdf_writer.appendPagesFromReader(pdf_reader, after_page_append)
    pdf_writer.addBlankPage(width=350, height=500)

    # pdf加密操作，第一个为
    # pdf_writer.encrypt('leafage', 'hahaha')

    # pdf_writer.write(open('hehepdf.pdf', 'wb'))

    # 写入pdf文件
    pdf_writer.write(open('testfile.pdf', 'wb'))


def after_page_append(writer):
    pass
    # print(writer)


def merge_pdf():
    # 创建一个用来合并文件的实例
    pdf_merger = PdfFileMerger()

    # 首先添加一个Week1_1.pdf文件
    pdf_merger.append('Week1_1.pdf')
    # 然后在第0页后面添加ex1.pdf文件
    pdf_merger.merge(0, 'ex1.pdf')
    # 添加书签
    pdf_merger.addBookmark('这是一个书签', 1)
    # 将其写入到文件中
    pdf_merger.write('merge_pdf.pdf')


if __name__ == '__main__':
    # get_info_pdf('ex1.pdf')
    write_pdf()
    # merge_pdf()

