# Flags are here
default holly_affection = 0
default holly_nickname = "Lily"
default holly_refusal_count = 0
default push_holly_count = 0
default delete_text = 0
default kidnap_ending_flag = False
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

    show holly d2base d2l1 d2r2 oface crazyeye:
        full
        center

    stop sound
    h_unknown "Finally, you're aaaaaall miiiiiiiine now"
    h_unknown "We can live together forever now, just the two us"
    scene black with eyeclose
    scene bg abandoned house with eyeopen
    show holly d2base d2l1 d2r2 oface crazyeye:
        center_upper
        medlong
    h_unknown "You couldn't hide from your true self, so now I'm setting you free"
    h_unknown "I know deep down inside you also want this to happen..."
    scene black with eyeclose
    scene bg abandoned house with eyeopen
    show holly d2base d2l1 d2r2 oface crazyeye:
        center_upper
        medclose
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
    show lily unibase unil1 unir1 spookeye noface at slide_in_left, fall_and_recover(height=400, 
                                                        fall_time=0.5, 
                                                        ground_time=1.5, 
                                                        recover_time=0.6)
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
    pause 1.0
    show lily at slow_moveoutright
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
    show school_girl_1 smileo at enter_from_right_to_center
    pause 1.0
    s1 "Hellooo...."
    show school_girl_1 at fast_moveoutright
    show school_girl_2 neutralface at enter_from_right_to_center
    pause 1.0
    s2 "What's up..."
    show school_girl_2 at fast_moveoutright
    show school_girl_3 grimaceface at enter_from_right_to_center
    pause 1.0
    s3 "...Rememeber my name..."
    show school_girl_3 at fast_moveoutright
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
        toleft
        center
    h "I WANT WX_YuriZ TO BE MINE, AND ONLY MINE!!!"
    show holly smugface:
        medium
        toleft
        center
    h "I LOVE YOU WX_YuriZ I'VE COME HERE JUST TO BE WITH YOU" 
    h "I FUCKING LOVE YOOOOOOOOOOOUUUUUUUUUU WX_YuriZ"
    show holly:
        full
        toleft
        slide_to(0.9)
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
            $ renpy.notify("Holly's Affection 💔")
            l "Who-who are you talking to"
            l "There's no girl named WX_YuriZ"
            l "what a du-dumb name..."
            show holly annoyedeye frownface
            h "Is that so?"
            h "Looks like my effort to get here are wasted how sad..."
        "N-n-no way are you holl–":
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
    show holly:
        full
        toleft
        slide_off_right(1.0)
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
            $ renpy.notify("Holly's Affection 💖")
            l_nvl "Are you really Holly?"
            l_nvl "You must be joking right?"
            h_nvl "Yes I'am"
            h_nvl "you want me to shout your name again tomorrow"
            show lily grimacecface
            l_nvl "How can you do this?"
        "Why would you this?":
            $ renpy.notify("Holly's Affection 💔")
            show lily grimacecface
            l_nvl "Why would you this?"
            l_nvl "are you out of of your mind"
            l_nvl "We only knew each other online"
            l_nvl "How can you do this?"
            h_nvl "Are my feelings not enough to do this?"
    h_nvl "anyways... can you just anwer my question"
    h_nvl "are you happy to see me 🥺"
    show lily shyface
    menu (nvl=True):
        "No":
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
            $ renpy.notify("Holly's Affection 💖")
            l_nvl "please stop what you're about to do"
            l_nvl "I'll do anything"
        "Just tell me what you want":
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
    show lily grimacecface
    l_nvl "You really leave me no choice…"
    h_nvl "see you after school tomorrow hihi <3"
    h_nvl "Good night XOXO"
    nvl clear

    l "What did I set myself up to?"
    l "I’m so tired there’s a lot of things that happened today… I wish I could just escape"
    stop music fadeout 1.0
    scene black with eyeclose_slow
    pause 1.0
    jump lily_monologue


label lily_monologue:
    scene black
    play music "audio/ambience/playground.ogg" fadein 2.0 volume 0.75
    pause 1.0

    python:
        lily_lines = [
            "Lilly…",
            "What are you doing?",
            "Lily!",
            "stop doing that, you're not a boy!",
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
    show lily_here:
        full
        center
    l "what's happening to me?"
    l "all these weird dreams... I've had recently"
    l "wha-what do they mean?"
    l "please make it stop..."
    play sound "audio/sfx/phone notification.ogg"
    show lily_here at centerright with ease
    
    h_nvl "Good morning my Yuri (emojis)"
    l_nvl "gm"
    h_nvl "Why are you so cold to me Lily?"
    h_nvl "Oppsss I forgot you're my girlfriend now"
    h_nvl "Yippie"
    h_nvl "*sent GIF*"
    h_nvl "I should call you something else now"
    h_nvl "What do you like???"
    h_nvl "how about…"

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
            $ renpy.notify("Holly's Affection 💔")
            $ holly_affection -= 1
            $ holly_nickname = "Lovely Lily"
            l_nvl "No you don't just call me by my name"
            l_nvl "This is so cringe you know"
            l_nvl "I don't want any of this"
            l_nvl "I'm not yours just so you know"
            h_nvl "So you don't like any of it huh?"
            h_nvl "boriiiiiiiing…"
            h_nvl "I'll pick one for you, how about..."
            h_nvl "Lovely Lily"
            h_nvl "Isn't cute?"
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
    l "When will she stop"
    l "I can't take this anymore..."
    l "What is she planning to do?"
    l "I guess I need to play along for now"
    play sound "audio/sfx/bus_horn.ogg"
    l "Commiinng"
    stop music fadeout 2.0
    show lily_here at fast_moveoutright
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
    t "alright I hope all of you have already settled in, let's forget what happened yesterday and get along nicely, okay?"
    t "so for today we'll discuss poetry"
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
    t "alright I hope you enjoyed listening to that one"
    t "Now, let's talk about more about the poem, let's dive in deep into its meaning"
    t "Lily!"
    show lily_here:
        full
        toright
        enter_from_left_to_leftish(0.1, 1.5)
    show teacher:
        full
        toleft
        slide_to(0.9)
    t "What do you think the poem is meaning of the poem?"
    l "{i}uhhh...{/i}"
    menu poem_meaning:
        "What do you think is the meaning of the poem"
        "People changing":
            l "It is about..."
            l "Pe-people change over time..."
            l "The person you knew today might be completely different tommorrow"
            $ renpy.notify("Holly's Affection 💔")
        "Hiding your true identity":
            l "It is about..."
            l "hiding your tru-true identity to people"
            l "Giving them an illusion, but your not truly that person they thought you are..."
            $ renpy.notify("Holly's Affection 💖") 
        "Passion fading":
            l "I think the poem is about..."
            l "passion fading away"
            l "how something can be hot at first you know it but goes cold with time..."
            $ renpy.notify("Holly's Affection 💔")
        "I dont know":
            l "I-I'm sorry but I don't know..."
    
    t "Is that so?"
    t "very well, interesting interpretation..." 
    hide lily_here with dissolve
    show teacher:
        slide_to(0.5)
    t "Next!" 
    t "Holly"
    show holly_here:
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
    h "It means…"
    h "Loft bread are bland, and stale but my love for Yuri will never go pale"
    h "I love you everyday with no fail"
    h "Together our love will prevail"
    h "So let's go explore each other and sail"
    t "Wow, that’s beautiful a beautiful poem *sobs*"
    hide teacher with dissolve
    hide holly_here with dissolve

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
    s1 "Cringeeeeeeee, what is she talking about"

    show school_girl_1 at center, school_idle
    show school_girl_2 at rightish, school_pop
    s2 "Can someone stitch this bitch's mouth, I can't handle her anymore"

    show school_girl_2 at rightish, school_idle
    show school_girl_3 at leftish, school_pop
    s3 "Guys I have an idea so that she'll never come to school again, later this lunch let's…"

    show school_girl_3 at leftish, school_idle
    show school_girl_4 at right, school_pop
    s4 "wow what a romantic poem, I can feel your passion burning hot"

    show school_girl_4 at right, school_idle
    show school_girl_5 at left, school_pop
    s5 "Can somebody tell me who is Yuri already?"
    s5 "buy yeah, I don't like bread either but they're good with peanut butter hehe"
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

    show lily_here:
        full
        toright
        slide_to(0.9, 1.0)
    show holly_here:
        full
        toright
        enter_from_left_slow(0.1, 1.5)
    h "Lily! Don't forget about our deal later"
    menu deal_later:
        "deal later?"
        "What deal?":
            $ renpy.notify("Holly's Affection 💔") 
            l "wha-what deal?"
            l "I don' remember any?"
            h "Don't pretend you don't know, we have a deal right"
            h "you agreed we'll go out"
            l "ohh... date, a friendly date"
            h "alright"
        "Yeah, I won't":
            $ renpy.notify("Holly's Affection 💖") 
            l "yeah, I won't"
            l "we have a deal..."
            h "yeah, this is gonna be fun"
            h "our first date together!"
            h "yipppie"
    
    h "also let's have lunch together today"
    h "nothing wrong with that, just like normal girlfrie-"
    l "sto-stop it, not here please…"
    h "Fine, just eat lunch with me right now… or else..." 
    l "alright… alright… I’ll go…"
    h "Yippieeeeeeee let’s go [holly_nickname]"
    show holly_here at slow_moveoutright
    show lily_here at slow_moveoutright
    pause 1.5
    scene black with wipeleft

    jump school_cafeteria_day_2


label school_cafeteria_day_2:
    play music "audio/ambience/cafeteria.ogg" fadein 1.0 volume 0.5
    h "Come on Lily, let’s sit right there"
    scene bg cafeteria seat with wipeleft
    show holly_here with dissolve:
        full
        centerleft
    show lily_here with dissolve:
        full 
        centerright
    h "This food is awful! How can you eat this every day?"
    l "Yeah..."
    h "Who do you usually eat lunch with?"
    l "..."
    h "Huh? Do you mean..."
    l "..."
    h "Awwww, my poor Lily... *sobs*"
    h "Alone, cold, and lonely..."
    h "*sobs*"
    h "Don't worry, I'm here now. I'll never leave your side!"
    l "it's nothing"
    menu holly_pity:
        "What should I say?"
        "Thanks":
            $ renpy.notify("Holly's Affection 💖") 
            l "Tha-thanks for being here with me"
        "I don't need your sympathy":
            $ renpy.notify("Holly's Affection 💔")   
            l "I don't need your pity"
            l "I'm fine by my own anyways"
    h "Don't worry, I'm on your side. I completely understand you."
    h "I know what you want, what you need, what you think..."
    h "But how about me?"
    h "After all of our time together, do you know me?"
    menu holly_knowledge:
        "Do you know Holly?"
        "Yeah":
            $ renpy.notify("Holly's Affection 💖")
            l "Yeah, of course..."
            l "I know you best, I can read you easily"
        "No":
            $ renpy.notify("Holly's Affection 💔") 
            l "No, of course not"
            l "We haven't really spend much time together"
    
    h "Alrigh alright then..."
    h "Let's play a game."
    l "What game?"
    l "Can we just have lunch, please...?"
    h "It's not a big deal. Just guess what I'm thinking, and you win!"

    scene bg napkin with dissolve
    call hangman_minigame(word_list=["LILY"], category="What am I thinking?") from _call_hangman_cafeteria_day1

    scene bg cafeteria seat with dissolve
    show holly_here with dissolve:
        full
        centerleft
    show lily_here with dissolve:
        full 
        centerright

    if hangman_result == "win":
        $ renpy.notify("Holly's Affection 💖")
        l "L-Lily...? You were thinking about me?"
        h "Of course! what else am I going to think about"
        h "You actually know me well, I'm touched"
    else:
        h "Aw, out of guesses already? It was \"LILY\"!"
        l "that was a dumb game"
        l "why would you think about me..."
        h "You don't know me well huh?"
        h "It's ok [holly_nickname] we have time to get to know each other"
        $ renpy.notify("Holly's Affection 💔")
    
    h "alright your turn, let me guess what's on your mind"
    l "no... I don't want to play this game anymore"
    h "come on it's just a game..."
    h "oh... we already ran out of napkins, can you get some for me [holly_nickname] pleaseeee"

    menu holly_napkin_request:
        "I don't want to play your games":
            $ holly_refusal_count += 1

            if holly_refusal_count == 1:
                l "I don't want to play your games"
                l "Go get it yourself"
                h "Is this how you'll treat me!"
                h "AFTER ALL THE THINGS I'VE DONE FOR YOU"
                h "NO!"
            else:
                $ no_text = " ".join(["NO!"] * (2 ** (holly_refusal_count - 1)))
                h "Is this how you'll treat me!"
                h "AFTER ALL THE THINGS I'VE DONE FOR YOU"
                h "[no_text]"

            $ renpy.notify("Holly's Affection 💔")
            jump holly_napkin_request

        "alright I'll get it":
            $ renpy.notify("Holly's Affection 💖")
            l "alright, alright I'll get it"
            h "hehe that's my [holly_nickname]"
            show lily_here at slow_moveoutright
            scene black with wipeleft
            jump school_cafeteria_counter


label school_cafeteria_counter:
    scene bg cafeteria counter with wipeleft
    show lily_here at enter_from_left_to_center
    pause 3.0
    l "*huff..."
    l "Wha-what have I done...?"
    l "I just wanted to be me..."
    l "To express myself freely..."
    l "This is a disaster…"
    l "I can't let her near me…"
    l "I-I don't feel safe…"
    l "I can't let her expose me, and out me…"
    l "If anybody here finds out about that side of me, I..."
    l "No, no, no, no, no, no..."
    l "I can't let that happen..."
    l "I am dead. I am dead. I am dead."
    l "I won't let that happen. I won't let her..."
    l "If I'm anywhere but here, I'll be doomed."
    l "this should be enough"
    l "I'm heading back"
    show lily_here at slow_moveoutleft
    scene black with wiperight
    jump school_cafeteria_day_2_bully_scene


label school_cafeteria_day_2_bully_scene:
    scene bg cafeteria seat with wiperight
    show school_girl_1 with dissolve:
        full
        centerright
    show school_girl_2 with dissolve:
        full
        rightish
    show school_girl_3 with dissolve:
        full
        right
    show holly_here with dissolve:
        full
        leftish

    s1 "What are you doing here, weirdo?"
    h "It's none of your business."
    s2 "This is our table, bitch!"
    s3 "If you want this table, then have it all to yourself!"

    play sound "audio/sfx/slime.ogg"
    # TODO: swap to Holly's dirty-uniform attribute once you tell me its name
    show holly_here at leftish, bump(-30)

    s1 "Hahahahah, gotcha!"
    s2 "Good one, hahaha!"
    s3 "That'll teach her."

    l "Oh god... what'll I do?"

    menu holly_bullied:
        "What will you do?"

        "Protect holly":
            show lily_here at enter_from_right_to_center
            l "Tha-thats enough!"
            s1 "oh there's two weirdos now"
            s2 "what will you do if we won't hahahhaha"
            s3 "boring come on now guys this is no longer fun"
            $ renpy.notify("Holly's Affection 💖") 
            show school_girl_1 at slow_moveoutright
            show school_girl_2 at slow_moveoutright
            show school_girl_3 at slow_moveoutright
            stop music fadeout 1.0
            l "are you alright"
            h "Yeah they're nothing"
            h "thank you"
            l "it's nothing you would've done the same right?"
            h "thank you"
            l "here's the napkin"
            h "it's fine forget it"
            h "..."
            h "Don't forget about later"
            l "yeah.. I won't"
            scene black with dissolve
            hide lily_here  with dissolve
            hide holly_here with dissolve
            jump date_intro

        "Pretend nothing happen":
            show school_girl_1 at slow_moveoutright
            show school_girl_2 at slow_moveoutright
            show school_girl_3 at slow_moveoutright
            show lily_here at enter_from_right_to_center
            stop music fadeout 1.0
            l "..."
            l "Here's your napkins..."
            $ renpy.notify("Holly's Affection 💔")
            h "Thank you..."
            h "Don't forget about later"
            h "Afters school"
            l "yea-yeah, I won't"
            stop music
            show lily at slow_moveoutright
            scene black with dissolve
            jump date_intro


label date_intro:
    play music "audio/ambience/rural night.ogg" volume 0.75
    scene bg park with dissolve

    show holly_here:
        full
        rightish
    with dissolve

    h "When is she coming"
    play sound "audio/sfx/walk on grass.ogg"
    show lily_here at enter_from_left_to_leftish
    stop sound

    h "..."
    h "Ohhh... there you are"
    h "Hellooooo [holly_nickname] you look cuter today"
    l "hello…"
    h "Why are you wearing that?"
    l "it's what everyone wears"
    h "That's not the Lily I knew"

    show holly_here:
        full
        toright
        slide_to(0.4, 0.8)
    h "Hear wear this"
    play sound "audio/sfx/clothes give.ogg" volume 0.5
    show holly_here:
        full
        toright
        slide_to(0.75, 0.8)
    pause 1.0
    h "change your clothes I want to date the Lily I know"

    scene black with dissolve
    scene bg park with dissolve

    show holly_here with dissolve:
        full
        rightish
    show lily_here at enter_from_left_to_leftish

    l "are you happy now?"
    h "Now that's the Lily I know"
    l "what do you plan"
    h "anywhere where you want to go"
    h "I'll let you decide, I'm happy wherever you want my [holly_nickname]"

    menu date_option:
        "Where do you want to go?"
        "Somewhere quite":
            $ renpy.notify("Holly's Affection 💖") 
            l "Take me to somewhere quite"
            l "Where nobody can see me... can see me like this"
            h "Your wish is granted [holly_nickname]"
            show holly_here at slow_moveoutright
            show lily_here at slow_moveoutright
            stop music
            
            scene black with wiperight
            jump abandoned_house_date_1
        "Some Cozy":
            $ renpy.notify("Holly's Affection 💖") 
            l "Take me to somewhere cozy"
            l "I want to be somewhere safe..."
            h "Perfect I know a place [holly_nickname]"
            show holly_here at slow_moveoutleft
            show lily_here at slow_moveoutleft
            stop music
            scene black with wipeleft
            jump restaurant_date


label restaurant_date:
    scene bg restaurant with wipeleft
    play music "audio/ambience/restaurant.ogg" volume 0.5 fadein 3.0
    
    show holly_here with dissolve:
        full
        rightish
    show lily_here with dissolve:
        full
        leftish
    
    h "Good choice [holly_nickname], I knew you have a great taste"
    l "Where even are we?"
    h "somewhere cozy, like you said"
    l "I haven't been here before, I'm not sure… am I safe with you here…"
    h "Don't worry, I'll make sure you're safe with me, I'll protect you with my life."
    h "How about we get to know each other, this is our first date after all"
    show holly_here:
        parallel:
            ease 0.5 medlong
        parallel:
            ease 0.5 rightish

    show lily_here:
        parallel:
            ease 0.5 medlong
        parallel:
            ease 0.5 leftish
    l "okay…"
    h "Do you have any hobbies?"

    menu hobby_choice_quite:
        "Do you have any hobbies?"

        "Yes":
            l "yeah... I have some"
            h "me too I also have some hobbies"

        "No":
            l "N-n-no, I don't have one"
            h "me too I also don't have any hobby"

    h "Hmmm... how about"
    h "What's your favourite color?"
    $ fav_color = renpy.input("What's your favorite color?").strip()
    if fav_color == "":
        $ fav_color = "lilac"
    l "I like [fav_color]"
    h "Ohh what a coincidence I also love [fav_color]"
    h "I can't believe it we're so similar haahahhahahahahah"

    h "Hmmm… What did you want to be when you grew up?"
    $ childhood_dream = renpy.input("What did you want to be when you grew up?").strip()
    if childhood_dream == "":
        $ childhood_dream = "Police"
    l "I want to be a [childhood_dream]"
    h "whaaaaaat!! me too! I also want to be a [childhood_dream]"
    h "We are really the same, I feel like I found my soulmate hehehe"

    h "Your turn ask me anything you want…"
    l "..."
    l "Whe-when will you stop this?"
    h "stop this?"
    stop music fadeout 1.0
    h "but [holly_nickname] we just got started"
    play music "audio/bgm/hollys theme.ogg" volume 0.4 fadein 3.0

    show holly_here:
        medlong
        toleft
        slide_to(0.6, 0.8)
    h "You wanted this didn't you"

    show holly_here:
        medlong
        toleft
        slide_to(0.5, 0.8)
    h "You told me before you wanted to do this"

    show holly_here:
        medlong
        toleft
        slide_to(0.4, 0.8)
    h "YOU TOLD ME YOU WANTED TO DO THIS!"

    l "da-da-the Lily you met and knew online, and the Lily you're with right now are different"
    l "a-a-I can't do this…"
    menu holly_pressure:
        "What do I do?"
        "Run away":
            l "I'm sorry I can't do this"
            show lily_here:
                bump (-40)
                medlong
                leftish
            h "No, not this time you can't run away from me here"
            h "Why are you doing this?"
            h "I though we are friends"
            h "What's wrong with you"
            l "I-is this what friends do?"
            l "please leave me alone"
            show holly_here:
                parallel:
                    ease 0.5 full
                parallel:
                    ease 0.5 right

            show lily_here:
                parallel:
                    ease 0.5 full
                parallel:
                    ease 0.5 left
            h "But you told me you want to do this"
            h "have something like this"
            h "experience something like this"
            l "you don't understand leave me alone"
            show lily_here at fast_moveoutleft
            scene black with wiperight
            jump abandoned_house_date_3
        "Push Holly":
            show holly_here:
                medlong
                toright
                slide_to(0.8, 0.8)
            l "get away from me..."
            h "Why are you doing this?"
            h "What's wrong with you"
            l "I am just doing it like everybody here does"
            l "a-am I doing it wrong"
            h "Why are you doing this to me"
            show holly_here:
                medlong
                toright
                slide_to(0.6, 0.8)
            h "Where's the Lily I know"
            l "..."
            show holly_here:
                medlong
                toright
                slide_to(0.4, 0.8)
            h "WHERE IS SHE?"
            t "erm... Ahem!"
            show teacher:
                full
                right
            
            show lily_here:
                parallel:
                    ease 0.5 full
                parallel:
                    ease 0.5 left

            show holly_here:
                parallel:
                    ease 0.5 full
                parallel:
                    ease 0.5 leftish
            
            t "What the hell are you two doing here, at this time of day or night"
            t "and why are you two so close to each other, uck!"
            l "i-its not what you think it's jus--"
            h "YES IT'S WHAT YOU THINK TEACH"
            h "ME AND HOLLY ARE ABOUT TO HOOK UP"
            h "ME AND HOLLY ARE MADLY IN LOVE WITH EACH OTHER"
            h "Is there anything wrong with that teach?"
            t "what the hell"
            h "I don't care what you think"
            h "YURI IS MINE!"
            t "what the--"
            t "ughhhh..."
            stop music fadeout 1.0
            t "You don't know what you are doing"
            t "You don't have an idea what you are doing"
            t "This is so wrong"
            t "You two are not normal..."
            t "and I will fix that"
            t "You two are coming with me!"
            t "It's for the best for both of you..."
            t "Security!"
            scene black with dissolve
            jump asylum_ending                 
        

label abandoned_house_date_1:
    $ time_of_day = "SILVERMOON"
    scene bg abandoned house with wiperight
    play music "audio/ambience/rural night.ogg" volume 0.5 fadein 2.0
    
    show holly_here with dissolve:
        full
        rightish
    show lily_here with dissolve:
        full
        leftish
    
    h "Good choice [holly_nickname], I knew you have a great taste"
    l "Where even are we?"
    h "somewhere quite, like you said"
    l "I haven't been here before, I'm not sure… am I safe with you here…"
    h "Don't worry, I'll make sure you're safe with me, I'll protect you with my life."
    h "How about we get to know each other, this is our first date after all"
    show holly_here:
        parallel:
            ease 0.5 medlong
        parallel:
            ease 0.5 rightish

    show lily_here:
        parallel:
            ease 0.5 medlong
        parallel:
            ease 0.5 leftish
    l "okay…"
    h "Do you have any hobbies?"

    menu hobby_choice:
        "Do you have any hobbies?"

        "Yes":
            l "yeah... I have some"
            h "me too I also have some hobbies"

        "No":
            l "N-n-no, I don't have one"
            h "me too I also don't have any hobby"

    h "Hmmm... how about"
    h "What's your favourite color?"
    $ fav_color = renpy.input("What's your favorite color?").strip()
    if fav_color == "":
        $ fav_color = "lilac"
    l "I like [fav_color]"
    h "Ohh what a coincidence I also love [fav_color]"
    h "I can't believe it we're so similar haahahhahahahahah"

    h "Hmmm… What did you want to be when you grew up?"
    $ childhood_dream = renpy.input("What did you want to be when you grew up?").strip()
    if childhood_dream == "":
        $ childhood_dream = "Police"
    l "I want to be a [childhood_dream]"
    h "whaaaaaat!! me too! I also want to be a [childhood_dream]"
    h "We are really the same, I feel like I found my soulmate hehehe"

    h "Your turn ask me anything you want…"
    l "..."
    l "Whe-when will you stop this?"
    h "stop this?"
    stop music fadeout 1.0
    h "but [holly_nickname] we just got started"
    play music "audio/bgm/hollys theme.ogg" volume 0.4 fadein 3.0

    show holly_here:
        medlong
        toleft
        slide_to(0.6, 0.8)
    h "You wanted this didn't you"

    show holly_here:
        medlong
        toleft
        slide_to(0.5, 0.8)
    h "You told me before you wanted to do this"

    show holly_here:
        medlong
        toleft
        slide_to(0.4, 0.8)
    h "YOU TOLD ME YOU WANTED TO DO THIS!"

    l "da-da-the Lily you met and knew online, and the Lily you're with right now are different"
    l "a-a-I can't do this…"
    menu holly_pressure_quite_1:
        "I can't do this..."
        "Run away":
            if push_holly_count == 0:
                show holly_here:
                    parallel:
                        ease 0.5 full
                    parallel:
                        ease 0.5 right

                show lily_here:
                    parallel:
                        ease 0.5 full
                    parallel:
                        ease 0.5 left
                l "I'm sorry I can't do this"
                show lily_here at fast_moveoutleft
                scene black with wiperight
                jump abandoned_house_date_2
            else: 
                l "Stop followin me!"
                l "please..."
                show lily_here at fast_moveoutleft
                scene black with wiperight
                jump abandoned_house_date_3


        "Push holly":
            $ push_holly_count += 1
            show holly_here:
                medlong
                toright
                slide_to(0.9, 0.8)

            if push_holly_count == 1:
                l "ge-get away from me..."
                show holly_here:
                    parallel:
                        ease 0.5 full
                    parallel:
                        ease 0.5 right

                show lily_here:
                    parallel:
                        ease 0.5 full
                    parallel:
                        ease 0.5 left
                h "Lily!"
                h "Why are you doing this?"
                h "I thought we were friends…"
                h "*sobs*"
                h "WAAAAAAAAAAAAAAAAAAAAAH!!!"
                l "I know… I know we were friends"
                l "bu-bu-but I"
                h "Why are you doing this to me?"
                h "Why are you like this?"
                h "What's wrong with you?"
                l "wha-what do you mean?"
                l "I'm just acting, like how we are supposed to act"
                h "Why can't you be like the Lily I knew, and the way you are supposed to act"
                h "You want to do something like this right"
                show holly_here:
                    full
                    toleft
                    slide_to(0.7, 1.0)
                h "Right?"

                show holly_here:
                    full
                    toleft
                    slide_to(0.4, 0.8)
                h "Right…"

                show holly_here:
                    full
                    toleft
                    slide_to(0.3, 0.6)
                h "RIGHT!"
                jump holly_pressure_quite_1
            else:
                show holly_here:
                    parallel:
                        ease 0.5 full
                    parallel:
                        ease 0.5 right
                l "Stop!"
                l "I don't feel safe around you"
                l "ca-can we stop this…"
                l "get away from me please"
                h "You told me you want to be closer with me…"

                show holly_here:
                    full
                    toleft
                    slide_to(0.7, 0.8)
                h "spend time with me…"

                show holly_here:
                    full
                    toleft
                    slide_to(0.4, 0.6)
                h "do things with me…"

                show holly_here:
                    full
                    toleft
                    slide_to(0.3, 0.5)
                h "BE CLOSER TO ME!"

                stop music fadeout 2.0
                l "I can't be seen doing like this here, if only you understand you'd knew"
                l "a-a-I'll be dead if I'm seen doing anything like this"
                h "..."
                show holly_here:
                    full
                    toleft
                    slide_to(0.6, 0.8)
                l "I'll be dead…"
                h "what do you mean?"
                l "I need to act like how am I supposed to act, not like a freak, not like a disgrace"
                h "what abo--"
                l "I can't be gay"
                h "..."
                l "It's already, can we just go home already…"
                h "yeah right… right..."
                h "Let's just go home now, we're still friends right?"
                l "yes of course…"
                scene black with fade
                jump evening_day_2


label abandoned_house_date_2:
    $ time_of_day = "DAY"
    scene bg outside abandoned house with wiperight

    show lily_here with dissolve:
        full
        left
    show holly_here with dissolve:
        full
        right

    h "Lily!"
    h "Why are you doing this?"
    h "I thought we were friends…"
    h "*sobs*"
    h "WAAAAAAAAAAAAAAAAAAAAAH!!!"
    l "I know… I know we were friends"
    l "bu-bu-but I"
    h "Why are you doing this to me?"
    h "Why are you like this?"
    h "What's wrong with you?"
    l "wha-what do you mean?"
    l "I'm just acting, like how we are supposed to act"
    h "Why can't you be like the Lily I knew, and the way you are supposed to act"
    h "You want to do something like this right"

    show holly_here:
        full
        toleft
        slide_to(0.7, 1.0)
    h "Right?"

    show holly_here:
        full
        toleft
        slide_to(0.4, 0.8)
    h "Right…"

    show holly_here:
        full
        toleft
        slide_to(0.3, 0.6)
    h "RIGHT!"
    menu holly_pressure_quite_2:
        "RIGHT!"
        "Run away":
            l "Stop followin me!"
            l "please"
            show lily_here at fast_moveoutleft
            scene black with wiperight
            jump abandoned_house_date_3

        "Push Holly":
            show holly_here:
                full
                toright
                slide_to(0.9, 0.8)
            l "Stop!"
            l "I don't feel safe around you"

            l "ca-can we stop this…"
            l "get away from me please"

            show holly_here:
                full
                toleft
                slide_to(0.5, 1.0)
            h "You told me you want to be closer with me…"

            show holly_here:
                full
                toleft
                slide_to(0.4, 0.8)
            h "spend time with me…"

            show holly_here:
                full
                toleft
                slide_to(0.3, 0.6)
            h "do things with me…"

            show holly_here:
                full
                toleft
                slide_to(0.2, 0.5)
            h "BE CLOSER TO ME!"

            stop music fadeout 2.0
            l "I can't be seen doing like this here, if only you understand you'd knew"
            l "a-a-I'll be dead if I'm seen doing anything like this"
            show holly_here:
                full
                toleft
                slide_to(0.6, 0.8)
            h "..."
            l "I'll be dead…"
            h "what do you mean?"
            l "I need to act like how am I supposed to act, not like a freak, not like a disgrace"
            h "what abo--"
            l "I can't be gay"
            h "..."
            l "It's already late, can we just go home already…"
            h "yeah right… right..."
            h "Let's just go home now, we're still friends right?"
            l "yes of course…"
            scene black with fade
            jump evening_day_2


label abandoned_house_date_3:
    scene bg tunnel with wiperight

    show lily_here with dissolve:
        full
        left
    show holly_here with dissolve:
        full
        right

    l "Stop!"
    l "I don't feel safe around you"

    l "ca-can we stop this…"
    l "get away from me please"

    show holly_here:
        full
        toleft
        slide_to(0.5, 1.0)
    h "You told me you want to be closer with me…"

    show holly_here:
        full
        toleft
        slide_to(0.4, 0.8)
    h "spend time with me…"

    show holly_here:
        full
        toleft
        slide_to(0.3, 0.6)
    h "do things with me…"

    show holly_here:
        full
        toleft
        slide_to(0.2, 0.5)
    h "BE CLOSER TO ME!"

    stop music fadeout 2.0
    l "I can't be seen doing like this here, if only you understand you'd knew"
    l "a-a-I'll be dead if I'm seen doing anything like this"
    show holly_here:
        full
        toleft
        slide_to(0.6, 0.8)
    h "..."
    l "I'll be dead…"
    h "what do you mean?"
    l "I need to act like how am I supposed to act, not like a freak, not like a disgrace"
    h "what abo--"
    l "I can't be gay"
    h "..."
    l "It's already, can we just go home already…"
    h "yeah right… right..."
    h "Let's just go home now, we're still friends right?"
    l "yes of course…"
    scene black with fade
    jump evening_day_2


label evening_day_2:
    $ time_of_day = "DAY"

    scene bg lily bedroom with dissolve
    play music "audio/ambience/night ambiance.ogg" fadein 2.0

    show lily_here with dissolve:
        full
        centerright

    l "I don't feel so good…"
    l "There's something wrong"
    l "No. everything's going wrong"

    play sound "audio/sfx/phone notification.ogg"
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
            $ renpy.notify("Holly's Affection 💖")

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
            l_nvl "I'll come talk to you tommorow"
            l_nvl "please delete this"

    nvl clear
    l "What is she planning with those pirctures"
    l "If those pictures comes out then..."
    stop music fadeout 1.0
    l "No no no no no no no no no no"
    scene black with eyeclose_slow
    jump lily_monologue_day_2


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
            "she's so rebellious",
            "she doesn't know who she is",
            "she acts so masculine",
            "she speaks so strong",
            "she likes other girls",
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
            "alright leave it up to me",
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
    show lily_here:
        full 
        center
    
    l "Another weird dream huh?"
    l "when will this stop?"
    l "What are those dreams even about?"
    show lily_here at centerright with ease
    play sound "audio/sfx/phone notification.ogg"

    h_nvl "Good morning [holly_nickname]"
    h_nvl "I hoped you slept well"
    h_nvl "Don't worry about the pictures. I just took them cuz they're just cute"
    h_nvl "I won't share them or anything"
    h_nvl "I understand you now"
    h_nvl "I'll keep you safe at your closet just as you like"
    h_nvl "see you later [holly_nickname]"

    l "Oh thank God"
    l "I hope I can trust her…"
    l "We are good friends on the internet"
    l "She helped me understand myself"
    l "after all... maybe… we might just have a little misunderstanding"
    l "she might not be really that bad at all"

    play sound "audio/sfx/bus_horn.ogg"
    l "uhhh... yeah... I still have school today"
    stop music fadeout 2.0
    show lily_here at fast_moveoutright
    l "cooommiiiing"
    scene black with wiperight_medium
    play sound "audio/sfx/running.ogg"
    pause 2.0

    jump bus_scene_day_3


label bus_scene_day_3:
    scene bg bus interior with wiperight
    show lily_here at enter_from_left_to_center

    play sound "audio/sfx/bus start.ogg"
    # SHOW: Picture of rural Southeast Asian country (Scene 1)
    l "This town is old, and rusty."
    l "I forgot the exact reason why I hated it."

    stop sound
    play music "audio/ambience/road ambiance.ogg" fadein 2.0
    # SHOW: Picture of rural Southeast Asian country (Scene 2)
    l "I just have this feeling ever since."
    l "Why can't I be me here? What am I scared of?"
    l "I don't remember…"
    l "I just know that if I don't act exactly as expected, something bad will happen…"
    l "Something out of a nightmare."
    l "Something that maybe I'd like to forget."
    l "I wonder if I leave this place, I'll be free from that feeling."
    # SHOW: Picture of a lily flower
    
    l "At least for now, I still feel safe online sharing who I really am."
    l "One day I'll come out of my closet and kiss a girl in front of everyone…"
    l "But not right now... She's just making things much harder for me."
    stop music fadeout 2.0
    l "I wish all of this would just end soon…"
    pause 1.0
    show lily_here at slow_moveoutright
    stop sound
    scene black with wiperight
    hide lily_here
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
    t "Good morning"
    t "For today, we're going to learn about plants, and flowers"
    t "Who here likes flowers?"
    s5 "oh me! I like it when you mix it with water, and yeast then heat it for a while it's really good"
    t "Thank you for your answer, but I'm talking about F-l-o-w-e-r flowers not F-l-o-u-r flour"
    t "let's move on... I have a question for you guys "
    t "does anybody here knows what flower symbolises innocence and rebirth"
    t "Lily!"
    t "What do you think is the answer"
    show lily_here:
        full
        toright
        enter_from_left_to_leftish(0.1, 1.5)
    show teacher:
        full
        toleft
        slide_to(0.9)
    l "{i}uhhh...{/i}"
    menu flower_meaning:
        "what flower symbolises innocence and rebirth"
        "Cosmos":
            l "Hmmm... Cosmos"
            t "Study harder, that's incorrect"
            $ renpy.notify("Holly's Affection 💔")
        "Daffodil":
            l "Uhhh... Daffodils?"
            t "Nice try but, that's not correct"
            $ renpy.notify("Holly's Affection 💖") 
        "Lily":
            l "I think the poem is about..."
            t "Very good correct!"
            $ renpy.notify("Holly's Affection 💖") 
        "I dont know":
            l "I don't know..."
            t "It's alright"
            t "I should've expected less from you"
            $ renpy.notify("Holly's Affection 💔")
    hide lily_here with dissolve
    show teacher:
        slide_to(0.5)
    t "The flower that symbolizes innocence and rebirth are Lilies "
    t "In Christian art Virgin Mary is usually depicted being given Lilies by Angel Gabriel."
    t "That's why lilies are usually used at weddings representing new beginnings,
    and at funerals which symbolizes the innocence of the soul after death." 
    t "alright moving on"
    show holly_here:
        full
        toright
        enter_from_left_to_leftish(0.1, 1.5)
    h "{i}hooooaaaaaah{/i}"
    t "Yes, holly!"
    h "huh? what did I do?"
    hide holly_here with dissolve
    t "No, I mean the flower is holly"
    t "Hollies are known for their bright red winter berries, symbolizing the holiday season"
    t "They are dioecious, meaning each bush or tree is strictly male or female"
    t "Now did you know that lilies, and hollies cannot grow together"
    t "Hollies grow into large, dense, woody shrubs or trees"
    t "They cast a deep shadow over lower-growing plants, starving sun-loving flowers like lilies and killing them"
    stop music
    play sound "audio/sfx/school bell.ogg"
    t "Before you leave, for your assignment this weekend I want you to take a sample of your favourite flower"
    t "Give it a brieft description, of what it is, what does it likes, and how to take care of it, submit it to me next week alright"
    t "Alright class dismissed"
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
    s1 "I can't believe that bitch Holly is still here I guess we haven't done enough"
    s1 "I won't survive a year in this class with her"

    show school_girl_1 at center, school_idle
    show school_girl_2 at rightish, school_pop
    s2 "I have a tea, so yesterday after class I have seen her with..."
    s2 "Two of them is too disgusting for me to handle"

    show school_girl_2 at rightish, school_idle
    show school_girl_3 at leftish, school_pop
    s3 "I see... but let's see what will happen next before doing something"

    show school_girl_3 at leftish, school_idle
    show school_girl_4 at right, school_pop
    s4 "He loves me, he loves me not, uh flowers symbol of love so romantic"

    show school_girl_4 at right, school_idle
    show school_girl_5 at left, school_pop
    s5 "Uhhhh..."
    s5 "What's the difference between flours, and flours aren't they the same"
    show school_girl_5 at left, school_idle

    play sound "audio/sfx/running.ogg"
    show school_girl_1 at slow_moveoutright
    show school_girl_2 at slow_moveoutright
    show school_girl_3 at slow_moveoutright
    show school_girl_4 at slow_moveoutright
    show school_girl_5 at slow_moveoutright
    pause 2.0

    show lily_here:
        full
        toright
        slide_to(0.9, 1.0)
    show holly_here:
        full
        toright
        enter_from_left_slow(0.1, 1.5)
    pause 1.0
    h "Lily, let’s take lunch together again today"
    h "Just as friends, just as you like, and want"
    h "We’re friends aren’t we?"
    menu lunch_day_2:
        "We're friends aren't we?"
        "Ignore":
            l "..."
            h "I’ll take that as a yes."
            l "Bu-bu-but I haven’t said anything…"            
            h "Don’t worry, I know how to act now."
            h "It’s just a casual friends' lunch, not a big deal."
        "Go with Holly":
            l "alright it's just a lunch anyways"
            h "Yaaaay! Let’s go!"
            h "I brought some food."
            l "You won't pull any of those games right?"
            h "Don’t worry, I know how to act now."
            h "It’s just a casual friends' lunch, not a big deal"
    show holly_here at slow_moveoutright
    show lily_here at slow_moveoutright
    scene black with wipeleft
    jump school_cafeteria_day_3


label school_cafeteria_day_3:
    play music "audio/ambience/cafeteria.ogg" fadein 1.0 volume 0.5
    h "That table occupied I guess, let's sit right here"
    scene bg cafeteria new seats with wipeleft

    show lily_here:
        full
        leftish
    show holly_here:
        full
        rightish
    with dissolve

    h "Here, have some of this."
    l "Thanks."
    h "You're welcome! Is it good?"
    l "It's better than what we usually have here at school."
    h "Ahahahhahahaha!"
    h "Yeah, the food here sucks."
    l "I know, hahahhahaha."
    h "I'm sorry about how I've acted these past few days."
    h "I didn't know your situation."
    l "It's fine... you're new here, so you had no idea about it."
    l "I also didn't mean to push you far away and paint you as an evil person."
    l "It's fine, we could still be friends…"

    show lily_here:
        full
        leftish
        bump(-40)
    play sound "audio/sfx/slime.ogg"
    l "Oh, shit, shit... my clothes!"
    l "What do I do?"
    l "How am I supposed to fix this…?"
    h "Calm down [holly_nickname]— I mean, Lily"
    h "I brought extra clothes. You can borrow them"

    show lily_here at slow_moveoutleft
    scene black with dissolve
    scene bg cafeteria new seats with dissolve

    show holly_here:
        full
        rightish
    with dissolve
    pause 1.0

    show lily_here at enter_from_left_to_leftish
    h "what is taking her so long"
    h "Tha-that fits you so well... *blushes*"
    l "This feels so uncomfortable."
    l "How can you wear this every day?"
    l "It feels like I'm sticking out too much right now."
    l "I feel like everyone's eyes are on me."

    show school_girl_1 at enter_from_right_to_rightish
    show school_girl_2 at enter_from_right_slow(0.9, 1.0)
    show school_girl_3 at enter_from_right_slow(0.5, 1.3)

    show lily_here:
        full
        toright
        slide_to(0.1, 0.8)
    show holly_here:
        full
        toright
        slide_to(0.25, 0.8)

    s1 "We are, indeed."
    s2 "What are you wearing... freak?"
    s3 "It looks so shit on you, haha!"
    s1 "Thank God the weirdos are now grouped together. It's easier to pick on you two."
    s2 "You look like such an eyesore. Get out of my sight now!"
    h "CUT IT!"
    h "I can tolerate your bullshit when it at me..."
    show holly_here:
        bump (-60)
        full
        toleft
    h "BUT NOT WITH LILYYYYYYYYYYYY!"

    show holly_here:
        bump (-40)
        full
        toleft
        slide_to(1.5, 0.6)
    show school_girl_1 at fast_moveoutright
    show school_girl_2 at fast_moveoutright
    show school_girl_3 at fast_moveoutright
    pause 1.0
    scene black with dissolve
    pause 1.0
    scene bg cafeteria new seats with dissolve

    show lily_here:
        full
        leftish
    with dissolve
    l "Is she gonna be ok"
    l "Did I treat her to harshly? Why is she still protecting me"
    show holly_here at enter_from_right_to_rightish
    l "Holly... you're here"
    h "yeah"
    l "Tha-thanks"
    l "It's my first time getting picked by them"
    l "I-it's scary…"
    h "It's alright, I'm here."
    h "Let's go shopping for some new clothes"
    h "It seems like the stains on your old clothes are really bad. I doubt you can wear them again."
    l "Re-really?"
    stop music fadeout 1.0
    l "Sounds like a good idea."
    l "Thank God you're here. I would have panicked if this happened to me alone hahahaha"
    h "yeah, let's go"
    scene black with dissolve
    jump shopping_date


label shopping_date:
    play music "audio/ambience/mall.ogg" fadein 2.0 volume 0.75
    l "I hope nobody sees us here"
    scene bg mall with dissolve
    pause 1.0
    show holly_here with dissolve:
        full
        rightish
    show lily_here with dissolve:
        full
        leftish

    l "If somebody sees us like this, we're surely dead"
    h "It's ok this is just friends doing errands right?"
    l "yeah right…"
    l "let's go hurry, the women's section should be at the second floor"
    h "boriiiiing… tomorrow's weekend anyways, let's have some fun"
    h "I've never seen you dressed like you told me you wanted to"
    h "Have you ever dressed like the way you wanted to?"
    l "n-no… I can't… Why would I?"
    h "give it a shot, it's not really a big deal"
    l "but I'm really here for to get replacement for my uniform"
    h "we can do that after, come on we have time"
    h "Alright, then decide what you want?"

    menu shopping_date_choice:
        "Alright, then decide what you want?"
        "Don't go with Holly":
            l "I'll just buy replacement for my uniform"
            l "I dont really need to go anywhere"
            l "I don't need to change my clothings"
            h "ah…"
            h "AAAAAAAAAAAAAAHHHHHHH!!!"
            h "ARE YOU SERIOUS"
            h "THEN WHY MAKE ME GO WITH YOU?"
            l "But yo-you're the one who insist to go here with me"
            h "hahahahaahaha"
            h "Yeah, right… right…"
            h "I didn't mean anything I said"
            h "I'll go now myself, have fun shopping"
            l "yeah… take care"
            l "You didn't take any photos this time, did you?"
            h "… ye-yeah"
            show holly_here at fast_moveoutright
            l "Thanks for coming alo—"
            l "long"
            l "..."
            show lily_here at slow_moveoutleft
            scene black with wipeleft
            jump women_section

        "Go with Holly":
            $ holly_affection += 4
            l "yeah your're right yeah have some time"
            l "we could shop around for a bit and try out stuff"
            h "Yippie!"
            h "I know you want to try it out don't you?"
            h "I really knew you better than anyone"
            l "I'm not really uncomfortable with my clothes..."
            h "don't worry it won't take too much time"
            h "we could get your uniform later"
            l "yeah"
            h "let's go"
            show holly_here at slow_moveoutright
            show lily_here at slow_moveoutright
            scene black with wiperight
            jump men_section


label women_section:
    scene bg women section with wipeleft
    show lily_here at enter_from_right_to_center
    l "Hmmm..."
    show lily_here:
        full
        slide_to(0.8)
    l "I don't have enough money for this one... hehe"
    show lily_here:
        full
        slide_to(0.1)
    l "This one's cheaper"
    l "I'll buy this"
    show lily_here at slide_off_right
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

    show holly_here:
        full
        rightish
    show lily_here:
        full
        leftish
    with dissolve

    h "let me pick clothes for you"
    h "I mean Lily"
    h "I think this will fit you well"
    show holly_here:
        full
        slide_to(0.9)
    h "and this"
    show holly_here:
        full
        slide_to(0.1)
    h "and this"
    show holly_here:
        full
        slide_to(0.75)
    l "Isn't this a bit too much"
    l "It's my first time trying this stuff"
    h "Don't worry I'm sure it'll fit you well Yur--"
    h "I mean Lily, hurry and try it out I'll wait for you"
    l "This is so embarrassing, I hope no one will see us"
    l "If someone noticed me wearing this then..."
    l "I'll be dead I'll be dead I'll be dead"
    show lily_here at fast_moveoutleft
    scene black with dissolve
    scene bg men section with dissolve

    show holly_here with dissolve:
        full
        rightish

    show lily_here at enter_from_left_to_leftish
    pause 1.0
    l "hello"
    l "I guess this is not too bad after all..."
    h "..."
    h "ah"
    h "AAAAAAAAAAAHHHHH"
    h "OMG OMG OMG OMG"
    h "it fits you so well, you're just like the Lily I imagined, the Lily I knew"
    h "THE REAL LILYYYYY"
    h "My [holly_nickname] Lily"
    l "o-ok calm down stop it or people would notice us"
    l "This feels so weird..."
    l "We're standing out too much... we're not acting like other people"
    l "Oh god... Oh god... I'm gonna get exposed this way"
    h "Don't worry I won't let that happen"
    l "Let's hurry and buy the things I actually need please!"
    l "I-I can't have anybody see me like this"
    l "If anyone notices me and out me..."
    l "I'll be... dead..."
    h "Don't worry no one will notice you"
    h "You look like a totally new different person"
    h "But..."

    show holly_here:
        full
        toleft
        slide_to(0.7, 1.0)
    h "It feels good doesn't it?"

    show holly_here:
        full
        toleft
        slide_to(0.6, 0.8)
    h "To let out the real you"
    h "Not the Lily of this town, but the Lily I want, and I'll have"

    show holly_here:
        full
        toleft
        slide_to(0.4, 0.6)
    h "One day it'll all come out but you'll have me"
    h "AND I'LL HAVE YO-"

    show school_girl_5 at enter_from_right_to_rightish
    s5 "Oh what a coincidence if it isn't Holly, and Lily"
    s5 "Hellooooooo, it's nice meeting you around here hehe"
    s5 "Hmmmm... what are you two doing here?"
    s5 "It's rare to see Lily around with anyone"
    s5 "You two seems supeeeeer close with each other"
    s5 "Ohh I see how it is, you two are..."

    menu shopping_date_s5_choice:
        "Ohh I see how it is, you two are..."

        "Deny":
            show lily_here:
                full
                slide_to (0.1, 0.3)
            l "No-no-no-no it's not what you're thinking…"
            l "We're ju-"
            s5 "Huh? you two are not role playing as undercover cop and a criminal"
            s5 "Aawww too bad I would love to join"
            h "Uh man You blew up my cover now she knows that I'm the criminal... game's over"
            s5 "ooppsss hehe, my bad"
            show school_girl_5 at slow_moveoutright
            l "That was a close one..."
            h "see I got this"
            h "I can save you"
            h "I just saved you"
            l "Let's just go home..."
            l "That's enough for today, I don't want to wear this again"
            l "I can't let anybody see me like this again"
            h "yeah right"
            l "I'm just gonna buy the things the I need now"
            scene black with dissolve
            stop music fadeout 1.0
            pause 1.0
            play sound "audio/sfx/cash register.ogg"
            c "That would be 1000"
            c "Thank you for shopping, come again soon!"
            jump evening_day_3

        "Run away":
            show lily_here at fast_moveoutleft
            show holly_here at fast_moveoutleft
            s5 "Hey wait!"
            s5 "You guys are role playing as undercover cop, and criminal right! I wanna join"
            s5 "awwww... there's next time I guess"
            jump men_section_getaway


label men_section_getaway:
    scene black with wipeleft
    scene bg women section with wipeleft
    show holly_here at enter_from_right_to_rightish
    show lily_here at enter_from_right_to_center
    show lily_here:
        full
        slide_to (0.3, 1.6)

    l "*huff* *huff* *huff*"
    l "I can no longer go on like this"
    l "Oh God... Oh God... I wonder what is she thinking"
    l "does she knew about our relationship"
    h "But we're just friends right?"
    h "I bet she's just thinking we're just playing some game"
    h "Don't worry about it"
    h "I'll talk to her, and explain. Go buy your things Lily"
    show holly_here at fast_moveoutright
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

    show lily_here with dissolve:
        full
        center
    
    l "What a long day…"
    l "A lot of things happened…"
    l "Holly seems to have changed."
    l "Did I judge her too quickly?"
    l "No no no... she doesn't undestand it"
    l "I'm just protecting myself..."
    l "But I'm glad she's trying her best to understand this place"
    l "She still didn't text me tonight"
    l "Is there something wrong?"
    l "Should I text her?"
    menu text_Holly_tonight:
        "Should I text her?"
        "Text Holly":
            $ renpy.notify("Holly's Affection 💖")
            show lily_here:
                full
                slide_to (0.7, 0.9)
            l_nvl "Helloooo H0lly"
            l_nvl "Are you awake"
            l "No replies huh"
        "Sleep":
            $ renpy.notify("Holly's Affection 💔") 
            l "Nevermind"
            l "She must be tired as well"
            l "I'll just sleep"
    l "But she was really helpful to me today, and she didn't put me on any drama"
    l "Am I wrong about her?"
    l "Is her drama over now"
    l "Hahahahahaha, I was worried about nothing…"
    l "I hope I won’t get any more of those weird dreams."
    l "What was all that about, anyways… Is it because of what happened lately?"
    l "I’m so tired…"
    l "I think I'm fallin aslee-"

    stop music fadeout 1.0
    scene black with eyeclose_slow
    pause 1.0
    jump lily_monologue_day_3


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
    show lily_here:
        full
        center
    l "..."
    l "I remember now."
    l "..."
    l "The-these are no-not my dreams..."
    l "..."
    stop music
    l "The-they are my me-me-memories..."
    l "What the fuck!"
    l "What the fuck!"
    l "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    camera at frantic_shake
    $ quick_menu = False
    window hide
    scene white with dissolve
    pause 2.0
    scene bg classroom with dissolve
    pause 2.0
    scene bg cafeteria counter with dissolve
    pause 2.0
    scene bg mall with dissolve
    pause 2.0
    scene black with dissolve
    show screen infinite_scream
    pause 12.0
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

    show lily_here with dissolve:
        full
        left
    l "AH"
    l "..."
    pause 4.0
    show holly_here at enter_from_right_to_rightish
    h "Lily?"
    h "What are you doing here?"
    l "..."
    h "Are you ok?"
    h "You'll get sick if you stay here"
    l "..."
    play sound "audio/sfx/dry thunder.ogg"
    h "It looks like it's going to rain hard"
    h "Don't worry I've got a nice place for you to hide"
    show holly_here:
        full
        slide_to (0.6, 0.6)
    h "I'll keep you safe there"
    show holly_here:
        full
        slide_to (0.4, 0.6)
    h "I'll protect you there"
    show holly_here:
        full
        slide_to (0.2, 0.6)
    h "You can be the real Lily, Yuri, or [holly_nickname] there"
    h "My Lily"
    h "and We'll be together forever"
    play sound "audio/sfx/thunder.ogg" volume 0.75
    scene black
    jump kidnap_ending


label kidnap_ending:
    $ time_of_day = 'RAIN'
    play music "audio/ambience/heavy rain.ogg" fadein 3.0 volume 0.5
    pause 1.0
    scene bg abandoned house with eyeopen
    show lily_here with dissolve:
        full
        left
    pause 2.0
    scene black with eyeclose_slow
    play sound "audio/sfx/breathe.ogg"
    pause 5.0
    scene bg abandoned house with eyeopen
    show holly_here with dissolve:
        full
        right
    stop sound
    h "Finally, you're aaaaaall miiiiiiiine now"
    h "We can live together forever now, just the two us"
    show holly_here with dissolve:
        full
        slide_to (0.6, 0.5)
    h "You couldn't hide from your true self, so now I'm setting you free"
    h "I know deep down inside you also want this to happen..."
    show holly_here with dissolve:
        full
        slide_to (0.3, 0.5)
    h "DON'T YOU?"
    play sound "audio/sfx/thunder.ogg" volume 0.75
    scene black with eyeclose
    scene bg abandoned house with eyeopen
    show lily_here with dissolve:
        medlong
        left
    show holly_here with dissolve:
        medlong
        right
    h "Telling you the truth..."
    h "I didn't saw you by accident, right then"
    h "I followed you"
    show holly_here:
        medlong
        slide_to(0.75, 1.0)
    h "I know everything about you Lily"
    h "EVERYTHING"
    h "I know your past"
    h "Present"
    h "and future"
    show holly_here:
        medlong
        slide_to(0.5, 1.0)
    h "The world out there is cruel for people like you Lily"
    h "You can't even be the real you Yuri"
    h "But don't worry you're safe here with me"
    h "I don't care who you are anymore whethe it's Lily, Yuri, or [holly_nickname]"
    h "At the end"
    show holly_here:
        medlong
        slide_to(0.25, 1.0)
    h "YOU ARE MINE"
    h "Do you want to be with me forever?"
    menu together_forever:
        "Together 4 Ever?"
        "Yes":
            show holly_here:
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
            play music "audio/bgm/ending theme.ogg" fadein 0.5
            pause 1.0
            show text "{font=cmunorm.ttf}{size=60}Thank you for playing :>{/size}{/font}" with dissolve
            pause 3.0
            show end_credits with dissolve
            pause
            $ renpy.full_restart()


label outted_ending:
    scene bg bed top view
    l "a"


label asylum_ending:
    scene black with dissolve
    play music "audio/ambience/asylum.ogg" fadein 1.0 volume 0.75
    scene bg mental asylum with fade

    show lily_here with dissolve:
        full
        center

    l "How did I end up here?"
    l "Am I really a freak..."
    l "Am I really not normal..."
    l "What's wrong with me..."
    l "..."
    l "I just want to be myself..."
    l "Is it wrong to be me..."
    l "..."

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
    show text "{font=cmunorm.ttf}{size=60}Thank you for playing :>{/size}{/font}" with dissolve
    pause 3.0
    show end_credits with dissolve
    pause
    $ renpy.full_restart()
