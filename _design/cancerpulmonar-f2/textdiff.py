import sys,re,difflib
from bs4 import BeautifulSoup
def words(p):
    s=BeautifulSoup(open(p,encoding='utf-8').read(),'html.parser')
    for t in s(['script','style','head']): t.decompose()
    return s.get_text(' ').split()
def attrs(p):
    s=BeautifulSoup(open(p,encoding='utf-8').read(),'html.parser')
    return sorted(set([a.get('href') for a in s.find_all('a') if a.get('href')])), sorted(set([i.get('alt') for i in s.find_all('img')]))
a,b=sys.argv[1],sys.argv[2]
wa,wb=words(a),words(b)
for op,i1,i2,j1,j2 in difflib.SequenceMatcher(None,wa,wb,autojunk=False).get_opcodes():
    if op!='equal': print(op,'OLD:',' '.join(wa[i1:i2])[:300],'| NEW:',' '.join(wb[j1:j2])[:300])
ha,ia=attrs(a);hb,ib=attrs(b)
print('hrefs only old:',set(ha)-set(hb)); print('hrefs only new:',set(hb)-set(ha)); print('alts diff:',set(ia)^set(ib))
