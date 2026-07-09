# Flags are here
default holly_affection = 0
default holly_nickname = "Lily"
default holly_refusal_count = 0
# Use like h "lets go [holly_nickname]"


# NVL characters are used for the phone texting
define l_nvl = Character("WX_YuriZ", kind=nvl, image="lily", callback=Phone_SendSound)
define h_nvl = Character("h0lly_m0lly", kind=nvl, image="holly", callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)


# this is yet another test

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
    show lily_here:
        full
        center
    l "What a weird dream..."
    l "..."
    l "Oh shit shit shit… what time is it?"
    play sound "audio/sfx/bus_horn.ogg"
    l "I’m gonna be late"
    stop music fadeout 2.0
    show lily_here at fast_moveoutright
    scene black with wiperight_medium
    play sound "audio/sfx/running.ogg"
    l "Comiiiiing!"
    pause 2.0

    jump bus_scene_day_1


label bus_scene_day_1:
    scene bg bus interior with wiperight
    show lily_here at slide_in_left, fall_and_recover(height=400, 
                                                        fall_time=0.5, 
                                                        ground_time=1.5, 
                                                        recover_time=0.6)
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
    show lily_here at centerright with ease
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
    show lily_here at slow_moveoutright
    stop sound
    scene black with wiperight
    hide lily_here
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
    show lily_here at enter_from_left_to_center
    l "huhhh..."
    l "what are they talking about"
    hide lily_here with dissolve
    show teacher at slide_in_right
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

    show lily_here at enter_from_right_to_center
    pause 2.0
    l "He-hello everyone my name is Li-lily..."
    l "a-and I hope for this year I can get to know you all better and make memories together."
    show lily_here at fast_moveoutright
    pause 1.0
    show teacher at slow_enter_from_left_to_center
    pause 1.5
    t "alright that's it for our first day of class"
    t "Oh wait nevermind we have a new student she transfered from another city"
    show teacher at slow_moveoutleft

    show holly_here:
        full
        toleft
        enter_from_right_slow(0.5, 2.5)
    pause 3.0
    h "My name is... my name Holly and for this year I want to have..." 
    show holly_here:
        medlong
        toleft
        center
    h "I WANT WX_YuriZ TO BE MINE, AND ONLY MINE!!!"
    show holly_here:
        medium
        toleft
        center
    h "I LOVE YOU WX_YuriZ I'VE COME HERE JUST TO BE WITH YOU" 
    h "I FUCKING LOVE YOOOOOOOOOOOUUUUUUUUUU WX_YuriZ"
    show holly_here:
        full
        toleft
        slide_to(0.9)
    show lily_here:
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
    show holly_here:
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
            show lily_here at slow_moveoutright
            scene black with fade
            jump school_office_day_1
        "Ignore":
            $ renpy.notify("Holly's Affection 💔")
            l "She must be referring to someone"
            l "There's a lot of people named Yuri out there"
            l "Calm down, I will not get exposed today..."
            show lily_here at slow_moveoutright
            scene black with fade
            jump evening_day_1
            

label school_office_day_1:
    scene bg school office
    l "I'll do this later"


label evening_day_1:
    scene bg Lily bedroom with dissolve
    play music "audio/ambience/night ambiance.ogg" fadein 2.0

    show lily_here:
        full
        left
    l "*huff...* Is this for real? What is going on? could she really be h0lly_m0lly?"
    show lily_here:
        full
        slide_to(0.9)
    l "Holy... Moly!"
    show lily_here:
        full
        slide_to(0.1)
    l "No way.... No way... No way... this is bad"
    show lily_here:
        full
        slide_to(0.9)
    l "She'll... she'll destroy my image in no time"
    show lily_here:
        full
        slide_to(0.1)
    l "I can't live like that, what will I do?"
    play sound "audio/sfx/phone notification.ogg"
    show lily_here:
        full
        slide_to(0.7)
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
    show lily_here at slow_moveoutleft
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
    play sound "audio/sfx/running.ogg"
    show school_girl_2 at slow_moveoutright
    play sound "audio/sfx/running.ogg"
    show school_girl_3 at slow_moveoutright
    play sound "audio/sfx/running.ogg"
    show school_girl_4 at slow_moveoutright
    play sound "audio/sfx/running.ogg"
    show school_girl_5 at slow_moveoutright
    
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

    jump school_cafeteria_day_1


label school_cafeteria_day_1:
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
    jump school_cafeteria_day_1_bully_scene


label school_cafeteria_day_1_bully_scene:
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
    scene bg park with dissolve

    show holly_here with dissolve:
        full
        rightish
    h "When she coming"
    show lily_here at slow_enter_from_left_to_center
    h "Ohhh... there you are"
    h "Hellooooo [holly_nickname] you look cuter today"
    l "hello…"
    h "Why are you wearing that?"
    h "That's not the Lily I knew"
    h "Hear wear this"

    scene bg black with fade
    scene bg park with dissolve

    show holly_here with dissolve:
        full
        rightish
    show lily_here at slow_enter_from_left_to_center

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
            show holly_here with slow_moveoutright
            show lily_here with slow_moveoutright
            scene black with wipeleft
            jump abandoned_house_date_1
        "Some Cozy":
            $ renpy.notify("Holly's Affection 💖") 
            l "Take me to somewhere cozy"
            l "I want to be somewhere safe..."
            h "Perfect I know a place [holly_nickname]"
            show holly_here with slow_moveoutleft
            show lily_here with slow_moveoutleft
            scene black with wiperight
            jump restaurant_date


label restaurant_date:
    scene bg restaurant with wiperight
    l "fuck"


label abandoned_house_date_1:
    scene bg abandoned house with wipeleft

    

label outted_ending:
    scene bg bed top view
    l "a"
