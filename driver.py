import html2text

def convertHTMLtoText(html: str):
   h = html2text.HTML2Text()
   h.ignore_links = True
   h.ignore_images = True
   h.feed(html)
   return h.close()
