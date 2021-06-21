import re




# pat = r'(ftp|http)://(.*?)\.(jpg|png)'
pat = '((http|https)((?!(http|https)).)*?.(jpeg|jpg|png))'

text = 'https://wewewewewrwrwrwrrwrwrwwrhttp:wewewew;http://www.google.image1.jpgwewewe;l12121212121http://www.google.imawewewe1wewewewe.jpg'


all = [x.group() for x in re.finditer(pat,text)]

print(all)