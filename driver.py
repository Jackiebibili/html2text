from .html2text import HTML2Text

def convertHTMLtoText(html: str)->str:
   h = HTML2Text()
   h.ignore_links = True
   h.ignore_images = True
   h.feed(html)
   return h.close()
