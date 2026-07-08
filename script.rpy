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
    h_unknown "I know deep down inside you also want this to happen…"
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
    show lily:
        center
    l "What a weird dream..."
    l "..."
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

    play sound "audio/sfx/bus start.ogg"
    l "OOOOUCCCCCHH!"
    l "I hate this morning already"
    stop sound
    play music "audio/ambience/road ambiance.ogg" fadein 2.0
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
    stop music fadeout 2.0
    play sound "audio/sfx/bus stopping.ogg"
    l "What does she mean by that..."
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
    stop music
    t "ermm..."
    t "Alright, alright everyone settle"
    t "for our first day of class..."
    t "for our first day of class, let’s get to know each other better and introduce ourselves, and and tell us what do you want to have for this year"
    show teacher at fast_moveoutright
    show school_girl_1 at enter_from_right_to_center
    pause 1.0
    s1 "Hellooo...."
    show school_girl_1 at fast_moveoutright
    show school_girl_2 at enter_from_right_to_center
    pause 1.0
    s2 "What's up..."
    show school_girl_2 at fast_moveoutright
    show school_girl_3 at enter_from_right_to_center
    pause 1.0
    s3 "...Rememeber my name..."
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
    t "alright that's it for our first day of class"
    t "Oh wait nevermind we have a new student she transfered from another city"
    show teacher at slow_moveoutleft

    show holly:
        full
        toleft
        enter_from_right_slow(0.5, 2.5)
    pause 3.0
    h "My name is... my name Holly and for this year I want to have..." 
    show holly:
        medlong
        center
    h "I WANT WX_YuriZ TO BE MINE, AND ONLY MINE!!!"
    show holly:
        medium
        center
    h "I LOVE YOU WX_YuriZ I'VE COME HERE JUST TO BE WITH YOU" 
    h "I FUCKING LOVE YOOOOOOOOOOOUUUUUUUUUU WX_YuriZ"
    show holly:
        full
        toleft
        ease 1.0 xpos 0.9
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
            h "Is that so?"
            h "Looks like my effort to get here are wasted how sad..."
        "N-n-no way are you holl–":
            $ renpy.notify("Holly's Affection 💖")
            l "I-is this reall..."
            l "N-n-no way are you holl–"
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
        easeout 1.0 xpos 1.5 xanchor 0.5
    t "What the hell is wrong with you! get out of this room and come to my office NOW! "
    show teacher:
        full
        fast_moveoutright
    s1 "What a weirdo, what is she even wearing"
    s2 "Oh God, what an entrance I hate her already"
    s3 "Her face makes me sick, I hope I’ll never get close to her for the whole year"
    s4 "Oh my, what a brave confession so romantic hihi"
    s5 "Uh... who’s WX_Yuri"
    s5 "Sick name!"
    l "Huh??? Who the is that girl? how does she know my name?" 
    l "If she's really her, then..."
    l "This is bad I can't let anyone know that name"
    l "what do I do?"
    menu holly_chase:
        "what do I do?"
        "Follow Holly":
            $ renpy.notify("Holly's Affection 💖")
            l "Is she really who am talking to?"
            l "I need to find out..."
            show lily at slow_moveoutright
            scene black with fade
            jump school_office_day_1
        "Ignore":
            $ renpy.notify("Holly's Affection 💔")
            l "She must be referring to someone"
            l "There's a lot of people named Yuri out there"
            l "Calm down, I will not get exposed today..."
            show lily at slow_moveoutright
            scene black with fade
            jump evening_day_1
            

label school_office_day_1:
    scene bg school office
    l "I'll do this later"


label evening_day_1:
    scene bg Lily bedroom with dissolve
    play music "audio/ambience/night ambiance.ogg" fadein 2.0

    show lily:
        full
        left
    l "*huff...* Is this for real? What is going on? could she really be h0lly_m0lly?"
    show lily:
        full
        ease 1.0 xpos 0.9
    l "Holy... Moly!"
    show lily:
        full
        ease 1.0 xpos 0.1
    l "No way.... No way... No way... this is bad"
    show lily:
        full
        ease 1.0 xpos 0.9
    l "She'll... she'll destroy my image in no time"
    show lily:
        full
        ease 1.0 xpos 0.1
    l "I can't live like that, what will I do?"
    play sound "audio/sfx/phone notification.ogg"
    show lily:
        full
        ease 1.0 xpos 0.7
    l "Is that her?"
    h_nvl "Good evening yuri, you looked so cute IRL <3"
    h_nvl "Why are you ignoring me?"
    h_nvl "Acting like you didn’t know me I thought we are friend"
    h_nvl "You haven’t answered my question earlier"
    h_nvl "Aren’t you happy to see me?"

    menu (nvl=True):
        "Are you really Holly?":
            $ renpy.notify("Holly's Affection 💖")
            l_nvl "Are you really Holly?"
            l_nvl "You must be joking right?"
            h_nvl "Yes I'am"
            h_nvl "you want me to shout your name again tomorrow"
            l_nvl "How can you do this?"
        "Why would you this?":
            $ renpy.notify("Holly's Affection 💔")
            l_nvl "Why would you this?"
            l_nvl "are you out of of your mind"
            l_nvl "We only knew each other online"
            l_nvl "How can you do this?"
            h_nvl "Are my feelings not enough to do this?"
    h_nvl "anyways... can you just anwer my question"
    h_nvl "are you happy to see me 🥺"
    menu (nvl=True):
        "No":
            $ renpy.notify("Holly's Affection 💔")
            l_nvl "are you serious?"
            l_nvl "no way"
            l_nvl "I'm more scared, than happy"
            h_nvl "HOW RUDE!!! "
            h_nvl "I'VE COME THIS WAY JUST FOR YOU"
            h_nvl "AND THIS IS HOW YOU'LL TREAT ME"
            l_nvl "I am scared that you'll justt"
            l_nvl "throw away my secrets"
            l_nvl "I won't let you destroy my image"
        "Yes":
            $ renpy.notify("Holly's Affection 💖")
            l_nvl "Yes"
            h_nvl "Awwwwwwwww"
            h_nvl "I'm happy to hear that, I'm gonna cry 🥺"
            h_nvl "I'm also very happy to finally see you IRL 💖"
            l_nvl "But not this way!!"
            l_nvl "I can't let you just"
            l_nvl "throw away my secrets"
            l_nvl "I won't let you do that"
    h_nvl "Too bad, it's too late for that now"
    l_nvl "What do you want anyway?"
    h_nvl "Why do you keep denying me, when I’ve come so far just to be with you :<"
    h_nvl "aren't we..."
    h_nvl "friends"
    l_nvl "We are friends, not like this"
    l_nvl "this is too far, I don't like this"
    h_nvl "what are you hiding anyways?"
    h_nvl "what are you afraid of?"
    h_nvl "Oh see... so that's how it is"
    h_nvl "I understand it now you're closeted, aren’t you?"
    h_nvl "With the way you act"
    h_nvl "the way you speak"
    h_nvl "nobody here knows the real you"
    h_nvl "right?"
    h_nvl "The lily I know the real Lily"
    l_nvl "stop it!"
    h_nvl "I know how much you hated this place"
    h_nvl "but don’t worry I’m here now I’ll save you"
    h_nvl "I wonder what will happen if everyone here will know"
    l_nvl "stop it!"
    l_nvl "stop it!"
    l_nvl "stop it!"
    menu (nvl=True):
        "Please stop this, I’ll do anything":
            $ renpy.notify("Holly's Affection 💖")
            l_nvl "please stop what you're about to do"
            l_nvl "I'll do anything"
        "Just tell me what you wan":
            $ renpy.notify("Holly's Affection 💖")
            l_nvl "Just tell me what you want"
            l_nvl "Just don't expose me"
            l_nvl "I'll do anything"
    h_nvl "GO OUT WITH ME"
    h_nvl "DO THE THINGS YOU SAID YOU WANT TO DO WITH ME" 
    h_nvl "BE THE REAL LILY WITH ME"
    l_nvl "I can’t believe you’re doing this, I thought you understand me"
    l_nvl "I thought we are friends"
    h_nvl "Yes I do, this is why I’m doing this! to save youuuuuuuu"
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
    show lily with dissolve
    l "Faaaaaaahh"
    l "If you are seeing this Can you edit a bit some of the text"
    l "Some of the dialogues are a bit too cheesy, unrealistic, and doesn't sound right"
    l "Here's a menu so you can just skip without returning to menu"
    menu optional_name:
        "Say Statement"
        "Choice 1":
            "fahhhhh"
        "Choice 2":
            "haaaahhh"
        