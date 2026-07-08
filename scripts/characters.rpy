# Put all the characters here
define l = Character(
    "Lily",
    image = "lily",
    color="#C8AABF",
)

define h_unknown = Character(
    "Mysterious Person",
    image = "holly",
    color="#B44E5D",
)

define h = Character(
    "Holly",
    image = "holly",
    color="#B44E5D",
)

define t = Character(
    "Teacher",
    image = "teacher",
    color="#000000",
)

define s1 = Character("School Girl 1", image="school_girl_1", color="#ffffff")
define s2 = Character("School Girl 2", image="school_girl_2", color="#ffffff")
define s3 = Character("School Girl 3", image="school_girl_3", color="#ffffff")
define s4 = Character("School Girl 4", image="school_girl_4", color="#ffffff")
define s5 = Character("School Girl 5", image="school_girl_5", color="#ffffff")


## LAYERED SPRITES
layeredimage holly:
    group base:
        attribute unibase:
            "images/sprites/Holly/hollyuni_base.png"
        attribute d2base:
            "images/sprites/Holly/hollyd2_base.png"
        attribute d3base:
            "images/sprites/Holly/hollyd3_base.png"

    group eye:
        attribute annoyedeye:
            "images/sprites/Holly/Faces/holly_eye_annoyed.png"
        attribute crazyeye:
            "images/sprites/Holly/Faces/holly_eye_crazy.png"
        attribute cryeye:
            "images/sprites/Holly/Faces/holly_eye_cry.png"
        attribute neutraleye:
            "images/sprites/Holly/Faces/hollyuni_eye_neutral.png"
        attribute shockeye:
            "images/sprites/Holly/Faces/holly_eye_shock.png"
        attribute winkeye:
            "images/sprites/Holly/Faces/holly_eye_wink.png"

    group face:
        attribute frownface:
            "images/sprites/Holly/Faces/holly_mouth_frown.png"
        attribute grimacecface:
            "images/sprites/Holly/Faces/holly_mouth_grimacec.png"
        attribute grimaceoface:
            "images/sprites/Holly/Faces/holly_mouth_grimaceo.png"
        attribute smileoface:
            "images/sprites/Holly/Faces/holly_mouth_smileo.png"
        attribute smilecface:
            "images/sprites/Holly/Faces/holly_mouth_smile.png"
        attribute oface:
            "images/sprites/Holly/Faces/holly_mouth_o.png"
        attribute smugface:
            "images/sprites/Holly/Faces/holly_mouth_smug.png"

    group lefthand:
        attribute unil1:
            "images/sprites/Holly/hollyuni_hand_l1.png"
        attribute unil2:
            "images/sprites/Holly/hollyuni_hand_l2.png"
        attribute d2l1:
            "images/sprites/Holly/hollyd2_hand_l1.png"
        attribute d2l2:
            "images/sprites/Holly/hollyd2_hand_l2.png"
        attribute d3l1:
            "images/sprites/Holly/hollyd3_hand_l1.png"
        attribute d3l2:
            "images/sprites/Holly/hollyd3_hand_l2.png"
        attribute pjl1:
            "images/sprites/Holly/hollyd2_hand_l1.png"
        attribute pjl2:
            "images/sprites/Holly/hollyd2_hand_l2.png"

    group righthand:
        attribute unir1:
            "images/sprites/Holly/hollyuni_hand_r1.png"
        attribute unir2:
            "images/sprites/Holly/hollyuni_hand_r2.png"
        attribute d2r1:
            "images/sprites/Holly/hollyd2_hand_r1.png"
        attribute d2r2:
            "images/sprites/Holly/hollyd2_hand_r2.png"
        attribute d3r1:
            "images/sprites/Holly/hollyd3_hand_r1.png"
        attribute d3r2:
            "images/sprites/Holly/hollyd3_hand_r2.png"
        attribute pjr1:
            "images/sprites/Holly/hollyd2_hand_r1.png"
        attribute pjr2:
            "images/sprites/Holly/hollyd2_hand_r2.png"


layeredimage lily:
    group base:
        attribute unibase:
            "images/sprites/Lily/lilyuni_base.png"
        attribute d2base:
            "images/sprites/Lily/lilyd2_base.png"
        attribute d3base:
            "images/sprites/Lily/lilyd3_base.png"
        attribute pjbase:
            "images/sprites/Lily/lilypj_base.png"

    group eye:
        attribute angryeye:
            "images/sprites/Lily/Faces/lily_eye_angry.png"
        attribute downeye:
            "images/sprites/Lily/Faces/lily_eye_down.png"
        attribute neutraleye:
            "images/sprites/Lily/Faces/lily_eye_neutral.png"
        attribute scaredeye:
            "images/sprites/Lily/Faces/lily_eye_scared.png"
        attribute thinkeye:
            "images/sprites/Lily/Faces/lily_eye_think.png"
        attribute cryeye:
            "images/sprites/Lily/Faces/cry_eye_think.png"

    group face:
        attribute frownface:
            "images/sprites/Lily/Faces/lily_mouth_frown.png"
        attribute grimacecface:
            "images/sprites/Lily/Faces/lily_mouth_grimacec.png"
        attribute grimaceoface:
            "images/sprites/Lily/Faces/lily_mouth_grimaceo.png"
        attribute smileoface:
            "images/sprites/Lily/Faces/lily_mouth_smileo.png"
        attribute smilecface:
            "images/sprites/Lily/Faces/lily_mouth_smile.png"
        attribute oface:
            "images/sprites/Lily/Faces/lily_mouth_o.png"
        attribute shyface:
            "images/sprites/Lily/Faces/lily_mouth_shy.png"
        attribute noface:
            "images/sprites/Lily/Faces/emptiness.png"

    group lefthand:
        attribute unil1:
            "images/sprites/Lily/lilyuni_hand_l1.png"
        attribute unil2:
            "images/sprites/Lily/lilyuni_hand_l2.png"
        attribute d2l1:
            "images/sprites/Lily/lilyd2_hand_l1.png"
        attribute d2l2:
            "images/sprites/Lily/lilyd2_hand_l2.png"
        attribute d3l1:
            "images/sprites/Lily/lilyd3_hand_l1.png"
        attribute d3l2:
            "images/sprites/Lily/lilyd3_hand_l2.png"
        attribute pjl1:
            "images/sprites/Lily/lilyd2_hand_l1.png"
        attribute pjl2:
            "images/sprites/Lily/lilyd2_hand_l2.png"
        attribute pjlphone:
            "images/sprites/Lily/lilypj_hand_lphone.png"

    group righthand:
        attribute unir1:
            "images/sprites/Lily/lilyuni_hand_r1.png"
        attribute unir2:
            "images/sprites/Lily/lilyuni_hand_r2.png"
        attribute d2r1:
            "images/sprites/Lily/lilyd2_hand_r1.png"
        attribute d2r2:
            "images/sprites/Lily/lilyd2_hand_r2.png"
        attribute d3r1:
            "images/sprites/Lily/lilyd3_hand_r1.png"
        attribute d3r2:
            "images/sprites/Lily/lilyd3_hand_r2.png"
        attribute pjr1:
            "images/sprites/Lily/lilypj_hand_r1.png"
        attribute pjr2:
            "images/sprites/Lily/lilypj_hand_r2.png"


## SHORTEN POSES AND EXPRESSION
init python:
    holly_poses = {
        "uni_idle":   ("unibase", "unil2", "unir1"),
        "d2_idle":    ("d2base", "d2l1", "d2r2"),
        "d2_alt":     ("d2base", "d2l2", "d2r1"),
        "d3_idle":    ("d3base", "d3l2", "d3r2"),
        "d3_alt":     ("d3base", "d3l1", "d3r2"),
        "crazy_pose": ("d3base", "d3l1", "d3r1"),
    }
    holly_exprs = {
        "playful":   ("oface", "crazyeye"),
        "smug":      ("smugface", "crazyeye"),
        "annoyed":   ("grimacecface", "annoyedeye"),
        "content":   ("smilecface", "neutraleye"),
        "sad":       ("frownface", "cryeye"),
        "surprised": ("smileoface", "shockeye"),
        "teasing":   ("grimaceoface", "winkeye"),
        "crazy":     ("grimaceoface", "crazyeye"),
    }

    for _pname, _pattrs in holly_poses.items():
        for _ename, _eattrs in holly_exprs.items():
            renpy.image(
                "holly %s %s" % (_pname, _ename),
                renpy.display.image.ImageReference(("holly",) + _pattrs + _eattrs)
            )

    lily_poses = {
        "uni_idle":   ("unibase", "unil1", "unir2"),
        "d2_idle":    ("d2base", "d2l2", "d2r1"),
        "d3_idle":    ("d3base", "d3l1", "d3r2"),
        "pj_phone":   ("pjbase", "pjlphone", "pjr2"),
        "crazy_pose": ("d3base", "d3l2", "d3r1"),
    }
    lily_exprs = {
        "shy_thinking":   ("shyface", "thinkeye"),
        "smile_down":     ("smilecface", "downeye"),
        "frown_thinking": ("frownface", "thinkeye"),
        "scared":         ("oface", "scaredeye"),
        "upset":          ("grimacecface", "angryeye"),
        "blank":          ("noface", "neutraleye"),
        "crazy":          ("oface", "scaredeye"),
    }

    for _pname, _pattrs in lily_poses.items():
        for _ename, _eattrs in lily_exprs.items():
            renpy.image(
                "lily %s %s" % (_pname, _ename),
                renpy.display.image.ImageReference(("lily",) + _pattrs + _eattrs)
            )