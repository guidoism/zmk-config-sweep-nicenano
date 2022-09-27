import re, jinja2
from pprint import pprint as pp
from itertools import zip_longest

# TODO: combos

def chunk(it, n):
    args = [iter(it)] * n
    return list(zip_longest(*args))


#    if len(ret) == n:
#        return ret
#    padding = [''] * ((n - len(ret)) // 2)
#    return padding + ret + padding

def make_key(k):
    print(k)
    k = k or ''
    sec = ''
    classes = ['key']
    if m := re.match(r'&none', k):
        k = ''
    elif m := re.match(r'&caps_word', k):
        k = 'CAPS'
    elif m := re.match(r'&bootloader', k):
        k = 'RESET'
    elif m := re.match(r'&bt (\S+)', k):
        k = m.group(1)
    elif m := re.match(r'&kp (\S+)', k):
        k = m.group(1)
    elif m := re.match(r'&sk (\S+)', k):
        k = m.group(1)
        classes.append('oneshot')
    elif m := re.match(r'&mo (\S+)', k):
        layers = {
            '1': 'NUM',
            '2': 'MOV',
        }
        k = m.group(1)
        k = layers.get(k, k)
    elif m := re.match(r'&mt (\S+) (\S+)', k):
        sec, k = m.groups()
        sec = pretty.get(sec, sec)
    k = pretty.get(k, k)
    if not k:
        classes.append('empty')
    classes.append(f'len{len(k)}')
    return {
        'classes': ' '.join(classes),
        'name': k,
        'secondary': sec,
    }

pretty = {k: v for k, v in [s.split() for s in open('pretty.tsv')]}
s = open('config/cradio.keymap').read()
layers = []
for name, layer in re.findall(r'(\w+_layer) {\s+bindings = <(.+?)>;', s, re.DOTALL):
    rows = []
    for row in chunk(re.findall(r'(&[^&]+)', layer, re.DOTALL), 10):
        row = [make_key(k) for k in row if k is not None]
        if len(row) == 4:
            row = [{'classes': 'gone'}] * 3 + row + [{'classes': 'gone'}] * 3
        rows.append(row)
    layers.append(rows)

environment = jinja2.Environment()
template = environment.from_string(open('pretty.html').read())
open('/tmp/aaa.html', 'w').write(template.render(layers=layers))









quit() ############## DEAD ################
for ln, layer in enumerate(chunk(tbl, 4)):
    parts = []
    parts.append(f'<a name="{ln}">')
    parts.append('<table class="keyboard-base">')
    for j, row in enumerate(layer):
        parts.append('<tr>')
        for i, k in enumerate(row):
            secondary = ''
            if m := re.match(r'(\S+)/(\S+)', k):
                k, secondary = m.groups()
            k = replace.get(k, k)
            secondary = replace.get(secondary, secondary)
            classes = 'key'
            if len(k) == 4:
                classes = classes + ' fourletters'
            if j == 1 and (1 <= i <= 4 or 7 <= i <= 10) or j == 3 and 4 <= i <= 7:
                classes = classes + ' homekey'
            if (i == 0 or i == 11 or j == 3) and ln > 5:
                if 'homekey' not in classes:
                      classes = classes + ' gone'
            if secondary:
                parts.append(f'<td class="{classes}">{k}<span class="secondary">{secondary}</span></td>')
            else:
                parts.append(f'<td class="{classes}">{k}</td>')
        parts.append('</tr>')
    parts.append('</table>')
    if ln == 4:
        parts.append('<br><hr><br>')
    open(f'/Users/guido/Downloads/keymap/{ln}.html', 'w').write(header + ('\n'.join(parts)))
    layer_parts.append('\n'.join(parts))
    parts = []
open('/Users/guido/Downloads/keymap.html', 'w').write(header + ('\n'.join(layer_parts)))
