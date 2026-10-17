import re,html
def stack(s):
    """Añade data-l (texto del encabezado) a cada td para apilar tablas en móvil."""
    def tb(m):
        t=m.group(0)
        th=[re.sub('<[^>]+>','',x).strip() for x in re.findall(r'<th[^>]*>(.*?)</th>',t,re.S)]
        if not th: return t
        def tr(r):
            i=[0]
            def td(c):
                a=c.group(1); n=int((re.search(r'colspan="(\d+)"',a) or [0,1])[1])
                lab=' · '.join(th[i[0]:i[0]+n]); i[0]+=n
                if 'data-l' in a: return c.group(0)
                return '<td'+a+' data-l="'+html.escape(lab,quote=True)+'">'
            return re.sub(r'<td([^>]*)>',td,r.group(0))
        return re.sub(r'<tr[^>]*>.*?</tr>',tr,t,flags=re.S)
    return re.sub(r'<table[^>]*>.*?</table>',tb,s,flags=re.S)
