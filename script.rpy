# Flags are here
default holly_affection = 0
default lily_courage = 0


# NVL characters are used for the phone texting
define l_nvl = Character("WX_YuriZ", kind=nvl, image="lily", callback=Phone_SendSound)
define h_nvl = Character("h0lly_m0lly", kind=nvl, image="holly", callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)


#Warning splash screen
# label splashscreen:
#     with Pause(1)

#     show screen warning_screen with dissolve
#     with Pause(5)

#     hide screen warning_screen with dissolve
#     with Pause(1)

#     return


# The game starts here.

label start:
    # Disclaimer Screen
    scene black
    $ quick_menu = False
    pause 1.0
    play music "audio/ambience/heavy rain.ogg" fadein 3.0 volume 0.4
    show screen disclaimer_screen with dissolve
    pause 5
    show screen press_to_continue with dissolve
    pause
    hide screen disclaimer_screen
    hide screen press_to_continue
    with dissolve

    # Basic Controls
    scene black with dissolve
    show screen basic_controls with dissolve
    pause 5
    show screen press_to_continue with dissolve
    pause
    hide screen basic_controls
    hide screen press_to_continue
    with dissolve
    
    $ quick_menu= True
    $ time_of_day = 'RAIN'
    scene bg abandoned house with eyeopen
    pause 2.0
    scene black with eyeclose_slow
    play sound "audio/sfx/breathe.ogg"
    pause 5.0
    scene bg abandoned house with eyeopen

    show holly with dissolve:
        full
        center
        flicker
    h_unknown "Finally, you're aaaaaall miiiiiiiine now"
    h_unknown "We can live together forever now, just the two us"
    scene black with eyeclose
    scene bg abandoned house with eyeopen
    show holly with dissolve:        
        center
        medlong
        flicker
    h_unknown "You couldn't hide from your true self, so now I'm setting you free"
    h_unknown "I know deep down inside you also want this to happen…"
    scene black with eyeclose
    scene bg abandoned house with eyeopen
    show holly with dissolve:        
        center
        medclose
        flicker
    play sound "audio/sfx/thunder.ogg" volume 0.75
    h_unknown "DON'T YOU!"
    stop music
    scene black with eyeclose_fast
    pause 4.0
    stop sound fadeout 1.0
    play sound "audio/sfx/alarm_beep.ogg"
    pause 5.0
    stop sound fadeout 1.0

    play music "audio/ambience/morning_ambience.ogg" fadein 3.0
    $ time_of_day = 'DAY'
    scene bg bed top view with eyeopen_slow
    show lily with dissolve
    l "What a fucking weird dream!"
    l "Oh shit shit shit… what time is it?"
    play sound "audio/sfx/bus_horn.ogg"
    l "I’m gonna be late"
    stop music fadeout 2.0
    show lily at fast_moveoutright
    scene black with wiperight_medium
    play sound "audio/sfx/running.ogg"
    l "Comiiiiing!"
    pause 2.0

    jump bus_scene_day_1


label bus_scene_day_1:
    scene bg bus interior with wiperight
    show lily at slide_in_left, fall_and_recover(height=400, fall_time=0.5, ground_time=1.5, recover_time=0.6)
    play sound "audio/sfx/fall_down.ogg"
    pause 3.6
    
    l "OOOOUCCCCCHH!"
    play music "audio/ambience/road ambiance.ogg" fadein 2.0
    l "I hate this morning already"
    l "School sucks"
    l "Everything here sucks"
    l "I've been living in this town for 16 years and nothing changed..."
    l "This town became so dull, and boring"
    l "The streets, buildings, the people seems to follow something nobody wants to change"
    l "Every eyes seems to be staring at me... "
    l "Waiting for me make me mistakes"
    l "If I won't comply, and act differently they'll beat, and curse me"
    l "I hate this it feels suffocating..."
    l "I want to be more like me, and everyone to not give a fuck who I wanted to be"
    l "This place... it's a trap there's, no one should go here"
    l "..."

    # Phone mode
    play sound "audio/sfx/phone notification.ogg"
    l "But at the very least there's still some place, and people that can understand me"
    show lily at centerright with ease
    h_nvl "HELLO!!!" 
    h_nvl "HI!!!" 
    h_nvl "HEY!!!" 
    h_nvl "HEY!!!" 
    h_nvl "YURIIII!!!" 
    l_nvl "what what?!"
    h_nvl "YURIIIIII!!!" 
    l_nvl "I'M HERE IM HERE!!"
    h_nvl "NO LIKE!!! ACTUALY YURI!!!!"
    h_nvl "ORANGE YURI!!!" 
    h_nvl "ANIME CONFIRMED!!!!" 
    h_nvl "NEXT JANUARY!!!!!!!!!!!!" 
    l_nvl "HOLY FRICK!!!!! ORANGE YURI!!!!?" 
    l_nvl "ACTUALLY??!!!!" 
    h_nvl "YEAAAAAA!!!" 
    l_nvl "MY BUTCH ICON… ON THE SCREEN…. HOLY CRAP" 
    h_nvl "HEY!!! its OUR butch icon!!!!! No gatekeeping!!!!!!" 
    l_nvl "Kitsugi Moga gonna look so gorgeous, oh my gawd." 
    l_nvl "We HAVE to watch it ASAP!!" 
    h_nvl "DUH??!!!?? Get ur ass ready and clear ur schedule!!!! January is the new pride month 🔥🔥🔥🔥" 
    l_nvl "I should be saying that to you!!! Prepare to get kidnapped 😈 "
    l_nvl "nobody else can match my yuri obsession like you, esp one with pretty masc urghh. #goals" 
    h_nvl "hehe~ don't bite off more than you can chew. You've barely seen my freakiness~" 
    h_nvl "also check this out, new necklace ✨"
    l_nvl "oh be still my beating heart 🤣 u do have great taste, I need that so badlt. hand it over right nowwwww!!! 🫵"
    h_nvl "NEVERRR!!!!" 
    l_nvl "muahahhahahaha it's a bestie's duty to steal their friend’s stuff 😘 gonna reach through the screen!" 
    h_nvl "screw you /j 🤣 I could never hate you. With all my heart, I love yuri and WX_YuriZ, one wayyyyyy more than the other~" 
    l_nvl "haha gay 🫵 jk, me too ✨" 
    l_nvl "Anyways I gotta go to school now urgh. So lame. Talk to you later!" 
    h_nvl "it wasn't a joke. see you soon 👋"
    nvl clear

    play sound "audio/sfx/bus stopping.ogg"
    l "What does she mean by that..."
    l "Whatever there's no way she'll go to a place like this"
    show lily at slow_moveoutright
    scene black with wiperight
    hide lily
    jump school_day_1
    

label school_day_1:
    scene bg classroom with wiperight

    s1 "Have you heard the news?"
    s2 "What news?"
    s3 "There's a new transfer student"
    s4 "Wow, transferring schools at highschool is she chasing someone? How Romantic"
    s5 "Where's our teacher?"
    show lily at enter_from_left_to_center
    l "huhhh..."
    l "what are they talking about"
    hide lily with dissolve
    show teacher at slide_in_right
    t "ermm..."
    t "Alright, alright everyone settle"
    t "for our first day of class..."
    t "for our first day of class, let’s get to know each other better and introduce ourselves, and and tell us what do you want to have for this year"
    show teacher at fast_moveoutright
    show school_girl_1 at enter_from_right_to_center
    pause 1.0
    s1 "blabla"
    show school_girl_1 at fast_moveoutright
    show school_girl_2 at enter_from_right_to_center
    pause 1.0
    s2 "blabla"
    show school_girl_2 at fast_moveoutright
    show school_girl_3 at enter_from_right_to_center
    pause 1.0
    s3 "blabla"
    show school_girl_3 at fast_moveoutright
    scene black with fade
    scene bg classroom with dissolve
    t "Lastly Lily! Can you introduce yourself to us please."

    show lily at enter_from_right_to_center
    pause 2.0
    l "He-hello everyone my name is Li-lily..."
    l "a-and I hope for this year I can get to know you all better and make memories together."
    show lily at fast_moveoutright
    pause 1.0
    show teacher at slow_enter_from_left_to_center
    pause 1.5
    t "alright that's it for our first day of cla--"
    t "Oh wait nevermind… we have a new student she transfer from another city"


