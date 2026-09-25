# -*- coding: utf-8 -*-
r"""KARUSELKA - User Guide (EN). Generator on the family template (_docstyle.py).
Run:  python _gen_manual_en.py    Output:  docs\KARUSELKA_Manual_EN.docx
"""

import json

import _docstyle as ds

OUT = r'D:\AI\ZCode\Project\KARUSELKA\work\docs\KARUSELKA_Manual_EN.docx'


def h1(doc, text):
    return ds.h1(doc, text)


def h2(doc, text):
    return ds.h2(doc, text)


def p(doc, text, bullet=False, italic=False, grey=False):
    return ds.p(doc, text, bullet=bullet, italic=italic, grey=grey)


def kv_note(doc, text):
    return ds.kv(doc, text)


def add_table(doc, rows, widths, sev_col=None):
    return ds.add_table(doc, rows, widths, sev_col=sev_col)


def _save(doc, out):
    ds.footer(doc.sections[1], 'KARUSELKA')
    ds.strip_tail(doc)
    doc.save(out)
    h1s = [t for t in ds.H1_REGISTRY if t.lower() not in ('table of contents', 'contents')]
    json.dump(h1s, open(out.replace('.docx', '.h1.json'), 'w', encoding='utf-8'),
              ensure_ascii=False)
    print('saved:', out)


doc = ds.new_doc('KARUSELKA', 'User Guide', 'V1.4.1  -  BLENDER 3.6+ / 4.2+')

p(doc, 'KARUSELKA is a fast turntable rig for Blender. Pick an object, press Create Rig - '
       'a camera orbits it on linear keyframes, ready to scrub or render as a showreel '
       'turntable. Two modes: the camera orbits the object, or the object spins under a '
       'static camera. Pairs with LAMPOCHKA: a light preset + a KARUSELKA turntable = a '
       'model showcase in two minutes.')

kv_note(doc, 'github.com/abyrvalg379/karuselka')

h1(doc, 'Contents')
ds.toc_field(doc, 'Table of contents: open the document in Word/LibreOffice and refresh '
                  'the field (F9) to fill in page numbers.')

h1(doc, '1. About KARUSELKA')
p(doc, 'Key features:', bullet=False)
for b in (
    'one click: Create Rig builds the rig and keyframes, working immediately;',
    'two modes: Camera - the camera orbits the object; Object - the object spins, camera static;',
    'constant rotation speed: interpolation is forced LINEAR, no ease-in-out on a turntable;',
    'shot presets Front / Three-Quarter / Top / Hero in one click, plus your own .json presets;',
    'output presets: resolution, samples and format (PNG frames / MP4 / WebM) for the render;',
    'collection assembly: the turntable covers a model built of many objects - bbox, radius '
    'and center across everything inside;',
    'live parameters: Frames, Rounds, Radius and Height change without rebuilding the rig;',
    'clean teardown: Remove Rig removes only what KARUSELKA created - your scene is untouched.',
):
    p(doc, b, bullet=True)

h1(doc, '2. Installation')
for b in (
    'Blender 4.2+: download karuselka_extension.zip from the latest release '
    'github.com/abyrvalg379/karuselka - Preferences - Get Extensions - Install from Disk.',
    'Blender 3.6-4.1: same release, file karuselka_legacy.zip, via Preferences - Add-ons - Install.',
    'The panel appears in the 3D viewport N-panel (N key) - KARUSELKA tab.',
):
    p(doc, b, bullet=True)

h1(doc, '3. Quick start')
for b in (
    'Select an object (or set the Target on the panel).',
    'Press Create Rig - the camera is already orbiting; scrub the timeline.',
    'Framing: shot presets Front / Three-Quarter / Top / Hero, or set Start Angle and Height by hand.',
    'Press Render Turntable - frames land in //turntable/ as <asset>_turntable.',
    'Remove the rig with Remove Rig when it is no longer needed.',
):
    p(doc, b, bullet=True)

h1(doc, '4. Rig and modes')
h2(doc, '4.1 Camera and Object')
p(doc, 'Mode Camera: the camera flies around the object - the classic showcase. Mode Object: '
       'the object spins on its axis, the camera stays still. In Object mode the model '
       'hierarchy root is parented to KARUSELKA_Empty (if the target already has a parent, '
       'the top of its parent chain is parented); Remove Rig restores the hierarchy with '
       'world transforms preserved.')
h2(doc, '4.2 What gets framed: Target and Collection')
p(doc, 'Target - the turntable object (the active object by default). The Collection field '
       'switches the rig to a root collection: bbox, auto-radius and rotation center are '
       'computed across every object inside - the turntable of a multi-part model covers it '
       'as a whole.')
h2(doc, '4.3 Orbit parameters')
add_table(doc, [
    ('Parameter', 'Meaning'),
    ('Frames', 'frames per full revolution; fps comes from the scene'),
    ('Rounds', 'number of revolutions, fractional allowed'),
    ('Dir', 'rotation direction as seen from above'),
    ('Start Angle', 'orbit angle at frame 1 (Front preset = -90)'),
    ('Center', 'rotation center: middle of the scope bbox or the 3D cursor'),
    ('Radius', 'orbit distance; 0 = auto: scope size × Margin'),
    ('Margin', 'auto-radius multiplier (2.5 by default) - the camera never crowds the model'),
    ('Height', 'camera height relative to the object center'),
], [3.8, 13.2])
p(doc, 'Edits to Frames / Rounds / Dir rebuild the rig live: the last keyframe slides to the '
       'new end and the timeline follows - no rebuild needed. Radius, Margin and Height move '
       'the camera immediately as well.')
h2(doc, '4.4 Camera')
p(doc, 'The rig camera becomes the scene camera (Numpad 0 and render); with your own camera '
       'KARUSELKA aims it at the target. Lens, DoF and near/far clip are edited right on the '
       'panel and applied immediately. Auto clip keeps a fixed 1000:1 ratio - small and large '
       'models frame without depth-buffer artifacts. Every Create Rig starts from clean '
       'defaults; the Keep Settings switch inherits the previous camera settings instead.')

h1(doc, '5. Shot presets')
p(doc, 'Four built-in presets set the start angle and the camera height as a fraction of the '
       'orbit radius - one click each: Front, Three-Quarter, Top, Hero. The current rig '
       'settings are saved to .json with Save Preset into the folder from Preferences '
       '(Presets Folder); files are picked up live and appear on the panel as user presets.')

h1(doc, '6. Rendering the turntable')
p(doc, 'Render Turntable - a non-blocking animation render. Output presets are applied for '
       'the duration of the render:')
add_table(doc, [
    ('Preset', 'Options'),
    ('Resolution', 'Square 1080 / 1080p / 1440p / 4K / 2048x858 / Scene (leave untouched)'),
    ('Samples', 'Draft / Normal / High / Scene'),
    ('Format', 'PNG frames / MP4 / WebM'),
], [3.8, 13.2])
for b in (
    'frames and files land in //turntable/ next to the .blend; the path is changed by the '
    'Output field;',
    'the turntable is named <asset>_turntable automatically (asset = the .blend file name; '
    'fallback - collection or target);',
    'if the scene has no lights, the panel warns before starting;',
    'Create Rig and Render Turntable set the scene range to 1..N themselves; engine, samples '
    'and format outside the presets are never touched.',
):
    p(doc, b, bullet=True)

h1(doc, '7. Remove Rig')
p(doc, 'Removes only what KARUSELKA created: the rig, the empty and the keyframes. Your '
       'camera stays, the previous scene camera returns. In Object mode the model hierarchy '
       'is un-parented back with world transforms preserved. The rig is always single: a '
       'repeated Create Rig rebuilds the existing one instead of stacking copies.')

h1(doc, '8. Workflows')
for t in (
    ('Model showcase in two minutes',
     'LAMPOCHKA: apply a light preset. KARUSELKA: Create Rig, the Three-Quarter preset, '
     'Render Turntable to MP4. Done.'),
    ('Spin instead of orbit',
     'Mode Object: the model rotates in place - handy for marketplace listings and standard '
     '360-degree loops.'),
    ('Turntable of a multi-part model',
     'A model of a dozen objects? Point at the Collection - radius and center are computed '
     'across the assembly, nothing clips or drifts.'),
    ('Client frame before the render',
     'Scrub the timeline with live shot presets: Front for the head-on view, Hero for the '
     'dramatic angle - show the client right in the viewport.'),
):
    h2(doc, t[0])
    p(doc, t[1])

h1(doc, '9. Troubleshooting')
add_table(doc, [
    ('Symptom', 'Cause', 'What to do'),
    ('The camera skips a stretch of the orbit', 'keyframes are not on linear interpolation',
     'KARUSELKA always sets LINEAR; if you edited the curves by hand - recreate the rig'),
    ('The object clips out of frame', 'the radius is small for the model size',
     'raise Margin or set Radius manually; for an assembly point at the Collection'),
    ('The render is empty / dark', 'no lights in the scene or the wrong camera',
     'the panel warns about lights; check that the rig camera is active (Numpad 0)'),
    ('Need the scene resolution back', 'output presets apply for the duration of the render',
     'pick the Scene preset - scene settings stay untouched'),
    ('Want your own camera back', 'the rig camera became active on Create Rig',
     'Remove Rig returns the previous active camera and removes only its own'),
    ('Did a second Create Rig stack a duplicate?', 'it does not: the rig is always single',
     'a repeated Create Rig rebuilds the rig from the current settings'),
], [4.6, 5.4, 7.0])

_save(doc, OUT)
