from flask import Flask, request, jsonify, render_template
import colorsys

app = Flask(__name__)


def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(red, green, blue):
    return f'#{red:02x}{green:02x}{blue:02x}'


def rgba_to_hex(red, green, blue, alpha):
    return f'#{red:02x}{green:02x}{blue:02x}{round(alpha * 255):02x}'


def hex_to_rgba(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4, 6))


def rgb_to_hsl(red, green, blue):
    red, green, blue = red / 255.0, green / 255.0, blue / 255.0
    hue, lightness, saturation = colorsys.rgb_to_hls(red, green, blue)
    return int(hue * 360), int(saturation * 100), int(lightness * 100)


def hsl_to_rgb(hue, saturation, lightness):
    hue = hue / 360.0
    saturation = saturation / 100.0
    lightness = lightness / 100.0
    red, green, blue = colorsys.hls_to_rgb(hue, lightness, saturation)
    return int(red * 255), int(green * 255), int(blue * 255)


def rgb_to_rgba(red, green, blue, alpha=1.0):
    return (red, green, blue, round(alpha * 255))


def rgba_to_rgb(red, green, blue, alpha):
    return (red, green, blue)


def hsl_to_hex(hue, saturation, lightness):
    red, green, blue = hsl_to_rgb(hue, saturation, lightness)
    return rgb_to_hex(red, green, blue)


def hsl_to_rgba(hue, saturation, lightness, alpha=1.0):
    red, green, blue = hsl_to_rgb(hue, saturation, lightness)
    return rgba_to_hex(red, green, blue, alpha)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['GET'])
def convert():
    input_value = request.args.get('value')
    conversion_type = request.args.get('type')

    try:
        if conversion_type == 'hex_to_rgb':
            rgb = hex_to_rgb(input_value)
            return jsonify({'rgb': rgb})
        elif conversion_type == 'rgb_to_hex':
            red, green, blue = map(int, input_value.split(','))
            hex_value = rgb_to_hex(red, green, blue)
            return jsonify({'hex': hex_value})
        elif conversion_type == 'hex_to_rgba':
            rgba = hex_to_rgba(input_value)
            return jsonify({'rgba': rgba})
        elif conversion_type == 'rgba_to_hex':
            red, green, blue, alpha = map(float, input_value.split(','))
            hex_value = rgba_to_hex(red, green, blue, alpha)
            return jsonify({'hex': hex_value})
        elif conversion_type == 'rgb_to_hsl':
            red, green, blue = map(int, input_value.split(','))
            hsl = rgb_to_hsl(red, green, blue)
            return jsonify({'hsl': hsl})
        elif conversion_type == 'hsl_to_rgb':
            hue, saturation, lightness = map(int, input_value.split(','))
            rgb = hsl_to_rgb(hue, saturation, lightness)
            return jsonify({'rgb': rgb})
        elif conversion_type == 'rgba_to_rgb':
            red, green, blue, alpha = map(int, input_value.split(','))
            rgb = rgba_to_rgb(red, green, blue, alpha)
            return jsonify({'rgb': rgb})
        elif conversion_type == 'rgb_to_rgba':
            red, green, blue = map(int, input_value.split(','))
            rgba = rgb_to_rgba(red, green, blue)
            return jsonify({'rgba': rgba})
        elif conversion_type == 'hsl_to_hex':
            hue, saturation, lightness = map(int, input_value.split(','))
            hex_value = hsl_to_hex(hue, saturation, lightness)
            return jsonify({'hex': hex_value})
        elif conversion_type == 'hsl_to_rgba':
            hue, saturation, lightness = map(int, input_value.split(','))
            rgba = hsl_to_rgba(hue, saturation, lightness)
            return jsonify({'rgba': rgba})
        else:
            return jsonify({'error': 'Invalid conversion type'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
