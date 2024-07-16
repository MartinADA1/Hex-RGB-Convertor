from flask import Flask, request, jsonify
import colorsys

app = Flask(__name__)

def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def rgba_to_hex(r, g, b, a):
    return f'#{r:02x}{g:02x}{b:02x}{int(a * 255):02x}'

def hex_to_rgba(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4, 6))

def rgb_to_hsl(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return int(h * 360), int(s * 100), int(l * 100)

def hsl_to_rgb(h, s, l):
    h, s, l = h / 360.0, s / 100.0, l / 100.0
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return int(r * 255), int(g * 255), int(b * 255)

def rgb_to_rgba(r, g, b, a=1.0):
    return (r, g, b, int(a * 255))

def rgba_to_rgb(r, g, b, a):
    return (r, g, b)

def hsl_to_hex(h, s, l):
    r, g, b = hsl_to_rgb(h, s, l)
    return rgb_to_hex(r, g, b)

def hsl_to_rgba(h, s, l, a=1.0):
    r, g, b = hsl_to_rgb(h, s, l)
    return rgba_to_hex(r, g, b, a)