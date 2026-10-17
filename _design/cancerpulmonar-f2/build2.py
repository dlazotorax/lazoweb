import re,os,json,base64,glob,sys
sys.path.insert(0,os.path.expanduser('~/nod'))
from f2_shell import TOP,BIO,CTA
H=os.path.expanduser('~/nod/')
old=open(H+'nodulo-pulmonar.html',encoding='utf-8').read()   # build v1 output (head, JSON-LD, pubs, refs)
faqs=json.load(open(H+'faq.json',encoding='utf-8'))
css=open(H+'estilo.css',encoding='utf-8').read()
main=open(H+'f2_main.html',encoding='utf-8').read()
# head
head=old[:old.index('<style>')]
head=re.sub(r'\s*<link rel="preconnect"[^>]*>','',head)
head=re.sub(r'\s*<link href="https://fonts.googleapis.com[^>]*>','',head)
ga=old[old.index('</style>')+8:old.index('</head>')]
fonts='''  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=DM+Sans:ital,wght@0,400;0,500;0,700;1,400&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/estilo.css" />'''
# pubs & refs
items=re.findall(r'<div class="pubs-item">.*?</div>\s*</div>',old,flags=re.S)
pubs='\n'.join('    '+i.replace('pubs-item','pub').replace('pubs-title','pub-t').replace('pubs-authors','pub-a').replace('pubs-meta','pub-m') for i in items)
refs=re.search(r'<ol class="refs-list">.*?</ol>',old,flags=re.S).group(0).replace('refs-list','refs')
from tblstack import stack
main=stack(main)
main=main.replace('@@PUBS@@',pubs).replace('@@REFS@@',refs)
faqhtml='\n<section class="section" id="faq"><div class="wrap">\n  <h2 class="h2">Preguntas frecuentes sobre el nódulo pulmonar</h2>\n  <div class="faq">\n'+''.join(f'    <details><summary>{q}</summary><p>{a}</p></details>\n' for q,a in faqs)+'  </div>\n</div></section>\n'
lds=re.findall(r'<script type="application/ld\+json">.*?</script>',old[old.index('</head>'):],flags=re.S)
body='<body>\n\n'+TOP.replace('@@ACT@@',' class="active"')+'\n'+main+BIO+faqhtml+CTA+'\n  '+'\n  '.join(lds)+'\n</body>\n</html>\n'
prod=head+fonts+'\n'+ga+'</head>\n'+body
for s in re.findall(r'<script type="application/ld\+json">(.*?)</script>',prod,flags=re.S): json.loads(s)
open(H+'f2/nodulo-pulmonar.html','w',encoding='utf-8').write(prod)
open(H+'f2/estilo.css','w',encoding='utf-8').write(css)
# maqueta: inline css, base href, data URIs for new images
m=prod.replace('<head>','<head>\n  <base href="https://cancerpulmonar.cl/" />',1).replace('  <link rel="stylesheet" href="/estilo.css" />','  <style>\n'+css+'\n  </style>')
IMG=os.path.expanduser('~/mnt/Paginas web/maqueta-nodulo-img/')
for f in glob.glob(IMG+'*.webp'):
    n=os.path.basename(f)
    m=m.replace('src="imgs/'+n+'"','src="data:image/webp;base64,'+base64.b64encode(open(f,'rb').read()).decode()+'"')
FJ=os.path.expanduser('~/mnt/Paginas web/lazoweb/dist/cancerpulmonar/imgs/foto-dr-lazo-bio.jpg')
m=m.replace('src="imgs/foto-dr-lazo-bio.jpg"','src="data:image/jpeg;base64,'+base64.b64encode(open(FJ,'rb').read()).decode()+'"').replace(' loading="lazy"','')
open(os.path.expanduser('~/mnt/Paginas web/maqueta-nodulo-pulmonar-f2.html'),'w',encoding='utf-8').write(m)
print('ok',len(items),'pubs; faqs',len(faqs),'; lds',len(lds))
