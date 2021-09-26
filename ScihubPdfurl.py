from requests_html import HTMLSession
import pandas as pd


def getpdfurl(doi):
  s = HTMLSession()
  headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'cookie': '__ddg1=vIZdy9vxnQG4nUio57zQ; session=0110d1d0ad673d3b1e0398e2e5ead499; __ddgid=ratXmk3e9CJ0O1M9; _ym_uid=1627210666935448269; _ym_d=1627210666; __ddg2=GCD2Zk9ymK4bFSZS; refresh=1632647003.7186; _ym_isad=2',
  'referer': 'https://sci-hub.se/',
  'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'embed',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
  baseurl = 'https://sci-hub.se/'
  r = s.get(baseurl + doi, headers=headers)
  pdfurl = r.html.find('#pdf')
  pdfs = []
  for pdf in pdfurl:
    try:
      url = pdf.find('embed', first=True).attrs['src'].split('#')[-2]
      if url.startswith('https:'):
        url = url
      else:
        url = 'https:' + url
    except:
      pass
    dic = {
      'doi':doi,
      'url':url
    }
    pdfs.append(dic)
  return pdfs


#print(getpdfurl('10.1007/s10555-020-09885-8'))

file = open('test.txt')
doilist = file.readlines()
pdfurllist = []
for doi in doilist:
  c = getpdfurl(doi)
  print(c)

