from PyPDF2 import PdfMerger

merger=PdfMerger()



class Merge():
    def MergePdf(Pdf):
        for pdf in Pdf:
            merger.append(pdf)
        merged_pdf = merger.write_to_bytes()
        return merger_pdf
