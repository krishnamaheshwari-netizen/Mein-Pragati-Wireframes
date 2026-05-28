"""
Mein Pragati Wireframe Generator
=================================
Renders ~30 remaining wireframes from declarative specs.
Six archetype templates; each spec selects one and provides content.
"""
import os, json, html
from pathlib import Path

ROOT = Path(__file__).parent.parent

# ---------- chrome ----------

def head(title, mobile=True):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
{'<meta name="viewport" content="width=375, initial-scale=1" />' if mobile else ''}
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" />
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,0,0&display=swap" />
<link rel="stylesheet" href="../shared/tokens.css" />
<link rel="stylesheet" href="../shared/components.css" />
<script src="../shared/wireframe-nav.js" defer></script>"""

MOBILE_BODY_STYLE = """<style>
body { width: 375px; min-height: 812px; background: var(--surface-1); }
.content { padding: var(--space-4); display: flex; flex-direction: column; gap: var(--space-3); padding-bottom: 90px; }
.field-card { background: var(--surface-0); border-radius: var(--radius-md); padding: var(--space-3) var(--space-4); box-shadow: var(--shadow-sm); }
.lbl { font-size: 11px; text-transform: uppercase; letter-spacing: 0.04em; color: var(--ink-500); font-weight: var(--w-semibold); margin-bottom: 6px; }
.val { font-size: 14px; color: var(--ink-900); }
.list-card { background: var(--surface-0); border-radius: var(--radius-md); box-shadow: var(--shadow-sm); overflow: hidden; }
.list-card .row { padding: var(--space-3) var(--space-4); border-top: 1px solid var(--surface-3); display: flex; gap: var(--space-3); align-items: center; }
.list-card .row:first-child { border-top: none; }
.list-card .row .icon-box { width: 36px; height: 36px; border-radius: var(--radius-md); background: var(--brand-primary-50); color: var(--brand-primary); display: inline-flex; align-items: center; justify-content: center; flex-shrink: 0; }
.list-card .row .body { flex: 1; min-width: 0; }
.list-card .row .title { font-size: 13px; font-weight: var(--w-semibold); color: var(--ink-900); }
.list-card .row .meta { font-size: 11px; color: var(--ink-500); margin-top: 2px; }
.bottom-bar { position: fixed; bottom: 0; left: 0; right: 0; background: var(--surface-0); padding: var(--space-3) var(--space-4); border-top: 1px solid var(--surface-3); display: flex; gap: var(--space-2); }
.bottom-bar .btn { flex: 1; }
.fab { position: fixed; right: var(--space-4); bottom: var(--space-6); }
.hero { background: linear-gradient(135deg, var(--brand-primary) 0%, var(--brand-primary-700) 100%); color: white; padding: var(--space-5) var(--space-4); margin: -16px -16px var(--space-3); border-radius: 0; position: relative; overflow: hidden; }
.hero::after { content: ''; position: absolute; right: -40px; top: -40px; width: 140px; height: 140px; background: rgba(255,255,255,0.08); border-radius: 50%; }
.hero .meta-lbl { font-size: 11px; opacity: 0.85; text-transform: uppercase; letter-spacing: 0.05em; font-weight: var(--w-semibold); }
.hero .big { font-size: 32px; font-weight: var(--w-bold); line-height: 1; margin: 6px 0; }
.hero .sub { font-size: 13px; opacity: 0.9; }
.kpi-row-m { display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-2); }
.kpi-card-m { background: var(--surface-0); border-radius: var(--radius-md); padding: var(--space-3); box-shadow: var(--shadow-sm); text-align: center; }
.kpi-card-m .num { font-size: 22px; font-weight: var(--w-bold); color: var(--ink-900); }
.kpi-card-m .lbl-k { font-size: 10px; color: var(--ink-500); text-transform: uppercase; letter-spacing: 0.04em; font-weight: var(--w-semibold); margin-top: 4px; }
.section-head-m { font-size: 11px; text-transform: uppercase; letter-spacing: 0.05em; color: var(--ink-500); font-weight: var(--w-semibold); padding: var(--space-2) 0; }
input.field-input-m, textarea.field-input-m { width: 100%; border: 1px solid var(--ink-100); border-radius: var(--radius-md); padding: 10px var(--space-3); font-family: inherit; font-size: 14px; outline: none; }
input.field-input-m:focus, textarea.field-input-m:focus { border-color: var(--brand-primary); }
textarea.field-input-m { min-height: 80px; resize: vertical; }
.radio-group-m { display: flex; gap: 6px; flex-wrap: wrap; }
.radio-item-m { padding: 8px 14px; border: 1px solid var(--ink-100); border-radius: var(--radius-md); font-size: 13px; color: var(--ink-700); }
.radio-item-m.selected { border-color: var(--brand-primary); background: var(--brand-primary-50); color: var(--brand-primary); font-weight: var(--w-medium); }
</style>"""

WEB_BODY_STYLE = """<style>
body { width: 1440px; min-height: 900px; background: var(--surface-1); display: grid; grid-template-columns: var(--web-sidebar-width) 1fr; grid-template-rows: var(--web-topbar-height) 1fr; grid-template-areas: "side top" "side main"; }
.topbar-wrap { grid-area: top; } .side-wrap { grid-area: side; } .main-wrap { grid-area: main; padding: var(--space-6); overflow-y: auto; }
.kpi-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--space-3); margin-bottom: var(--space-5); }
.kpi-row .kpi-card { padding: var(--space-3) var(--space-4); }
.kpi-row .kpi-card .label { font-size: 11px; font-weight: var(--w-semibold); text-transform: uppercase; letter-spacing: 0.04em; }
.kpi-row .kpi-card .value { font-size: 22px; }
.banner { padding: var(--space-3) var(--space-4); border-radius: var(--radius-md); display: flex; gap: 8px; align-items: center; margin-bottom: var(--space-4); font-size: 13px; }
.banner.info { background: var(--status-info-bg); color: var(--status-info-ink); }
.banner.warn { background: var(--status-warning-bg); color: var(--status-warning-ink); }
.banner.danger { background: var(--status-danger-bg); color: var(--status-danger-ink); }
.scheme-tag { display: inline-block; font-size: 11px; padding: 2px 7px; border-radius: var(--radius-sm); font-weight: var(--w-medium); }
.scheme-tag.scheme { background: rgba(26, 62, 119, 0.1); color: var(--chart-1); }
.scheme-tag.services { background: rgba(0, 176, 240, 0.1); color: var(--chart-4); }
.scheme-tag.awareness { background: rgba(213, 56, 20, 0.1); color: var(--chart-3); }
.bar-track { width: 100%; height: 6px; background: var(--surface-2); border-radius: 99px; overflow: hidden; }
.bar-track .bar-fill { height: 100%; background: var(--status-success); }
.section-h { display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-3); }
.section-h h3 { margin: 0; font-size: 16px; }
.two-col { display: grid; grid-template-columns: 2fr 1fr; gap: var(--space-4); }
.split-col { display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-3); }
.field-block { margin-bottom: var(--space-3); }
.field-block label { font-size: 11px; text-transform: uppercase; letter-spacing: 0.04em; color: var(--ink-500); font-weight: var(--w-semibold); display: block; margin-bottom: 4px; }
.field-block .value-text { font-size: 14px; color: var(--ink-900); font-weight: var(--w-medium); }
.field-block input, .field-block select, .field-block textarea { width: 100%; padding: 8px var(--space-3); border: 1px solid var(--ink-100); border-radius: var(--radius-md); font-family: inherit; font-size: 14px; outline: none; }
</style>"""

def status_bar():
    return """<div class="mobile-statusbar"><span>9:41</span><span class="right"><span class="material-symbols-rounded">signal_cellular_4_bar</span><span class="material-symbols-rounded">wifi</span><span class="material-symbols-rounded">battery_full</span></span></div>"""

def mobile_appbar(title, back_link=None, right_icon=None, avatar=None):
    avatar_html = f'<div class="avatar avatar-sm">{avatar}</div>' if avatar else ''
    back_html = f'<button class="icon-btn" data-link-to="{back_link}"><span class="material-symbols-rounded">arrow_back</span></button>' if back_link else ''
    right_html = f'<button class="icon-btn"><span class="material-symbols-rounded">{right_icon}</span></button>' if right_icon else ''
    return f'<div class="mobile-appbar">{back_html}{avatar_html}<div class="title">{html.escape(title)}</div>{right_html}</div>'

def web_topbar(role="admin"):
    avatar = "MV" if role == "admin" else "SS"
    role_tag = "Admin" if role == "admin" else ""
    return f"""<div class="topbar-wrap"><div class="web-topbar"><div class="brand">Mein Pragati</div><div class="crisil-mark">A CRISIL Foundation initiative{' · ' + role_tag if role_tag else ''}</div><div class="right"><div class="refresh-badge"><span class="material-symbols-rounded">schedule</span> Last refreshed 09:38</div><div class="avatar avatar-sm">{avatar}</div></div></div></div>"""

def web_sidebar(role="admin", active_item=None):
    if role == "admin":
        user = ('MV', 'Maya Vengurlekar', 'CRISIL Foundation · Admin')
        items = [
            ('Programme', 'space_dashboard', 'P4-M6-S01'),
            ('Dashboard', 'dashboard', None),
            ('SHGs', 'diversity_3', 'P4-M5-S01'),
            ('Users', 'person', None),
            ('Masters', 'location_city', None),
            ('Sakhi Transactions', 'bar_chart', 'P1-M16-S01'),
            ('Household Resilience', 'groups', None),
            ('Training Kit', 'important_devices', None),
            ('Reports', 'event_note', None),
            ('Feedback', 'chat', 'P1-M17-S02'),
            ('Messages', 'forum', 'P1-M2-S03'),
        ]
    else:  # NGO
        user = ('SS', 'Sandeep Singh', 'NGO Partner — SeSTA')
        items = [
            ('Dashboard', 'dashboard', None),
            ('Sakhi Transactions', 'bar_chart', 'P1-M16-S01'),
            ('Rejected & Action', 'error', 'P0-M1-S04'),
            ('Household Resilience', 'groups', None),
            ('FO Details', 'person', None),
            ('Attendance', 'how_to_reg', 'P2-M3-S03'),
            ('Centre Details', 'apartment', None),
            ('Sakhi Details', 'people', None),
            ('Best Activities', 'photo_library', 'P2-M12-S03'),
            ('Reports', 'event_note', None),
            ('Feedback', 'chat', 'P1-M17-S02'),
            ('Messages', 'forum', 'P1-M2-S01'),
        ]
    items_html = ""
    for label, icon, link in items:
        active = 'active' if label == active_item else ''
        dl = f' data-link-to="{link}"' if link and label != active_item else ''
        items_html += f'<a class="nav-item {active}"{dl}><span class="material-symbols-rounded">{icon}</span> {label}</a>'
    return f"""<div class="side-wrap"><div class="web-sidebar" style="height: calc(100vh - var(--web-topbar-height));"><div class="user-block"><div class="avatar">{user[0]}</div><div><div class="name">{user[1]}</div><div class="role">{user[2]}</div></div></div><nav>{items_html}</nav></div></div>"""

def page_header(title, subtitle, actions=None):
    parts = []
    for a in (actions or []):
        variant = a.get('variant','btn-secondary')
        attr = ' data-link-to="' + a['to'] + '"' if a.get('to') else ''
        icon = '<span class="material-symbols-rounded">' + a.get('icon','') + '</span> ' if a.get('icon') else ''
        parts.append('<button class="btn ' + variant + '"' + attr + '>' + icon + a['label'] + '</button>')
    actions_html = ''.join(parts)
    return f"""<div class="page-header"><div class="title-block"><div class="title">{title}</div><div class="subtitle">{subtitle}</div></div><div class="actions">{actions_html}</div></div>"""

def screen_id_badge(sid):
    return f'<div class="screen-id-badge">{sid}</div>'

# ---------- archetypes ----------

def render_mobile_list(spec):
    """Mobile list screen: appbar + sections of cards."""
    sections_html = ""
    for sec in spec.get('sections', []):
        if sec.get('hero'):
            h = sec['hero']
            sections_html += f"""<div class="hero"><div class="meta-lbl">{h.get('label','')}</div><div class="big">{h['title']}</div>{f'<div class="sub">{h["sub"]}</div>' if h.get('sub') else ''}</div>"""
        if sec.get('head'):
            sections_html += f'<div class="section-head-m">{sec["head"]}</div>'
        if sec.get('banner'):
            sections_html += f'<div class="banner {sec["banner"].get("type","info")}"><span class="material-symbols-rounded">{sec["banner"].get("icon","info")}</span><span>{sec["banner"]["text"]}</span></div>'
        if sec.get('kpis'):
            kpi_html = ''.join(f'<div class="kpi-card-m"><div class="num">{k["num"]}</div><div class="lbl-k">{k["label"]}</div></div>' for k in sec['kpis'])
            sections_html += f'<div class="kpi-row-m">{kpi_html}</div>'
        if sec.get('rows'):
            rows_html = ''
            for row in sec['rows']:
                link_attr = f' data-link-to="{row["link"]}"' if row.get('link') else ''
                meta = row.get('meta', '')
                trailing = ''
                if row.get('pill'):
                    p = row['pill']
                    trailing = f'<span class="pill pill-{p["type"]}"><span class="dot"></span> {p["text"]}</span>'
                elif row.get('amount'):
                    trailing = f'<span style="font-size:14px;font-weight:var(--w-semibold);font-variant-numeric:tabular-nums;">{row["amount"]}</span>'
                elif row.get('arrow', True):
                    trailing = '<span class="material-symbols-rounded" style="color:var(--ink-300);">chevron_right</span>'
                icon = row.get('icon', 'circle')
                rows_html += f'<div class="row"{link_attr}><div class="icon-box"><span class="material-symbols-rounded">{icon}</span></div><div class="body"><div class="title">{row["title"]}</div><div class="meta">{meta}</div></div>{trailing}</div>'
            sections_html += f'<div class="list-card">{rows_html}</div>'
    bottom = ''
    if spec.get('bottom_buttons'):
        btn_parts = []
        for b in spec['bottom_buttons']:
            variant = b.get('variant','btn-secondary')
            attr = ' data-link-to="' + b['to'] + '"' if b.get('to') else ''
            icon = '<span class="material-symbols-rounded">' + b['icon'] + '</span> ' if b.get('icon') else ''
            btn_parts.append('<button class="btn ' + variant + '"' + attr + '>' + icon + b['label'] + '</button>')
        btns = ''.join(btn_parts)
        bottom = f'<div class="bottom-bar">{btns}</div>'
    fab = ''
    if spec.get('fab'):
        f = spec['fab']
        fab = '<a href="#" class="btn-fab fab" data-link-to="' + f.get('to','') + '"><span class="material-symbols-rounded">' + f.get('icon','add') + '</span></a>'
    return f"""{head(spec['title'])}{MOBILE_BODY_STYLE}</head><body>{screen_id_badge(spec['id'])}{status_bar()}{mobile_appbar(spec.get('app_title', spec['title']), back_link=spec.get('back'), right_icon=spec.get('right_icon'))}<div class="content">{sections_html}</div>{fab}{bottom}</body></html>"""

def render_mobile_form(spec):
    """Mobile form screen: appbar + fields + bottom button."""
    fields_html = ''
    for f in spec.get('fields', []):
        if f.get('type') == 'radio':
            opts = ''.join(f'<div class="radio-item-m {"selected" if i==0 else ""}">{o}</div>' for i, o in enumerate(f['options']))
            fields_html += f'<div class="field-card"><div class="lbl">{f["label"]}</div><div class="radio-group-m">{opts}</div></div>'
        elif f.get('type') == 'textarea':
            fields_html += f'<div class="field-card"><div class="lbl">{f["label"]}</div><textarea class="field-input-m" placeholder="{f.get("placeholder","")}">{f.get("value","")}</textarea></div>'
        elif f.get('type') == 'banner':
            fields_html += f'<div class="banner {f.get("variant","info")}"><span class="material-symbols-rounded">{f.get("icon","info")}</span><span>{f["text"]}</span></div>'
        elif f.get('type') == 'value':
            fields_html += f'<div class="field-card"><div class="lbl">{f["label"]}</div><div class="val">{f["value"]}</div></div>'
        else:
            fields_html += f'<div class="field-card"><div class="lbl">{f["label"]}</div><input class="field-input-m" type="{f.get("type","text")}" placeholder="{f.get("placeholder","")}" value="{f.get("value","")}" /></div>'
    bottom = ''
    if spec.get('bottom_buttons'):
        btn_parts = []
        for b in spec['bottom_buttons']:
            variant = b.get('variant','btn-secondary')
            attr = ' data-link-to="' + b['to'] + '"' if b.get('to') else ''
            icon = '<span class="material-symbols-rounded">' + b['icon'] + '</span> ' if b.get('icon') else ''
            btn_parts.append('<button class="btn ' + variant + '"' + attr + '>' + icon + b['label'] + '</button>')
        btns = ''.join(btn_parts)
        bottom = f'<div class="bottom-bar">{btns}</div>'
    return f"""{head(spec['title'])}{MOBILE_BODY_STYLE}</head><body>{screen_id_badge(spec['id'])}{status_bar()}{mobile_appbar(spec.get('app_title', spec['title']), back_link=spec.get('back'))}<div class="content">{fields_html}</div>{bottom}</body></html>"""

def render_web_dashboard(spec):
    """Web admin/NGO dashboard with KPI cards and sections."""
    role = spec.get('role', 'admin').lower()
    sb_role = 'admin' if role == 'admin' else 'ngo'
    kpis_html = ''
    if spec.get('kpis'):
        kpis_html = '<div class="kpi-row">'
        for k in spec['kpis']:
            bg = k.get('bg', 'var(--brand-primary-50)')
            ic_color = k.get('color', 'var(--brand-primary)')
            kpis_html += f'<div class="kpi-card"><div class="icon-circle" style="background:{bg};color:{ic_color};"><span class="material-symbols-rounded">{k.get("icon","insights")}</span></div><div><div class="label">{k["label"]}</div><div class="value">{k["value"]}</div><div class="sub">{k.get("sub","")}</div></div></div>'
        kpis_html += '</div>'

    sections_html = ''
    for sec in spec.get('sections', []):
        if sec.get('banner'):
            sections_html += f'<div class="banner {sec["banner"].get("type","info")}"><span class="material-symbols-rounded">{sec["banner"].get("icon","info")}</span><span>{sec["banner"]["text"]}</span></div>'
        if sec.get('cards'):
            cards_html = ''
            for c in sec['cards']:
                link_attr = f' data-link-to="{c.get("link","")}"' if c.get('link') else ''
                cards_html += f'<div class="card card-bordered"{link_attr}><div class="card-header"><div class="title">{c["title"]}</div></div><p style="margin:0;font-size:13px;color:var(--ink-700);line-height:1.5;">{c.get("desc","")}</p></div>'
            sections_html += f'<div style="display:grid;grid-template-columns:repeat({sec.get("cols",3)},1fr);gap:var(--space-3);margin-bottom:var(--space-4);">{cards_html}</div>'
        if sec.get('table'):
            t = sec['table']
            head_html = ''.join(f'<th{" class=text-right" if c.get("align")=="right" else ""}>{c["label"]}</th>' for c in t['columns'])
            rows_html = ''
            for r in t['rows']:
                cells = ''
                for i, c in enumerate(t['columns']):
                    v = r.get(c['key'], '')
                    align = ' class="text-right"' if c.get('align') == 'right' else ''
                    cells += f'<td{align}>{v}</td>'
                rows_html += f'<tr>{cells}</tr>'
            sections_html += f'<div class="section-h"><h3>{sec.get("title","")}</h3>{sec.get("toolbar","")}</div><div class="table-wrap"><table class="data-table"><thead><tr>{head_html}</tr></thead><tbody>{rows_html}</tbody></table></div>'
        if sec.get('content_html'):
            sections_html += sec['content_html']

    return f"""{head(spec['title'], mobile=False)}{WEB_BODY_STYLE}</head><body>{screen_id_badge(spec['id'])}{web_topbar(sb_role)}{web_sidebar(sb_role, active_item=spec.get('active_item'))}<div class="main-wrap">{page_header(spec.get('h_title', spec['title']), spec.get('h_sub',''), spec.get('actions'))}{kpis_html}{sections_html}</div></body></html>"""

def render_web_form(spec):
    """Web form/edit screen: 2-col layout with form on left, side info on right."""
    role = spec.get('role', 'admin').lower()
    sb_role = 'admin' if role == 'admin' else 'ngo'
    fields_html = ''
    for f in spec.get('fields', []):
        ft = f.get('type', 'text')
        if ft == 'value':
            fields_html += f'<div class="field-block"><label>{f["label"]}</label><div class="value-text">{f["value"]}</div></div>'
        elif ft == 'textarea':
            fields_html += f'<div class="field-block"><label>{f["label"]}</label><textarea rows="3">{f.get("value","")}</textarea></div>'
        elif ft == 'select':
            opts = ''.join(f'<option{" selected" if i==0 else ""}>{o}</option>' for i, o in enumerate(f.get('options', [])))
            fields_html += f'<div class="field-block"><label>{f["label"]}</label><select>{opts}</select></div>'
        else:
            fields_html += f'<div class="field-block"><label>{f["label"]}</label><input type="{ft}" value="{f.get("value","")}" placeholder="{f.get("placeholder","")}" /></div>'

    side_html = ''
    for sc in spec.get('side_cards', []):
        parts = []
        for i in sc.get('items', []):
            parts.append('<div style="margin-bottom:var(--space-2);font-size:12px;"><strong>' + i["label"] + ':</strong> ' + i["value"] + '</div>')
        items_html = ''.join(parts)
        desc = sc.get('desc','')
        desc_html = '<p style="margin:0;font-size:12px;color:var(--ink-500);">' + desc + '</p>' if desc else ''
        side_html += '<div class="card" style="margin-bottom:var(--space-3);"><div class="card-header"><div class="title" style="font-size:14px;">' + sc["title"] + '</div></div>' + items_html + desc_html + '</div>'

    return f"""{head(spec['title'], mobile=False)}{WEB_BODY_STYLE}</head><body>{screen_id_badge(spec['id'])}{web_topbar(sb_role)}{web_sidebar(sb_role, active_item=spec.get('active_item'))}<div class="main-wrap">{page_header(spec.get('h_title', spec['title']), spec.get('h_sub',''), spec.get('actions'))}<div class="two-col"><div class="card" style="padding:var(--space-5);">{fields_html}<div style="display:flex;justify-content:flex-end;gap:8px;padding-top:var(--space-3);border-top:1px solid var(--surface-3);margin-top:var(--space-3);"><button class="btn btn-tertiary" data-link-to="{spec.get('back','')}">Cancel</button><button class="btn btn-primary">{spec.get('save_label','Save')}</button></div></div><div>{side_html}</div></div></div></body></html>"""

# ---------- specs ----------

SCREENS = [
  # ====== PHASE 2 REMAINDER ======
  {'archetype': 'mobile_form', 'id':'P2-M4-S06', 'phase':2, 'sprint':7, 'module':'M-4', 'moduleName':'Mobile FO Create Sakhi removed',
   'title':'FO — Create Sakhi removed (banner)', 'role':'FO', 'platform':'mobile',
   'app_title':'Sakhi onboarding', 'back':'DHW-1',
   'purpose':'Soft-landing communication for FOs whose ability to create Sakhis from mobile has been moved to the NGO admin web flow. Sakhi onboarding now sits with the NGO admin.',
   'fields':[
     {'type':'banner','variant':'warn','icon':'info','text':'Sakhi onboarding has moved. NGO admin onboards new Sakhis via the web portal (single or bulk CSV). Please request a Sakhi via Messages — your NGO will action within 48 hours.'},
     {'type':'value','label':'Why this change','value':'A single onboarding path improves data quality, reduces duplicates, and lets your NGO manage the village master sheet centrally.'},
     {'type':'value','label':'Need to onboard a Sakhi today?','value':'Tap "Request via Messages" below. We pre-fill a template with your details — you just confirm and send.'},
   ],
   'bottom_buttons':[
     {'label':'Back','variant':'btn-secondary','to':'DHW-1'},
     {'label':'Request via Messages','variant':'btn-primary','icon':'forum','to':'P1-M2-S06'},
   ]},

  {'archetype': 'mobile_form', 'id':'P2-M18-S01', 'phase':2, 'sprint':8, 'module':'M-18', 'moduleName':'Approval window',
   'title':'Sakhi — Create transaction (window-aware)', 'role':'Sakhi', 'platform':'mobile',
   'app_title':'New transaction', 'back':'DHW-1',
   'purpose':'Create-transaction form with date picker that visibly greys out dates outside the 15-day approval window for the current cycle. A banner explains the window state and time remaining.',
   'fields':[
     {'type':'banner','variant':'warn','icon':'schedule','text':'January window closes in 5 days (Feb 15). Pick a meeting date in January only — earlier months are closed.'},
     {'type':'value','label':'Beneficiary','value':'Rina Kalita (tap to change)'},
     {'type':'value','label':'Meeting date — valid range','value':'1 Jan 2026 — 31 Jan 2026 only · earlier dates greyed out'},
     {'type':'text','label':'Meeting date','value':'25 Jan 2026','placeholder':''},
     {'type':'select','label':'Scheme','options':['PMJJBY','PMSBY','APY','KCC','Bhamashah']},
     {'type':'text','label':'Remuneration amount','value':'436','placeholder':'₹'},
   ],
   'bottom_buttons':[
     {'label':'Cancel','variant':'btn-secondary','to':'DHW-1'},
     {'label':'Save & submit','variant':'btn-primary','icon':'send','to':'DHW-1'},
   ]},

  {'archetype': 'mobile_list', 'id':'P2-M18-S02', 'phase':2, 'sprint':8, 'module':'M-18', 'moduleName':'Approval window',
   'title':'Sakhi — Window closing banner', 'role':'Sakhi', 'platform':'mobile',
   'app_title':'Home','back':None, 'right_icon':'sync',
   'purpose':'Home banner that shows the days remaining in the current 15-day approval window. Becomes more urgent as cutoff approaches.',
   'sections':[
     {'hero':{'label':'Window closes in 3 days','title':'12 pending transactions','sub':'Submit before 15 Feb to be counted in January cycle.'}},
     {'head':'What to do today'},
     {'rows':[
       {'icon':'list_alt','title':'Review 12 pending','meta':'You can edit, complete and submit','link':'DHW-1'},
       {'icon':'help','title':'How the 15-day window works','meta':'Each month gives 15 days into next month to log'},
       {'icon':'phone','title':'Need an extension? Talk to your FO','meta':'Only NGO admin can grant grace day extension'},
     ]},
   ]},

  {'archetype': 'mobile_list', 'id':'P2-FO2-S01', 'phase':2, 'sprint':8, 'module':'FO-2', 'moduleName':'Training Records',
   'title':'FO — Training Records list', 'role':'FO', 'platform':'mobile',
   'app_title':'Training Records', 'right_icon':'filter_alt',
   'purpose':'FO views past monthly training sessions she submitted, with approval status from NGO admin. Tile to add a new session.',
   'sections':[
     {'kpis':[{'num':'12','label':'Sessions this year'},{'num':'10','label':'Approved'}]},
     {'head':'This month'},
     {'rows':[
       {'icon':'school','title':'PMJJBY refresher · 18 Jan','meta':'8 Sakhis attended · 1 photo','pill':{'type':'success','text':'Approved'}},
       {'icon':'school','title':'KCC walkthrough · 11 Jan','meta':'6 Sakhis attended · 2 photos','pill':{'type':'warning','text':'Pending NGO'}},
     ]},
     {'head':'Earlier'},
     {'rows':[
       {'icon':'school','title':'FHC counselling refresher · 28 Dec','meta':'9 Sakhis · 3 photos','pill':{'type':'success','text':'Approved'}},
       {'icon':'school','title':'Fraud awareness · 14 Dec','meta':'7 Sakhis · 1 photo','pill':{'type':'success','text':'Approved'}},
     ]},
   ],
   'fab':{'icon':'add','to':'P2-FO2-S02'}},

  {'archetype': 'mobile_form', 'id':'P2-FO2-S02', 'phase':2, 'sprint':8, 'module':'FO-2', 'moduleName':'Training Records',
   'title':'FO — Add training record', 'role':'FO', 'platform':'mobile',
   'app_title':'New training session', 'back':'P2-FO2-S01',
   'purpose':'FO captures the details of a monthly training session she conducted: date, agenda, participants, photos. Submitted to NGO admin for approval.',
   'fields':[
     {'type':'text','label':'Topic','placeholder':'e.g. PMJJBY refresher','value':'PMJJBY refresher'},
     {'type':'date','label':'Date','value':'2026-01-25'},
     {'type':'text','label':'Participants count','value':'8','placeholder':'Number of Sakhis present'},
     {'type':'textarea','label':'Agenda / what was covered','value':'Walked through the new claim process · refresher on premium amounts · Q&A on common rejections.'},
     {'type':'banner','variant':'info','icon':'add_a_photo','text':'Upload 1-4 photos of the training (group, board, attendance sheet).'},
     {'type':'value','label':'After you save','value':'Goes to NGO admin for approval. You will see status update in the list.'},
   ],
   'bottom_buttons':[
     {'label':'Save draft','variant':'btn-secondary'},
     {'label':'Submit','variant':'btn-primary','icon':'send','to':'P2-FO2-S01'},
   ]},

  {'archetype': 'web_dashboard', 'id':'P2-FO2-S03', 'phase':2, 'sprint':8, 'module':'FO-2', 'moduleName':'Training Records',
   'title':'NGO — Training Records approval queue', 'role':'NGO', 'platform':'web', 'active_item':'Sakhi Details',
   'h_title':'Training Records — Approval queue', 'h_sub':'Review training sessions submitted by FOs · Approve or reject with feedback',
   'purpose':'NGO admin queue of FO training sessions awaiting review. Each row has FO, topic, photos, attendance, date and inline approve/reject.',
   'kpis':[
     {'label':'Pending review','value':'8','sub':'oldest is 3 days','icon':'pending'},
     {'label':'Approved this month','value':'31','sub':'+12% vs last','icon':'check_circle','bg':'var(--status-success-bg)','color':'var(--status-success)'},
     {'label':'Rejected this month','value':'2','sub':'usually photo issues','icon':'block','bg':'var(--status-danger-bg)','color':'var(--status-danger)'},
     {'label':'Avg review time','value':'4h','sub':'within SLA','icon':'schedule','bg':'var(--status-info-bg)','color':'var(--status-info)'},
   ],
   'sections':[
     {'title':'Awaiting your review','table':{
       'columns':[{'key':'fo','label':'FO'},{'key':'topic','label':'Topic'},{'key':'date','label':'Date'},{'key':'count','label':'Attended'},{'key':'photos','label':'Photos'},{'key':'action','label':'Action'}],
       'rows':[
         {'fo':'<strong>Dhaniram Deka</strong><div style="font-size:11px;color:var(--ink-500);">Morigaon</div>','topic':'KCC walkthrough','date':'11 Jan 2026','count':'6','photos':'2','action':'<button class="btn btn-primary btn-sm">Review</button>'},
         {'fo':'<strong>Pranab Das</strong><div style="font-size:11px;color:var(--ink-500);">Nalbari</div>','topic':'APY enrollment process','date':'15 Jan 2026','count':'11','photos':'3','action':'<button class="btn btn-primary btn-sm">Review</button>'},
         {'fo':'<strong>Surya Bora</strong><div style="font-size:11px;color:var(--ink-500);">Darrang</div>','topic':'Fraud awareness — UPI scams','date':'18 Jan 2026','count':'14','photos':'4','action':'<button class="btn btn-primary btn-sm">Review</button>'},
       ]}}
   ]},

  {'archetype': 'mobile_list', 'id':'P2-FO9-S01', 'phase':2, 'sprint':8, 'module':'FO-9', 'moduleName':'Active Sakhi monthly view',
   'title':'FO — Active Sakhis (monthly view)', 'role':'FO', 'platform':'mobile',
   'app_title':'My Sakhis — January',
   'purpose':'FO sees her assigned Sakhis with January counts: linkages, awareness, transactions. Month picker at the top. Tap to drill into individual Sakhi performance.',
   'sections':[
     {'head':'January 2026 · 18 active Sakhis'},
     {'kpis':[{'num':'18 / 18','label':'Active'},{'num':'342','label':'Linkages'}]},
     {'rows':[
       {'icon':'person','title':'Sumitra Devi','meta':'37 linkages · 142 beneficiaries · ₹3,840','pill':{'type':'success','text':'Top'}},
       {'icon':'person','title':'Suranjana Das','meta':'31 linkages · 118 beneficiaries · ₹3,240'},
       {'icon':'person','title':'Tara Bora','meta':'28 linkages · 96 beneficiaries · ₹2,800'},
       {'icon':'person','title':'Runamoni Deka','meta':'24 linkages · 88 beneficiaries · ₹2,640'},
       {'icon':'person','title':'Fatema Begum','meta':'10 linkages · 32 beneficiaries · ₹980','pill':{'type':'warning','text':'Needs support'}},
     ]},
   ]},

  {'archetype': 'web_dashboard', 'id':'P2-M14-S01', 'phase':2, 'sprint':8, 'module':'M-14', 'moduleName':'Reports expansion',
   'title':'Reports — FO tab (new)', 'role':'NGO', 'platform':'web', 'active_item':'Reports',
   'h_title':'Reports', 'h_sub':'8 tabs · added: FO performance · Quarterly · Half-yearly',
   'purpose':'Reports module gains a new FO tab parallel to Sakhi. Shows per-FO aggregate metrics with the same period selector applied to monthly/quarterly/half-yearly.',
   'actions':[{'label':'Download Excel','variant':'btn-secondary','icon':'download'}],
   'sections':[
     {'content_html':'<div class="tabs" style="margin-bottom:var(--space-4);"><div class="tab">Sakhi</div><div class="tab active">FO <span style="margin-left:4px;background:var(--brand-primary);color:white;padding:1px 6px;border-radius:99px;font-size:10px;">NEW</span></div><div class="tab">Schemes</div><div class="tab">Monthly</div><div class="tab">Quarterly</div><div class="tab">Half-yearly</div><div class="tab">Milestones</div><div class="tab">Budget</div></div><div class="seg-control" style="margin-bottom:var(--space-4);"><button>This week</button><button class="active">January</button><button>Q3</button><button>H2</button></div>'},
     {'title':'FO aggregate · January 2026','table':{
       'columns':[{'key':'fo','label':'FO'},{'key':'sakhis','label':'Active Sakhis','align':'right'},{'key':'linkages','label':'Linkages','align':'right'},{'key':'income','label':'Income (₹)','align':'right'},{'key':'attendance','label':'Attendance','align':'right'},{'key':'rejected','label':'Rejected','align':'right'}],
       'rows':[
         {'fo':'<strong>Dhaniram Deka</strong>','sakhis':'18','linkages':'342','income':'31,420','attendance':'96%','rejected':'4'},
         {'fo':'<strong>Ramen Kalita</strong>','sakhis':'22','linkages':'418','income':'38,560','attendance':'91%','rejected':'6'},
         {'fo':'<strong>Pranab Das</strong>','sakhis':'25','linkages':'468','income':'42,180','attendance':'100%','rejected':'3'},
         {'fo':'<strong>Jugnu Medhi</strong>','sakhis':'19','linkages':'298','income':'27,120','attendance':'82%','rejected':'5'},
         {'fo':'<strong>Surya Bora</strong>','sakhis':'21','linkages':'248','income':'22,840','attendance':'65%','rejected':'9'},
       ]}}
   ]},

  {'archetype': 'web_dashboard', 'id':'P2-M14-S03', 'phase':2, 'sprint':8, 'module':'M-14', 'moduleName':'Reports expansion',
   'title':'Reports — User Dump download', 'role':'NGO', 'platform':'web', 'active_item':'Reports',
   'h_title':'Download User Dump', 'h_sub':'Export all users with their attributes · scoped to your geographic access',
   'purpose':'CSV export of user roster for HR / audit / capacity-planning. Admin picks scope (state/district/block/role/active status) then downloads.',
   'sections':[
     {'content_html':'''<div class="card" style="padding:var(--space-5);"><h3 style="margin:0 0 var(--space-3);">Choose what to include</h3>
     <div class="split-col" style="margin-bottom:var(--space-4);"><div class="field-block"><label>Roles</label><div style="display:flex;gap:6px;"><span class="filter-chip active">FOs</span><span class="filter-chip active">Sakhis</span><span class="filter-chip">Admins</span></div></div><div class="field-block"><label>Status</label><div style="display:flex;gap:6px;"><span class="filter-chip active">Active</span><span class="filter-chip">Inactive</span><span class="filter-chip">Exit</span></div></div></div>
     <div class="split-col" style="margin-bottom:var(--space-4);"><div class="field-block"><label>State</label><select><option>All my states</option><option>Assam</option><option>Rajasthan</option></select></div><div class="field-block"><label>District</label><select><option>All</option></select></div></div>
     <div class="field-block"><label>Columns</label><div style="display:flex;flex-wrap:wrap;gap:6px;"><span class="filter-chip active">Name</span><span class="filter-chip active">Mobile</span><span class="filter-chip active">Geo</span><span class="filter-chip active">Joining date</span><span class="filter-chip">Email</span><span class="filter-chip">GSE status</span><span class="filter-chip">Batch year</span><span class="filter-chip">Secondary job</span></div></div>
     <div class="banner info" style="margin-top:var(--space-4);"><span class="material-symbols-rounded">info</span> Export will contain <strong>266 rows</strong> (12 FOs + 248 Sakhis + 6 admins) across 5 districts.</div>
     <div style="display:flex;justify-content:flex-end;gap:8px;padding-top:var(--space-4);border-top:1px solid var(--surface-3);margin-top:var(--space-4);"><button class="btn btn-tertiary">Cancel</button><button class="btn btn-primary"><span class="material-symbols-rounded">download</span> Download CSV (266 rows)</button></div></div>'''}
   ]},

  {'archetype': 'mobile_form', 'id':'DHW-4', 'phase':2, 'sprint':6, 'module':'DHW-4', 'moduleName':'Photo evidence quality check',
   'title':'Photo evidence quality check — concept', 'role':'Sakhi', 'platform':'mobile',
   'app_title':'Photo check', 'back':'DHW-1',
   'purpose':'On-device quality check on every evidence photo before it leaves the device. Catches blur, darkness, low resolution. Forces a retake instead of getting rejected later.',
   'fields':[
     {'type':'banner','variant':'warn','icon':'warning','text':'This photo looks blurry. Please retake — the FO will likely reject it.'},
     {'type':'value','label':'What we checked','value':'✅ Brightness: ok · ❌ Sharpness: blurred 47% · ✅ Resolution: 1920×1080 · ✅ Size: 1.2 MB'},
     {'type':'value','label':'Tips for a better photo','value':'1. Stand 30-60 cm from the document. 2. Tap on the document on screen to focus. 3. Make sure both hands are steady. 4. Daylight is better than tubelight.'},
   ],
   'bottom_buttons':[
     {'label':'Use anyway','variant':'btn-secondary'},
     {'label':'Retake','variant':'btn-primary','icon':'photo_camera'},
   ]},

  {'archetype': 'web_dashboard', 'id':'DHW-6', 'phase':2, 'sprint':7, 'module':'DHW-6', 'moduleName':'Saved filter presets',
   'title':'Saved filter presets', 'role':'NGO', 'platform':'web', 'active_item':'Sakhi Transactions',
   'h_title':'Saved filter presets', 'h_sub':'Save commonly-used filter combinations. One-click apply on revisit.',
   'purpose':'A management screen for the saved filter presets that show up in the Transactions filter drawer. Reorder, rename, delete, share with team.',
   'sections':[
     {'title':'Your presets','table':{
       'columns':[{'key':'star','label':''},{'key':'name','label':'Name'},{'key':'desc','label':'What it filters'},{'key':'use','label':'Used','align':'right'},{'key':'action','label':''}],
       'rows':[
         {'star':'★','name':'<strong>My pending queue</strong>','desc':'Status: Pending NGO · My districts only · Last 30 days','use':'42×','action':'<button class="btn btn-secondary btn-sm">Apply</button> <button class="icon-btn"><span class="material-symbols-rounded">edit</span></button>'},
         {'star':'★','name':'<strong>January KCC linkages</strong>','desc':'Scheme: KCC · Meeting date: Jan 2026 · Status: Approved','use':'18×','action':'<button class="btn btn-secondary btn-sm">Apply</button> <button class="icon-btn"><span class="material-symbols-rounded">edit</span></button>'},
         {'star':'★','name':'<strong>Barpeta district only</strong>','desc':'District: Barpeta · All schemes · All status','use':'56×','action':'<button class="btn btn-secondary btn-sm">Apply</button> <button class="icon-btn"><span class="material-symbols-rounded">edit</span></button>'},
         {'star':'☆','name':'<strong>Sumitra Devi performance</strong>','desc':'Sakhi: Sumitra Devi · Last 60 days · All status','use':'8×','action':'<button class="btn btn-secondary btn-sm">Apply</button> <button class="icon-btn"><span class="material-symbols-rounded">edit</span></button>'},
       ]}},
     {'content_html':'<div class="card card-bordered" style="margin-top:var(--space-4);"><div style="display:flex;gap:8px;align-items:center;"><span class="material-symbols-rounded" style="color:var(--brand-primary);">tips_and_updates</span><div><div style="font-size:14px;font-weight:var(--w-semibold);">Tip: share presets with your team</div><div style="font-size:12px;color:var(--ink-500);">Click the share icon next to a preset name to send it to other NGO Partners in your org.</div></div></div></div>'},
   ]},

  # ====== PHASE 3 ======
  {'archetype': 'mobile_form', 'id':'P3-M11-S02', 'phase':3, 'sprint':9, 'module':'M-11', 'moduleName':'My Budget',
   'title':'My Budget — Add income', 'role':'Sakhi', 'platform':'mobile',
   'app_title':'Add income', 'back':'P3-M11-S01',
   'purpose':'Quick income entry. Choose date, source, category, amount. Mein Pragati earnings are auto-pulled — manual entry is for other income (e.g. tailoring, dairy, gifts).',
   'fields':[
     {'type':'date','label':'Date','value':'2026-01-28'},
     {'type':'select','label':'Source','options':['Other income (manual)','Mein Pragati (auto)']},
     {'type':'select','label':'Category','options':['Tailoring','Dairy','Farming','Gift','Other']},
     {'type':'text','label':'Amount (₹)','value':'200','placeholder':'How much?'},
     {'type':'textarea','label':'Note (optional)','placeholder':'Anything else to remember…'},
   ],
   'bottom_buttons':[
     {'label':'Cancel','variant':'btn-secondary','to':'P3-M11-S01'},
     {'label':'Save income','variant':'btn-primary','icon':'check','to':'P3-M11-S01'},
   ]},

  {'archetype': 'mobile_form', 'id':'P3-M11-S03', 'phase':3, 'sprint':9, 'module':'M-11', 'moduleName':'My Budget',
   'title':'My Budget — Add expense', 'role':'Sakhi', 'platform':'mobile',
   'app_title':'Add expense', 'back':'P3-M11-S01',
   'purpose':'Quick expense entry. Pick a category from icons, enter amount and a note. Categories shown are a placeholder — final list pending from Biswajit.',
   'fields':[
     {'type':'date','label':'Date','value':'2026-01-28'},
     {'type':'radio','label':'Category','options':['Food','Transport','Health','Education','Other']},
     {'type':'text','label':'Amount (₹)','value':'200','placeholder':'How much?'},
     {'type':'textarea','label':'Note (optional)','placeholder':'e.g. bus fare to zonal office'},
   ],
   'bottom_buttons':[
     {'label':'Cancel','variant':'btn-secondary','to':'P3-M11-S01'},
     {'label':'Save expense','variant':'btn-primary','icon':'check','to':'P3-M11-S01'},
   ]},

  {'archetype': 'mobile_list', 'id':'P3-M11-S05', 'phase':3, 'sprint':9, 'module':'M-11', 'moduleName':'My Budget',
   'title':'My Budget — Month summary', 'role':'Sakhi', 'platform':'mobile',
   'app_title':'January summary', 'back':'P3-M11-S01',
   'purpose':'End-of-month roll-up. Shows total in, total out, savings, category breakdown. Simple table — no charts per SOW.',
   'sections':[
     {'hero':{'label':'January 2026 saved','title':'₹ 2,180','sub':'₹ 3,840 earned · ₹ 1,660 spent'}},
     {'head':'Where money came from'},
     {'rows':[
       {'icon':'badge','title':'Mein Pragati','meta':'7 linkages approved','amount':'₹ 3,200'},
       {'icon':'storefront','title':'Tailoring (Other)','meta':'2 entries','amount':'₹ 440'},
       {'icon':'redeem','title':'Gift (Other)','meta':'1 entry','amount':'₹ 200'},
     ]},
     {'head':'Where money went'},
     {'rows':[
       {'icon':'school','title':'Education','meta':'School fees','amount':'₹ 800'},
       {'icon':'restaurant','title':'Food & groceries','meta':'6 entries','amount':'₹ 460'},
       {'icon':'medical_services','title':'Health','meta':'2 entries','amount':'₹ 220'},
       {'icon':'directions_bus','title':'Transport','meta':'4 entries','amount':'₹ 180'},
     ]},
   ]},

  {'archetype': 'mobile_list', 'id':'P3-M8-S02', 'phase':3, 'sprint':10, 'module':'M-8', 'moduleName':'Beneficiary Receipts',
   'title':'Sakhi — Generate receipt (after approval)', 'role':'Sakhi', 'platform':'mobile',
   'app_title':'Approved · receipt ready',
   'purpose':'After NGO approval, the Sakhi sees a "Generate Receipt" CTA on the approved transaction. Shows beneficiary, transaction details, and lets her pick a delivery channel.',
   'sections':[
     {'banner':{'type':'success','icon':'check_circle','text':'Approved by NGO yesterday · receipt is ready'}},
     {'head':'Transaction'},
     {'rows':[
       {'icon':'person','title':'Rina Kalita · PMJJBY','meta':'Insurance · ₹ 436 · 12 Jan','arrow':False},
     ]},
     {'head':'Send the receipt to Rina'},
     {'rows':[
       {'icon':'print','title':'Printable card (A6)','meta':'Print on Bluetooth printer','link':'P3-M8-S01'},
       {'icon':'sms','title':'SMS with PDF link','meta':'Send to 9485 67xxxx'},
       {'icon':'campaign','title':'IVR · read aloud in Assamese','meta':'~45 sec call, beneficiary presses 1 to confirm'},
       {'icon':'share','title':'WhatsApp share','meta':'Send as image from your phone'},
     ]},
   ],
   'bottom_buttons':[
     {'label':'Skip for now','variant':'btn-secondary'},
     {'label':'Send via 2 channels','variant':'btn-primary','icon':'send','to':'P3-M8-S01'},
   ]},

  {'archetype': 'mobile_list', 'id':'P3-FO6-S01', 'phase':3, 'sprint':11, 'module':'FO-6', 'moduleName':'Badges',
   'title':'FO — Badges & leaderboard', 'role':'FO', 'platform':'mobile',
   'app_title':'Recognition',
   'purpose':'FO sees badges they have earned and a state-internal leaderboard. Refreshed monthly on the 5th from previous-month performance.',
   'sections':[
     {'hero':{'label':'YOUR DECEMBER BADGE','title':'Top FO · Assam','sub':'Earned 27 Jan · monthly · state-wise'}},
     {'head':'Your trophy cabinet'},
     {'rows':[
       {'icon':'emoji_events','title':'Top FO · December 2025','meta':'342 linkages this month','arrow':False},
       {'icon':'trending_up','title':'Most-improved Sakhi mentor · Q3','meta':'+38% income across your 18 Sakhis','arrow':False},
       {'icon':'workspace_premium','title':'100% attendance · November','meta':'Marked every working day','arrow':False},
     ]},
     {'head':'Leaderboard · Assam · December'},
     {'rows':[
       {'icon':'looks_one','title':'You · Dhaniram Deka','meta':'342 linkages · Morigaon'},
       {'icon':'looks_two','title':'Pranab Das · Nalbari','meta':'318 linkages'},
       {'icon':'looks_3','title':'Ramen Kalita · Barpeta','meta':'298 linkages'},
       {'icon':'person','title':'Jugnu Medhi · Kamrup','meta':'4 · 256 linkages'},
       {'icon':'person','title':'Surya Bora · Darrang','meta':'5 · 218 linkages'},
     ]},
   ]},

  {'archetype': 'web_dashboard', 'id':'P3-FO6-S03', 'phase':3, 'sprint':11, 'module':'FO-6', 'moduleName':'Badges',
   'title':'Admin — Badge criteria configuration', 'role':'admin', 'platform':'web', 'active_item':'Dashboard',
   'h_title':'Badge criteria', 'h_sub':'Configure which badges exist, how they are calculated, and when they refresh',
   'purpose':'Admin defines the badge taxonomy. Each badge has a name, a criteria expression, a recipient type (FO or Sakhi), a refresh schedule, a visibility scope.',
   'kpis':[
     {'label':'Active badges','value':'12','sub':'across FO + Sakhi','icon':'emoji_events'},
     {'label':'Awarded last cycle','value':'87','sub':'Dec 2025','icon':'workspace_premium','bg':'var(--status-success-bg)','color':'var(--status-success)'},
     {'label':'Next refresh','value':'5 Feb','sub':'4 days away','icon':'schedule','bg':'var(--status-info-bg)','color':'var(--status-info)'},
     {'label':'Scope','value':'State-wise','sub':'cross-NGO','icon':'public'},
   ],
   'sections':[
     {'title':'Badges','table':{
       'columns':[{'key':'name','label':'Badge'},{'key':'who','label':'For'},{'key':'crit','label':'Criteria'},{'key':'sched','label':'Refresh'},{'key':'scope','label':'Scope'},{'key':'action','label':''}],
       'rows':[
         {'name':'<strong>🏆 Top FO</strong>','who':'FO','crit':'Top 1 per state by linkage count','sched':'Monthly · 5th','scope':'State, cross-NGO','action':'<button class="btn btn-secondary btn-sm">Edit</button>'},
         {'name':'<strong>🥇 Top Sakhi</strong>','who':'Sakhi','crit':'Top 5 per district by income','sched':'Monthly · 5th','scope':'District','action':'<button class="btn btn-secondary btn-sm">Edit</button>'},
         {'name':'<strong>💪 Most-improved Sakhi mentor</strong>','who':'FO','crit':'Highest % income growth across own Sakhis','sched':'Quarterly','scope':'State','action':'<button class="btn btn-secondary btn-sm">Edit</button>'},
         {'name':'<strong>📅 100% attendance</strong>','who':'FO','crit':'Marked every working day','sched':'Monthly','scope':'State','action':'<button class="btn btn-secondary btn-sm">Edit</button>'},
         {'name':'<strong>🎓 GSE certified — first cycle</strong>','who':'Sakhi','crit':'Cleared GSE exam in onboarding cycle','sched':'On certification','scope':'NGO','action':'<button class="btn btn-secondary btn-sm">Edit</button>'},
       ]}}
   ]},

  {'archetype': 'mobile_list', 'id':'P3-M13-S01', 'phase':3, 'sprint':11, 'module':'M-13', 'moduleName':'Training Kit videos',
   'title':'Training Kit — videos (mobile)', 'role':'Sakhi', 'platform':'mobile',
   'app_title':'Training Kit', 'right_icon':'search',
   'purpose':'Sakhi/FO Training Kit extended with video content. Card grid mixes PDF cards (existing) and video cards (new — with play icon + duration).',
   'sections':[
     {'head':'Newly added'},
     {'rows':[
       {'icon':'play_circle','title':'PMJJBY refresher (4 min)','meta':'Video · हिन्दी · added 3 days ago'},
       {'icon':'play_circle','title':'KCC walkthrough (8 min)','meta':'Video · অসমীয়া · added 5 days ago'},
       {'icon':'play_circle','title':'Bhamashah scheme update (5 min)','meta':'Video · हिन्दी · added 1 week ago'},
     ]},
     {'head':'Schemes'},
     {'rows':[
       {'icon':'picture_as_pdf','title':'PMSBY brochure','meta':'PDF · English + हिन्दी'},
       {'icon':'picture_as_pdf','title':'APY enrollment process','meta':'PDF · English'},
       {'icon':'play_circle','title':'PMSBY claim story (3 min)','meta':'Video · हिन्दी'},
     ]},
     {'head':'Services'},
     {'rows':[
       {'icon':'picture_as_pdf','title':'Account opening checklist','meta':'PDF · English + हिन्दी'},
       {'icon':'play_circle','title':'KYC document handling (6 min)','meta':'Video · অসমীয়া'},
     ]},
   ]},

  {'archetype': 'web_form', 'id':'P3-M13-S03', 'phase':3, 'sprint':11, 'module':'M-13', 'moduleName':'Training Kit videos',
   'title':'Admin — Upload training video', 'role':'admin', 'platform':'web', 'active_item':'Training Kit',
   'h_title':'Upload training video', 'h_sub':'Extends Training Kit with video uploads · plays on mobile in any of 3 languages',
   'purpose':'Admin uploads a training video, picks the scheme/state, attaches caption files for each supported language, and publishes to the field.',
   'fields':[
     {'type':'text','label':'Title','value':'PMJJBY refresher','placeholder':''},
     {'type':'select','label':'Type','options':['Scheme','Services','Awareness']},
     {'type':'select','label':'Scheme','options':['PMJJBY','PMSBY','APY','KCC','Bhamashah']},
     {'type':'select','label':'State (audience)','options':['All','Assam only','Rajasthan only']},
     {'type':'textarea','label':'Short description','value':'4-minute refresher on the new PMJJBY claim process, with screen-by-screen walkthrough.'},
     {'type':'value','label':'Video file','value':'pmjjby-refresher.mp4 · 12.4 MB · 4:08 duration · ✅ uploaded'},
     {'type':'value','label':'Captions','value':'हिन्दी (हिन्दी-captions.vtt) · অসমীয়া (assamese-captions.vtt) — both uploaded'},
   ],
   'side_cards':[
     {'title':'Reach','items':[{'label':'Audience','value':'All Sakhis in Assam'},{'label':'Devices','value':'5,274 active'}],'desc':'Will appear in Training Kit on next sync.'},
     {'title':'File size guidance','desc':'Keep under 25 MB. Mobile data is precious. Use 480p portrait for screen-walkthroughs.'},
   ],
   'save_label':'Publish to field',
   'back':None},

  {'archetype': 'web_dashboard', 'id':'DHW-7', 'phase':3, 'sprint':10, 'module':'DHW-7', 'moduleName':'Profile completion meter',
   'title':'Profile completion meter — concept', 'role':'admin', 'platform':'web', 'active_item':'Users',
   'h_title':'Profile completion across the cadre', 'h_sub':'Gamified profile hygiene · gentle prompts in-app · admin sees the roll-up',
   'purpose':'Track completeness of Sakhi and FO profiles (GSE date, exam cert, photo, batch year, etc.). Surfacing gaps gives admin a data-hygiene lever without nagging.',
   'kpis':[
     {'label':'Profile avg','value':'78%','sub':'+12% vs last quarter','icon':'trending_up','bg':'var(--status-success-bg)','color':'var(--status-success)'},
     {'label':'Below 50%','value':'48','sub':'Sakhis need attention','icon':'warning','bg':'var(--status-warning-bg)','color':'var(--status-warning)'},
     {'label':'Missing GSE date','value':'124','sub':'most common gap','icon':'event'},
     {'label':'Missing photo','value':'67','sub':'second-most common','icon':'image_not_supported'},
   ],
   'sections':[
     {'title':'Cadre profiles · sorted by completeness','table':{
       'columns':[{'key':'name','label':'Name'},{'key':'role','label':'Role'},{'key':'meter','label':'Completeness'},{'key':'missing','label':'Missing'},{'key':'action','label':''}],
       'rows':[
         {'name':'<strong>Sumitra Devi</strong>','role':'Sakhi','meter':'<div style="display:flex;gap:8px;align-items:center;"><div class="bar-track"><div class="bar-fill" style="width:100%;"></div></div><span>100%</span></div>','missing':'—','action':'<button class="btn btn-secondary btn-sm">View</button>'},
         {'name':'<strong>Pushpa Kanwar</strong>','role':'Sakhi','meter':'<div style="display:flex;gap:8px;align-items:center;"><div class="bar-track"><div class="bar-fill" style="width:85%;"></div></div><span>85%</span></div>','missing':'GSE date · Secondary job','action':'<button class="btn btn-secondary btn-sm">View</button>'},
         {'name':'<strong>Fatema Begum</strong>','role':'Sakhi','meter':'<div style="display:flex;gap:8px;align-items:center;"><div class="bar-track"><div class="bar-fill" style="width:62%;background:var(--status-warning);"></div></div><span>62%</span></div>','missing':'Photo · Exam cert · Secondary job','action':'<button class="btn btn-secondary btn-sm">View</button>'},
         {'name':'<strong>Aarti Bhargav</strong>','role':'Sakhi','meter':'<div style="display:flex;gap:8px;align-items:center;"><div class="bar-track"><div class="bar-fill" style="width:38%;background:var(--status-danger);"></div></div><span>38%</span></div>','missing':'Photo · GSE date · Exam cert · Email · Batch year','action':'<button class="btn btn-secondary btn-sm">View</button>'},
       ]}}
   ]},

  # ====== PHASE 4 ======
  {'archetype': 'web_form', 'id':'P4-M5-S02', 'phase':4, 'sprint':12, 'module':'M-5', 'moduleName':'SHG entity',
   'title':'SHG detail — Manalisha SHG', 'role':'admin', 'platform':'web', 'active_item':'SHGs',
   'h_title':'Manalisha SHG · SHG-AS-04392', 'h_sub':'Bahjani village · Barpeta district · Formed 2021',
   'purpose':'Full SHG profile. Replaces the free-text institution name with structured fields: federation/VO, SRLM linkage, RF receipt, member list, assigned Sakhi.',
   'actions':[{'label':'Open in mobile','variant':'btn-secondary','icon':'smartphone'},{'label':'Edit','variant':'btn-primary','icon':'edit'}],
   'fields':[
     {'type':'value','label':'SHG name','value':'Manalisha SHG'},
     {'type':'value','label':'Federation / VO','value':'Bahjani Mahila Sangha'},
     {'type':'value','label':'Formation date','value':'14 March 2021'},
     {'type':'value','label':'Assigned Sakhi','value':'Sumitra Devi (since June 2023)'},
     {'type':'value','label':'Member count','value':'12 women'},
     {'type':'value','label':'SRLM linked?','value':'✅ Yes · linked since 22 Aug 2022'},
     {'type':'value','label':'Revolving Fund received?','value':'✅ Yes · ₹ 15,000 received on 14 Nov 2022'},
     {'type':'value','label':'VO membership','value':'✅ Bahjani Mahila Sangha'},
     {'type':'value','label':'Avg resilience score','value':'82 / 100 (High band)'},
   ],
   'side_cards':[
     {'title':'Members','desc':'12 women — tap the list below to see each member, her FHC score, and her linkage history.','items':[]},
     {'title':'History','items':[{'label':'2021','value':'Formed · 12 founder members'},{'label':'2022','value':'SRLM linkage · RF received'},{'label':'2023','value':'Sumitra Devi joined as Sakhi'},{'label':'2024','value':'Internal savings crossed ₹1 lakh'}]},
   ],
   'back':'P4-M5-S01'},

  {'archetype': 'web_dashboard', 'id':'P4-M5-S05', 'phase':4, 'sprint':12, 'module':'M-5', 'moduleName':'Cluster',
   'title':'Cluster list (admin)', 'role':'admin', 'platform':'web', 'active_item':'SHGs',
   'h_title':'Sakhi clusters', 'h_sub':'A cluster is a group of Sakhis working in the same geo — typically 8-15 Sakhis under one FO',
   'purpose':'Cluster modelling (separate from Centre — Q-1 in implementation plan). Shows clusters with their FO and member count.',
   'sections':[
     {'banner':{'type':'warn','icon':'flag','text':'Cluster is modelled as a separate entity from Centre (per recommendation in implementation plan §6 Q-1). Awaiting Crisil sign-off.'}},
     {'title':'Clusters · Assam + Rajasthan','table':{
       'columns':[{'key':'name','label':'Cluster'},{'key':'fo','label':'Lead FO'},{'key':'sakhis','label':'Sakhis','align':'right'},{'key':'geo','label':'Geography'},{'key':'avg','label':'Avg income','align':'right'},{'key':'action','label':''}],
       'rows':[
         {'name':'<strong>Bahjani Cluster</strong>','fo':'Dhaniram Deka','sakhis':'18','geo':'Bahjani · Sorbhog · Bhabanipur','avg':'₹ 2,950','action':'<button class="btn btn-secondary btn-sm">View</button>'},
         {'name':'<strong>Sorbhog Cluster</strong>','fo':'Ramen Kalita','sakhis':'22','geo':'Sorbhog · Barpeta','avg':'₹ 3,180','action':'<button class="btn btn-secondary btn-sm">View</button>'},
         {'name':'<strong>Nalbari Central</strong>','fo':'Pranab Das','sakhis':'25','geo':'Nalbari · Mukalmua','avg':'₹ 3,420','action':'<button class="btn btn-secondary btn-sm">View</button>'},
         {'name':'<strong>Hajo Cluster</strong>','fo':'Jugnu Medhi','sakhis':'19','geo':'Hajo · Kamrup','avg':'₹ 2,640','action':'<button class="btn btn-secondary btn-sm">View</button>'},
         {'name':'<strong>Ajeetgarh Cluster</strong>','fo':'Rajesh Kumar','sakhis':'14','geo':'Ajeetgarh · Sikar','avg':'₹ 2,420','action':'<button class="btn btn-secondary btn-sm">View</button>'},
         {'name':'<strong>Alwar Rural Cluster</strong>','fo':'Vinod Khan','sakhis':'16','geo':'Alwar Rural · Alwar','avg':'₹ 2,580','action':'<button class="btn btn-secondary btn-sm">View</button>'},
       ]}}
   ]},

  {'archetype': 'web_dashboard', 'id':'P4-M5-S08', 'phase':4, 'sprint':12, 'module':'M-5', 'moduleName':'SHG migration',
   'title':'SHG migration tool — free-text → entity', 'role':'admin', 'platform':'web', 'active_item':'SHGs',
   'h_title':'SHG migration · auto-match review', 'h_sub':'Resolving 8,217 beneficiary records that have free-text SHG names · 6,891 auto-matched, 1,326 need manual review',
   'purpose':'One-time admin utility to resolve legacy free-text "institution_name" values into formal SHG entities. Fuzzy-matches with confidence score; admin confirms or rejects each match.',
   'kpis':[
     {'label':'Total records','value':'8,217','sub':'with free-text SHG','icon':'inventory'},
     {'label':'Auto-matched','value':'6,891','sub':'high confidence','icon':'verified','bg':'var(--status-success-bg)','color':'var(--status-success)'},
     {'label':'Need review','value':'1,326','sub':'medium / low confidence','icon':'pending','bg':'var(--status-warning-bg)','color':'var(--status-warning)'},
     {'label':'New SHGs created','value':'248','sub':'no match found','icon':'add_circle','bg':'var(--status-info-bg)','color':'var(--status-info)'},
   ],
   'sections':[
     {'title':'Needs your review','table':{
       'columns':[{'key':'ben','label':'Beneficiary'},{'key':'orig','label':'Free-text name'},{'key':'sugg','label':'Suggested match'},{'key':'conf','label':'Confidence'},{'key':'action','label':'Action'}],
       'rows':[
         {'ben':'<strong>Rina Kalita</strong><div style="font-size:11px;color:var(--ink-500);">Bahjani</div>','orig':'<code>Manalisa SHG</code>','sugg':'Manalisha SHG (SHG-AS-04392)','conf':'92%','action':'<button class="btn btn-primary btn-sm">Confirm</button> <button class="btn btn-tertiary btn-sm">Other…</button>'},
         {'ben':'<strong>Anjali Bora</strong><div style="font-size:11px;color:var(--ink-500);">Sorbhog</div>','orig':'<code>Sarsoti SHG</code>','sugg':'Saraswati Mahila Samiti (SHG-AS-04391)','conf':'78%','action':'<button class="btn btn-primary btn-sm">Confirm</button> <button class="btn btn-tertiary btn-sm">Other…</button>'},
         {'ben':'<strong>Geeta Devi</strong><div style="font-size:11px;color:var(--ink-500);">Bahjani</div>','orig':'<code>Mahila Group</code>','sugg':'<em>No good match</em>','conf':'21%','action':'<button class="btn btn-secondary btn-sm">Create new</button> <button class="btn btn-tertiary btn-sm">Skip</button>'},
         {'ben':'<strong>Fatema Begum</strong><div style="font-size:11px;color:var(--ink-500);">Mayong</div>','orig':'<code>Mayong shg</code>','sugg':'Mayong Mahila SHG (SHG-AS-04188)','conf':'88%','action':'<button class="btn btn-primary btn-sm">Confirm</button> <button class="btn btn-tertiary btn-sm">Other…</button>'},
       ]}}
   ]},

  {'archetype': 'web_dashboard', 'id':'P4-M6-S04', 'phase':4, 'sprint':12, 'module':'M-6', 'moduleName':'Programme Mgmt',
   'title':'Tranche release tracker', 'role':'admin', 'platform':'web', 'active_item':'Programme',
   'h_title':'Tranche release & disbursement', 'h_sub':'All 5 implementation partners · FY 2025-26 · live status against the MoU schedule',
   'purpose':'Detailed tranche tracker per IP. Shows planned schedule, released amounts, due dates, late warnings.',
   'kpis':[
     {'label':'Committed FY','value':'₹ 14.2 cr','sub':'across 7 active MoUs','icon':'savings'},
     {'label':'Disbursed YTD','value':'₹ 8.4 cr','sub':'59% of FY commitment','icon':'paid','bg':'var(--status-success-bg)','color':'var(--status-success)'},
     {'label':'Pending','value':'₹ 5.8 cr','sub':'5 tranches due next 90 days','icon':'schedule','bg':'var(--status-info-bg)','color':'var(--status-info)'},
     {'label':'Overdue','value':'₹ 0.4 cr','sub':'1 tranche · 14 days late','icon':'warning','bg':'var(--status-warning-bg)','color':'var(--status-warning)'},
   ],
   'sections':[
     {'title':'Tranches','table':{
       'columns':[{'key':'ngo','label':'IP'},{'key':'po','label':'PO Number'},{'key':'trn','label':'Tranche'},{'key':'planned','label':'Planned'},{'key':'amt','label':'Amount','align':'right'},{'key':'status','label':'Status'},{'key':'action','label':''}],
       'rows':[
         {'ngo':'SeSTA','po':'PO-2025-AS-001','trn':'T1','planned':'Apr 2025','amt':'₹ 0.8 cr','status':'<span class="pill pill-success"><span class="dot"></span> Released</span>','action':'<button class="icon-btn"><span class="material-symbols-rounded">receipt</span></button>'},
         {'ngo':'SeSTA','po':'PO-2025-AS-001','trn':'T2','planned':'Jul 2025','amt':'₹ 0.8 cr','status':'<span class="pill pill-success"><span class="dot"></span> Released</span>','action':'<button class="icon-btn"><span class="material-symbols-rounded">receipt</span></button>'},
         {'ngo':'SeSTA','po':'PO-2025-AS-001','trn':'T3','planned':'Oct 2025','amt':'₹ 0.8 cr','status':'<span class="pill pill-warning"><span class="dot"></span> In progress</span>','action':'<button class="btn btn-primary btn-sm">Release</button>'},
         {'ngo':'RGVN','po':'PO-2025-AS-002','trn':'T1','planned':'Apr 2025','amt':'₹ 0.9 cr','status':'<span class="pill pill-success"><span class="dot"></span> Released</span>','action':''},
         {'ngo':'RGVN','po':'PO-2025-AS-002','trn':'T2','planned':'Jul 2025','amt':'₹ 0.9 cr','status':'<span class="pill pill-success"><span class="dot"></span> Released</span>','action':''},
         {'ngo':'G. Sahara','po':'PO-2025-AS-003','trn':'T2','planned':'10 Jan 2026','amt':'₹ 0.4 cr','status':'<span class="pill pill-warning"><span class="dot"></span> 14 days late</span>','action':'<button class="btn btn-danger btn-sm">Resolve</button>'},
       ]}}
   ]},

  {'archetype': 'web_dashboard', 'id':'P4-M7-S02', 'phase':4, 'sprint':13, 'module':'M-7', 'moduleName':'SROI',
   'title':'Social Value dashboard (SROI)', 'role':'admin', 'platform':'web', 'active_item':'Dashboard',
   'h_title':'Social Value of Linkages', 'h_sub':'₹ value of social impact created · per-scheme coefficient × approved linkages = total social value',
   'purpose':'SROI dashboard. Shows total social value created across geographies, NGOs, time. Tied to the coefficient master defined separately.',
   'kpis':[
     {'label':'Total social value YTD','value':'₹ 38.4 cr','sub':'4.6× the ₹8.4 cr disbursed','icon':'attach_money','bg':'var(--status-success-bg)','color':'var(--status-success)'},
     {'label':'Per beneficiary','value':'₹ 1,142','sub':'average across 33.6 lakh','icon':'volunteer_activism'},
     {'label':'YoY change','value':'+24%','sub':'vs FY 2024-25','icon':'trending_up','bg':'var(--status-success-bg)','color':'var(--status-success)'},
     {'label':'Top scheme by SROI','value':'PMJJBY','sub':'₹14.2 cr (37%)','icon':'health_and_safety'},
   ],
   'sections':[
     {'banner':{'type':'warn','icon':'flag','text':'Coefficients are placeholder values. Final table pending CRISIL M&E sign-off.'}},
     {'title':'By geography','table':{
       'columns':[{'key':'geo','label':'Geography'},{'key':'link','label':'Linkages','align':'right'},{'key':'val','label':'Social value (₹)','align':'right'},{'key':'per','label':'Per linkage','align':'right'},{'key':'yoy','label':'YoY','align':'right'}],
       'rows':[
         {'geo':'<strong>Assam</strong>','link':'12,420','val':'₹ 22.8 cr','per':'₹ 18,360','yoy':'+22%'},
         {'geo':'<strong>Rajasthan</strong>','link':'8,180','val':'₹ 15.6 cr','per':'₹ 19,070','yoy':'+27%'},
       ]}},
     {'title':'By scheme · top 5','table':{
       'columns':[{'key':'sch','label':'Scheme'},{'key':'coef','label':'Coefficient','align':'right'},{'key':'link','label':'Linkages','align':'right'},{'key':'val','label':'Social value (₹)','align':'right'}],
       'rows':[
         {'sch':'PMJJBY (Life insurance)','coef':'₹ 28,000','link':'5,080','val':'₹ 14.2 cr'},
         {'sch':'APY (Atal Pension)','coef':'₹ 24,500','link':'3,820','val':'₹ 9.4 cr'},
         {'sch':'PMSBY (Accident)','coef':'₹ 18,200','link':'4,210','val':'₹ 7.7 cr'},
         {'sch':'KCC (Credit)','coef':'₹ 22,000','link':'2,340','val':'₹ 5.1 cr'},
         {'sch':'Bhamashah (State scheme)','coef':'₹ 8,500','link':'2,310','val':'₹ 2.0 cr'},
       ]}}
   ]},

  {'archetype': 'web_dashboard', 'id':'P4-M7-S01', 'phase':4, 'sprint':13, 'module':'M-7', 'moduleName':'SROI Coefficient Master',
   'title':'SROI coefficient master', 'role':'admin', 'platform':'web', 'active_item':'Masters',
   'h_title':'SROI coefficients per scheme', 'h_sub':'Define the rupee value of social impact per linkage type · drives the entire SROI dashboard',
   'purpose':'Admin maintains the coefficient table that feeds the SROI dashboard. Each scheme has a coefficient, a source, a last-updated date.',
   'actions':[{'label':'Import from CSV','variant':'btn-secondary','icon':'upload'},{'label':'Add coefficient','variant':'btn-primary','icon':'add'}],
   'sections':[
     {'banner':{'type':'warn','icon':'flag','text':'Placeholder values shown. Final coefficients pending CRISIL M&E methodology sign-off (Q-4 of implementation plan).'}},
     {'title':'Coefficients','table':{
       'columns':[{'key':'sch','label':'Scheme'},{'key':'cat','label':'Category'},{'key':'val','label':'₹ per linkage','align':'right'},{'key':'src','label':'Source / basis'},{'key':'upd','label':'Updated'},{'key':'action','label':''}],
       'rows':[
         {'sch':'<strong>PMJJBY</strong>','cat':'<span class="scheme-tag scheme">Scheme</span> Life insurance','val':'₹ 28,000','src':'CRISIL M&E framework v2.1','upd':'12 Jan 2026','action':'<button class="btn btn-secondary btn-sm">Edit</button>'},
         {'sch':'<strong>PMSBY</strong>','cat':'<span class="scheme-tag scheme">Scheme</span> Accident insurance','val':'₹ 18,200','src':'CRISIL M&E framework v2.1','upd':'12 Jan 2026','action':'<button class="btn btn-secondary btn-sm">Edit</button>'},
         {'sch':'<strong>APY</strong>','cat':'<span class="scheme-tag scheme">Scheme</span> Pension','val':'₹ 24,500','src':'KPMG impact study 2024','upd':'8 Jan 2026','action':'<button class="btn btn-secondary btn-sm">Edit</button>'},
         {'sch':'<strong>KCC</strong>','cat':'<span class="scheme-tag scheme">Scheme</span> Credit','val':'₹ 22,000','src':'NABARD farm-income survey','upd':'8 Jan 2026','action':'<button class="btn btn-secondary btn-sm">Edit</button>'},
         {'sch':'<strong>Account opening</strong>','cat':'<span class="scheme-tag services">Services</span> Banking','val':'₹ 4,800','src':'Internal estimate','upd':'15 Dec 2025','action':'<button class="btn btn-secondary btn-sm">Edit</button>'},
         {'sch':'<strong>Fraud awareness</strong>','cat':'<span class="scheme-tag awareness">Awareness</span> Education','val':'₹ 1,200','src':'Internal estimate','upd':'15 Dec 2025','action':'<button class="btn btn-secondary btn-sm">Edit</button>'},
       ]}}
   ]},

  {'archetype': 'mobile_list', 'id':'P4-M7-S03', 'phase':4, 'sprint':13, 'module':'M-7', 'moduleName':'SROI Sakhi card',
   'title':'Sakhi — Social value card', 'role':'Sakhi', 'platform':'mobile',
   'app_title':'Your impact', 'back':'DHW-1',
   'purpose':'Motivational view for the Sakhi: how much social value her own approved linkages have created. Personal, in her language.',
   'sections':[
     {'hero':{'label':'YOUR IMPACT THIS YEAR','title':'₹ 6.4 lakh','sub':'of social value created across 37 households'}},
     {'head':'Breakdown by scheme'},
     {'rows':[
       {'icon':'health_and_safety','title':'PMJJBY · 14 linkages','meta':'₹ 28,000 × 14','amount':'₹ 3.92 L'},
       {'icon':'health_and_safety','title':'PMSBY · 8 linkages','meta':'₹ 18,200 × 8','amount':'₹ 1.46 L'},
       {'icon':'savings','title':'APY · 5 linkages','meta':'₹ 24,500 × 5','amount':'₹ 1.22 L'},
       {'icon':'volunteer_activism','title':'Other services · 10 linkages','meta':'mixed','amount':'₹ 0.32 L'},
     ]},
     {'head':'What this means'},
     {'rows':[
       {'icon':'info','title':'Social value is not income','meta':'It is the long-term financial protection your work brings to families.','arrow':False},
       {'icon':'group','title':'You reached 142 unique beneficiaries','meta':'37 transactions, 142 women + their families','arrow':False},
     ]},
   ]},

  {'archetype': 'web_dashboard', 'id':'P4-M15-S01', 'phase':4, 'sprint':13, 'module':'M-15', 'moduleName':'Dashboard cards',
   'title':'Dashboard — new KPI cards', 'role':'admin', 'platform':'web', 'active_item':'Dashboard',
   'h_title':'Dashboard', 'h_sub':'New cards: Top 5 Linkages by income · Total Linkages · Onboarded/Active/Inactive/Exit Sakhi split · Batch-wise · SHG-SRLM-RF-VO counts',
   'purpose':'The main admin dashboard with the new KPI cards added from CR-4, CR-9, CR-10, A-B1, A-B2. Visually communicates which cards are net-new vs preserved from the current dashboard.',
   'kpis':[
     {'label':'Total linkages (NEW)','value':'20,600','sub':'+18% vs last quarter','icon':'link','bg':'var(--brand-primary-50)','color':'var(--brand-primary)'},
     {'label':'Onboarded Sakhis','value':'5,274','sub':'cumulative','icon':'group'},
     {'label':'Active · Inactive · Exit (NEW split)','value':'4,890 / 248 / 136','sub':'92.7% active','icon':'group_work','bg':'var(--status-success-bg)','color':'var(--status-success)'},
     {'label':'SHGs linked to SRLM (NEW)','value':'4,128','sub':'71.9% of total','icon':'verified','bg':'var(--status-info-bg)','color':'var(--status-info)'},
   ],
   'sections':[
     {'content_html':'<div class="banner info"><span class="material-symbols-rounded">new_releases</span> The dashboard gains 8 new cards. The existing 24 stay where they are — these slot in alongside.</div>'},
     {'title':'Top 5 Linkages by income (NEW)','table':{
       'columns':[{'key':'rank','label':'#'},{'key':'name','label':'Scheme or service'},{'key':'cnt','label':'Linkages','align':'right'},{'key':'inc','label':'Total income (₹)','align':'right'}],
       'rows':[
         {'rank':'1','name':'APY (Atal Pension Yojana)','cnt':'3,820','inc':'₹ 5.34 lakh'},
         {'rank':'2','name':'PMJJBY','cnt':'5,080','inc':'₹ 22.1 lakh (premiums)'},
         {'rank':'3','name':'KCC application','cnt':'2,340','inc':'₹ 16.8 lakh'},
         {'rank':'4','name':'PMSBY','cnt':'4,210','inc':'₹ 18.4 lakh'},
         {'rank':'5','name':'Account opening','cnt':'2,180','inc':'₹ 4.36 lakh'},
       ]}},
     {'title':'Batch-wise Sakhi count (NEW)','table':{
       'columns':[{'key':'yr','label':'Batch year'},{'key':'tot','label':'Total','align':'right'},{'key':'act','label':'Active','align':'right'},{'key':'inact','label':'Inactive','align':'right'},{'key':'exit','label':'Exit','align':'right'}],
       'rows':[
         {'yr':'<strong>2021</strong>','tot':'1,840','act':'1,672','inact':'92','exit':'76'},
         {'yr':'<strong>2022</strong>','tot':'1,210','act':'1,138','inact':'48','exit':'24'},
         {'yr':'<strong>2023</strong>','tot':'1,080','act':'1,028','inact':'34','exit':'18'},
         {'yr':'<strong>2024</strong>','tot':'780','act':'742','inact':'28','exit':'10'},
         {'yr':'<strong>2025</strong>','tot':'364','act':'358','inact':'4','exit':'2'},
         {'yr':'<strong>Onboarded only (no batch tag)</strong>','tot':'—','act':'—','inact':'42','exit':'6'},
       ]}}
   ]},

  {'archetype': 'web_form', 'id':'P4-M19-S01', 'phase':4, 'sprint':13, 'module':'M-19', 'moduleName':'Data archiving',
   'title':'Data archive — request', 'role':'admin', 'platform':'web', 'active_item':'Masters',
   'h_title':'Archive previous years', 'h_sub':'Move 3+ year-old transaction data to archive partition · keeps queries on current data fast',
   'purpose':'Admin requests a year of transactions to be archived. The data remains queryable on-demand but no longer slows down live dashboards.',
   'fields':[
     {'type':'select','label':'Year to archive','options':['FY 2021-22','FY 2022-23 (5,84,210 transactions)','FY 2020-21']},
     {'type':'value','label':'What will happen','value':'Selected year\'s transactions move to the archive partition. Dashboards and reports for current FY will get faster. The data stays queryable via the Archive viewer.'},
     {'type':'value','label':'Estimated archive size','value':'~ 1.8 GB · ~ 5.8 lakh transactions · ~ 2.4 lakh evidence photos'},
     {'type':'value','label':'Reversal','value':'You can request un-archive within 30 days. After that, restoring takes a support ticket.'},
     {'type':'textarea','label':'Reason for archival (audit log)','placeholder':'Optional — for the audit trail','value':'Annual archival of FY 2022-23 data per programme retention policy.'},
   ],
   'side_cards':[
     {'title':'Archived previously','items':[{'label':'FY 2018-19','value':'archived 12 Apr 2024'},{'label':'FY 2019-20','value':'archived 18 Apr 2024'},{'label':'FY 2020-21','value':'archived 22 May 2025'}]},
     {'title':'Performance impact','desc':'Archiving FY 2022-23 will shrink the live transaction table by ~31% — dashboard queries will be ~2× faster.'},
   ],
   'save_label':'Request archival',
   'back':None},

  {'archetype': 'web_dashboard', 'id':'DHW-8', 'phase':4, 'sprint':12, 'module':'DHW-8', 'moduleName':'Audit trail',
   'title':'Audit trail viewer', 'role':'admin', 'platform':'web', 'active_item':'Masters',
   'h_title':'Audit trail', 'h_sub':'Every change to every entity — who, when, what changed · supports CSR compliance and support investigations',
   'purpose':'Searchable audit log of all field-level edits across the system. Filter by entity type, user, date range, action. Click any row for before/after diff.',
   'sections':[
     {'content_html':'<div class="card" style="padding:var(--space-4);margin-bottom:var(--space-4);"><div class="split-col"><div class="field-block"><label>Entity</label><select><option>All</option><option>Beneficiary</option><option>Transaction</option><option>Sakhi</option><option>FO</option><option>SHG</option><option>MoU</option></select></div><div class="field-block"><label>User</label><input placeholder="Search…" /></div></div><div class="split-col"><div class="field-block"><label>Date from</label><input type="date" value="2026-01-01" /></div><div class="field-block"><label>Date to</label><input type="date" value="2026-01-31" /></div></div></div>'},
     {'title':'Recent changes','table':{
       'columns':[{'key':'when','label':'When'},{'key':'who','label':'Who'},{'key':'what','label':'What'},{'key':'entity','label':'Entity'},{'key':'action','label':''}],
       'rows':[
         {'when':'09:42 · 28 Jan','who':'Sandeep Singh (NGO)','what':'Changed feedback status: <span style="color:var(--ink-500);">Pending</span> → <strong>Read</strong>','entity':'Feedback · Sumitra Devi','action':'<button class="btn btn-secondary btn-sm">Diff</button>'},
         {'when':'09:14 · 28 Jan','who':'Sumitra Devi (Sakhi)','what':'Re-submitted rejected transaction (3rd edit)','entity':'Transaction TX-25127','action':'<button class="btn btn-secondary btn-sm">Diff</button>'},
         {'when':'18:42 · 27 Jan','who':'Sandeep Singh (NGO)','what':'Approved 6 transactions in bulk','entity':'Transactions × 6','action':'<button class="btn btn-secondary btn-sm">Diff</button>'},
         {'when':'14:08 · 27 Jan','who':'Maya Vengurlekar (Admin)','what':'Updated SROI coefficient for PMJJBY: ₹ 26,000 → <strong>₹ 28,000</strong>','entity':'SROI coefficient · PMJJBY','action':'<button class="btn btn-secondary btn-sm">Diff</button>'},
         {'when':'11:32 · 26 Jan','who':'Sandeep Singh (NGO)','what':'Reassigned 14 Sakhis from FO Surya Bora → <strong>FO Pranab Das</strong>','entity':'FO assignment','action':'<button class="btn btn-secondary btn-sm">Diff</button>'},
         {'when':'09:14 · 26 Jan','who':'Pragat Dhwani (Admin)','what':'Created new SHG: Manalisha SHG (SHG-AS-04392)','entity':'SHG (new)','action':'<button class="btn btn-secondary btn-sm">Diff</button>'},
       ]}}
   ]},

  # ====== PROFILE / LEADERBOARD CONTINUED (Phase 3 leftovers) ======
  {'archetype': 'mobile_list', 'id':'P3-FO6-S02', 'phase':3, 'sprint':11, 'module':'FO-6', 'moduleName':'Badges',
   'title':'Sakhi — Badges & leaderboard', 'role':'Sakhi', 'platform':'mobile',
   'app_title':'Recognition',
   'purpose':'Sakhi-side version of the badge gallery. Sees her own state-internal leaderboard ranking + her own earned badges.',
   'sections':[
     {'hero':{'label':'DECEMBER BADGE','title':'Top Sakhi · Barpeta district','sub':'37 linkages · ₹3,840 income · 142 beneficiaries reached'}},
     {'head':'Your trophy cabinet'},
     {'rows':[
       {'icon':'emoji_events','title':'Top Sakhi · Barpeta · December','meta':'#1 by income','arrow':False},
       {'icon':'verified','title':'GSE certified · first cycle','meta':'Cleared 18 Sep 2023','arrow':False},
       {'icon':'workspace_premium','title':'100% attendance · November','meta':'24/24 working days','arrow':False},
     ]},
     {'head':'Leaderboard · Barpeta · December'},
     {'rows':[
       {'icon':'looks_one','title':'You · Sumitra Devi','meta':'37 linkages · ₹3,840','arrow':False},
       {'icon':'looks_two','title':'Suranjana Das','meta':'31 linkages · ₹3,240'},
       {'icon':'looks_3','title':'Tara Bora','meta':'28 linkages · ₹2,800'},
       {'icon':'person','title':'Runamoni Deka','meta':'4 · 24 linkages'},
       {'icon':'person','title':'Aarti Bhargav','meta':'5 · 21 linkages'},
     ]},
   ]},

  {'archetype': 'mobile_form', 'id':'P4-M5-S06', 'phase':4, 'sprint':12, 'module':'M-5', 'moduleName':'SHG dropdown on beneficiary form',
   'title':'Beneficiary form — SHG dropdown (new)', 'role':'Sakhi', 'platform':'mobile',
   'app_title':'Add beneficiary', 'back':'DHW-1',
   'purpose':'The Sakhi\'s add-beneficiary form now references SHG as a real entity. Replaces the free-text "Institution name" with a structured search-select.',
   'fields':[
     {'type':'banner','variant':'info','icon':'new_releases','text':'SHG is now a real entity (not free text). Pick from the list below or tap "Create new SHG" at the bottom.'},
     {'type':'text','label':'Beneficiary name','value':'Rina Kalita'},
     {'type':'text','label':"Father / husband",'value':'Bipin Kalita'},
     {'type':'radio','label':'Gender','options':['Female','Male','Others']},
     {'type':'text','label':'Mobile','value':'9485 67xxxx'},
     {'type':'select','label':'Village','options':['Bahjani','Sorbhog','Bhabanipur']},
     {'type':'value','label':'Is this beneficiary an SHG member?','value':'Yes'},
     {'type':'select','label':'SHG (search-select)','options':['Manalisha SHG · SHG-AS-04392','Saraswati Mahila Samiti · SHG-AS-04391','+ Create new SHG…']},
     {'type':'value','label':'Members of selected SHG','value':'Manalisha SHG has 12 members · SRLM linked · RF received ₹15k'},
   ],
   'bottom_buttons':[
     {'label':'Cancel','variant':'btn-secondary','to':'DHW-1'},
     {'label':'Save','variant':'btn-primary','icon':'check'},
   ]},
]

# ---------- run ----------

PHASE_DIR = {0:'phase-0', 1:'phase-1', 2:'phase-2', 3:'phase-3', 4:'phase-4'}

RENDERERS = {
    'mobile_list': render_mobile_list,
    'mobile_form': render_mobile_form,
    'web_dashboard': render_web_dashboard,
    'web_form': render_web_form,
}

def main():
    new_built_manifest_entries = []
    drop_planned_ids = set()
    written = 0

    for spec in SCREENS:
        archetype = spec['archetype']
        renderer = RENDERERS.get(archetype)
        if not renderer:
            print(f"!! unknown archetype {archetype} for {spec['id']}")
            continue
        out_dir = ROOT / PHASE_DIR[spec['phase']]
        out_dir.mkdir(exist_ok=True)
        # filename from id
        fname = spec['id'].lower().replace('p0-m1-','sakhi-rejected-').replace('-','-') + '.html'
        # simpler: just use id directly
        fname = spec['id'].lower() + '.html'
        out_path = out_dir / fname
        html_str = renderer(spec)
        out_path.write_text(html_str)
        written += 1

        # manifest entry
        new_built_manifest_entries.append({
            'id': spec['id'],
            'phase': spec['phase'],
            'sprint': spec.get('sprint', 1),
            'module': spec.get('module', ''),
            'moduleName': spec.get('moduleName', ''),
            'title': spec['title'],
            'role': spec['role'],
            'platform': spec['platform'],
            'src': f"{PHASE_DIR[spec['phase']]}/{fname}",
            'status': 'built',
            'purpose': spec.get('purpose', ''),
            'features': spec.get('features', []),
            'lookAndFeel': spec.get('lookAndFeel', []),
            'addresses': spec.get('addresses', []),
            'assumptions': spec.get('assumptions', []),
            'existingReference': spec.get('existingReference', ''),
        })
        drop_planned_ids.add(spec['id'])
        print(f"✓ {spec['id']:14} {archetype:14} {out_path.relative_to(ROOT)}")

    # Also register the 22 manually-built screens from Phase 0/1/2 earlier
    manual_screens = [
        # Phase 0
        {'id':'P0-M1-S02','phase':0,'sprint':1,'module':'M-1','moduleName':'Rejected loop','title':'Sakhi: Rejected detail (edit+resubmit)','role':'Sakhi','platform':'mobile','src':'phase-0/sakhi-rejected-detail.html','status':'built','purpose':'Sakhi opens a rejected transaction, sees the FO/NGO reason in a red banner, edits the flagged field (typically evidence photo), and resubmits — the approval chain is NOT reset.'},
        {'id':'P0-M1-S03','phase':0,'sprint':1,'module':'M-1','moduleName':'Rejected loop','title':'FO: Action-Taken tracking view','role':'FO','platform':'mobile','src':'phase-0/fo-action-taken.html','status':'built','purpose':'FO sees rejections she has raised against her Sakhis, with action status: awaiting Sakhi, resubmitted, window expired. Counter strip at top.'},
        {'id':'P0-M1-S04','phase':0,'sprint':1,'module':'M-1','moduleName':'Rejected loop','title':'Admin/NGO: Rejected & Action-Taken module','role':'NGO','platform':'web','src':'phase-0/web-rejected-transactions.html','status':'built','purpose':'Web admin dashboard for all rejected transactions across the NGO, with reason, status, and age. Convergent fix for CR-8 + FO-8.'},
        {'id':'P0-M1-S05','phase':0,'sprint':1,'module':'M-1','moduleName':'Rejected loop','title':'Sakhi: All rejected list','role':'Sakhi','platform':'mobile','src':'phase-0/sakhi-rejected-list.html','status':'built','purpose':'Sakhi sees every rejection she has + their action status. Tap any to open the fix-and-resubmit detail screen.'},
        # Phase 1
        {'id':'P1-M9-S01','phase':1,'sprint':2,'module':'M-9','moduleName':'Notification matrix','title':'Admin: Notification matrix','role':'admin','platform':'web','src':'phase-1/web-notification-matrix.html','status':'built','purpose':'Admin manages which events trigger which channels (push/SMS/email/IVR) for each role. Visible flag on the placeholder event list.'},
        {'id':'P1-M9-S02','phase':1,'sprint':2,'module':'M-9','moduleName':'Notification matrix','title':'Sakhi: Notifications (aggregated)','role':'Sakhi','platform':'mobile','src':'phase-1/sakhi-notifications.html','status':'built','purpose':'Sakhi notifications inbox — aggregated by type (not per-record). Per rural-UX recommendation to avoid notification storms.'},
        {'id':'P1-M2-S02','phase':1,'sprint':3,'module':'M-2','moduleName':'Messages','title':'Messages: Sent history (NGO)','role':'NGO','platform':'web','src':'phase-1/web-messages-sent.html','status':'built','purpose':'NGO sees past broadcasts, who they went to, read percentages. Edit/delete actions per row.'},
        {'id':'P1-M2-S03','phase':1,'sprint':3,'module':'M-2','moduleName':'Messages','title':'Messages: Admin view-only','role':'admin','platform':'web','src':'phase-1/web-messages-admin-view.html','status':'built','purpose':'CRISIL admin sees every broadcast from every NGO. View-only — no compose / edit. Filter by NGO.'},
        {'id':'P1-M2-S04','phase':1,'sprint':3,'module':'M-2','moduleName':'Messages','title':'FO: Messages inbox','role':'FO','platform':'mobile','src':'phase-1/fo-messages-inbox.html','status':'built','purpose':'FO inbox with Received and Sent tabs. Forward-to-my-Sakhis is a primary action.'},
        {'id':'P1-M2-S05','phase':1,'sprint':3,'module':'M-2','moduleName':'Messages','title':'FO: Message detail','role':'FO','platform':'mobile','src':'phase-1/fo-message-detail.html','status':'built','purpose':'FO reads an NGO broadcast in full. Can mark unread or forward to assigned Sakhis.'},
        {'id':'P1-M2-S06','phase':1,'sprint':3,'module':'M-2','moduleName':'Messages','title':'FO: Compose message (to Sakhis)','role':'FO','platform':'mobile','src':'phase-1/fo-message-compose.html','status':'built','purpose':'FO writes a broadcast for all her assigned Sakhis. 200-word limit, one photo, optional subject. Voice-input shortcut.'},
        {'id':'P1-M2-S08','phase':1,'sprint':3,'module':'M-2','moduleName':'Messages','title':'Sakhi: Message detail','role':'Sakhi','platform':'mobile','src':'phase-1/sakhi-message-detail.html','status':'built','purpose':'Sakhi reads a broadcast with sender info, body, attachments. Read receipt back to sender. Replies disabled (broadcast — use Feedback for chat).'},
        {'id':'P1-M16-S02','phase':1,'sprint':4,'module':'M-16','moduleName':'Transactions list','title':'Transactions: Filter drawer','role':'NGO','platform':'web','src':'phase-1/web-transactions-filter-drawer.html','status':'built','purpose':'Multi-select filter drawer for Sakhi Transactions list. District/Block/Scheme/Status multi-pills, date range, beneficiary search, saved presets.'},
        {'id':'P1-M17-S01','phase':1,'sprint':4,'module':'M-17','moduleName':'Feedback chat','title':'Feedback chat (Read/Action-taken/Pending)','role':'NGO','platform':'web','src':'phase-1/web-feedback-chat.html','status':'built','purpose':'NGO chat with Sakhis and FOs. Each message has sender name + timestamp + status (Read / Action Taken / Pending) that the admin updates inline.'},
        {'id':'P1-M17-S02','phase':1,'sprint':4,'module':'M-17','moduleName':'Feedback chat','title':'Feedback list (with status column)','role':'NGO','platform':'web','src':'phase-1/web-feedback-list.html','status':'built','purpose':'Roll-up view of all feedback threads with status, sender role, last update by. KPI cards for pending vs action-taken counts.'},
        {'id':'DHW-3','phase':1,'sprint':2,'module':'DHW-3','moduleName':'Voice input','title':'Voice-to-text on remarks (concept)','role':'Sakhi','platform':'mobile','src':'phase-1/dhwani-voice-input.html','status':'built','purpose':'On-device speech-to-text in Hindi/Assamese on any free-text field. Recording sheet with live transcript and audio visualisation.'},
        # Phase 2
        {'id':'P2-M3-S03','phase':2,'sprint':6,'module':'M-3','moduleName':'Attendance','title':'Attendance: FO list (NGO web)','role':'NGO','platform':'web','src':'phase-2/web-attendance-list.html','status':'built','purpose':'NGO admin sees all FOs with attendance %, days present this month, last marked. Below-80% FOs flagged.'},
        {'id':'P2-M3-S04','phase':2,'sprint':6,'module':'M-3','moduleName':'Attendance','title':'Attendance: Per-FO calendar','role':'NGO','platform':'web','src':'phase-2/web-attendance-calendar.html','status':'built','purpose':'Month grid per FO. Each cell shows Present / Absent / Off with marked timestamp. Click a day for location and device detail.'},
        {'id':'P2-M12-S01','phase':2,'sprint':6,'module':'M-12','moduleName':'Best Activities','title':'FO: Best Activities list','role':'FO','platform':'mobile','src':'phase-2/fo-best-activities-list.html','status':'built','purpose':'FO views her own uploaded Best Activities (stories + photos of standout work by her Sakhis).'},
        {'id':'P2-M12-S02','phase':2,'sprint':6,'module':'M-12','moduleName':'Best Activities','title':'FO: Add Best Activity','role':'FO','platform':'mobile','src':'phase-2/fo-best-activity-add.html','status':'built','purpose':'Photo + title + 500-word story + optional Sakhi/Beneficiary tag. Auto-attaches location. Voice-input shortcut available.'},
        {'id':'P2-M12-S03','phase':2,'sprint':6,'module':'M-12','moduleName':'Best Activities','title':'Admin gallery (Best Activities)','role':'admin','platform':'web','src':'phase-2/web-best-activities-gallery.html','status':'built','purpose':'Admin sees all activities as a card gallery. Filter by region, date, FO. Download for case studies.'},
        {'id':'P2-M4-S02','phase':2,'sprint':7,'module':'M-4','moduleName':'Bulk onboarding','title':'Bulk Sakhi — Step 2 Download & Upload','role':'NGO','platform':'web','src':'phase-2/web-bulk-sakhi-step2.html','status':'built','purpose':'NGO admin downloads the templated CSV (pre-filled with scope) + village master sheet, fills the data offline, then drops the file back to upload.'},
        {'id':'P2-M4-S03','phase':2,'sprint':7,'module':'M-4','moduleName':'Bulk onboarding','title':'Bulk Sakhi — Step 3 Validate','role':'NGO','platform':'web','src':'phase-2/web-bulk-sakhi-step3.html','status':'built','purpose':'Server validates the uploaded CSV row by row. Pass / Warn / Fail per row with inline error message. Bulk fixes for common patterns.'},
    ]
    new_built_manifest_entries.extend(manual_screens)
    drop_planned_ids.update(s['id'] for s in manual_screens)

    # Update manifest
    manifest_path = ROOT / 'shared' / 'manifest.json'
    with manifest_path.open() as f:
        manifest = json.load(f)
    # Drop matched ids from plannedScreens
    manifest['plannedScreens'] = [s for s in manifest['plannedScreens'] if s.get('id') not in drop_planned_ids]
    # Append new built entries (avoiding duplicates already in screens)
    existing_built_ids = {s['id'] for s in manifest['screens']}
    for e in new_built_manifest_entries:
        if e['id'] not in existing_built_ids:
            manifest['screens'].append(e)
            existing_built_ids.add(e['id'])
    manifest['version'] = '1.2'
    manifest['updated'] = '2026-05-28'

    with manifest_path.open('w') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"\n✓ Wrote {written} new wireframes")
    print(f"✓ Manifest: {len(manifest['screens'])} built · {len(manifest['plannedScreens'])} planned")
    return manifest

if __name__ == '__main__':
    manifest = main()

