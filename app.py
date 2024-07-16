from flask import Flask, request, jsonify
import colorsys

# quick test

app = Flask(__name__)

def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def rgba_to_hex(r, g, b, a):
    return f'#{r,:02x}{g:02x}{b:02x}{int(a * 255):02x}'

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
    return (r, g, b, int(a * 256))

def rgba_to_rgb(r, g, b, a):
    return (r, g, b)

def hsl_to_hex(h, s, l):
    r, g, b = hsl_to_rgb(h, s, l)
    return rgb_to_hex(r, g, b)

def hsl_to_rgba(h, s, l, a=1.0):
    r, g, b = hsl_to_rgb(h, s, l)
    return rgba_to_hex(r, g, b, a)

@app.route('/convert', methods=['GET'])
def convert():
    input_value = request.args.get('value')
    conversion_type = request.args.get('type')

    try:
        if conversion_type == 'hex_to_rgb':
            rgb = hex_to_rgb(input_value)
            return jsonify({'rgb': rgb})
        elif conversion_type == 'rgb_to_hex':
            r, g, b = map(int, input_value.split(','))
            hex_value = rgb_to_hex(r, g, b)
            return jsonify({'hex': hex_value})
        elif conversion_type == 'hex_to_rgba':
            rgba = hex_to_rgba(input_value)
            return jsonify({'rgba': rgba})
        elif conversion_type == 'rgba_to_hex':
            r, g, b, a = map(float, input_value.split(','))
            hex_value = rgba_to_hex(r, g, b, a)
            return jsonify({'hex': hex_value})
        elif conversion_type == 'rgb_to_hsl':
            r, g, b = map(int, input_value.split(','))
            hsl = rgb_to_hsl(r, g, b)
            return jsonify({'hsl': hsl})
        elif conversion_type == 'hsl_to_rgb':
            h, s, l = map(int, input_value.split(','))
            rgb = hsl_to_rgb(h, s, l)
            return jsonify({'rgb': rgb})
        elif conversion_type == 'rgba_to_rgb':
            r, g, b, a = map(int, input_value.split(','))
            rgb = rgba_to_rgb(r, g, b, a)
            return jsonify({'rgb': rgb})
        elif conversion_type == 'rgb_to_rgba':
            r, g, b = map(int, input_value.split(','))
            rgba = rgb_to_rgba(r, g, b)
            return jsonify({'rgba': rgba})
        elif conversion_type == 'hsl_to_hex':
            h, s, l = map(int, input_value.split(','))
            hex_value = hsl_to_hex(h, s, l)
            return jsonify({'hex': hex_value})
        elif conversion_type == 'hsl_to_rgba':
            h, s, l = map(int, input_value.split(','))
            rgba = hsl_to_rgba(h, s, l)
            return jsonify({'rgba': rgba})
        else:
            return jsonify({'error': 'Invalid conversion type'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400