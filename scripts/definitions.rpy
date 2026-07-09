init python:
    import re

    # ── Tints ───────────────────────────────────────────
    tint_dark       = im.matrix.tint(0.42, 0.58, 0.82) * im.matrix.brightness(0.06)
    tint_moonlit    = im.matrix.tint(0.48, 0.62, 0.95) * im.matrix.brightness(0.18)
    tint_silvermoon = im.matrix.tint(0.55, 0.60, 0.78) * im.matrix.brightness(-0.05)
    tint_sunset     = im.matrix.tint(1.0,  0.78, 0.18) * im.matrix.brightness(0.13)
    tint_dawn       = im.matrix.tint(0.75, 0.65, 1.0)  * im.matrix.brightness(0.00)
    tint_dim        = im.matrix.tint(0.90, 0.90, 1.0)  * im.matrix.brightness(-0.1)
    tint_rain       = im.matrix.tint(0.72, 0.73, 0.82) * im.matrix.brightness(0.04)

    # ── Image Loading ────────────────────────────────────
    for file in renpy.list_files():

        if file.startswith('images/bg/'):
            if any(suffix in file for suffix in ["_day", "_dawn", "_dusk", "_night", "_moonlit", "_silvermoon", "_sepia", "_rain"]):
                continue
            img_path = re.sub(r'images/', '', file)
            match = re.match(r'images/bg/(.+)\.(png|jpg|webp)', file)
            if match:
                img_name = match.group(1)
                renpy.image(img_name + "_day",        img_path)
                renpy.image(img_name + "_dawn",       im.MatrixColor(img_path, tint_dawn))
                renpy.image(img_name + "_dusk",       im.MatrixColor(img_path, tint_sunset))
                renpy.image(img_name + "_night",      im.MatrixColor(img_path, tint_dark))
                renpy.image(img_name + "_moonlit",    im.MatrixColor(img_path, tint_moonlit))
                renpy.image(img_name + "_silvermoon", im.MatrixColor(img_path, tint_silvermoon))
                renpy.image(img_name + "_sepia",      im.Sepia(img_path))
                renpy.image(img_name + "_rain",       im.MatrixColor(img_path, tint_rain))
                renpy.image(img_name, ConditionSwitch(
                    "time_of_day == 'DAY'",         img_name + "_day",
                    "time_of_day == 'DAWN'",        img_name + "_dawn",
                    "time_of_day == 'DUSK'",        img_name + "_dusk",
                    "time_of_day == 'NIGHT'",       img_name + "_night",
                    "time_of_day == 'MOONLIT'",     img_name + "_moonlit",
                    "time_of_day == 'SILVERMOON'",  img_name + "_silvermoon",
                    "time_of_day == 'SEPIA'",       img_name + "_sepia",
                    "time_of_day == 'RAIN'",        img_name + "_rain",
                    "True",                         img_name + "_day"
                ))

        if file.startswith('images/sprites/'):
            img_path = re.sub(r'images/', '', file)
            match = re.match(r'images/sprites/.*/(.+)\.(png|jpg|webp)', file)
            if match:
                img_name = match.group(1)
                renpy.image(img_name + "_day",        img_path)
                renpy.image(img_name + "_dawn",       im.MatrixColor(img_path, tint_dawn))
                renpy.image(img_name + "_dusk",       im.MatrixColor(img_path, tint_sunset))
                renpy.image(img_name + "_night",      im.MatrixColor(img_path, tint_dark))
                renpy.image(img_name + "_moonlit",    im.MatrixColor(img_path, tint_moonlit))
                renpy.image(img_name + "_silvermoon", im.MatrixColor(img_path, tint_silvermoon))
                renpy.image(img_name + "_dim",        im.MatrixColor(img_path, tint_dim))
                renpy.image(img_name + "_sepia",      im.Sepia(img_path))
                renpy.image(img_name + "_rain",       im.MatrixColor(img_path, tint_rain))
                renpy.image(img_name, ConditionSwitch(
                    "sprite_effect == 'DIM'",       img_name + "_dim",
                    "time_of_day == 'DAY'",         img_name + "_day",
                    "time_of_day == 'DAWN'",        img_name + "_dawn",
                    "time_of_day == 'DUSK'",        img_name + "_dusk",
                    "time_of_day == 'NIGHT'",       img_name + "_night",
                    "time_of_day == 'MOONLIT'",     img_name + "_moonlit",
                    "time_of_day == 'SILVERMOON'",  img_name + "_silvermoon",
                    "time_of_day == 'SEPIA'",       img_name + "_sepia",
                    "time_of_day == 'RAIN'",        img_name + "_rain",
                    "True",                         img_name + "_day"
                ))

default time_of_day = 'DAY'
default sprite_effect = None