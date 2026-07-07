init python:
    import re
    # 1. Define Tints
    tint_dark   = im.matrix.tint(0.42, 0.58, 0.82) * im.matrix.brightness(0.06)
    tint_sunset = im.matrix.tint(1.0,  0.78, 0.18) * im.matrix.brightness(0.13)
    tint_dawn   = im.matrix.tint(0.75, 0.65, 1.0)  * im.matrix.brightness(0.00)
    tint_dim    = im.matrix.tint(0.90, 0.90, 1.0)  * im.matrix.brightness(-0.1)
    tint_rain = im.matrix.tint(0.72, 0.73, 0.82) * im.matrix.brightness(0.04)

    # 2. Automate Image Loading
    for file in renpy.list_files():
        # --- BACKGROUNDS ---
        if file.startswith('images/bg/'):
            if any(suffix in file for suffix in ["_day", "_dawn", "_dusk", "_night", "_sepia", "_rain"]):
                continue
            img_path = re.sub(r'images/', '', file)
            match = re.match(r'images/bg/(.+)\.(png|jpg|webp)', file)
            if match:
                img_name = match.group(1)
                renpy.image(img_name + "_day",   img_path)
                renpy.image(img_name + "_dawn",  im.MatrixColor(img_path, tint_dawn))
                renpy.image(img_name + "_dusk",  im.MatrixColor(img_path, tint_sunset))
                renpy.image(img_name + "_night", im.MatrixColor(img_path, tint_dark))
                renpy.image(img_name + "_sepia", im.Sepia(img_path))
                renpy.image(img_name + "_rain",  im.MatrixColor(img_path, tint_rain))
                renpy.image(img_name, ConditionSwitch(
                    "time_of_day == 'DAY'",   img_name + "_day",
                    "time_of_day == 'DAWN'",  img_name + "_dawn",
                    "time_of_day == 'DUSK'",  img_name + "_dusk",
                    "time_of_day == 'NIGHT'", img_name + "_night",
                    "time_of_day == 'SEPIA'", img_name + "_sepia",
                    "time_of_day == 'RAIN'",  img_name + "_rain", 
                    "True",                   img_name + "_day"
                ))

        # --- SPRITES ---
        if file.startswith('images/sprites/'):
            img_path = re.sub(r'images/', '', file)
            match = re.match(r'images/sprites/.*/(.+)\.(png|jpg|webp)', file)
            if match:
                img_name = match.group(1)
                renpy.image(img_name + "_day",   img_path)
                renpy.image(img_name + "_dawn",  im.MatrixColor(img_path, tint_dawn))
                renpy.image(img_name + "_dusk",  im.MatrixColor(img_path, tint_sunset))
                renpy.image(img_name + "_night", im.MatrixColor(img_path, tint_dark))
                renpy.image(img_name + "_dim",   im.MatrixColor(img_path, tint_dim))
                renpy.image(img_name + "_sepia", im.Sepia(img_path))
                renpy.image(img_name + "_rain",  im.MatrixColor(img_path, tint_rain))  # ← NEW
                renpy.image(img_name, ConditionSwitch(
                    "sprite_effect == 'DIM'", img_name + "_dim",
                    "time_of_day == 'DAY'",   img_name + "_day",
                    "time_of_day == 'DAWN'",  img_name + "_dawn",
                    "time_of_day == 'DUSK'",  img_name + "_dusk",
                    "time_of_day == 'NIGHT'", img_name + "_night",
                    "time_of_day == 'SEPIA'", img_name + "_sepia",
                    "time_of_day == 'RAIN'",  img_name + "_rain",  # ← NEW
                    "True",                   img_name + "_day"
                ))

# 3. Global Variables
default time_of_day = 'DAY'
default sprite_effect = None