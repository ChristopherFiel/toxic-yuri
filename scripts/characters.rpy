# Dialogue sfx
define sounds = [
    'audio/dialogue_sfx/A1.ogg', 'audio/dialogue_sfx/A2.ogg', 'audio/dialogue_sfx/A3.ogg',
    'audio/dialogue_sfx/A4.ogg', 'audio/dialogue_sfx/A5.ogg',
    'audio/dialogue_sfx/B1.ogg', 'audio/dialogue_sfx/B2.ogg', 'audio/dialogue_sfx/B3.ogg',
    'audio/dialogue_sfx/B4.ogg', 'audio/dialogue_sfx/B5.ogg'
]

init python:
    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": 
            renpy.sound.play(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))

        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

# Put all the characters here
define l = Character(
    "Lily",
    image = "lily",
    color="#C8AABF",
    callback=type_sound
)

define h_unknown = Character(
    "Shadowy Figure",
    image = "holly",
    color="#B44E5D",
    callback=type_sound
)

define h = Character(
    "Holly",
    image = "holly",
    color="#B44E5D",
    callback=type_sound
)

define t = Character(
    "Teacher",
    image = "teacher",
    color="#000000",
    callback=type_sound
)

define c = Character(
    "Cashier",
    image = "lily",
    color="#85BB65",
)

define s1 = Character("School Girl 1", image="school_girl_1",callback=type_sound, color="#ffffff")
define s2 = Character("School Girl 2", image="school_girl_2",callback=type_sound, color="#ffffff")
define s3 = Character("School Girl 3", image="school_girl_3",callback=type_sound, color="#ffffff")
define s4 = Character("School Girl 4", image="school_girl_4",callback=type_sound, color="#ffffff")
define s5 = Character("School Girl 5", image="school_girl_5",callback=type_sound, color="#ffffff")

# Shaders
transform silhouette_fade_in:
    matrixcolor TintMatrix("#000000")
    alpha 0.0
    ease 0.8 alpha 1.0

transform silhouette_fade_out:
    matrixcolor TintMatrix("#000000")
    alpha 1.0
    ease 0.8 alpha 0.0

transform silhouette_idle:
    matrixcolor TintMatrix("#000000")

transform dirty_tint_soft:
    matrixcolor TintMatrix("#5c4433") * 0.5 + IdentityMatrix() * 0.5


## LAYERED SPRITES
layeredimage holly:
    group base:
        attribute unibase:
            "images/sprites/Holly/hollyuni_base.png"
        attribute d2base:
            "images/sprites/Holly/hollyd2_base.png"
        attribute d3base:
            "images/sprites/Holly/hollyd3_base.png"
        attribute unibasedirty:
            "images/sprites/Holly/hollyuni_basedirty.png"

    group eye:
        attribute annoyedeye:
            "images/sprites/Holly/Faces/holly_eye_annoyed.png"
        attribute crazyeye:
            "images/sprites/Holly/Faces/holly_eye_crazy.png"
        attribute cryeye:
            "images/sprites/Holly/Faces/holly_eye_cry.png"
        attribute neutraleye:
            "images/sprites/Holly/Faces/holly_eye_neutral.png"
        attribute shockeye:
            "images/sprites/Holly/Faces/holly_eye_shock.png"
        attribute winkeye:
            "images/sprites/Holly/Faces/holly_eye_wink.png"
        attribute thinkeye:
            "images/sprites/Holly/Faces/holly_eye_think.png"

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
        attribute unibasedirty:
            "images/sprites/Lily/lilyuni_basedirty.png"


    group eye:
        attribute angryeye:
            "images/sprites/Lily/Face/lily_eye_angry.png"
        attribute downeye:
            "images/sprites/Lily/Face/lily_eye_down.png"
        attribute neutraleye:
            "images/sprites/Lily/Face/lily_eye_neutral.png"
        attribute scaredeye:
            "images/sprites/Lily/Face/lily_eye_scared.png"
        attribute thinkeye:
            "images/sprites/Lily/Face/lily_eye_think.png"
        attribute cryeye:
            "images/sprites/Lily/Face/lily_eye_cry.png"
        attribute spookeye:
            "images/sprites/Lily/Face/lily_eye_spook.png"
        attribute emptiness:
            "images/sprites/Lily/Face/emptiness.png"

    group face:
        attribute frownface:
            "images/sprites/Lily/Face/lily_mouth_frown.png"
        attribute grimacecface:
            "images/sprites/Lily/Face/lily_mouth_grimacec.png"
        attribute grimaceoface:
            "images/sprites/Lily/Face/lily_mouth_grimaceo.png"
        attribute smileoface:
            "images/sprites/Lily/Face/lily_mouth_smileo.png"
        attribute smilecface:
            "images/sprites/Lily/Face/lily_mouth_smile.png"
        attribute oface:
            "images/sprites/Lily/Face/lily_mouth_o.png"
        attribute shyface:
            "images/sprites/Lily/Face/lily_mouth_shy.png"
        attribute noface:
            "images/sprites/Lily/Face/emptiness.png"

    group lefthand:
        attribute unil1:
            "images/sprites/Lily/lilyuni_hand_l1.png"
        attribute unil2:
            "images/sprites/Lily/lilyuni_hand_l2.png"
        attribute unilphone:
            "images/sprites/Lily/lilyuni_hand_lphone.png"
        attribute d2l1:
            "images/sprites/Lily/lilyd2_hand_l1.png"
        attribute d2l2:
            "images/sprites/Lily/lilyd2_hand_l2.png"
        attribute d3l1:
            "images/sprites/Lily/lilyd3_hand_l1.png"
        attribute d3l2:
            "images/sprites/Lily/lilyd3_hand_l2.png"
        attribute pjl1:
            "images/sprites/Lily/lilypj_hand_l1.png"
        attribute pjl2:
            "images/sprites/Lily/lilypj_hand_l2.png"
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

# to pick a mouth attribute when showing them, e.g.:
#   show school_girl_1 neutralface
#   show school_girl_3 smileoface
layeredimage school_girl_1:
    always:
        "images/sprites/npc/npc_base.png"
    always:
        "images/sprites/npc/npc_hair_1.png"

    group mouth:
        attribute neutralface default:
            "images/sprites/npc/npc_mouth_neutral.png"
        attribute grimaceface:
            "images/sprites/npc/npc_mouth_grimace.png"
        attribute oface:
            "images/sprites/npc/npc_mouth_o.png"
        attribute smileoface:
            "images/sprites/npc/npc_mouth_smileo.png"


layeredimage school_girl_2:
    always:
        "images/sprites/npc/npc_base.png"
    always:
        "images/sprites/npc/npc_hair_2.png"

    group mouth:
        attribute neutralface default:
            "images/sprites/npc/npc_mouth_neutral.png"
        attribute grimaceface:
            "images/sprites/npc/npc_mouth_grimace.png"
        attribute oface:
            "images/sprites/npc/npc_mouth_o.png"
        attribute smileoface:
            "images/sprites/npc/npc_mouth_smileo.png"


layeredimage school_girl_3:
    always:
        "images/sprites/npc/npc_base.png"
    always:
        "images/sprites/npc/npc_hair_3.png"

    group mouth:
        attribute neutralface default:
            "images/sprites/npc/npc_mouth_neutral.png"
        attribute grimaceface:
            "images/sprites/npc/npc_mouth_grimace.png"
        attribute oface:
            "images/sprites/npc/npc_mouth_o.png"
        attribute smileoface:
            "images/sprites/npc/npc_mouth_smileo.png"


layeredimage school_girl_4:
    always:
        "images/sprites/npc/npc_base.png"
    always:
        "images/sprites/npc/npc_hair_4.png"

    group mouth:
        attribute neutralface default:
            "images/sprites/npc/npc_mouth_neutral.png"
        attribute grimaceface:
            "images/sprites/npc/npc_mouth_grimace.png"
        attribute oface:
            "images/sprites/npc/npc_mouth_o.png"
        attribute smileoface:
            "images/sprites/npc/npc_mouth_smileo.png"


layeredimage school_girl_5:
    always:
        "images/sprites/npc/npc_base.png"
    always:
        "images/sprites/npc/npc_hair_5.png"

    group mouth:
        attribute neutralface default:
            "images/sprites/npc/npc_mouth_neutral.png"
        attribute grimaceface:
            "images/sprites/npc/npc_mouth_grimace.png"
        attribute oface:
            "images/sprites/npc/npc_mouth_o.png"
        attribute smileoface:
            "images/sprites/npc/npc_mouth_smileo.png"