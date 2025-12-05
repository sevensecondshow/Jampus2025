
define mc = Character('Tin', color="#c8ffc8", image="tin")
define n = Character('???', color="#c8ffc8")
define kw = Character('Kwiyer', color="#F1F794", image="kw")
define nx = Character('Nixon', color="#544B13", image ="nixon")
define kd = Character('KD Pantz', color="#EB8FE6")
define h = Character('Herscheles', color="#6E90FF")

image screen0 = "introscreen_ph.png"
image screen1 = "boat_placeholder.png"
image ship_screen_center = "shipscreen_center.png"
image ship_screen_left = "shipscreen_left.png"
image ship_screen_right = "shipscreen_right.png"

default Day_01_kd_Conversation = False
default Day_01_Kwiyer_Conversation = False
default Day_01_Nixon_Conversation = False
default Quest_KD = False
default Quest_NX = False
default Quest_KW = False

label start:
    $ trust_points = 50
    $ union_ending_points = 0
    $ nixon_ending_points = 0
    $ kd_ending_points = 0

    scene screen0

    #call screen frame_text()
    show screen frame_text

    screen frame_text:
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            # add Solid ("#520303")
            # xsize 600
            # ysize 200
            # xoffset 690
            # yoffset 440
            text "DAYS UNTIL DECISION: 14"
            # hbox:
            #     textbutton "DAYS UNTIL DECISION: 14" action Jump(intro01)
            #     ypos 0.5
            #     xpos 0.15

    pause 5
    hide screen frame_text

    #n "our home, the north pole, has melted all away over the course of a short, rapid hundred years."
    #n "our boss, santa, has held onto a dream of dry land for the whole of humanity."
    #n "we are elves, on his grand sleigh on the seas, the Last Hope."
    #n "the lights flicker, as it has been doing for the past few months. our fuel supplies are low, see."
    #n "as sea levels continue to rise, it’s harder to find fuel- and freshwater."
    #n "we’re a crew, now 39. One of our coworkers has been missing for some time… it’s our duty to find out what happened."
    n """
    our home, the north pole, has melted all away over the course of a short, rapid hundred years.

    our boss, santa, has held onto a dream of dry land for the whole of humanity.

    we are elves, on his grand sleigh on the seas, the Last Hope.

    the lights flicker, as it has been doing for the past few months. our fuel supplies are low, see.

    as sea levels continue to rise, it’s harder to find fuel- and freshwater.

    we’re a crew, now 39. One of our coworkers has been missing for some time… it’s our duty to find out what happened.
    """


menu:
    "you keep saying this. i’m not sure we’re getting any closer":
        jump negative01
    "we’ll get there.":
        jump positive01

label negative01:
    $ trust_points -= 1
    scene screen1
    with fade

    mc sad "come on, at least let me be a little edgy if we’re at the end of the world."
    jump intro_02


label positive01:
    $ trust_points += 1

    scene screen1
    with fade

    mc neutral "you think so? that’s… kind of you, thanks"
    jump intro_02

label intro_02:

    mc neutral "i hear it’s starting to get pretty close to the draw."
    mc "union wants to nix santa and nixon wants to spy on the union."
    mc "this is starting to get a bit too much, we still haven’t even found out what happened to jeffany."
    mc "we completely run out of power in 14 days. after that, we’re at the mercy of the world. what do you think?"

menu:
    "we should talk to the union.":
        jump positive02
    "we should wiretap the union.":
        jump negative02

label positive02:
    $ trust_points += 1
    mc neutral "you’re right, maybe it’s time we got more involved. anything they’ve got has to be better than this, right?"
    jump intro_03

label negative02:
    $ trust_points -= 1
    mc surprised "oh- wow, i.. really? you’d take nixon’s deal?"
    mc "maybe let's change the subject."
    jump intro_03

label intro_03:

    if trust_points >= 5:

        mc neutral "you’re the only person i can lean on."
        mc "no matter what happens, you’re my partner for whatever that means these days."
        mc "5999 people left on earth, and you’re the only person i can trust."
        jump intro_04

    if trust_points <= 4:

        mc angry "you’re the only person i can lean on."
        mc "no matter what happens, you’re my partner for whatever that means these days."
        mc "..."
        mc "5999 people left on earth, and you’re the only person i can trust."
        jump intro_04
        
label intro_04:
    mc neutral "our shift is starting soon,"

## SHIFT START: GALLEY 

label shift_start_galley:
    mc neutral "mic check, one two, one two, you read me?"

menu:
    "yes.":
        jump shift_start_galley_02

label shift_start_galley_02:
    mc "perfect. what's in store for us?"
    mc "the only thing we really have to do is handle the shipment from the Entire Nation of Switzerland and I'd like to talk to at least 2 people about jeffany's disappearance."
    # tutorial dialogue
    mc "{i}When you want to send me somewhere else, cycle through your cameras and press 'enter' to direct me. {/i}"
    mc "{i} click on items or people if you want me to investigate, i'll be listening for your input.{/i}"

menu:
    "bridge":
        jump day_01_bridge
    "engine room":
        jump day_01_engineroom
    "factory cam 1":
        jump day_01_factorycam01
    "deck 3, hallway 4":
        jump day_01_deckthree
    "deck 2, stern":
        jump day_01_stern
    "galley":
        jump day_01_galley


label day_01_bridge:
    mc "that's off limits right now. let's try somewhere else?"
    jump day_01_center


label day_01_engineroom:
    mc "i don't have the keys, maybe some other time."
    jump day_01_center


label day_01_factorycam01:
    $ Day_01_Kwiyer_Conversation = False
    mc sad "if we must.."
    mc angry "the factory smells unpleasant as always. i'm not sure how much longer i can stand to inhale plastic fumes like this."
    kw smile "Hiya, Tin! Merry day, I think. What are you up to?"

menu:
    "Can you remind us when you last saw Jeffany?":
        jump day_01_center
        # still needs filling out
    "We might want to get involved with the Union.":
        jump day_01_factorycam01_kwiyer01

label day_01_factorycam01_kwiyer01:
    kw smile "Oh!!"
    kw "Of course! Yes! Thank you!"
    kw "We have nightly meetings in the galley, most nights we're just chatting but every so often we've got some business to discuss."
    kw neutral "Honestly, I'm surprised they're still honoring the contract.."
    kw "Um, to an extent."
    kw sad "The only thing is… We're so few now, and some people are on the fence. Would you be able to talk to them about coming to a meeting?"

menu:
    "We can do that.":
        jump positive_factorycam01
    "On second thought, that sounds a bit out of our depth.":
        jump negative_factorycam01

label positive_factorycam01:
    kw "Perfect, thank you so much! If you ever see the following people, could you bring it up? "
    $ trust_points += 1
    # Get Item: Employee List
    $ Day_01_Kwiyer_Conversation = True
    $ Quest_KW = True
    jump day_01_center

label negative_factorycam01:
    kw "Oh! Sure, yeah, no worries. Thanks for the interest! I hope we see you at the meeting.."
    $ trust_points -= 1
    $ Day_01_Kwiyer_Conversation = True
    jump day_01_center



label day_01_deckthree:
    $ Day_01_Nixon_Conversation = False
    mc angry "I forgot how loud the lights are here."
    nx "Oh, Tin, perfect! Just who I wanted to see. Have you given any thought to the offer?"

menu:
    "Can you remind us what that was?":
        jump day_01_deckthree_nixon_01
    "Let's talk about it.":
        jump day_01_deckthree_nixon_02

label day_01_deckthree_nixon_01:
    nx "Well, sure!"
    nx "We're worried that The Union is skewing people's perspectives on things. We run the jolliest ship in the whole world!"
    nx "The world's Last Hope for Christmas cheer!"
    nx "And The UNION wants to take it away from everyone. We can't have that, can we?"

label day_01_deckthree_nixon_02:
    nx "So, what will it be?"

menu:
    "We'll wear the bug.":
        jump day_01_deckthree_nixon_03
    "We wont do it.":
        jump day_01_deckthree_nixon_04

label day_01_deckthree_nixon_03:
    nx "Excellent. Sit as close as possible to the staff rep."
    $ trust_points -= 10
    # Get Item: Bug
    $ Day_01_Nixon_Conversation = True
    $ Quest_NX = True
    jump day_01_center

label day_01_deckthree_nixon_04:
    nx "If you change your mind.. You know how to find me."
    $ trust_points += 1
    $ Day_01_Nixon_Conversation = True
    jump day_01_center


label day_01_stern:
    $ Day_01_kd_Conversation = False
    mc "it's as good a day as any, i guess. at least the ocean breeze is nice, we still have that."
    mc "it looks like KD Pantz is here if we want to talk to him"
    kd "Tin Foyle you wonderful elf, you! How are you and your partner-in-security doing?"
    kd "Do you see the beautiful nation of Switzerland still hard at work while everything's gone under? How admirable!"
    kd "Not very chatty if you ask me, but I'm here to take care of obligations!"
    kd "Unlike SOME people on the bridge,"
    kd "but I digress!"

menu:
    "Did you handle the shipment?":
        jump day_01_stern_kd_01
    "What are you doing out here?":
        jump day_01_stern_kd_02

label day_01_stern_kd_01:
    kd "Yes, in fact I did! Taking initiative as always, of course, for the good of the ship since darling, dear, big boss Claus is ever so busy designing toys for the factory."
    kd "Oh, with that much free time I don't know what I'd do!"
    $ Day_01_kd_Conversation = True
    jump day_01_center

label day_01_stern_kd_02:
    kd "Oh, you know, just enjoying the sweet, salt air and schem-" 
    kd "planning, of course, planning and thinking and organizing, et cetra!"
    kd "You know, if I was in charge I think we could really turn this boat around! In fact, would you be willing to sign and share this petition?"

menu:
    "Sign, but decline to share.":
        jump day_01_stern_kd_03
    "Yeah, anything's better than this, why not? Sign and share.":
        jump day_01_stern_kd_04
    "Decline entirely.":
        jump day_01_stern_kd_05

label day_01_stern_kd_03:
    # FILL OUT
    kd "oh"
    $ Day_01_kd_Conversation = True
    jump day_01_center

label day_01_stern_kd_04:
    kd "I knew I could count on you two! Talk to me next week, about it, yeah? We've got big stuff coming!"
    $ Day_01_kd_Conversation = True
    $ Quest_KD = True
    jump day_01_center

label day_01_stern_kd_05:
    # FILL OUT
    kd "oh"
    $ Day_01_kd_Conversation = True
    jump day_01_center




label day_01_galley:
    if Day_01_kd_Conversation == True:
        mc "yum! let's go"       
    elif Day_01_Kwiyer_Conversation == True:
        mc "yum! let's go"
    elif Day_01_Nixon_Conversation == True:
        mc "yum! let's go"
    else:
    # if no
        mc "i wanna check in with a leader first."

    mc "Oh! Herscheles is here. They were pretty close to Jeffany.. I don't think we should bring it up.."
    mc "But... I'll trust you to make the right choice."
    h "...."
    h "Oh, Foyle.. and friend, I assume. What's up?"

    if Quest_KD == True:
        menu:
            "Talk about the Union.":
                jump day_01_galley_herc_01
            # if kd quest ->
            "What do you think about management?":
                jump day_01_galley_herc_02
            "Bring up Jeffany.":
                jump day_01_galley_herc_03
    else:
        menu:
            "Talk about the Union.":
                jump day_01_galley_herc_01
            "Bring up Jeffany.":
                jump day_01_galley_herc_03       


label day_01_galley_herc_01:
    h "Ah, yeah, them… I dunno, what's the point in having a union anymore when we live in an apocalypse?"

    if Quest_KW == True and Quest_NX == True:
        menu:
            "(neutral) You're right. Disregard.": 
                $ trust_points -= 1
            # trust roll check
                jump day_01_galley_herc_04
            # if union quest ->
            "There's a meeting tonight and they want people's input.": #(no change to trust)
                jump day_01_center
            # if nixon quest ->
            "You're right, you might want to talk to Nixon.":
            # trust roll check
                jump day_01_center
    elif Quest_KW == True and Quest_NX == False: # if only Quest_KW is true
        menu:
            "(neutral) You're right. Disregard.":
                $ trust_points -= 1
            # trust roll check
                jump day_01_galley_herc_04
            # if union quest ->
            "There's a meeting tonight and they want people's input.": #(no change to trust)
                jump day_01_center
    elif Quest_KW == False and Quest_NX == True:
        menu:
            "(neutral) You're right. Disregard.":
                $ trust_points -= 1
            # trust roll check
                jump day_01_galley_herc_04
            # if nixon quest ->
            "You're right, you might want to talk to Nixon.":
            # trust roll check
                jump day_01_center
    else: # QuestKW and QuestNX are False
        menu:
            "(neutral) You're right. Disregard.": 
                $ trust_points -= 1
            # trust roll check
                jump day_01_galley_herc_04




label day_01_galley_herc_02:
    h "They're not my favorite in the world."
    # FILL OUT CONTINUE
    jump day_01_center

label day_01_galley_herc_03:
    # TRUST ROLL CHECK
    jump day_01_center

label day_01_galley_herc_04:
    # if trust roll success
    h "Uhuh... Anything else?"
    # if trust roll fail
    mc "Well, actually..!"
    mc "Kwiyer seems like she really cares about getting people's opinions.."
    h "You think so?"
    mc "I have a good feeling about her. Even just as someone to talk to, it seems like she's really trying."
    h "Huh.. Ok, sure."
    $ union_ending_points += 1
    jump day_01_center





label day_01_center:

    call screen shipscreen_nav_center

    scene ship_screen_center with dissolve

    screen shipscreen_nav_center():
        add "shipscreen_center"
        modal True

        imagebutton auto "ship_map_bridge_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "move to ship bridge")
            unhovered SetVariable("screen_tooltip", "")
            action Jump("day_01_bridge")

        imagebutton auto "ship_map_d2_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "move to deck 2")
            unhovered SetVariable("screen_tooltip", "")
            action Jump("day_01_stern")

        imagebutton auto "ship_map_d3_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "move to ship bridge")
            unhovered SetVariable("screen_tooltip", "")
            action Jump("day_01_deckthree")

        imagebutton auto "ship_map_engine_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "move to deck 3")
            unhovered SetVariable("screen_tooltip", "")
            action Jump("day_01_engineroom")

        imagebutton auto "ship_map_galley_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "move to galley")
            unhovered SetVariable("screen_tooltip", "")
            action Jump("day_01_galley")

        imagebutton auto "ship_map_factory_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "move to factory")
            unhovered SetVariable("screen_tooltip", "")
            action Jump("day_01_factorycam01")

        # imagebutton auto "move_screen_left_%s":
        #     focus_mask True
        #     hovered SetVariable("screen_tooltip", "move screen left")
        #     unhovered SetVariable("screen_tooltip", "")
        #     action Jump("day_01_left")

        # imagebutton auto "move_screen_right_%s":
        #     focus_mask True
        #     hovered SetVariable("screen_tooltip", "move screen right")
        #     unhovered SetVariable("screen_tooltip", "")
        #     action Jump("day_01_right")


        imagebutton auto "ciara_cd_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "Iconic CD")
            unhovered SetVariable("screen_tooltip", "")
            action Jump("click_on_cd")

        imagebutton auto "radio_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "choose what is on the radio")
            unhovered SetVariable("screen_tooltip", "")
            action Jump("click_on_radio")





label day_01_left:
    call screen shipscreen_nav_left
    scene ship_screen_left with dissolve

    screen shipscreen_nav_left():
        add "shipscreen_left"
        modal True

        imagebutton auto "move_screen_right_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "move screen right")
            unhovered SetVariable("screen_tooltip", "")
            action Jump("day_01_center")

label day_01_right:
    call screen shipscreen_nav_right
    scene ship_screen_right with dissolve

    screen shipscreen_nav_right():
        add "shipscreen_right"
        modal True

        imagebutton auto "move_screen_left_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "move screen right")
            unhovered SetVariable("screen_tooltip", "")
            action Jump("day_01_center")



label click_on_cd:
    scene shipscreen_ciara_cd
    pause 2.0
    "I see you are interested in relics of the past."

    jump day_01_center

label click_on_radio:
    scene shipscreen_radio
    "Choose the tunes"
    call screen radio_choose
    return

    

screen radio_choose:
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        frame: 
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            textbutton "101.9" action Jump("radio_1019")
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            text "103.5"
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            text "104.9"
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            textbutton "turn off" action Jump("turn_off_radio")
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            textbutton "return" action Jump("call_hide_screens_ui")
            

label radio_1019:
    play music "audio/background.mp3" fadeout 2.0 fadein 2.0
    "playing 101.9 - your favorite elf's favorite radio station"
    jump call_hide_screens_ui

label turn_off_radio:
    stop music fadeout 2.0
    "i'm too stressed for music"
    jump call_hide_screens_ui
    

label call_hide_screens_ui:
    hide radio_choose
    jump day_01_center