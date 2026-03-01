import re

fname = 'c:\\Users\\Administrator\\Downloads\\Resume Builder\\resume-builder-ats.html'
with open(fname, 'r', encoding='utf-8') as f:
    text = f.read()

# Scale CSS font sizes by -2.5pt
def replace_pt(m):
    val = float(m.group(1))
    return f"font-size: {val - 2.5:g}pt"
text = re.sub(r'font-size:\s*([0-9.]+)pt', replace_pt, text)

# Scale Docx font sizes by -5 (which is 2.5pt in half-points)
def scale_val(m):
    tag = m.group(1)
    val = int(m.group(2))
    return f'<{tag} w:val="{val - 5}"/>'

text = re.sub(r'<(w:sz|w:szCs) w:val="([0-9]+)"/>', scale_val, text)

with open(fname, 'w', encoding='utf-8') as f:
    f.write(text)
