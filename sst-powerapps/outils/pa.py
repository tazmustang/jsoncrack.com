# -*- coding: utf-8 -*-
"""Mini-bibliothèque : construction de contrôles Power Apps et sortie YAML (format « Coller le code »)."""

V = {  # versions des contrôles (format pa.yaml)
    'label': 'Label@2.5.1', 'button': 'Classic/Button@2.2.0', 'text': 'Classic/TextInput@2.3.2',
    'drop': 'Classic/DropDown@2.3.1', 'combo': 'Classic/ComboBox@2.4.0', 'date': 'Classic/DatePicker@2.6.0',
    'radio': 'Classic/Radio@2.3.0', 'check': 'Classic/CheckBox@2.1.0', 'rect': 'Rectangle@2.3.0',
    'cont': 'GroupContainer@1.3.0', 'gal': 'Gallery@2.15.0', 'html': 'HtmlViewer@2.1.0', 'image': 'Image@2.2.3',
    'icon': 'Classic/Icon@2.5.0',
}


def s(txt):
    """Littéral texte Power Fx."""
    return '"' + str(txt).replace('"', '""') + '"'


class C:
    def __init__(self, name, kind, props=None, children=None, variant=None):
        self.name, self.kind, self.props = name, kind, dict(props or {})
        self.children = children if children is not None else []
        self.variant = variant

    def add(self, *cs):
        for c in cs:
            if isinstance(c, (list, tuple)):
                self.add(*c)
            elif c is not None:
                self.children.append(c)
        return self


def _val(v):
    if isinstance(v, bool):
        v = 'true' if v else 'false'
    v = str(v)
    if not v.startswith('='):
        v = '=' + v
    return v


def _emit_prop(k, v, ind):
    v = _val(v)
    sp = ' ' * ind
    if '\n' in v or ': ' in v or ' #' in v or v.endswith(':') or v != v.strip() or '\t' in v:
        lines = [sp + k + ': |-'] + [sp + '  ' + ln for ln in v.split('\n')]
        return lines
    return [sp + k + ': ' + v]


def emit_control(c, ind):
    sp = ' ' * ind
    out = [sp + '- ' + c.name + ':', sp + '    Control: ' + V[c.kind]]
    if c.variant:
        out.append(sp + '    Variant: ' + c.variant)
    if c.props:
        out.append(sp + '    Properties:')
        for k, v in c.props.items():
            out += _emit_prop(k, v, ind + 6)
    if c.children:
        out.append(sp + '    Children:')
        for ch in c.children:
            out += emit_control(ch, ind + 6)
    return out


def emit_screen(name, props, children):
    out = ['Screens:', '  ' + name + ':', '    Properties:']
    for k, v in props.items():
        out += _emit_prop(k, v, 6)
    out.append('    Children:')
    for ch in children:
        out += emit_control(ch, 6)
    return '\n'.join(out) + '\n'


NAMES = set()


def uniq(n):
    assert n not in NAMES, 'Nom en double : ' + n
    NAMES.add(n)
    return n


# ------------------------------------------------------------------ fabriques
def label(name, text, **p):
    d = {'Text': text, 'Color': 'cTexte', 'Size': 12}
    d.update(p)
    return C(uniq(name), 'label', d)


def rect(name, fill, **p):
    d = {'Fill': fill, 'BorderThickness': 0}
    d.update(p)
    return C(uniq(name), 'rect', d)


def button(name, text, onselect, style='plein', color='cVert', **p):
    r = 6
    d = {'Text': text, 'OnSelect': onselect, 'Size': 11, 'FontWeight': 'FontWeight.Semibold',
         'RadiusTopLeft': r, 'RadiusTopRight': r, 'RadiusBottomLeft': r, 'RadiusBottomRight': r}
    if style == 'plein':
        d.update({'Fill': color, 'Color': 'Color.White', 'BorderThickness': 0,
                  'HoverFill': 'ColorFade(%s, -0.15)' % color, 'PressedFill': 'ColorFade(%s, -0.3)' % color,
                  'HoverColor': 'Color.White', 'PressedColor': 'Color.White'})
    elif style == 'contour':
        d.update({'Fill': 'Color.White', 'Color': color, 'BorderColor': color, 'BorderThickness': 2,
                  'HoverFill': 'cBleuPale', 'HoverColor': color, 'HoverBorderColor': color,
                  'PressedFill': 'cBordure', 'PressedColor': color, 'PressedBorderColor': color})
    elif style == 'lien':
        d.update({'Fill': 'Color.Transparent', 'Color': color, 'BorderThickness': 0, 'HoverFill': 'cBleuPale',
                  'HoverColor': color, 'PressedFill': 'cBordure', 'PressedColor': color, 'Align': 'Align.Left'})
    d.update(p)
    return C(uniq(name), 'button', d)


def pill(name, text, fill, color='Color.White', **p):
    d = {'Text': text, 'OnSelect': 'false', 'Fill': fill, 'Color': color, 'BorderThickness': 0,
         'HoverFill': fill, 'PressedFill': fill, 'HoverColor': color, 'PressedColor': color,
         'DisabledFill': fill, 'DisabledColor': color, 'DisplayMode': 'DisplayMode.View',
         'Size': 10, 'FontWeight': 'FontWeight.Semibold', 'Height': 28,
         'RadiusTopLeft': 14, 'RadiusTopRight': 14, 'RadiusBottomLeft': 14, 'RadiusBottomRight': 14, 'TabIndex': -1}
    d.update(p)
    return C(uniq(name), 'button', d)


def cont(name, variant='ManualLayout', children=None, **p):
    d = {'Fill': 'Color.Transparent', 'BorderThickness': 0, 'DropShadow': 'DropShadow.None'}
    if variant == 'AutoLayout':
        d.update({'LayoutDirection': 'LayoutDirection.Vertical', 'LayoutGap': 6,
                  'LayoutAlignItems': 'LayoutAlignItems.Stretch'})
    d.update(p)
    return C(uniq(name), 'cont', d, children or [], variant)


def card_props(r=8):
    return {'Fill': 'Color.White', 'BorderColor': 'cBordure', 'BorderThickness': 1,
            'RadiusTopLeft': r, 'RadiusTopRight': r, 'RadiusBottomLeft': r, 'RadiusBottomRight': r}


INPUT_STYLE = {'BorderColor': 'cBordure', 'HoverBorderColor': 'cBleu', 'FocusedBorderColor': 'cBleu',
               'FocusedBorderThickness': 2, 'Color': 'cTexte', 'Size': 12, 'Fill': 'Color.White'}
