# Flags are here
default holly_affection = 0
default holly_nickname = "Lily"
default holly_refusal_count = 0
default push_holly_count = 0
default delete_text = 0
# Use like h "lets go [holly_nickname]"


# NVL characters are used for the phone texting
define l_nvl = Character("WX_YuriZ", kind=nvl, image="lily", callback=Phone_SendSound)
define h_nvl = Character("h0lly_m0lly", kind=nvl, image="holly", callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)


#plz work plz work plz work

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
    stop music
    scene black
    $ quick_menu = False
    pause 1.0
    play music "audio/ambience/heavy rain.ogg" fadein 3.0 volume 0.5
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

    show holly d2base d2l2 d2r2 oface crazyeye:
        full
        center
        silhouette_idle

    stop sound
    h_unknown "Finally, you're aaaaaall miiiiiiiine now"
    h_unknown "We can live together forever now, just the two us"
    scene black with eyeclose
    scene bg abandoned house with eyeopen
    show holly d2base d2l1 d2r2 oface crazyeye:
        center_lower
        medlong
        silhouette_idle
    h_unknown "You couldn't hide from your true self, so now I'm setting you free"
    h_unknown "I know deep down inside you also want this to happen..."
    scene black with eyeclose
    scene bg abandoned house with eyeopen
    show holly d2base d2l1 d2r2 oface crazyeye:
        center_lowest
        medclose
        silhouette_idle
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
    show lily pjbase scaredeye grimaceoface pjl2 pjr2:
        full
        center
    show lily neutraleye frownface
    l "What a weird dream..."
    l "..."
    show lily spookeye oface
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
    show lily unibase unil1 unir1 spookeye noface:
        slide_in_left
        fall_and_recover(height=400, fall_time=0.5, ground_time=1.5, recover_time=0.6)
        slide_to_vert (1.1, 0.3)
        slide_to (0.45, 0.6)
    play sound "audio/sfx/fall_down.ogg"
    pause 3.6

    play sound "audio/sfx/bus start.ogg"
    l "OOOOUCCCCCHH!"
    show lily downeye
    l "I hate this morning already"
    stop sound
    play music "audio/ambience/road ambiance.ogg" fadein 2.0
    l "School sucks"
    l "Everything here sucks"
    l "I've been living in this town for 16 years and nothing changed..."
    l "This town became so dull, and boring"
    l "The streets, buildings, the people seems to follow something nobody wants to change"
    show lily thinkeye
    l "Every eyes seems to be staring at me... "
    l "Waiting for me make me mistakes"
    l "If I won't comply, and act differently they'll beat, and curse me"
    show lily cryeye unir2
    l "I hate this it feels suffocating..."
    l "I want to be more like me, and everyone to not give a fuck who I wanted to be"
    l "This place... it's a trap there's, no one should go here"
    l "..."

    # Phone mode
    play sound "audio/sfx/phone notification.ogg"
    show lily neutraleye unir1
    l "But at the very least there's still some place, and people that can understand me"
    show lily downeye unilphone at centerright with ease
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
    stop music fadeout 2.0
    play sound "audio/sfx/bus stopping.ogg"
    show lily thinkeye
    l "What does she mean by that..."
    show lily unil1 neutraleye
    l "Whatever there's no way she'll go to a place like this"
    show lily at bus_slow_moveoutright
    pause 1.0
    stop sound
    scene black with wiperight
    hide lily
    jump school_day_1
    

label school_day_1:
    scene bg classroom with wiperight
    pause 2.0
    
    play music "audio/ambience/classroom ambience.ogg" fadein 3.0 volume 0.5
    s1 "Have you heard the news?"
    s2 "What news?"
    s3 "There's a new transfer student"
    s4 "Wow, transferring schools at highschool is she chasing someone? How Romantic"
    s5 "Where's our teacher?"
    show lily unibase unil1 unir1 thinkeye noface at enter_from_left_to_center
    l "huhhh..."
    l "what are they talking about"
    hide lily with dissolve
    show teacher at slide_in_right
    t "ermm..."
    t "Alright, alright everyone settle"
    t "for our first day of class..."
    t "for our first day of class, let’s get to know each other better and introduce ourselves, and and tell us what do you want to have for this year"
    show teacher at fast_moveoutright
    show school_girl_1 smileoface at enter_from_right_to_center
    pause 1.0
    s1 "Hey, don't look at me that way, don't you know my name..."
    show school_girl_1 at fast_moveoutright
    show school_girl_2 neutralface at enter_from_right_to_center
    pause 1.0
    s2 "What's up everyone remember my name..."
    show school_girl_2 at fast_moveoutright
    show school_girl_3 grimaceface at enter_from_right_to_center
    pause 1.0
    s3 "I don't need an introduction just don't mess with me this year, that's all"
    show school_girl_3 at fast_moveoutright
    show school_girl_4 smileoface at enter_from_right_to_center
    pause 1.0
    s4 "Oh my... This is embarassing I'm..."
    show school_girl_4 at fast_moveoutright
    show school_girl_5 neutralface at enter_from_right_to_center
    pause 1.0
    s5 "I am uhhh..."
    s5 "uhhh..."
    show school_girl_5 at fast_moveoutright
    scene black with fade
    scene bg classroom with dissolve
    t "Lastly Lily! Can you introduce yourself to us please."

    show lily unibase unil2 unir2 spookeye at enter_from_right_to_center
    pause 2.0
    l "He-hello everyone my name is Li-lily..."
    l "a-and I hope for this year I can get to know you all better and make memories together."
    show lily at fast_moveoutright
    pause 1.0
    show teacher at slow_enter_from_left_to_center
    pause 1.5
    t "alright that's it for our first day of class"
    t "Oh wait nevermind we have a new student she transfered from another city"
    show teacher at slow_moveoutleft

    show holly unibase unil1 unir1 neutraleye smugface:
        full
        toleft
        enter_from_right_slow(0.5, 2.5)
    pause 3.0
    show holly smileoface
    h "My name is... my name Holly and for this year I want to have..." 
    show holly crazyeye:
        medlong
        center_upper
    h "I WANT WX_YuriZ TO BE MINE, AND ONLY MINE!!!"
    show holly smugface:
        medium
        center_uppest
    h "I LOVE YOU WX_YuriZ I'VE COME HERE JUST TO BE WITH YOU" 
    h "I FUCKING LOVE YOOOOOOOOOOOUUUUUUUUUU WX_YuriZ"
    show holly:
        full
        slide_to_vert(0.5, 0.2)
        slide_to(0.8)
    show lily:
        full
        toright
        enter_from_left_to_leftish(0.1, 1.5)
    pause 1.5
    h "Aren't you happy to see me?"
    l "What is she doing wait... no way..."
    l "Wha-what should I say?"
    "The choices you make affects the story of the game choose carefully"

    menu first_meet:
        "Wha-what should I say?"
        "Who-who are you talking to":
            $ holly_affection -= 1
            $ renpy.notify("Holly's Affection 💔")
            l "Who-who are you talking to"
            l "There's no girl named WX_YuriZ"
            l "what a du-dumb name..."
            show holly annoyedeye frownface
            h "Is that so?"
            h "Looks like my effort to get here are wasted how sad..."
        "N-n-no way are you holl–":
            $ holly_affection += 1
            $ renpy.notify("Holly's Affection 💖")
            l "I-is this reall..."
            l "N-n-no way are you holl–"
            show holly winkeye smugface
            h "How nice you noticed me"
            h "I thought you're going to pretend"
            l "but why?"
            l "I won't be your friend here..."
            h "what do you mea--"
    
    play sound "audio/sfx/school bell.ogg"
    show teacher:
        full
        slide_in_left
    show holly at slide_off_right
    t "What the hell is wrong with you! get out of this room and come to my office NOW!"
    show teacher:
        full
        fast_moveoutright
    s1 "What a weirdo, what is she even wearing"
    s2 "Oh God, what an entrance I hate her already"
    s3 "Her face makes me sick, I hope I’ll never get close to her for the whole year"
    s4 "Oh my, what a brave confession so romantic hihi"
    s5 "Uh... who’s WX_Yuri"
    s5 "Sick name!"
    show lily spookeye
    l "Huh??? Who the is that girl? how does she know my name?" 
    l "If she's really her, then..."
    l "This is bad I can't let anyone know that name"
    l "what do I do?"
    l "..."
    s5 "Yuri is such a sick name, I wish I have her name"
    l "ye-yeah... right there's a lot of people named Yuri out there"
    l "She must be referring to someone"
    l "There's no way h0lly will come to this place just to see me"
    l "Calm down, I will not get exposed today..."
    show lily at slow_moveoutright
    scene black with fade
    jump evening_day_1
            

label evening_day_1:
    scene bg Lily bedroom with dissolve
    play music "audio/ambience/night ambiance.ogg" fadein 2.0

    show lily pjbase pjl1 pjr2 scaredeye frownface:
        full
        left
    l "*huff...* Is this for real? What is going on? could she really be h0lly_m0lly?"
    show lily thinkeye oface:
        full
        slide_to(0.9)
    l "Holy... Moly!"
    show lily grimacecface:
        full
        slide_to(0.1)
    l "No way.... No way... No way... this is bad"
    show lily scaredeye grimaceoface:
        full
        slide_to(0.9)
    l "She'll... she'll destroy my image"
    show lily spookeye frownface:
        full
        slide_to(0.1)
    l "I can't live like that, what will I do?"
    play sound "audio/sfx/phone notification.ogg"
    show lily pjlphone downeye:
        full
        slide_to(0.7)
    l "Is that her?"
    h_nvl "Good evening yuri, you looked so cute IRL <3"
    h_nvl "Why are you ignoring me?"
    h_nvl "Acting like you didn’t know me I thought we are friends"
    h_nvl "You haven’t answered my question earlier"
    h_nvl "Aren’t you happy to see me?"

    menu (nvl=True):
        "Are you really Holly?":
            $ holly_affection += 1
            $ renpy.notify("Holly's Affection 💖")
            l_nvl "Are you really Holly?"
            l_nvl "You must be joking right?"
            h_nvl "Yes I'am"
            h_nvl "you want me to shout your name again tomorrow"
            show lily grimacecface
            l_nvl "How can you do this?"
        "Why would you this?":
            $ holly_affection -= 1
            $ renpy.notify("Holly's Affection 💔")
            show lily grimacecface
            l_nvl "Why would you this?"
            l_nvl "are you out of of your mind"
            l_nvl "We only knew each other online"
            l_nvl "How can you do this?"
            h_nvl "Are my feelings not enough to do this?"
    h_nvl "anyways... can you just anwer my question"
    h_nvl "are you happy to see me 🥺"
    stop music
    show lily shyface
    menu (nvl=True):
        "No":
            $ holly_affection -= 1
            $ renpy.notify("Holly's Affection 💔")
            show lily grimaceoface angryeye
            l_nvl "are you serious?"
            l_nvl "no way"
            l_nvl "I'm more scared, than happy"
            show lily downeye frownface
            h_nvl "HOW RUDE!!! "
            h_nvl "I'VE COME THIS WAY JUST FOR YOU"
            h_nvl "AND THIS IS HOW YOU'LL TREAT ME"
            show lily oface
            l_nvl "I am scared that you'll justt"
            l_nvl "throw away my secrets"
            l_nvl "I won't let you destroy my image"
        "Yes":
            $ holly_affection += 1
            $ renpy.notify("Holly's Affection 💖")
            show lily thinkeye
            l_nvl "Yes"
            h_nvl "Awwwwwwwww"
            h_nvl "I'm happy to hear that, I'm gonna cry 🥺"
            h_nvl "I'm also very happy to finally see you IRL 💖"
            show lily downeye frownface pjr2
            l_nvl "But not this way!!"
            l_nvl "I can't let you just"
            l_nvl "throw away my secrets"
            l_nvl "I won't let you do that"
    show lily downeye frownface pjr2
    play music "audio/bgm/hollys theme.ogg" fadein 1.0
    h_nvl "Too bad, it's too late for that now"
    l_nvl "What do you want anyway?"
    h_nvl "Why do you keep denying me, when I’ve come so far just to be with you :<"
    h_nvl "aren't we..."
    h_nvl "friends"
    show lily grimacecface
    l_nvl "We are friends, not like this"
    l_nvl "this is too far, I don't like this"
    show lily frownface
    h_nvl "what are you hiding anyways?"
    h_nvl "what are you afraid of?"
    h_nvl "Oh see... so that's how it is"
    h_nvl "I understand it now you're closeted, aren’t you?"
    show lily spookeye grimacecface
    h_nvl "With the way you act"
    h_nvl "the way you speak"
    h_nvl "nobody here knows the real you"
    show lily downeye
    h_nvl "right?"
    h_nvl "The Lily I know the real Lily"
    show lily grimaceoface
    l_nvl "stop it!"
    show lily grimacecface
    h_nvl "I know how much you hated this place"
    h_nvl "but don’t worry I’m here now I’ll save you"
    h_nvl "I wonder what will happen if everyone here will know the real you"
    show lily grimaceoface
    l_nvl "stop it!"
    l_nvl "stop it!"
    l_nvl "stop it!"
    show lily frownface
    menu (nvl=True):
        "Please stop this, I’ll do anything":
            $ holly_affection += 1
            $ renpy.notify("Holly's Affection 💖")
            l_nvl "please stop what you're about to do"
            l_nvl "I'll do anything"
        "Just tell me what you want":
            $ holly_affection += 1
            $ renpy.notify("Holly's Affection 💖")
            l_nvl "Just tell me what you want"
            l_nvl "Just don't expose me"
            l_nvl "I'll do anything"
    show lily spookeye shyface
    h_nvl "GO OUT WITH ME"
    h_nvl "DO THE THINGS YOU SAID YOU WANT TO DO WITH ME" 
    h_nvl "BE THE REAL LILY WITH ME"
    show lily downeye pjr2
    l_nvl "I can’t believe you’re doing this, I thought you understand me"
    l_nvl "I thought we are friends"
    h_nvl "Yes I do, this is why I’m doing this! to save youuuuuuuu"
    stop music fadeout 1.0
    show lily grimacecface
    play music "audio/ambience/night ambiance.ogg" fadein 1.0
    l_nvl "You really leave me no choice…"
    h_nvl "see you after school tomorrow hihi <3"
    h_nvl "Good night XOXO"
    nvl clear

    l "What did I set myself up to?"
    l "I’m so tired there’s a lot of things that happened today… I wish I could just escape"
    scene black with eyeclose_slow
    pause 1.0
    jump lily_monologue


label lily_monologue:
    scene black
    play music "audio/ambience/playground.ogg" fadein 2.0 volume 0.75
    pause 1.0

    python:
        lily_lines = [
            "Lily…",
            "What are you doing?",
            "Lily!",
            "Stop doing that, you're not a boy!",
            "Lily",
            "Stop wearing your father's army uniform that's for boys",
            "Lily",
            "Here play with this dolls instead drop that toy gun, that's not a for girls",
            "Lily",
            "Watch your mouth! girls never says bad words",
            "Lily",
            "This is not how I expect a girl like you should behave",
            "Lily?",
            "can you just be a normal girl",
            "I'm so disappointed you grew up like this",
            "I can't believe I raised a freak like you, I failed as your mother…",
            "I'm sorry",
            "Lily"
        ]

        for line in lily_lines:
            txt = Text(line, xalign=0.5, yalign=0.5, xsize=900, text_align=0.5,
                    color="#ffffff", size=62, outlines=[(2, "#000000", 0, 0)])
            renpy.show("water_line", what=txt, at_list=[water_in], zorder=100)
            renpy.pause(0.9, hard=False)
            renpy.pause(get_line_pause(line), hard=False)
            renpy.show("water_line", what=txt, at_list=[water_out], zorder=100)
            renpy.pause(0.7, hard=False)
            renpy.hide("water_line")
            renpy.pause(0.3, hard=False)

    stop music fadeout 1.0
    jump morning_day_2


label morning_day_2:
    play sound "audio/sfx/alarm_beep.ogg"
    pause 5.0
    stop sound fadeout 1.0

    play music "audio/ambience/morning_ambience.ogg" fadein 3.0
    scene bg bed top view with eyeopen_slow
    show lily pjbase pjl2 pjr2 frownface cryeye:
        full
        center
    l "what's happening to me?"
    l "All these weird dreams I've had recently..."
    show lily scaredeye grimacecface
    l "Wha-what do they mean?"
    l "Please make it stop..."
    play sound "audio/sfx/phone notification.ogg"
    show lily downeye frownface pjlphone at centerright with ease
    
    h_nvl "Good morning my Yuri 🌻🤗"
    l_nvl "gm"
    h_nvl "Why are you so cold to me Lily?"
    show lily shyface
    h_nvl "Oppsss I forgot you're my girlfriend now"
    h_nvl "Yippie"
    h_nvl "*sent GIF*"
    h_nvl "I should call you something else now"
    h_nvl "What do you like???"
    h_nvl "how about..."

    # --- Holly floods the chat, auto-advancing without clicks ---
    $ _old_afm_enable = _preferences.afm_enable
    $ _old_afm_time = _preferences.afm_time
    $ _preferences.afm_enable = True
    $ _preferences.afm_time = 2

    h_nvl "babe"
    h_nvl "babyyyyy"
    h_nvl "sweetheart"
    h_nvl "my lovely lilllyyyy <3"
    h_nvl "Blossom"
    h_nvl "Snowflake"
    h_nvl "Sunflower"
    h_nvl "My World"
    h_nvl "Shining Star"

    # restore normal click-to-continue
    $ _preferences.afm_enable = _old_afm_enable
    $ _preferences.afm_time = _old_afm_time
    # --- end flood ---

    menu (nvl=True):
        "Just call me by name":
            $ holly_affection -= 1
            $ renpy.notify("Holly's Affection 💔")
            $ holly_nickname = "Lovely Lily"
            show lily grimacecface
            l_nvl "No, don't! Just call me by my name"
            l_nvl "This is so cringe you know"
            l_nvl "I don't want any of this"
            l_nvl "I'm not yours just so you know"
            h_nvl "So you don't like any of it huh?"
            h_nvl "boriiiiiiiing…"
            h_nvl "I'll pick one for you, how about..."
            show lily shyface
            h_nvl "Lovely Lily"
            h_nvl "Isn't cute?"
            show lily frownface
            h_nvl "See you later"
            h_nvl "My lovely Lily"

        "Blossom":
            $ holly_affection += 1
            $ renpy.notify("Holly's Affection 💖") 
            $ holly_nickname = "Blossom"
            l_nvl "I dont mind being called blossom"
            l_nvl "It's cute too"
            h_nvl "YESSSSSSSSS!"
            h_nvl "it sounds so cute, my heart is about to explode <3"
            l_nvl "nothing wrong with calling a friend that"
            h_nvl "Yeah... Right"
            h_nvl "see you later, my Blossom"

        "Shining Star":
            $ holly_affection += 2
            $ renpy.notify("Holly's Affection 💖") 
            $ holly_nickname = "Shining Star"
            l_nvl "I want to be your Shining star"
            l_nvl "It's cute and funny"
            l_nvl "I guess friends can call each other like that"
            h_nvl "Yeah, obviously"
            h_nvl "I love it, its so cuteeee my haaarrrt"
            h_nvl "see you later, my shining star"

        "Lovely Lily":
            $ holly_affection += 3
            $ renpy.notify("Holly's Affection 💖") 
            $ holly_nickname = "Lovely Lily"
            l_nvl "I want to be called Lovely"
            l_nvl "No one's ever called me like that"
            l_nvl "We're friends anyways so I guess..."
            l_nvl "It's alright"
            h_nvl "Yaaaaaaassss"
            h_nvl "I was hoping you choose that"
            h_nvl "I love that nickname"
            h_nvl "I love it"
            h_nvl "I love it"
            h_nvl "I love it, my heart is about to explode"
            h_nvl "See you later my Lovely Lily"
    nvl clear
    stop music
    show lily pjl1 thinkeye 
    l "When will she stop"
    l "I can't take this anymore..."
    l "What is she planning to do?"
    l "I guess I need to play along for now"
    play sound "audio/sfx/bus_horn.ogg"
    l "Commiinng"
    stop music fadeout 2.0
    show lily at fast_moveoutright
    scene black with wiperight_medium
    play sound "audio/sfx/running.ogg"
    stop sound
    
    jump school_day_2


label school_day_2:
    play sound "audio/sfx/bus stopping.ogg"
    pause 4.0
    scene black with wiperight
    pause 2.0
    stop sound
    scene bg classroom with dissolve
    play music "audio/ambience/classroom ambience.ogg" fadein 3.0 volume 0.75
    show teacher with dissolve:
        full
        center
    t "Alright I hope all of you have already settled in, let's forget what happened yesterday and get along nicely, okay?"
    t "So for today we'll discuss poetry."
    t "I have here a poem by Amy Lowell, an American poet born in 1874, titled \"A Decade\""
    t "I'll read it for all of you..."
    hide teacher with dissolve
    pause 1.0

    python:
        poem_stanzas = [
            "When you came, you were like red wine and honey,",
            "And the taste of you burnt my mouth with its sweetness.",
            "Now you are like morning bread,",
            "Smooth and pleasant.,",
            "I hardly taste you at all for I know your savour.",
            "But I am completely nourished."
        ]

        for stanza in poem_stanzas:
            txt = Text(stanza, xalign=0.5, yalign=0.5, xsize=900, text_align=0.5,
                    color="#ffffff", size=64, outlines=[(2, "#000000", 0, 0)],
                    line_spacing=6)
            renpy.show("water_line", what=txt, at_list=[water_in], zorder=100)
            renpy.pause(0.9, hard=False)
            renpy.pause(get_line_pause(stanza), hard=False)
            renpy.show("water_line", what=txt, at_list=[water_out], zorder=100)
            renpy.pause(0.7, hard=False)
            renpy.hide("water_line")
            renpy.pause(0.5, hard=False)

    show teacher with dissolve:
        full
        center
    t "Alright I hope you enjoyed listening to that one."
    t "Now, let's talk about more about the poem, let's dive in deep into its meaning."
    t "Lily!"
    show lily unibase unil1 unir2 spookeye noface:
        full
        toright
        enter_from_left_to_leftish(0.1, 1.0)
    show teacher:
        full
        toleft
        slide_to(0.9)
    t "What do you think the poem is meaning of the poem?"
    show lily thinkeye
    l "{i}uhhh...{/i}"
    menu poem_meaning:
        "What do you think is the meaning of the poem"
        "People changing":
            l "It is about..."
            l "Pe-people change over time..."
            l "The person you knew today might be completely different tommorrow."
            $ renpy.notify("Holly's Affection 💔")
            $ holly_affection -= 1
        "Hiding your true identity":
            l "It is about..."
            l "Hiding your tru-true identity from people."
            l "Giving them an illusion, but you're not truly that person they thought you are..."
            $ renpy.notify("Holly's Affection 💖")
            $ holly_affection += 1
        "Passion fading":
            l "I think the poem is about..."
            l "Passion fading away..."
            l "How something can be hot at first you know it but goes cold with time..."
            $ renpy.notify("Holly's Affection 💔")
            $ holly_affection -= 1
        "I dont know":
            l "I-I'm sorry but I don't know..."
    
    show lily downeye
    t "Is that so?"
    t "Very well, interesting interpretation..." 
    hide lily with dissolve
    show teacher:
        slide_to(0.5)
    t "Next!" 
    t "Holly"
    show holly unibase unil2 unir1 neutraleye smilecface:
        full
        toright
        enter_from_left_to_leftish(0.1, 1.5)
    show teacher:
        full
        toleft
        slide_to(0.9)
    h "Huh, oh come on!"
    t "What does the line \"Now you are like morning bread\" mean?"
    h "Do I really need to answer that question"
    show holly unil1 smileoface
    h "It means…"
    show holly crazyeye
    h "Loft bread are bland, and stale but my love for Yuri will never go pale"
    h "I love you everyday with no fail"
    h "Together our love will prevail"
    h "So let's go explore each other and sail"
    t "Wow, that’s beautiful a beautiful poem *sobs*"
    hide teacher with dissolve
    hide holly with dissolve

    show school_girl_1 with dissolve:
        full
        center
    show school_girl_2 with dissolve:
        full
        rightish
    show school_girl_3 with dissolve:
        full
        leftish
    show school_girl_4 with dissolve:
        full
        right
    show school_girl_5 with dissolve:
        full
        left

    show school_girl_1 grimaceface at center, school_pop
    s1 "Cringeeeeeeee, what is she talking about?"

    show school_girl_1 neutralface at center, school_idle
    show school_girl_2 oface at rightish, school_pop
    s2 "Can someone stitch this bitch's mouth, I can't handle her anymore."

    show school_girl_2 neutralface at rightish, school_idle
    show school_girl_3 smileoface at leftish, school_pop
    s3 "Guys I have an idea so that she'll never come to school again, later this lunch let's…"

    show school_girl_3 at leftish, school_idle
    show school_girl_4 smileoface at right, school_pop
    s4 "Wow what a romantic poem, I can feel your passion burning hot!"

    show school_girl_4 at right, school_idle
    show school_girl_5 grimaceface at left, school_pop
    s5 "Can somebody tell me who is Yuri already?"
    show school_girl_5 neutralface
    s5 "But yeah, I don't like bread either but they're good with peanut butter hehe~"
    show school_girl_5 at left, school_idle

    play sound "audio/sfx/school bell.ogg"
    stop music
    t "alright class dismissed"
    play sound "audio/sfx/running.ogg"
    show school_girl_1 at slow_moveoutright
    show school_girl_2 at slow_moveoutright
    show school_girl_3 at slow_moveoutright
    show school_girl_4 at slow_moveoutright
    show school_girl_5 at slow_moveoutright
    pause 2.0

    show lily unibase unil2 unir2 downeye noface:
        full
        toright
        slide_to(0.9, 0.8)
    show holly unibase unil2 unir1 neutraleye smugface:
        full
        toright
        enter_from_left_slow(0.2, 1.6)
    pause 2.0
    h "Lily! Don't forget about our deal later~"
    menu deal_later:
        "Deal later?"
        "What deal?":
            $ holly_affection -= 1
            $ renpy.notify("Holly's Affection 💔") 
            l "Wha-what deal?"
            l "I don' remember any?"
            show holly annoyedeye frownface
            h "Don't pretend you don't know, we have a deal right?"
            h "You agreed we'll go out."
            show lily neutraleye
            l "Ohh... date, a friendly date!"
            show holly thinkeye
            h "Alright."
        "Yeah, I won't":
            $ holly_affection += 1
            $ renpy.notify("Holly's Affection 💖") 
            show lily neutraleye
            l "Yeah, I won't."
            l "We have a deal..."
            show holly winkeye smileoface
            h "Yeah, this is gonna be fun."
            h "Our first date together!"
            h "Yipppie!!"
    show holly smugface
    h "Also let's have lunch together today."
    h "Nothing wrong with that, just like normal girlfrie-"
    show lily spookeye
    l "Sto-stop it, not here please…"
    h "Fine, just eat lunch with me right now… or else..." 
    l "Alright… alright… I’ll go…"
    show lily downeye
    h "Yippieeeeeeee let’s go [holly_nickname]"
    show holly at slow_moveoutright
    show lily at slow_moveoutright
    pause 1.5
    scene black with wipeleft

    jump school_cafeteria_day_2


label school_cafeteria_day_2:
    play music "audio/ambience/cafeteria.ogg" fadein 1.0 volume 0.5
    h "Come on Lily, let’s sit right there~"
    scene bg cafeteria seat with wipeleft
    show holly unibase unil1 unir1 smilecface neutraleye with dissolve:
        full
        toright
        centerleft
    show lily unibase unil1 unir2 neutraleye noface with dissolve:
        full
        toright
        centerright
    show holly shockeye frownface
    h "This food is awful! How can you eat this every day?"
    l "Yeah..."
    h "Who do you usually eat lunch with?"
    l "..."
    h "Huh? Do you mean..."
    l "..."
    show holly cryeye oface
    h "Awwww, my poor Lily... *sobs*"
    h "Alone, cold, and lonely..."
    h "*sobs*"
    h "Don't worry, I'm here now. I'll never leave your side!"
    show holly frownface
    l "Tt's nothing..."
    show lily thinkeye
    menu holly_pity:
        "What should I say?"   
        "Thanks.":
            $ holly_affection += 1
            $ renpy.notify("Holly's Affection 💖") 
            show lily unir1 neutraleye
            l "Tha-thanks for being here with me"
        "I don't need your sympathy.":
            $ holly_affection -= 1
            $ renpy.notify("Holly's Affection 💔")
            show lily unil2 angryeye
            l "I don't need your pity"
            l "I'm fine by my own anyways"
    show holly crazyeye smugface
    h "Don't worry, I'm on your side. I completely understand you."
    h "I know what you want, what you need, what you think..."
    show holly neutraleye
    h "But how about me?"
    h "After all of our time together, do you know me?"
    show lily thinkeye
    menu holly_knowledge:
        "Do you know Holly?"
        "Yeah":
            $ holly_affection += 1
            $ renpy.notify("Holly's Affection 💖")
            l "Yeah, of course..."
            l "I know you best, I can read you easily."
        "No":
            $ holly_affection -= 1
            $ renpy.notify("Holly's Affection 💔") 
            l "No, of course not."
            l "We haven't really spent much time together."
    show lily neutraleye
    show holly neutraleye smilecface unir2
    h "Alright alright then..."
    h "Let's play a game."
    show lily spookeye unil2 unir2
    l "What game?"
    l "Can we just have lunch, please...?"
    h "It's not a big deal. Just guess what I'm thinking, and you win!"

    scene bg napkin with dissolve
    call hangman_minigame(word_list=["LILY"], category="What am I thinking?") from _call_hangman_cafeteria_day1

    scene bg cafeteria seat with dissolve
    show holly unibase unil1 unir1 smilecface neutraleye with dissolve:
        full
        toright
        centerleft
    show lily unibase unil1 unir2 neutraleye noface with dissolve:
        full
        toright
        centerright

    if hangman_result == "win":
        $ holly_affection += 1
        $ renpy.notify("Holly's Affection 💖")
        l "L-Lily...? You were thinking about me?"
        h "Of course! what else am I going to think about?"
        show holly smugface unir2
        h "You actually know me well, I'm touched!"
    else:
        h "Aw, out of guesses already? It was \"LILY\"!"
        show holly frownface
        l "That was a dumb game."
        l "Why would you think about me..."
        show holly cryeye
        h "You don't know me well huh?"
        show holly neutraleye smilecface    
        h "It's ok [holly_nickname] we have time to get to know each other"
        $ holly_affection -= 1
        $ renpy.notify("Holly's Affection 💔")

    show holly winkeye smileoface unil1
    h "Alright your turn, let me guess what's on your mind!"
    show lily unir2 downeye
    l "No... I don't want to play this game anymore"
    h "Come on it's just a game..."
    show holly thinkeye oface unir2
    h "Oh... we already ran out of napkins, can you get some for me [holly_nickname] pleaseeee"

    menu holly_napkin_request:
        "I don't want to play your games.":
            $ holly_refusal_count += 1

            if holly_refusal_count == 1:
                l "I don't want to play your games"
                l "Go get it yourself"
                show holly grimaceoface
                h "Is this how you'll treat me!"
                h "AFTER ALL THE THINGS I'VE DONE FOR YOU"
                h "NO!"
                show holly frownface
            else:
                $ no_text = " ".join(["NO!"] * (2 ** (holly_refusal_count - 1)))
                show holly grimaceoface
                h "Is this how you'll treat me!"
                h "AFTER ALL THE THINGS I'VE DONE FOR YOU"
                h "[no_text]"
                show holly frownface

            jump holly_napkin_request

        "Alright I'll get it.":
            $ holly_affection += 1
            $ renpy.notify("Holly's Affection 💖")
            show holly winkeye smugface
            l "Alright, alright I'll get it."
            h "Hehe that's my [holly_nickname]"
            show lily unibase unil1 unir2 neutraleye noface:
                full
                toleft
            show lily at slow_moveoutright
            scene black with wipeleft
            jump school_cafeteria_counter


label school_cafeteria_counter:
    scene bg cafeteria counter with wipeleft
    show lily unibase unil2 unir1 downeye at enter_from_left_to_center
    pause 3.0
    l "*huff..."
    l "Wha-what have I done...?"
    show lily cryeye
    l "I just wanted to be me..."
    l "To express myself freely..."
    l "This is a disaster…"
    l "I can't let her near me…"
    show lily unir2
    l "I-I don't feel safe…"
    l "I can't let her expose me, and out me…"
    l "If anybody here finds out about that side of me, I..."
    l "No, no, no, no, no, no..."
    l "I can't let that happen..."
    show lily scaredeye
    l "I am dead. I am dead. I am dead."
    l "I won't let that happen. I won't let her..."
    l "If I'm anywhere but here, I'll be doomed."
    show lily cryeye
    l "This should be enough."
    show lily:
        toright
    l "I'm heading back."
    show lily at slow_moveoutleft
    scene black with wiperight
    jump school_cafeteria_day_2_bully_scene


label school_cafeteria_day_2_bully_scene:
    scene bg cafeteria seat with wiperight
    show school_girl_1 with dissolve:
        full
        righty
    show school_girl_2 with dissolve:
        full
        rightish
    show school_girl_3 with dissolve:
        full
        right
    show holly unibase unil2 unir1 annoyedeye smilecface with dissolve:
        full
        leftish
    show school_girl_1 oface
    s1 "What are you doing here, weirdo?"
    show school_girl_1 neutralface
    show holly smileoface
    h "It's none of your business."
    show holly smilecface
    s2 "This is our table, bitch!"
    show school_girl_1 smileoface
    show school_girl_2 smileoface
    show school_girl_3 smileoface
    s3 "If you want this table, then have it all to yourself!"

    play sound "audio/sfx/slime.ogg"
    show holly unibasedirty unil2 grimacecface at leftish, bump(-30)
    show school_girl_1 smileoface
    show school_girl_2 smileoface
    show school_girl_3 smileoface
    s1 "Hahahahah, gotcha!"
    s2 "Good one, hahaha!"
    s3 "That'll teach her."

    l "Oh god... what'll I do?"

    menu holly_bullied:
        "What will you do?"

        "Protect holly":
            show lily unibase unil2 unir1 angryeye noface at enter_from_right_to_center
            l "Tha-thats enough!"
            show holly shockeye oface
            show school_girl_1 grimaceface
            s1 "Oh there's two weirdos now."
            s2 "What will you do if we won't hahahhaha!"
            show school_girl_3 neutralface
            s3 "Boring come on now guys this is no longer fun."
            $ holly_affection += 2 
            $ renpy.notify("Holly's Affection 💖") 
            show school_girl_1 at slow_moveoutright
            show school_girl_2 at slow_moveoutright
            show school_girl_3 at slow_moveoutright
            stop music fadeout 1.0
            show lily neutraleye:
                toright
            l "Are you alright?"
            show holly neutraleye smilecface
            h "Yeah they're nothing."
            h "Thank you."
            l "It's nothing... You would've done the same right?"
            show holly winkeye smugface
            h "Of course."
            l "Here's the napkin"
            show holly smilecface thinkeye
            h "It's fine, forget it."
            h "..."
            h "Don't forget about later."
            show lily downeye unil1
            l "Yeah.. I won't"
            scene black with dissolve
            hide lily  with dissolve
            hide holly with dissolve
            pause 1.0
            jump date_intro

        "Pretend nothing happen":
            show school_girl_1 at slow_moveoutright
            show school_girl_2 at slow_moveoutright
            show school_girl_3 at slow_moveoutright
            show lily unibase unil2 unir1 neutraleye at enter_from_right_to_center
            stop music fadeout 1.0
            pause 1.0
            l "..."
            l "They're gone now"
            show lily:
                toright
            l "Here's your napkins..."
            $ holly_affection -= 4
            $ renpy.notify("Holly's Affection 💔")
            show holly smilecface thinkeye
            h "Thank you..."
            h "Don't forget about later"
            h "Afters school"
            show lily downeye unir2
            l "Yea-yeah, I won't"
            stop music
            show lily at slow_moveoutright
            scene black with dissolve
            pause 1.0
            jump date_intro


label date_intro:
    play music "audio/ambience/rural night.ogg" volume 0.75
    scene bg park with dissolve

    show holly d2base d2l2 d2r1 frownface annoyedeye:
        full
        rightish
    with dissolve

    h "When is she coming"
    play sound "audio/sfx/walk on grass.ogg"
    show lily unibase unil1 unir2 downeye noface at enter_from_left_to_leftish
    stop sound

    show holly oface
    h "..."
    h "Ohhh... there you are"
    l "Hello…"
    h "Why are you wearing that?????? Your UNIFORM??!?! On our FIRST DATE?!??!"
    l "It's a clean set if that's what you're worried about... And... I don't have many clothes..."
    show holly cryeye oface 
    h "Oh..."
    show holly neutraleye
    h "Okay, fair. But that girlish uniform and skirt is not the Lily I know."
    h "Luckily I came prepared~"

    show holly:
        full
        slide_to(0.5, 0.8)
    h "Here wear this."
    play sound "audio/sfx/clothes give.ogg" volume 0.5
    show holly:
        full
        slide_to(0.75, 0.8)
    pause 1.0
    h "Change your clothes. I want to date the Lily I know."

    scene black with dissolve
    scene bg park with dissolve

    show holly d2base d2l2 d2r1 smilecface neutraleye with dissolve:
        full
        rightish
    show lily d2base d2l2 d2r2 shyface downeye at enter_from_left_to_leftish
    pause 1.0
    l "Are you happy now?"
    show holly winkeye smugface
    h "Now that's the Lily I know"
    l "So... What's the plan...?"
    show holly smileoface
    h "Anywhere you want to go~"
    h "I'll let you decide, I'm happy wherever you want my [holly_nickname]"
    show holly neutraleye smilecface
    show lily thinkeye

    menu date_option:
        "Where do you want to go?"
        "Somewhere quiet":
            $ holly_affection += 2
            $ renpy.notify("Holly's Affection 💖") 
            show lily downeye frownface
            l "Take me to somewhere quiet."
            l "Where nobody can see me... can see me like this..."
            show holly winkeye
            h "Your wish is granted [holly_nickname]"
            show holly at slow_moveoutright
            show lily at slow_moveoutright
            stop music
            
            scene black with wiperight
            jump abandoned_house_date_1
        "Some Cozy":
            $ holly_affection -= 1
            $ renpy.notify("Holly's Affection 💖") 
            show lily downeye frownface
            l "Take me to somewhere cozy"
            l "I want to be somewhere safe..."
            show holly winkeye
            h "Perfect! I know a place [holly_nickname]"
            show holly at slow_moveoutleft
            show lily at slow_moveoutleft
            stop music
            scene black with wipeleft
            jump restaurant_date


label restaurant_date:
    scene bg restaurant with wipeleft
    play music "audio/ambience/restaurant.ogg" volume 0.5 fadein 3.0
    
    show holly d2base d2l2 d2r1 smilecface neutraleye with dissolve:
        full
        rightish
    show lily d2base d2l2 d2r2 shyface downeye with dissolve:
        full
        leftish
    
    h "Good choice [holly_nickname], I knew you have great taste~"
    show lily oface
    l "Where even are we?"
    show lily shyface
    h "somewhere cozy, like you said."
    l "I haven't been here before, I'm not sure… am I safe with you here…"
    h "Don't worry, I'll make sure you're safe with me, I'll protect you with my life."
    show holly winkeye smileoface
    h "How about we get to know each other, this is our first date after all."
    show holly:
        parallel:
            ease 0.5 medlong
        parallel:
            ease 0.5 rightish

    show lily:
        parallel:
            ease 0.5 medlong
        parallel:
            ease 0.5 leftish
    l "Okay…"
    h "Do you have any hobbies?"
    show lily downeye
    menu hobby_choice_quite:
        "Do you have any hobbies?"

        "Yes":
            $ holly_affection += 1
            $ renpy.notify("Holly's Affection 💖") 
            l "Yeah... I have some."
            h "Me too, I also have some hobbies!!"

        "No":
            $ holly_affection += 1
            $ renpy.notify("Holly's Affection 💖") 
            l "N-n-no, I don't have one."
            h "Me too, I also don't have any hobbies!!"
    
    show holly thinkeye smilecface
    h "Hmmm... how about"
    show holly neutraleye smileoface
    h "What's your favourite color?"
    "Input your answer by typing"
    $ fav_color = renpy.input("What's your favorite color?").strip()
    if fav_color == "":
        $ fav_color = "lilac"
    l "I like [fav_color]"
    show holly crazyeye d2r2
    $ holly_affection += 1
    $ renpy.notify("Holly's Affection 💖") 
    h "Ohh what a coincidence I also love [fav_color]"
    h "I can't believe it we're so similar haahahhahahahahah"

    show holly winkeye smileoface
    h "Hmmm… What did you want to be when you grew up?"
    $ childhood_dream = renpy.input("What did you want to be when you grew up?").strip()
    if childhood_dream == "":
        $ childhood_dream = "Police"
    $ holly_affection += 1
    l "I want to be a [childhood_dream]"
    show holly crazyeye d2r2
    $ renpy.notify("Holly's Affection 💖") 
    h "whaaaaaat!! me too! I also want to be a [childhood_dream]"
    h "We are really the same, I feel like I found my soulmate hehehe"

    show holly smugface neutraleye
    h "Your turn ask me anything you want…"
    show lily neutraleye frownface
    l "..."
    l "Whe-when will you stop this?"
    show holly frownface
    h "Stop this?"
    stop music fadeout 1.0

    show holly annoyedeye smilecface d2r1
    h "but [holly_nickname] we just got started"
    play music "audio/bgm/hollys theme.ogg" volume 0.4 fadein 3.0

    show lily spookeye d2r2 d2l1
    show holly:
        medlong
        toleft
        slide_to(0.6, 0.8)
    h "You wanted this didn't you?"

    show holly smileoface:
        medlong
        toleft
        slide_to(0.5, 0.8)
    h "You told me before you wanted to do this."

    show holly crazyeye smugface:
        medlong
        toleft
        slide_to(0.4, 0.8)
    h "YOU TOLD ME YOU WANTED TO DO THIS!"

    show lily scaredeye grimaceoface d2r2
    l "Da-da-the Lily you met and knew online, and the Lily you're with right now are different!"
    l "A-a-I can't do this…"
    show lily grimacecface

    menu holly_pressure:
        "What do I do?"
        "Run away":
            $ holly_affection -= 1
            $ renpy.notify("Holly's Affection 💔")
            l "I'm sorry I can't do this"
            show lily:
                bump (-40)
                medlong
                leftish
            show holly annoyedeye grimaceoface d2r1 d2l2
            h "No, not this time you can't run away from me here"
            h "Why are you doing this?"
            show holly cryeye
            h "I though we are friends."
            h "What's wrong with you?!"
            show lily grimaceoface d2r1
            l "I-is this what friends do?"
            l "Please leave me alone!!!"
            show holly:
                parallel:
                    ease 0.5 full
                parallel:
                    ease 0.5 right

            show lily:
                parallel:
                    ease 0.5 full
                parallel:
                    ease 0.5 left
            h "But you told me you want to do this"
            h "To have something like this!"
            h "Experience something like this!!"
            show lily grimacecface spookeye
            l "You don't understand! Leave me alone!!"
            show lily at fast_moveoutleft
            scene black with wiperight
            jump abandoned_house_date_3
        "Push Holly":
            $ holly_affection -= 1
            $ renpy.notify("Holly's Affection 💔")
            show holly shockeye oface:
                medlong
                toleft
                slide_to(0.8, 0.8)
            l "Get away from me..."
            show holly cryeye frownface
            h "Why are you doing this?"
            h "What's wrong with you??!!?"
            show lily angryeye d2r1
            l "I am just reacting like anybody else would!"
            l "W-What am I doing wrong????"
            show holly grimacecface
            h "Why are you doing this to me."
            show holly:
                medlong
                toright
                slide_to(0.7, 0.8)
            h "Where's the Lily I know?"
            l "..."
            show holly grimaceoface:
                medlong
                toright
                slide_to(0.5, 0.8)
            h "WHERE IS SHE?"
            t "Erm... Ahem!"
            show teacher:
                full
                right
            
            show lily spookeye oface d2r1 d2r1:
                parallel:
                    ease 0.5 full
                parallel:
                    ease 0.5 left

            show holly shockeye oface d2l2 d2r1:
                parallel:
                    ease 0.5 full
                parallel:
                    ease 0.5 leftish
            
            t "What the hell are you two doing here, at this time of day or night"
            t "And why are you two so close to each other, uck!"
            show lily grimaceoface
            l "I-its not what you think it's jus--"
            show holly crazyeye smileoface d2l1 
            h "YES IT'S WHAT YOU THINK TEACH!"
            show holly crazyeye d2r2
            h "ME AND HOLLY ARE ABOUT TO HOOK UP!!!!"
            h "ME AND HOLLY ARE MADLY IN LOVE WITH EACH OTHER!!!!!"
            show holly neutraleye smugface d2r1
            h "Is there anything wrong with that teach?"
            t "What the hell?!??!?!"
            show holly crazyeye d2r2
            h "I don't care what you think"
            h "YURI IS MINE!!!!"
            t "What the--"
            t "Ughhhh..."
            stop music fadeout 1.0
            t "You don't know what you are doing"
            t "You don't have an idea what you are doing"
            t "This is so wrong"
            t "You two are not normal..."
            show lily scaredeye grimacecface
            t "And I will fix that."
            t "You two are coming with me!"
            t "It's for the best for both of you..."
            t "Security!"
            scene black with dissolve
            jump asylum_ending                 
        

label abandoned_house_date_1:
    $ time_of_day = "SILVERMOON"
    scene bg abandoned house with wiperight
    play music "audio/ambience/rural night.ogg" volume 0.5 fadein 2.0
    
    show holly d2base d2l2 d2r1 smilecface neutraleye with dissolve:
        full
        rightish
    show lily d2base d2l2 d2r2 shyface downeye with dissolve:
        full
        leftish
    
    h "Good choice [holly_nickname], I knew you have a great taste"
    l "Where even are we?"
    show lily shyface
    h "Somewhere quiet, like you said"
    l "I haven't been here before, I'm not sure… am I safe with you here…"
    h "Don't worry, I'll make sure you're safe with me, I'll protect you with my life."
    show holly winkeye smileoface
    h "How about we get to know each other, this is our first date after all"
    show holly:
        parallel:
            ease 0.5 medlong
        parallel:
            ease 0.5 rightish

    show lily:
        parallel:
            ease 0.5 medlong
        parallel:
            ease 0.5 leftish
    l "Okay…"
    h "Do you have any hobbies?"
    show lily downeye

    menu hobby_choice:
        "Do you have any hobbies?"

        "Yes":
            $ holly_affection += 1
            $ renpy.notify("Holly's Affection 💖") 
            l "Yeah... I have some."
            h "Me too, I also have some hobbies!!"

        "No":
            $ holly_affection += 1
            $ renpy.notify("Holly's Affection 💖") 
            l "N-n-no, I don't have one."
            h "Me too, I also don't have any hobbies!!"
    
    show holly thinkeye smilecface
    h "Hmmm... how about"
    h "What's your favourite color?"
    "Input your answer by typing"
    $ fav_color = renpy.input("What's your favorite color?").strip()
    if fav_color == "":
        $ fav_color = "lilac"
    l "I like [fav_color]"
    $ holly_affection += 1
    $ renpy.notify("Holly's Affection 💖") 
    show holly crazyeye d2r2
    h "Ohh what a coincidence I also love [fav_color]"
    h "I can't believe it we're so similar haahahhahahahahah"

    show holly winkeye smileoface
    h "Hmmm… What did you want to be when you grew up?"
    $ childhood_dream = renpy.input("What did you want to be when you grew up?").strip()
    if childhood_dream == "":
        $ childhood_dream = "Police"
    l "I want to be a [childhood_dream]"
    $ holly_affection += 1
    $ renpy.notify("Holly's Affection 💖") 
    show holly crazyeye d2r2
    h "Whaaaaaat!! me too! I also want to be a [childhood_dream]"
    h "We are really the same, I feel like I found my soulmate hehehe"

    show holly smugface neutraleye
    h "Your turn ask me anything you want…"

    show lily neutraleye frownface
    l "..."
    l "Whe-when will you stop this?"

    show holly frownface
    h "Stop this?"
    stop music fadeout 1.0
    show holly annoyedeye smilecface d2r1
    h "but [holly_nickname] we just got started"
    play music "audio/bgm/hollys theme.ogg" volume 0.4 fadein 3.0

    show lily spookeye d2r2 d2l1
    show holly:
        medlong
        toleft
        slide_to(0.6, 0.8)
    h "You wanted this didn't you"

    show holly smileoface:
        medlong
        toleft
        slide_to(0.5, 0.8)
    h "You told me before you wanted to do this."

    show holly crazyeye smugface:
        medlong
        toleft
        slide_to(0.4, 0.8)
    h "YOU TOLD ME YOU WANTED TO DO THIS!"

    show lily scaredeye grimaceoface d2r2
    l "Da-da-the Lily you met and knew online, and the Lily you're with right now are different!"
    l "A-a-I can't do this…"

    show lily grimacecface
    menu holly_pressure_quite_1:
        "I can't do this..."
        "Run away":
            if push_holly_count == 0:
                show holly annoyedeye smugface:
                    parallel:
                        ease 0.5 full
                    parallel:
                        ease 0.5 right

                show lily cryeye d2l2 d2r2 grimacecface:
                    parallel:
                        ease 0.5 full
                    parallel:
                        ease 0.5 left
                l "I'm sorry I can't do this"
                show lily at fast_moveoutleft
                scene black with wiperight
                jump abandoned_house_date_2
            else: 
                show lily cryeye d2l2 d2r2 grimacecface
                l "Stop followin me!"
                l "Please..."
                show lily at fast_moveoutleft
                scene black with wiperight
                jump abandoned_house_date_3


        "Push holly":
            $ push_holly_count += 1
            show holly shockeye oface:
                medlong
                slide_to(0.9, 0.8)

            if push_holly_count == 1:
                l "Ge-get away from me..."
                show holly annoyedeye oface:
                    parallel:
                        ease 0.5 full
                    parallel:
                        ease 0.5 right

                show lily:
                    parallel:
                        ease 0.5 full
                    parallel:
                        ease 0.5 left
                h "Lily!"
                h "Why are you doing this?"
                show holly cryeye frownface d2r2
                h "I thought we were friends..."
                show holly grimaceoface
                h "WAAAAAAAAAAAAAAAAAAAAAH!!!"
                show holly d2r1 frownface
                l "I know... I know we were friends-"
                l "Bu-bu-but I"
                h "Why are you doing this to me?"
                h "Why are you like this?"
                h "What's wrong with you?"
                show lily oface 
                l "wha-what do you mean?"
                l "I'm just acting, like how we are supposed to act!"
                show lily frownface
                show holly frownface
                h "Why can't you be like the Lily I know??? Why give that up for how you 'are supposed to act'?!??!"
                h "You want to do something like this right?"
                show holly neutraleye smileoface:
                    full
                    toleft
                    slide_to(0.7, 1.0)
                h "Right?"

                show holly crazyeye smugface:
                    full
                    toleft
                    slide_to(0.4, 0.8)
                h "Right…"

                show holly:
                    full
                    toleft
                    slide_to(0.3, 0.6)
                h "RIGHT!"
                jump holly_pressure_quite_1
            else:
                show holly:
                    parallel:
                        ease 0.5 full
                    parallel:
                        ease 0.5 right
                l "Stop!"
                l "I don't feel safe around you"
                l "ca-can we stop this…"
                l "get away from me please"
                h "You told me you want to be closer with me…"

                show holly annoyedeye grimacecface:
                    full
                    toleft
                    slide_to(0.7, 0.8)
                h "spend time with me…"

                show holly grimaceoface:
                    full
                    toleft
                    slide_to(0.4, 0.6)
                h "do things with me..."

                show holly crazyeye grimacecface:
                    full
                    toleft
                    slide_to(0.3, 0.5)
                h "BE CLOSER TO ME!"

                stop music fadeout 2.0
                show lily d2l2 
                l "I can't be seen doing like this here, if only you understand you'd knew"
                l "a-a-I'll be dead if I'm seen doing anything like this"
                show holly d2l2 shockeye oface:
                    full
                    toleft
                    slide_to(0.6, 0.8)
                h "..."
                l "I'll be dead…"
                h "what do you mean?"
                show holly frownface
                l "I need to act like how am I supposed to act, not like a freak, not like a disgrace"
                h "what abo--"
                show lily grimacecface
                l "I can't be gay"
                h "..."
                l "It's already, can we just go home already..."
                show lily frownface
                show holly neutraleye oface
                h "yeah right… right..."
                h "Let's just go home now, we're still friends right?"
                l "yes of course…"
                scene black with fade
                jump evening_day_2


label abandoned_house_date_2:
    $ time_of_day = "DAY"
    scene bg outside abandoned house with wiperight

    show holly d2base d2l1 d2r1 grimaceoface shockeye with dissolve:
        full
        right
    show lily d2base d2l2 d2r1 scaredeye grimaceoface with dissolve:
        full 
        left

    h "Lily!"
    show holly shockeye oface
    h "Why are you doing this?"
    show holly cryeye frownface d2r2
    h "I thought we were friends…"
    show holly grimaceoface
    h "WAAAAAAAAAAAAAAAAAAAAAH!!!"
    show holly d2r1 frownface
    show lily grimacecface
    l "I know... I know we were friends"
    l "bu-bu-but I"
    show lily d2l1 d2r2
    h "Why are you doing this to me?"
    h "Why are you like this?"
    h "What's wrong with you?"
    show lily oface 
    l "wha-what do you mean?"
    l "I'm just acting, like how we are supposed to act"
    h "Why can't you be like the Lily I knew, and the way you are supposed to act"
    h "You want to do something like this right"

    show holly neutraleye smileoface:
        full
        toleft
        slide_to(0.7, 1.0)
    h "Right?"

    show holly crazyeye smugface:
        full
        toleft
        slide_to(0.4, 0.8)
    h "Right…"

    show holly:
        full
        toleft
        slide_to(0.3, 0.6)
    h "RIGHT!"
    menu holly_pressure_quite_2:
        "RIGHT!"
        "Run away":
            l "Stop followin me!"
            l "please"
            show lily at fast_moveoutleft
            scene black with wiperight
            jump abandoned_house_date_3

        "Push Holly":
            show holly d2l2 annoyedeye oface:
                full
                slide_to(0.9, 0.8)
            l "Stop!"
            l "I don't feel safe around you"
            show lily d2l1 d2r2 scaredeye oface
            l "ca-can we stop this…"
            l "get away from me please"

            show holly d2l1 annoyedeye grimaceoface:
                full
                toleft
                slide_to(0.5, 1.0)
            h "You told me you want to be closer with me…"

            show holly annoyedeye grimacecface:
                full
                toleft
                slide_to(0.4, 0.8)
            h "spend time with me…"

            show holly grimaceoface:
                full
                toleft
                slide_to(0.3, 0.6)
            h "do things with me…"

            show holly crazyeye grimacecface:
                full
                toleft
                slide_to(0.2, 0.5)
            h "BE CLOSER TO ME!"

            stop music fadeout 2.0
            show lily d2l2 
            l "I can't be seen doing like this here, if only you understand you'd knew"
            l "a-a-I'll be dead if I'm seen doing anything like this"
            show holly d2l2 shockeye oface:
                full
                toleft
                slide_to(0.6, 0.8)
            h "..."
            l "I'll be dead…"
            h "what do you mean?"
            l "I need to act like how am I supposed to act, not like a freak, not like a disgrace"
            show holly frownface
            h "what abo--"
            show lily grimacecface
            l "I can't be gay"
            h "..."
            l "It's already late, can we just go home already..."
            show lily frownface
            show holly neutraleye oface
            h "yeah right… right..."
            h "Let's just go home now, we're still friends right?"
            l "yes of course…"
            scene black with fade
            jump evening_day_2


label abandoned_house_date_3:
    scene bg tunnel with wiperight

    show holly d2base d2l1 d2r1 grimacecface shockeye with dissolve:
        full
        right
    show lily d2base d2l2 d2r1 scaredeye frownface with dissolve:
        full 
        left

    l "Stop!"
    l "I don't feel safe around you"
    show lily d2l1 d2r2 scaredeye oface
    l "ca-can we stop this…"
    l "get away from me please"

    show holly annoyedeye grimaceoface:
        full
        toleft
        slide_to(0.5, 1.0)
    h "You told me you want to be closer with me…"

    show holly annoyedeye grimacecface:
        full
        toleft
        slide_to(0.4, 0.8)
    h "spend time with me..."

    show holly grimaceoface:
        full
        toleft
        slide_to(0.3, 0.6)
    h "do things with me..."

    show holly crazyeye grimacecface:
        full
        toleft
        slide_to(0.2, 0.5)
    h "BE CLOSER TO ME!"

    stop music fadeout 2.0
    show lily d2l2
    l "I can't be seen doing like this here, if only you understand you'd knew"
    l "a-a-I'll be dead if I'm seen doing anything like this"
    show holly d2l2 shockeye oface:
        full
        toleft
        slide_to(0.6, 0.8)
    h "..."
    l "I'll be dead…"
    h "what do you mean?"
    l "I need to act like how am I supposed to act, not like a freak, not like a disgrace"
    show holly frownface
    h "what abo--"
    show lily grimacecface
    l "I can't be gay"
    h "..."
    l "It's already, can we just go home already..."
    show lily frownface
    show holly neutraleye oface
    h "yeah right... right..."
    h "Let's just go home now, we're still friends right?"
    l "yes of course…"
    scene black with fade
    jump evening_day_2


label evening_day_2:
    $ time_of_day = "DAY"

    scene bg lily bedroom with dissolve
    play music "audio/ambience/night ambiance.ogg" fadein 2.0

    show lily pjbase pjl1 pjr2 spookeye frownface with dissolve:
        full
        center
    l "I don't feel so good…"
    l "There's something wrong"
    l "No. everything's going wrong"
    l "Is that Holly?"
    show lily pjlphone downeye:
        full
        slide_to (0.6, 0.5)
    play sound "audio/sfx/phone notification.ogg"
    h_nvl "{image=images/objects/pic 1.webp}"
    show lily shyface
    h_nvl "{image=images/objects/pic 2.webp}"
    show lily frownface
    h_nvl "{image=images/objects/pic 3.webp}"
    show lily grimacecface
    h_nvl "{image=images/objects/pic 4.webp}"
    h_nvl "We looked so cute here, [holly_nickname] :3"
    l_nvl "What the hell? When did you take this?!"
    l_nvl "what are you going to do with these?"
    l_nvl "Delete this right now!!!"
    h_nvl "See you tomorrow."
    h_nvl "Good night [holly_nickname]"


label delete_this_menu:
    menu (nvl=True):
        "Delete this!":
            $ delete_text += 1

            if delete_text == 1:
                l_nvl "Hey what the hell"
                l_nvl "Delete this now!"
                jump delete_this_menu

            elif delete_text == 2:
                l_nvl "HEY Don't sleep on me!"
                l_nvl "You can't be seriou"
                l_nvl "Delete this now!"
                jump delete_this_menu

            elif delete_text >= 3:
                l_nvl "D"
                l_nvl "E"
                l_nvl "L"
                l_nvl "E"
                l_nvl "T"
                l_nvl "E"
                l_nvl "T"
                l_nvl "H"
                l_nvl "I"
                l_nvl "S"
                jump delete_this_menu

        "Give up":
            show lily frownface
            l_nvl "I'll come talk to you tommorow"
            l_nvl "please delete this"

    nvl clear
    show lily pjl1 pjr2 thinkeye
    l "What is she planning with those pirctures"
    show lily pjl2 grimacecface spookeye
    l "If those pictures comes out then..."
    stop music fadeout 1.0
    l "No no no no no no no no no no"
    scene black with eyeclose_slow
    if holly_affection >= 4:
        jump lily_monologue_day_2
    else:
        jump outted_ending


label lily_monologue_day_2:
    scene black
    play music "audio/ambience/female talk.ogg" fadein 1.0 volume 0.75
    pause 1.0

    python:
        left_lines = [
            "There's something wrong with Lily...",
            "What can we do?",
            "She's not normal",
            "Is this what happens when someone grows up away from their father",
            "She's so rebellious",
            "She doesn't know who she is",
            "She acts so masculine",
            "She speaks so strong",
            "She likes other girls",
            "That's not normal",
        ]

        for line in left_lines:
            show_positioned_line(line, 0.2)

    stop music
    play music "audio/ambience/male talk.ogg" fadein 0.5 volume 0.75

    python:
        right_lines = [
            "Ahh I see",
            "That's indeed not normal",
            "Do you want me to fix your daughter...",
            "Lily, what a beautiful name",
            "Alright leave it up to me",
            "I'll fix her",
            "I'll fix her good...",
        ]

        renpy.pause(0.8, hard=False)

        for line in right_lines:
            show_positioned_line(line, 0.8)

    stop music fadeout 3.0
    pause 2.0
    jump morning_day_3


label morning_day_3:
    play sound "audio/sfx/alarm_beep.ogg"
    pause 5.0
    stop sound fadeout 1.0
    play music "audio/ambience/morning_ambience.ogg" fadein 3.0
    scene bg bed top view with eyeopen_slow
    show lily pjbase pjl1 pjr2 cryeye frownface:
        full 
        center
    
    l "Another weird dream, huh?"
    l "When will this stop?"
    show lily thinkeye
    l "What are those dreams even about?"
    show lily downeye pjlphone at centerright with ease
    play sound "audio/sfx/phone notification.ogg"

    h_nvl "Good morning [holly_nickname]"
    h_nvl "I hoped you slept well"
    h_nvl "Don't worry about the pictures. I just took them cuz they're just cute"
    h_nvl "I won't share them or anything"
    h_nvl "I understand you now"
    h_nvl "I'll keep you safe at your closet just as you like"
    h_nvl "see you later [holly_nickname]"

    show lily pjl1 pjr2 
    l "Oh thank God."
    l "I hope I can trust her…"
    l "We are good friends online"
    show lily downeye smilecface
    l "She helped me understand myself."
    l "After all... maybe… we might just have had a little misunderstanding."
    l "She might not be really that bad at all."

    play sound "audio/sfx/bus_horn.ogg"
    show lily thinkeye frownface
    l "Uhhh... yeah... I still have school today..."
    stop music fadeout 2.0
    show lily at fast_moveoutright
    l "Cooommiiiing-"
    scene black with wiperight_medium
    play sound "audio/sfx/running.ogg"
    pause 2.0

    jump bus_scene_day_3


label bus_scene_day_3:
    scene bg bus interior with wiperight
    show lily unibase unil1 unir1 neutraleye at enter_from_left_to_center

    play sound "audio/sfx/bus start.ogg"
    # SHOW: Picture of rural Southeast Asian country (Scene 1)
    l "This town is old, and rusty."
    l "I forgot the exact reason why I hated it."

    stop sound
    play music "audio/ambience/road ambiance.ogg" fadein 2.0
    # SHOW: Picture of rural Southeast Asian country (Scene 2)
    l "I just have this feeling ever since..."
    show lily thinkeye unir2
    l "Why can't I be me here? What am I scared of?"
    l "I don't remember…"
    l "I just know that if I don't act exactly as expected, something bad will happen…"
    show lily cryeye
    l "Something out of a nightmare."
    l "Something that maybe I'd like to forget."
    show lily downeye
    l "I wonder if I leave this place, I'll be free from that feeling."
    # SHOW: Picture of a lily flower
    
    l "At least for now, I still feel safe online sharing who I really am."
    show lily neutraleye
    l "One day, I'll come out of my closet and kiss a girl in front of everyone…"
    show lily downeye
    l "But not right now... She's just making things so much harder for me."
    stop music fadeout 2.0
    l "I wish all of this would just end soon…"
    pause 1.0
    show lily at slow_moveoutright
    stop sound
    scene black with wiperight
    hide lily
    jump school_day_3
    

label school_day_3:
    play sound "audio/sfx/bus stopping.ogg"
    pause 4.0
    scene black with wiperight
    pause 2.0
    stop sound
    scene bg classroom with dissolve
    play music "audio/ambience/classroom ambience.ogg" fadein 3.0 volume 0.75
    show teacher with dissolve:
        full
        center
    t "Good morning."
    t "For today, we're going to learn about plants and flowers."
    t "Who here likes flowers?"
    s5 "Oh me! I like it when you mix it with water and yeast, then heat it for a while. It's really good!"
    t "Thank you for your answer, but I'm talking about F-l-o-w-e-r flowers, not F-l-o-u-r flour"
    t "Let's move on... I have a question for you guys."
    t "Does anybody here know what flower symbolises innocence and rebirth?"
    t "Lily!"
    t "What do you think is the answer?"
    show lily unibase unil1 unir1 spookeye:
        full
        toright
        enter_from_left_to_leftish(0.1, 1.5)
    show teacher:
        full
        toleft
        slide_to(0.9)
    l "{i}Uhhh...{/i}"
    menu flower_meaning:
        "What flower symbolises innocence and rebirth?"
        "Cosmos":
            l "Hmmm... Cosmos?"
            t "Study harder, that's incorrect."
            $ renpy.notify("Holly's Affection 💔")
        "Daffodil":
            l "Uhhh... Daffodils?"
            t "Nice try but that's not correct."
            $ renpy.notify("Holly's Affection 💖") 
        "Lily":
            l "I think the poem is about... lilies?"
            t "Very good, correct!"
            $ renpy.notify("Holly's Affection 💖") 
        "I don't know":
            l "I don't know..."
            t "It's alright."
            t "I should've expected less from you."
            $ renpy.notify("Holly's Affection 💔")
    hide lily with dissolve
    show teacher:
        slide_to(0.5)
    t "The flower that symbolizes innocence and rebirth are Lilies."
    t "In Christian art, the Virgin Mary is usually depicted being given Lilies by the Angel Gabriel."
    t "That's why lilies are usually used at weddings, representing new beginnings,
    and at funerals which symbolizes the innocence of the soul after death." 
    t "Alright moving on~"
    show holly unibase unil1 unir1 neutraleye oface:
        full
        toright
        enter_from_left_to_leftish(0.1, 1.5)
    h "{i}hooooaaaaaah{/i}" #whats hoooooaaaaah?
    t "Yes, holly!"
    show holly shockeye frownface
    h "Huh? What did I do?"
    hide holly with dissolve
    t "No, I mean the flower is holly."
    t "Hollies are known for their bright red winter berries, symbolizing the holiday season."
    t "They are dioecious, meaning each bush or tree is strictly male or female."
    t "Now, did you know that lilies and hollies cannot grow together?"
    t "Hollies grow into large, dense, woody shrubs or trees."
    t "They cast a deep shadow over lower-growing plants, starving sun-loving flowers like lilies and killing them."
    stop music
    play sound "audio/sfx/school bell.ogg"
    t "Before you leave, for your assignment this weekend, I want you to take a sample of your favourite flower."
    t "Give it a brief description of what it is, what does it likes, and how to take care of it, submit it to me next week, okay?"
    t "Alright, class dismissed!"
    show teacher at slow_moveoutright
    pause 2.0

    show school_girl_1 with dissolve:
        full
        center
    show school_girl_2 with dissolve:
        full
        rightish
    show school_girl_3 with dissolve:
        full
        leftish
    show school_girl_4 with dissolve:
        full
        right
    show school_girl_5 with dissolve:
        full
        left

    show school_girl_1 at center, school_pop
    s1 "I can't believe that bitch Holly is still here. I guess we haven't done enough."
    show school_girl_1 grimaceface

    s1 "I won't survive a year in this class with her."

    show school_girl_1 at center, school_idle
    show school_girl_2 oface at rightish, school_pop
    s2 "I have some tea~"
    s2 "So, yesterday after class, I saw her with..."
    s2 "The two of them are too disgusting for me to handle-"
    show school_girl_2 neutralface

    show school_girl_2 at rightish, school_idle
    show school_girl_3 at leftish, school_pop
    s3 "I see... but let's see what will happen next before doing something."

    show school_girl_3 at leftish, school_idle
    show school_girl_4 smileoface at right, school_pop
    s4 "He loves me, he loves me not. Ohhh~ Flowers being a symbol of love is so romantic."

    show school_girl_4 at right, school_idle
    show school_girl_5 at left, school_pop
    s5 "Uhhhh..."
    s5 "What's the difference between flours and flours? Aren't they the same?"
    show school_girl_5 at left, school_idle

    play sound "audio/sfx/running.ogg"
    show school_girl_1 at slow_moveoutright
    show school_girl_2 at slow_moveoutright
    show school_girl_3 at slow_moveoutright
    show school_girl_4 at slow_moveoutright
    show school_girl_5 at slow_moveoutright
    pause 2.0

    show lily unibase unil1 unir1 downeye:
        full
        toright
        slide_to(0.9, 1.0)
    show holly unibase unil2 unir1 neutraleye smilecface:
        full
        toright
        enter_from_left_slow(0.1, 1.5)
    pause 1.0
    h "Lily, let’s take lunch together again today!"
    show holly winkeye smileoface
    h "Just as friends, just as you like, and want."
    h "We’re friends, aren’t we?"
    menu lunch_day_2:
        "We're friends, aren't we?"
        "Ignore":
            l "..."
            h "I’ll take that as a yes."
            show lily neutraleye unil2
            l "Bu-bu-but I haven’t said anything…"            
            h "Don’t worry, I know how to act now."
            h "It’s just a casual friends' lunch, not a big deal."
        "Go with Holly":
            show lily neutraleye
            l "Alright, it's just lunch anyways"
            show holly smugface
            h "Yaaaay! Let’s go!"
            h "I brought some food."
            l "You won't pull any of those games right?"
            show holly smilecface neutraleye unil1
            h "Don’t worry, I know how to act now."
            h "It’s just a casual friends' lunch, not a big deal~"
    show holly at slow_moveoutright
    show lily at slow_moveoutright
    scene black with wipeleft
    jump school_cafeteria_day_3


label school_cafeteria_day_3:
    play music "audio/ambience/cafeteria.ogg" fadein 1.0 volume 0.5
    h "That table is occupied I guess. Let's sit right here"
    scene bg cafeteria new seats with wipeleft

    show lily unibase unil1 unir2 neutraleye:
        full
        leftish
    show holly unibase unil1 unir1 neutraleye smilecface:
        full
        rightish
    with dissolve

    h "Here, have some of this."
    show lily thinkeye
    l "Thanks."
    show holly winkeye smileoface
    h "You're welcome! Is it good?"
    l "It's better than what we usually have here at school."
    h "Ahahahhahahaha!"
    h "Yeah, the food here sucks."
    show lily neutraleye
    l "I know, hahahhahaha."
    show holly thinkeye frownface unil2
    h "..."
    h "Listen... I'm sorry about how I've acted these past few days."
    h "I didn't know your situation."
    show lily unil2 
    l "It's fine... you're new here, so you had no idea about it."
    l "I also didn't mean to push you far away and paint you as an evil person."
    l "It's fine, we could still be friends…"

    show lily:
        full
        leftish
        bump(-40)
    play sound "audio/sfx/slime.ogg"
    show lily unibasedirty unir2 unil1 scaredeye
    show holly shockeye
    l "Oh, shit, shit... my clothes!"
    l "What do I do?"
    l "How am I supposed to fix this…?"
    show lily cryeye
    show holly unil1 winkeye smilecface
    h "Calm down [holly_nickname]— I mean, Lily."
    h "I brought extra clothes. You can borrow them."

    show lily at slow_moveoutleft
    scene black with dissolve
    scene bg cafeteria new seats with dissolve

    show holly unibase unil2 unir1 neutraleye frownface:
        full
        rightish
    with dissolve
    pause 1.0

    show lily unibasepants downeye unil1 unir2 at enter_from_left_to_leftish
    h "What is taking her so long?"
    show holly crazyeye smilecface unir2
    h "Tha-that fits you so well... *blushes*"
    show holly winkeye
    l "This feels so uncomfortable."
    l "How can you wear this every day?"
    show lily unil2
    l "It feels like I'm sticking out too much right now."
    l "I feel like everyone's eyes are on me."

    show school_girl_1 at enter_from_right_to_rightish
    show school_girl_2 at enter_from_right_slow(0.9, 1.0)
    show school_girl_3 at enter_from_right_slow(0.5, 1.3)

    show lily:
        full
        toright
        slide_to(0.1, 0.8)
    show holly:
        full
        toright
        slide_to(0.25, 0.8)

    show school_girl_1 smileoface
    s1 "We are, indeed."
    s2 "What are you wearing... freak?"
    show holly frownface unir1
    show school_girl_2 smileoface
    s3 "It looks so shit on you, haha!"
    s1 "Thank God the weirdos are now grouped together. It's easier to pick on you two."
    show school_girl_2 grimacecface
    show holly annoyedeye grimacecface
    s2 "You look like such an eyesore. Get out of my sight now!"
    show holly grimaceoface
    h "CUT IT!"
    show holly unir2
    h "I can tolerate your bullshit when it at me..."
    show holly unil1 unir1:
        bump (-60)
        full
        toleft
    h "BUT NOT WITH LILYYYYYYYYYYYY!"

    show holly:
        bump (-40)
        full
        toleft
        slide_to(1.5, 0.6)
    show school_girl_1 oface at fast_moveoutright
    show school_girl_2 oface at fast_moveoutright
    show school_girl_3 oface at fast_moveoutright
    pause 1.0
    scene black with dissolve
    pause 1.0
    scene bg cafeteria new seats with dissolve

    show lily unibasepants unil1 unir2 downeye:
        full
        leftish
    with dissolve
    l "Is she gonna be ok"
    l "Did I treat her too harshly? Why is she still protecting me..."
    show holly unibase unil2 unir2 winkeye smilecface at enter_from_right_to_rightish
    show lily neutraleye
    l "Holly... you're here!"
    h "Yeah~"
    l "Tha-thanks..."
    l "It's my first time getting picked by them-"
    l "I-it's scary…"
    show holly neutraleye smileoface unil1
    h "It's alright, I'm here."
    h "Let's go shopping for some new clothes!"
    show holly frownface thinkeye
    h "It seems like the stains on your old clothes are really bad. I doubt you can wear them again."
    show holly smilecface unil2
    show lily spookeye
    l "Re-really?"
    stop music fadeout 1.0
    show lily downeye
    l "Sounds like a good idea."
    l "Thank God you're here. I would have panicked if this happened to me alone hahahaha."
    show holly winkeye unil1
    h "Yeah, let's go."
    scene black with dissolve
    jump shopping_date


label shopping_date:
    play music "audio/ambience/mall.ogg" fadein 2.0 volume 0.75
    l "I hope nobody sees us here..."
    scene bg mall with dissolve
    pause 1.0
    show holly d3base d3l2 d3r1 smilecface neutraleye with dissolve:
        full
        rightish
    show lily unibasepants unil1 unir2 downeye with dissolve:
        full
        leftish

    l "If somebody sees us like this, we're surely dead-"
    show holly winkeye d3r2
    h "It's ok. This is just friends doing errands, right?"
    show lily thinkeye
    l "Yeah right…"
    l "Let's go hurry, the women's section should be at the second floor."
    show holly frownface neutraleye d3r1
    h "Boriiiiing… tomorrow's a weekend anyways, let's have some fun!"
    h "I've never seen you dressed like how you told me you wanted to."
    h "Have you ever dressed the way you wanted to?"
    show lily unil2 unir1 spookeye
    l "N-no… I can't… Why would I?"
    h "Give it a shot, it's not really a big deal!"
    show lily thinkeye unil1 unir1
    l "But I'm really here to get a replacement for my uniform..."
    show holly d3l1 winkeye smilecface
    h "We can do that after. Come on, we have time!"
    h "Alright, then decide what you want?"

    menu shopping_date_choice:
        "Alright, then decide what you want?"
        "Don't go with Holly":
            l "I'll just buy a replacement for my uniform."
            l "I don't really need to go anywhere else."
            l "I don't need to change my clothing..."
            show holly shockeye oface
            h "Ah…"
            show holly annoyedeye
            h "AAAAAAAAAAAAAAHHHHHHH!!!"
            show holly grimaceoface
            h "ARE YOU SERIOUS"
            h "THEN WHY MAKE ME GO WITH YOU?"
            show lily scaredeye unil2
            l "But yo-you're the one who insists on coming here with me!"
            show holly neutraleye smugface
            h "Hahahahaahaha..."
            h "Yeah, right… right…"
            show holly winkeye
            h "I didn't mean anything I said."
            h "I'll go now myself, have fun shopping~"
            show lily downeye
            l "Yeah… take care..."
            show lily neutraleye
            l "You didn't take any photos this time, did you?"
            h "… Ye-yeah"
            show holly frownface annoyedeye at fast_moveoutright
            l "Thanks for coming alo—"
            l "Along"
            show lily cryeye 
            l "..."
            show lily at slow_moveoutleft
            scene black with wipeleft
            jump women_section

        "Go with Holly":
            $ holly_affection += 4
            show lily unil1 unir1 smilecface
            l "Yeah, you're right, we have some time."
            l "We could shop around for a bit and try out stuff!"
            show holly neutraleye smugface d3l2 d3r1
            h "Yippie!"
            h "I knew you wanted to try it out."
            show holly d3l1 winkeye
            h "I really know you better than anyone else~"
            show lily downeye
            l "I'm not really uncomfortable with my clothes..."
            h "Don't worry. It won't take too much time."
            h "We could get your uniform later."
            show lily neutraleye
            l "Yeah."
            h "Let's go!"
            show holly at slow_moveoutright
            show lily at slow_moveoutright
            scene black with wiperight
            jump men_section


label women_section:
    scene bg women section with wipeleft
    show lily unibasepants unil2 unir1 thinkeye at enter_from_right_to_center
    l "Hmmm..."
    show lily:
        full
        slide_to(0.8)
    l "I don't have enough money for this one... hehe."
    show lily unil1 downeye:
        full
        slide_to(0.1)
    l "This one's cheaper-"
    l "I'll buy this."
    show lily at slide_off_right
    pause 1.0
    scene black with dissolve
    stop music fadeout 1.0
    pause 1.0
    play sound "audio/sfx/cash register.ogg"
    c "That would be 1000"
    c "Thank you for shoping come again!"
    $ kidnap_ending_flag = True
    jump evening_day_3


label men_section:
    scene bg men section with wiperight

    show holly d3base d3l2 d3r1 neutraleye smugface:
        full
        rightish
    show lily unibasepants unil1 unir2 neutraleye:
        full
        leftish
    with dissolve

    h "Let me pick clothes for you."
    h "I mean Lily-"
    h "I think this will fit you well!"
    show holly d3l1:
        full
        slide_to(0.9)
    h "And this-"
    show holly d3l2 d3r2 crazyeye smilecface:
        full
        slide_to(0.1)
    h "And this!!"
    show holly neutraleye smugface:
        full
        slide_to(0.75)
    show lily spookeye unil2
    l "Isn't this a bit too much?!"
    l "It's my first time trying this stuff..."
    show holly winkeye
    h "Don't worry. I'm sure it'll fit you well Yur--"
    h "I mean Lily. Hurry and try it out, I'll wait for you!"
    show lily downeye unir1
    l "This is so embarrassing, I hope no one will see us."
    l "If someone noticed me wearing this then..."
    l "I'll be dead I'll be dead I'll be dead-"
    show lily at fast_moveoutleft
    scene black with dissolve
    scene bg men section with dissolve

    show holly d3base d3l2 d3r1 neutraleye smugface with dissolve:
        full
        rightish

    show lily d3base d3l1 d3r1 neutraleye shyface at enter_from_left_to_leftish
    pause 1.0
    l "Hello?"
    show lily smilecface
    show holly crazyeye frownface
    l "I guess this is not too bad after all..."
    h "..."
    show holly oface
    h "Ah."
    h "AAAAAAAAAAAHHHHH"
    show holly smileoface d3r2 
    h "OMG OMG OMG OMG"
    h "It fits you so well!!!! You're just like the Lily I imagined, the Lily I knew!"
    h "THE REAL LILYYYYY"
    h "My [holly_nickname]"
    show lily spookeye d3l2
    show holly winkeye smilecface
    l "O-ok calm down. Stop it, or people will notice us!"
    l "This feels so weird..."
    show lily thinkeye frownface
    l "We're standing out too much... we're not acting like other people."
    l "Oh god... Oh god... I'm gonna get exposed this way!"
    show lily d3r2
    h "Don't worry, I won't let that happen."
    l "Let's hurry and buy the things I actually need, please!"
    l "I-I can't have anybody see me like this."
    show lily frownface cryeye
    l "If anyone notices me and out me..."
    l "I'll be... dead..."
    h "Don't worry, no one will notice you"
    h "You look like a totally new and different person!"
    h "But..."

    show holly d3l2 d3r1 neutraleye smileoface:
        full
        toleft
        slide_to(0.7, 1.0)
    h "It feels good, doesn't it?"

    show holly smugface d3r2:
        full
        toleft
        slide_to(0.6, 0.8)
    h "To let out the real you."
    h "Not the Lily of this town, but the Lily I want, and I'll have."

    show holly crazyeye d3l1:
        full
        toleft
        slide_to(0.4, 0.6)
    h "One day it'll all come out, but you'll have me~"
    h "AND I'LL HAVE YO-"

    show school_girl_5 smileoface at enter_from_right_to_rightish
    show holly shockeye oface 
    show lily spookeye grimacecface
    s5 "Oh, what a coincidence if it isn't Holly. And... Lily?"
    s5 "Hellooooooo, it's nice meeting you around here hehe."
    s5 "Hmmmm... what are you two doing here?"
    show school_girl_5 oface
    s5 "It's rare to see Lily around with anyone."
    s5 "You two seem supeeeeer close with each other."
    s5 "Ohh, I see how it is, you two are..."

    menu shopping_date_s5_choice:
        "Ohh, I see how it is, you two are..."

        "Deny":
            show lily:
                full
                slide_to (0.1, 0.3)
            l "No-no-no-no it's not what you're thinking…"
            l "We're ju-"
            show school_girl_5 smileoface
            s5 "Huh? You two are not role-playing as an undercover cop and a criminal?"
            s5 "Aawww, too bad. I would love to join!"
            show holly winkeye smileoface d3l1 d3r1
            h "Uh, man. You blew up my cover, now she knows that I'm the criminal... game's over."
            s5 "Ooppsss hehe, my bad~"
            show school_girl_5 at slow_moveoutright
            show lily cryeye d3l2 d3r2 frownface
            l "That was a close one..."
            show holly neutraleye smilecface d3l2 d3r2
            h "See, I got this."
            h "I can save you-"
            h "I just saved you!"
            show lily downeye smilecface d3l1
            l "Let's just go home..."
            l "That's enough for today. I don't want to wear this again!"
            show lily d3l2 cryeye smileoface
            l "I can't let anybody see me like this again..."
            show holly thinkeye frownface
            h "Yeah, right..."
            l "I'm just gonna buy the things that I need now..."
            scene black with dissolve
            stop music fadeout 1.0
            pause 1.0
            play sound "audio/sfx/cash register.ogg"
            c "That would be 1000"
            c "Thank you for shopping, come again soon!"
            jump evening_day_3

        "Run away":
            show lily at fast_moveoutleft
            show holly at fast_moveoutleft
            s5 "Hey, wait!"
            s5 "You guys are role-playing as undercover cops and criminals, right? I wanna join!"
            s5 "Awwww... there's next time, I guess"
            jump men_section_getaway


label men_section_getaway:
    scene black with wipeleft
    scene bg women section with wipeleft
    show holly d3base d3l2 d3r1 neutraleye frownface at enter_from_right_to_rightish
    show lily d3base d3l2 d3r1 neutraleye frownface at enter_from_right_to_center
    show lily:
        full
        slide_to (0.3, 1.6)

    l "*huff* *huff* *huff*"
    l "I can no longer go on like this"
    show lily spookeye grimacecface
    l "Oh God... Oh God... I wonder what she is thinking-"
    l "Does she know about our relationship?"
    show holly winkeye smilecface d3l1 d3r2
    h "But we're just friends, right?"
    h "I bet she's just thinking we're just playing some game."
    h "Don't worry about it!"
    show holly neutraleye smileoface
    h "I'll talk to her, and explain. Go buy your things, Lily."
    show holly at fast_moveoutright
    l "Tha-thanks..."
    scene black with dissolve
    stop music fadeout 1.0
    pause 1.0
    play sound "audio/sfx/cash register.ogg"
    c "That would be 1000"
    c "Thank you for shopping, come again soon!"
    jump evening_day_3


label evening_day_3:
    scene bg lily bedroom with dissolve
    play music "audio/ambience/night ambiance.ogg" fadein 2.0

    show lily pjbase pjl1 pjr2 downeye frownface with dissolve:
        full
        center
    
    l "What a long day…"
    l "A lot of things happened…"
    show lily smilecface
    l "Holly seems to have changed."
    show lily thinkeye
    l "Did I judge her too quickly?"
    show lily downeye frownface pjl2
    l "No no no... she doesn't understand yet."
    l "I'm just protecting myself..."
    l "But I'm glad she's trying her best to understand this place."
    l "Wait, she still hasn't texted me goodnight?"
    show lily spookeye
    l "Is there something wrong?"
    l "Should I text her?"
    menu text_Holly_tonight:
        "Should I text her?"
        "Text Holly":
            $ renpy.notify("Holly's Affection 💖")
            show lily downeye:
                full
                slide_to (0.7, 0.9)
            l_nvl "Helloooo H0lly"
            l_nvl "Are you awake"
            l "No replies, huh?"
        "Sleep":
            $ renpy.notify("Holly's Affection 💔") 
            show lily neutraleye
            l "Nevermind."
            l "She must be tired as well."
            l "I'll just sleep."
    
    show lily shyface downeye pjl1 pjr1
    l "But she was really helpful to me today, and she didn't put me in any drama."
    l "In fact, she actually stood up for me!"
    l "Am I wrong about her?"
    l "Is her drama over now?"
    show lily smileoface pjl2
    l "Hahahahahaha, I was worried about nothing…"
    show lily smilecface downeye
    l "I hope I won’t get any more of those weird dreams."
    l "What was all that about, anyways… Is it because of what has happened lately?"
    l "I’m so tired…"
    l "I think I'm fallin aslee-"

    stop music fadeout 1.0
    scene black with eyeclose_slow
    pause 1.0
    if holly_affection >= 8:
        jump lily_monologue_day_3
    else:
        jump outted_ending


label lily_monologue_day_3:
    scene black
    play sound "audio/ambience/tension.ogg" fadein 1.0 volume 0.75
    pause 1.0

    python:
        left_lines = [
            "Lilyyyy",
            "Oh Lilyyyyyyy",
            "Where are youuuuu...",
            "Oh there you are",
            "Your mother told me I should take care of you",
            "So today I'm teaching you things",
            "Things that a girl like you should do",
            "Girls at your age are a bit rebellious",
            "You don't know what you want, what you should do",
            "But I can fix that",
            "I’ll teach you how a girl like you should behave, act, and like",
        ]

        for line in left_lines:
            show_positioned_line(line, 0.2)

    stop sound
    # play sound "audio/sfx/kissing.ogg" fadein 1.0 volume 0.5

    python:
        right_lines = [
            "Like this",
            "This thing is what a girl and a boy do...",
            "This is what you should like",
            "This is what you should do",
            "You should never do this with anyone else",
            "Especially with a girl",
        ]

        renpy.pause(0.8, hard=False)

        for line in right_lines:
            show_positioned_line(line, 0.8)

    stop sound fadeout 1.0
    pause 1.0
    jump morning_day_4


label morning_day_4:
    play sound "audio/sfx/alarm_beep.ogg"
    pause 5.0
    stop sound fadeout 1.0

    play music "audio/ambience/morning_ambience.ogg" fadein 3.0
    scene bg bed top view with eyeopen_slow
    show lily pjbase pjl1 pjr2 frownface spookeye with dissolve:
        full
        center
    l "..."
    l "I remember now."
    l "..."
    l "The-these are no-not my dreams..."
    l "..."
    stop music
    show lily grimacecface scaredeye
    l "The-they are my me-me-memories..."
    l "What the fuck!"
    l "What the fuck!"
    show lily grimaceoface 
    l "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    camera at frantic_shake
    $ quick_menu = False
    window hide
    show screen infinite_scream
    scene white with dissolve
    pause 2.0
    scene bg classroom with dissolve
    pause 2.0
    scene bg cafeteria counter with dissolve
    pause 2.0
    scene bg mall with dissolve
    pause 2.0
    scene black with dissolve
    pause 2.0
    stop music fadeout 1.0
    camera at shake_settle
    pause 1.0
    hide screen infinite_scream with dissolve
    jump kidnap_intro


label kidnap_intro:
    $ time_of_day = 'RAIN'
    $ quick_menu = True
    play music "audio/ambience/drizzle.ogg" fadein 1.0
    pause 1.0
    scene bg rainy tree with fade

    show lily pjbase pjl2 pjr2 frownface emptiness with dissolve:
        full
        left
    l "AH"
    l "..."
    show holly d2base d2l2 d2r1 shockeye oface at enter_from_right_to_rightish
    pause 3.0
    h "Lily?"
    h "What are you doing here?"
    l "..."
    h "Are you ok?"
    show holly neutraleye
    h "You'll get sick if you stay here"
    l "..."
    play sound "audio/sfx/dry thunder.ogg"
    show holly d2l1 d2r1 thinkeye smileoface:
        full
        slide_to (0.7, 0.6)
    h "It looks like it's going to rain hard"
    h "Don't worry I've got a nice place for you to hide"
    show holly d2l2 d2r2 neutraleye smugface:
        full
        slide_to (0.4, 0.6)
    h "I'll keep you safe there"
    show holly:
        full
        slide_to (0.3, 0.6)
    h "I'll protect you there"
    show holly:
        full
        slide_to (0.2, 0.6)
    show holly crazyeye smugface
    h "You can be the real Lily, Yuri, or [holly_nickname] there"
    h "My Lily"
    h "and We'll be together forever"
    play sound "audio/sfx/thunder.ogg" volume 0.75
    scene black
    pause 1.0
    jump kidnap_ending


label kidnap_ending:
    $ time_of_day = 'RAIN'
    play music "audio/ambience/heavy rain.ogg" fadein 3.0 volume 0.5
    pause 1.0
    scene bg abandoned house with eyeopen
    show lily pjbase pjl2 pjr1 frownface emptiness with dissolve:
        full
        left
    pause 2.0
    scene black with eyeclose_slow
    play sound "audio/sfx/breathe.ogg"
    pause 5.0
    scene bg abandoned house with eyeopen
    show lily pjbase pjl2 pjr2 frownface emptiness with dissolve:
        full
        left
    show holly d2base d2l2 d2r1 oface crazyeye with dissolve:
        full
        right
    stop sound
    h "Finally, you're aaaaaall miiiiiiiine now"
    h "We can live together forever now, just the two us"
    show holly d2base d2l2 d2r2 smilecface crazyeye:
        full
        slide_to (0.6, 0.5)
    h "You couldn't hide from your true self, so now I'm setting you free"
    h "I know deep down inside you also want this to happen..."
    show holly d2base d2l1 d2r2 smugface crazyeye:
        full
        slide_to (0.3, 0.5)
    h "DON'T YOU?"
    play sound "audio/sfx/thunder.ogg" volume 0.75
    scene black with eyeclose
    scene bg abandoned house with eyeopen
    show lily pjbase pjl2 pjr2 frownface emptiness with dissolve:
        medlong
        left
    show holly d2base d2l2 d2r2 smugface crazyeye with dissolve:
        medlong
        right
    h "Telling you the truth..."
    h "I didn't saw you by accident, right then"
    h "I followed you"
    show holly:
        medlong
        slide_to(0.75, 1.0)
    h "I know everything about you Lily"
    h "EVERYTHING"
    h "I know your past"
    h "Present"
    h "and future"
    show holly:
        medlong
        slide_to(0.5, 1.0)
    h "The world out there is cruel for people like you Lily"
    h "You can't even be the real you Yuri"
    h "But don't worry you're safe here with me"
    h "I don't care who you are anymore whethe it's Lily, Yuri, or [holly_nickname]"
    h "At the end"
    show holly:
        medlong
        slide_to(0.25, 1.0)
    h "YOU ARE MINE"
    h "Do you want to be with me forever?"
    menu together_forever:
        "Together 4 Ever?"
        "Yes":
            show holly:
                medlong
                slide_to(0.75, 1.0)
            h "Good"
            h "You don't have a choice anyways"
            h "HAHAHHAHAHAHHHHHHAHA"
            h "Lily"
            h "I love U"
            h "I love U"
            $ quick_menu = False
            window hide
            show screen infinite_iloveu
            pause 6.0
            stop music fadeout 1.0
            scene black with fade
            play music "audio/bgm/ending theme.ogg" fadein 1.0
            pause 2.0
            "Bad End"
            "Play the game again to reach all 3 endings"
            window hide
            hide screen infinite_iloveu
            show text "{font=gui/fonts/cmunorm.ttf}{size=120}Thank you for playing :>{/size}{/font}"
            pause 3.0
            show end_credits with dissolve
            pause
            "Check out more of our works at {a=https://x.com/CharlieDuckArt}{color=#1da1f2}Charlie Duck{/color}{/a}"
            "and at {a=https://chrisux.itch.io/}{color=#1da1f2}Chrisux{/color}{/a} for more games like this"
            scene black with dissolve
            pause 1.0
            $ renpy.full_restart()


label outted_ending:
    scene black with dissolve
    stop music fadeout 1.0
    pause 1.0

    play music "audio/ambience/morning_ambience.ogg" fadein 2.0
    scene bg bed top view with eyeopen_slow
    show lily pjbase pjl2 pjr1 neutraleye oface with dissolve:
        full
        center
    l "..."
    l "Hmmm..."
    l "I didn't have any weird dream tonight"
    l "and I woke up earlier today..."
    l "it's uncanny"
    play sound "audio/sfx/phone notification.ogg"
    show lily frownface
    l "It's Holly, what is she up to again"
    show lily pjlphone downeye:
        full
        slide_to(0.6, 0.5)
    h_nvl "Hello Yuri"
    h_nvl "I'm sorry I acted to abruptly"
    h_nvl "What I've done is a bit too far"
    h_nvl "I'm sorry 🥺🥺"
    h_nvl "Anyways enjoy your school year without me"
    h_nvl "I'm going back"
    h_nvl "I wish you well XW_YuriZ 😉"
    show lily thinkeye pjbase pjl1 pjr2:
        full
        slide_to(0.45, 0.5)
    l "She left just like that"
    l "Is everything going back to normal"
    show lily neutraleye smilecface
    l "I'm free"
    show lily smileoface
    l "Hahahahaha... Finally"
    l "Perhaps, I treated her too harshly"
    show lily smilecface
    play sound "audio/sfx/bus_horn.ogg"
    l "Commiinng"
    stop music fadeout 2.0
    show lily at fast_moveoutright
    scene black with wiperight_medium
    play sound "audio/sfx/running.ogg"
    stop sound
    pause 1.0
    jump outted_ending_2


label outted_ending_2:
    play sound "audio/sfx/bus stopping.ogg"
    pause 4.0
    scene black with wiperight
    pause 2.0
    stop sound
    scene bg classroom with dissolve
    play music "audio/ambience/classroom ambience.ogg" fadein 3.0 volume 0.75
    show lily unibase unil1 unir1 neutraleye noface at enter_from_left_to_center
    pause 1.0
    l "huh..."
    l "I guess I'm too early for class"
    play sound "audio/sfx/running.ogg"
    
    show school_girl_1 with dissolve:
        full
        slide_to (0.6, 1.0)
    show school_girl_2 with dissolve:
        full
        rightish
    show school_girl_3 with dissolve:
        full
        leftish
    show school_girl_4 with dissolve:
        full
        right
    show school_girl_5 with dissolve:
        full
        left
    stop music fadeout 1.0

    show school_girl_1 grimaceface at school_pop
    s1 "Oh there's the gay fag"
    show lily spookeye
    s1 "I can't believe I'm sitting next to her"
    s1 "Oh no will I catch her gay virus"

    play music "audio/bgm/hollys theme.ogg" fadein 1.0
    show school_girl_1 neutralface at school_idle
    show school_girl_2 oface at rightish, school_pop
    s2 "FREAAAAAAAAAAAK"
    s2 "Get away from me!"
    s2 "You don't desserve to be here"

    show school_girl_2 neutralface at rightish, school_idle
    show school_girl_3 smileoface at leftish, school_pop
    s3 "uccckkk... the air's poisoned with hey gay mist"
    s3 "Be careful"
    s3 "Can we vote to kick her out to this school"
    s3 "She's poisoning the air"

    show school_girl_3 at leftish, school_idle
    show school_girl_4 smileoface at right, school_pop
    s4 "I believe in all kinds of love"
    s4 "But not like that"
    s4 "Eeeeeeeew"

    show school_girl_4 at right, school_idle
    show school_girl_5 smileoface at left, school_pop
    s5 "I don't care what they all think"
    s5 "You have a sick username Lily"
    show school_girl_5 at left, school_idle
    t "LILYYYYYYYY!!"
    hide school_girl_1 with dissolve
    hide school_girl_2 with dissolve
    hide school_girl_3 with dissolve
    hide school_girl_4 with dissolve
    hide school_girl_5 with dissolve

    show teacher at enter_from_right_to_rightish
    l "Wha-what's happening. what did I do?"
    t "Or should I say WX_Yuri"
    l "huh? Ho-how did you"
    t "and here I thought your the quite, and well behaved one"
    t "I'm dissapointed"
    l "Wha-what did I do?"
    t "Explain this?"
    show screen object_viewer
    t "What kind of sickness is this"
    show lily scaredeye
    t "This is unaccepatable go to my office NOW!"
    l "Bu-bu-but... I--"
    t "Save your words later"
    t "People like you are the ones destroying the society"
    t "tssk"
    show teacher at slow_moveoutright
    pause 2.0
    stop music fadeout 2.0
    scene black with dissolve
    pause 1.0
    jump road_ending


label road_ending:
    $ time_of_day = 'RAIN'
    play music "audio/ambience/rainy road.ogg" fadein 1.0 volume 0.75
    pause 1.0
    scene bg rainy road with dissolve
    show lily unibase unil1 unir2 emptiness:
        full
        left
    l "I see..."
    l "So this is her goodbye"
    show lily:
        full
        slide_to (0.25, 1.0)
    l "I should've known better"
    l "Now everyone here knows about Yuri"
    l "They will never stop bullying me"
    l "Until they fixed me"
    l "Until I'm liked them"
    l "Until I turn straight"
    l "Maybe they're right..."
    show lily:
        full
        slide_to (0.45, 1.0)
    l "There's something wrong with me..."
    play sound "audio/sfx/truck horn.ogg" volume 0.5
    show screen white_out(duration=3.0) with whiteout_dissolve
    pause 1.0
    scene black with dissolve
    stop music fadeout 1.0
    stop sound
    pause 5.0
    play music "audio/bgm/ending theme.ogg" fadein 0.5
    pause 2.0
    "Bad end"
    "Play the game again to unlock all 3 endings"
    window hide
    show text "{font=gui/fonts/cmunorm.ttf}{size=120}Thank you for playing :>{/size}{/font}"
    pause 3.0
    show end_credits with dissolve
    pause
    "Check out more of our works at {a=https://x.com/CharlieDuckArt}{color=#1da1f2}Charlie Duck{/color}{/a}"
    "and at {a=https://chrisux.itch.io/}{color=#1da1f2}Chrisux{/color}{/a} for more games like this"
    scene black with dissolve
    pause 1.0
    $ renpy.full_restart()


label asylum_ending:
    scene black with dissolve
    play music "audio/ambience/asylum.ogg" fadein 1.0 volume 0.75
    scene bg mental asylum with fade

    show lily pjbase pjl2 pjr2 frownface emptiness with dissolve:
        full
        center

    l "How did I end up here?"
    l "Am I really a freak..."
    l "Am I really not normal..."
    l "What's wrong with me..."
    show lily grimacecface scaredeye:
        parallel:
            ease 0.5 medlong
        parallel:
            ease 0.5 center
    l "..."
    l "I just want to be myself..."
    l "Is it wrong to be me..."
    l "..."
    show lily grimaceoface cryeye
    l "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    camera at frantic_shake
    $ quick_menu = False
    window hide
    show screen infinite_scream
    pause 6.0
    stop music fadeout 1.0
    camera at shake_settle
    pause 1.0
    hide screen infinite_scream with dissolve
    pause 1.0
    scene black with fade
    play music "audio/bgm/ending theme.ogg" fadein 0.5
    pause 1.0
    "Bad end"
    "Play the game again to unlock all 3 endings"
    window hide
    show text "{font=gui/fonts/cmunorm.ttf}{size=120}Thank you for playing :>{/size}{/font}"
    pause 3.0
    show end_credits with dissolve
    pause
    "Check out more of our works at {a=https://x.com/CharlieDuckArt}{color=#1da1f2}Charlie Duck{/color}{/a}"
    "and at {a=https://chrisux.itch.io/}{color=#1da1f2}Chrisux{/color}{/a} for more games like this"
    scene black with dissolve
    pause 1.0
    $ renpy.full_restart()
