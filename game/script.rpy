
define tin = Character('Tin', color="#c8ffc8", image="tin")
define n = Character('???', color="#c8ffc8")
define kw = Character('Kwiyer', color="#F1F794", image="kw")
define nx = Character('Nixon', color="#544B13", image ="nixon")
define kd = Character('KD Pantz', color="#EB8FE6", image ="kdpantz")
define h = Character('Herscheles', color="#6E90FF", image ="h")

image factory_01 = "FACTORY_1.png"
image factory_02 = "FACTORY_2.png"
#image factory_02_kw = "FACTORY_2_KWIYER.png"
image galley_01 = "GALLEY_1.png"
image galley_02 = "GALLEY_2.png"
#image galley_02_h = "GALLEY_2_HERSH.png"
image hall_center = "HALL_CENTER.png"
image hall_left = "HALL_LEFT.png"
#image hall_left_nx = "HALL_LEFT_NIXON.png"
image hall_right = "HALL_RIGHT.png"
image stern_center = "STERN_CENTER.png"
image stern_right = "STERN_RIGHT.png"
#image stern_right_kd = "STERN_RIGHT_KD.png"



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

define config.default_music_volume = 0.75
define config.default_sfx_volume = 0.75
define config.default_voice_volume = 0.75

label start:
    $ trust_points = 5
    $ union_ending_points = 0
    $ nixon_ending_points = 0
    $ kd_ending_points = 0
    $ readyforaudio_puzzle_01 = False
    $ Day_01_Kwiyer_Conversation = False
    $ Day_01_Nixon_Conversation = False
    $ Day_01_kd_Conversation = False
    $ Day_01_h_Conversation = False

    scene stern_center

    show screen frame_text

    screen frame_text:
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            text "DAYS UNTIL DECISION: 14"

    play music "audio/tension01.ogg" fadeout 2.0 fadein 2.0 volume 0.35
    queue music "audio/tension01.ogg"
    pause 5.0
    hide screen frame_text

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
    show tin angry at left
    tin "come on, at least let me be a little edgy if we’re at the end of the world."
    jump intro_02


label positive01:
    $ trust_points += 1
    show tin neutral at left
    tin "you think so? that’s… kind of you, thanks"
    jump intro_02

label intro_02:

    tin neutral "i hear it’s starting to get pretty close to the draw."
    tin "union wants to nix santa and nixon wants to spy on the union."
    tin "this is starting to get a bit too much, we still haven’t even found out what happened to jeffany."
    tin "we completely run out of power in 14 days. after that, we’re at the mercy of the world. what do you think?"

menu:
    "we should talk to the union.":
        jump positive02
    "we should wiretap the union.":
        jump negative02

label positive02:
    $ trust_points += 1
    tin neutral "you’re right, maybe it’s time we got more involved. anything they’ve got has to be better than this, right?"
    show screen frame_text_00
    screen frame_text_00:
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            text "Tin seems to have appreciated that."
    pause 2.0
    hide screen frame_text_00
    jump intro_03

label negative02:
    $ trust_points -= 1
    tin @ surprised "oh- wow, i.. really? you’d take nixon’s deal?"
    show screen frame_text_01
    screen frame_text_01:
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            text "The silence is awkward."
    pause 2.0
    hide screen frame_text_01
    tin @ angry "maybe let's change the subject."
    jump intro_03

label intro_03:

    if trust_points >= 5:

        tin neutral "you’re the only person i can lean on."
        tin "no matter what happens, you’re my partner for whatever that means these days."
        tin "5999 people left on earth, and you’re the only person i can trust."
        jump intro_04
    else:

        tin angry "you’re the only person i can lean on."
        tin "no matter what happens, you’re my partner for whatever that means these days."
        tin "..."
        tin "5999 people left on earth, and you’re the only person i can trust."
        jump intro_04
        
label intro_04:
    tin neutral "our shift is starting soon,"

## SHIFT START: GALLEY 

label shift_start_galley:
    scene galley_01 with dissolve
    show tin neutral at left
    tin neutral "mic check, one two, one two, you read me?"

menu:
    "yes.":
        jump shift_start_galley_02

label shift_start_galley_02:
    tin smile "perfect. what's in store for us?"
    tin neutral "the only thing we really have to do is handle the shipment from the Entire Nation of Switzerland and I'd like to talk to at least 2 people about jeffany's disappearance."
    # tutorial dialogue
    tin "{i}When you want to send me somewhere else, cycle through your cameras and press 'enter' to direct me. {/i}"
    tin "{i}click on items or people if you want me to investigate, i'll be listening for your input.{/i}"

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
    scene hall_right
    show tin neutral at left
    tin neutral "that's off limits right now. let's try somewhere else?"
    jump day_01_center


label day_01_engineroom:
    scene hall_right
    show tin neutral at left
    if readyforaudio_puzzle_01:
        jump day_01_audio_puzzle
    else: 
        tin neutral "i don't have the keys, maybe some other time."
        jump day_01_center


label day_01_factorycam01:
    scene factory_02
    call screen hall_kw

    screen hall_kw():
 
        imagebutton:
            focus_mask True
            xalign 0.5
            yalign 0.5
            idle "FACTORY_2_KWIYER.png"
            hovered SetVariable("screen_tooltip", "That's Kwiyer, head of the union.")
            unhovered SetVariable("screen_tooltip", "")
            action Jump("day_01_factorycam02")


label day_01_factorycam02:

    if Day_01_Kwiyer_Conversation == True:
        show tin neutral at left
        tin "I don't think I have anything else to say here."
        jump day_01_center
    else:
        show tin angry at left
        tin "if we must.."
        tin "the factory smells unpleasant as always. i'm not sure how much longer i can stand to inhale plastic fumes like this."
        show kw smile at right
        kw "Hiya, Tin! Merry day, I think. What are you up to?"

menu:
    "Can you remind us when you last saw Jeffany?":
        jump day_01_factorycam01_kwiyer02
        # still needs filling out
    "We might want to get involved with the Union.":
        jump day_01_factorycam01_kwiyer01

label day_01_factorycam01_kwiyer02:
    kw "Oh, um..."
    kw @ sad "Actually, I guess I don't remember when I saw them last."
    kw "I don't think I've seen them today, at the very least, I'm sure of that!"
    kw "Sorry I can't be more help. But, if I do see them soon, I'll let them know you're looking!"
    jump day_01_center

label day_01_factorycam01_kwiyer01:
    kw "Oh!!"
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
    kw smile "Perfect, thank you so much! If you ever see the following people, could you bring it up? "
    hide kw
    $ trust_points += 1
    show screen frame_text_00
    screen frame_text_00:
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            text "Tin seems to have appreciated that."
    pause 2.0
    hide screen frame_text_00
    # Get Item: Employee List
    # SHOW A LIST OF EMPLOYEES
    """
    Kwiyer leaves a list with the following names on it: \n
    KD Pantz

    Herscheles \n
    Nixon

    Mull \n
    """
    $ Day_01_Kwiyer_Conversation = True
    $ Quest_KW = True
    jump day_01_center

label negative_factorycam01:
    kw sad "Oh! Sure, yeah, no worries. Thanks for the interest! I hope we see you at the meeting.."
    hide kw
    $ trust_points -= 1
    show screen frame_text_01
    screen frame_text_01:
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            text "The silence is awkward."
    pause 2.0
    hide screen frame_text_01
    $ Day_01_Kwiyer_Conversation = True
    jump day_01_center


label day_01_deckthree:
    scene hall_left
    call screen hall_nixon

    screen hall_nixon():
 
        imagebutton:
            focus_mask True
            xalign 0.5
            yalign 0.5
            idle "HALL_LEFT_NIXON.png"
            hovered SetVariable("screen_tooltip", "That's Nixon.")
            unhovered SetVariable("screen_tooltip", "")
            action Jump("day_01_deckthree_01")

label day_01_deckthree_01:
    if Day_01_Nixon_Conversation == True:
        show tin neutral at left
        tin  "I don't think I wish talk to this elf again."
        jump day_01_center
    else:
        show tin angry at left
        tin "I forgot how loud the lights are here."
        show nixon at right
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
    hide nixon
    $ trust_points -= 10
    show screen frame_text_01
    screen frame_text_01:
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            text "The silence is awkward."
    pause 2.0
    hide screen frame_text_01
    # Get Item: Bug
    $ Day_01_Nixon_Conversation = True
    $ Quest_NX = True
    jump day_01_center

label day_01_deckthree_nixon_04:
    nx "If you change your mind.. You know how to find me."
    hide nixon
    $ trust_points += 1
    show screen frame_text_00
    screen frame_text_00:
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            text "Tin seems to have appreciated that."
    pause 2.0
    hide screen frame_text_00
    $ Day_01_Nixon_Conversation = True
    jump day_01_center


label day_01_stern:
    scene stern_right
    call screen stern_kd

    screen stern_kd():
        imagebutton:
            focus_mask True
            xalign 0.5
            yalign 0.5
            idle "STERN_RIGHT_KD.png"
            hovered SetVariable("screen_tooltip", "That's KD Pantz. He's always scheming something...")
            unhovered SetVariable("screen_tooltip", "")
            action Jump("day_01_stern_01")


label day_01_stern_01:
    if Day_01_kd_Conversation == True:
        show tin neutral at left
        tin "As nice as it is up here, we should really be thorough."
        jump day_01_center
    else:
        show tin smile at left
        tin "it's as good a day as any, i guess. at least the ocean breeze is nice, we still have that."
        tin neutral "it looks like KD Pantz is here if we want to talk to him"
        show kdpantz at right
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
    hide kd
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
    kd "Hey, as long as you sign it, you're doing everything I need!"
    hide kd
    $ Day_01_kd_Conversation = True
    jump day_01_center

label day_01_stern_kd_04:
    kd "I knew I could count on you two! Talk to me next week, about it, yeah? We've got big stuff coming!"
    hide kd
    $ Day_01_kd_Conversation = True
    $ Quest_KD = True
    jump day_01_center

label day_01_stern_kd_05:
    # FILL OUT
    kd "oh, well... see you, then."
    hide kd
    $ Day_01_kd_Conversation = True
    jump day_01_center




label day_01_galley:
    scene galley_02
    call screen galley_h

    screen galley_h():
        imagebutton:
            focus_mask True
            xalign 0.5
            yalign 0.5
            idle "GALLEY_2_HERSH.png"
            hovered SetVariable("screen_tooltip", "That's Herscheles - Hersh for short. He's the cook.")
            unhovered SetVariable("screen_tooltip", "")
            action Jump("day_01_galley_01")

label day_01_galley_01:
    show tin neutral at left
    if readyforaudio_puzzle_01 == True:
        tin @ angry "I have somewhere else to be."
        jump day_01_center

    if Day_01_h_Conversation == True:
        tin @ surprised "Err - wait, you want me to ask Hersch about Jeffany...?"
        jump day_01_galley_herc_03

    if Day_01_kd_Conversation == True:
        tin @ smile "yum! let's go"       
    elif Day_01_Kwiyer_Conversation == True:
        tin @ smile "yum! let's go"
    elif Day_01_Nixon_Conversation == True:
        tin @ smile "yum! let's go"
    else:
    # if not talked to anyone yet
        tin "i wanna check in with a leader first before stopping in here."
        jump day_01_center

    tin @ surprised "Oh! Herscheles is here. They were pretty close to Jeffany.. I don't think we should bring it up.."
    tin neutral "But... I'll trust you to make the right choice."
    show h neutral at right
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
    h @ sad "Ah, yeah, them… I dunno, what's the point in having a union anymore when we live in an apocalypse?"

    if Quest_KW == True and Quest_NX == True:
        menu:
            "(neutral) You're right. Disregard.": 
                jump day_01_galley_herc_04
            # if union quest ->
            "There's a meeting tonight and they want people's input.":
                jump day_01_galley_herc_05
            # if nixon quest ->
            "You're right, you might want to talk to Nixon.":
            # trust roll check
                jump day_01_center
    elif Quest_KW == True and Quest_NX == False: # if only Quest_KW is true
        menu:
            "(neutral) You're right. Disregard.":
                jump day_01_galley_herc_04
            # if union quest ->
            "There's a meeting tonight and they want people's input.": 
                jump day_01_galley_herc_05
    elif Quest_KW == False and Quest_NX == True:
        menu:
            "(neutral) You're right. Disregard.":
                jump day_01_galley_herc_04
            # if nixon quest ->
            "You're right, you might want to talk to Nixon.":
            # trust roll check
                jump day_01_galley_herc_06
    else: # QuestKW and QuestNX are False
        menu:
            "(neutral) You're right. Disregard.": 
                jump day_01_galley_herc_04




label day_01_galley_herc_02:
    h "Management's not my favorite in the world. I keep hearing that Pantz guy muttering about how he should be in charge."

    menu:
        "Wanna sign a petition?":
            jump day_01_galley_herc_02a
        "Don't bring it up.":
            jump day_01_galley_herc_02b
    #jump day_01_center

label day_01_galley_herc_02a:
    h "A petition? What do we need that for?"
    tin "It looks like KD Pantz is looking for support. I think we've about all had enough, right?"
    h "But what would it.. Like.. Do?"
    tin smile "That's a good question! Umm, I think it's just for his confidence, maybe?"
    h "What the hell, why not.." #[+1 to KD's cause]
    hide h
    $ kd_ending_points +=1
    $ Day_01_h_Conversation = True
    jump day_01_center

label day_01_galley_herc_02b:
    $ trust_roll = renpy.random.randint(1, 20)
    if trust_roll > 10:
        show screen frame_text_03
        screen frame_text_03:
            frame:
                xpadding 40
                ypadding 20
                xalign 0.5
                yalign 0.5
                text "Tin seems to trust our opinion here."
        pause 2.0
        hide screen frame_text_03
        tin @ angry "Hm, yeah… Surely anything's better than this.."
        hide h
        $ trust_points -=1
        $ Day_01_h_Conversation = True
        jump day_01_center
    else:
        show screen frame_text_02
        screen frame_text_02:
            frame:
                xpadding 40
                ypadding 20
                xalign 0.5
                yalign 0.5
                text "Tin doesn't seem to trust us."
        pause 2.0
        hide screen frame_text_02
        tin angry "Well, actually, there's a petition you could sign."
        $ trust_points -=1
        jump day_01_galley_herc_02a

label day_01_galley_herc_03:
    play music "audio/tension02.ogg" noloop fadeout 5.0 fadein 4.0 volume 0.35
    queue music "audio/tension01.ogg"

    $ trust_roll = renpy.random.randint(1, 20)
    if trust_roll > 10:
        show screen frame_text_03
        screen frame_text_03:
            frame:
                xpadding 40
                ypadding 20
                xalign 0.5
                yalign 0.5
                text "Tin seems to trust our opinion here."
        pause 2.0
        hide screen frame_text_03
        tin @ surprised "Um...[[quietly]] are you sure…? Ok…"
        tin neutral "[[clears throat]] We need to ask a few things about.. Jeffany.."
        show h sad at right
        h sad """...
        Somebody killed her
        I know it.. I just…
        I keep going over everything. What do you need to know?
        """
    else:
        show screen frame_text_02
        screen frame_text_02:
            frame:
                xpadding 40
                ypadding 20
                xalign 0.5
                yalign 0.5
                text "Tin doesn't seem to trust us."
        pause 2.0
        hide screen frame_text_02
        tin @ angry "[[quietly]] No, I already said we're not doing that."
        show h neutral at right
        h neutral "What?"
        tin "No, it's nothing, it's just-"
        h "You want to avoid talking about Jeffany?"
        tin @ surprised " "
        h @ sad "You can ask. It's tough. But you can ask."

    tin "Well, we can't rewind the tapes… The engine rooms been scrambled, and that's one of the places we haven't been able to look. Got any ideas?"
    h sad "...."
    h "You listen to the radio a lot?"
    tin "What?"
    h "The radio."
    tin "Sure, at the end of our shift we usually hang back and..."
    h neutral "When you two listen to the radio tonight... I think heavy metal feels like the mood."
    tin @ surprised "Oh.. Um.. Sure."
    hide h

    pause 2.0
    tin "Alright, that's everything for today… Let's unwind with that radio, huh?"
    $ readyforaudio_puzzle_01 = True
    jump day_01_center

label day_01_galley_herc_04:
    $ trust_points -= 1
    $ trust_roll = renpy.random.randint(1, 20)
    if trust_roll > 10:
        # if trust roll success
        show screen frame_text_03
        screen frame_text_03:
            frame:
                xpadding 40
                ypadding 20
                xalign 0.5
                yalign 0.5
                text "Tin seems to trust our opinion here."
        pause 2.0
        hide screen frame_text_03
        h "Uhuh... Anything else?"
    else:
        show screen frame_text_02
        screen frame_text_02:
            frame:
                xpadding 40
                ypadding 20
                xalign 0.5
                yalign 0.5
                text "Tin doesn't seem to trust us."
        pause 2.0
        hide screen frame_text_02
        # if trust roll fail
        tin @ smile "Well, actually..!"
        tin @ smile "Kwiyer seems like she really cares about getting people's opinions.."
        h "You think so?"
        tin @ smile "I have a good feeling about her. Even just as someone to talk to, it seems like she's really trying."
        h "Huh.. Ok, sure."
        hide h
        $ union_ending_points += 1

    $ Day_01_h_Conversation = True
    jump day_01_center

label day_01_galley_herc_05:
    #(no change to trust)
    h "Oh, yeah? Ok.. Sure, I might pop by, but I'm not committing to anything."
    hide h
    $ Day_01_h_Conversation = True
    jump day_01_center

label day_01_galley_herc_06:
    $ trust_roll = renpy.random.randint(1, 20)
    if trust_roll > 10:
        show screen frame_text_03
        screen frame_text_03:
            frame:
                xpadding 40
                ypadding 20
                xalign 0.5
                yalign 0.5
                text "Tin seems to trust our opinion here."
        pause 2.0
        hide screen frame_text_03
        h "Really? What does he have to offer?"
        tin "Security, I think. I don't know what will happen, but it's better to be safe than sorry, right?"
        h "Yeah, I guess so… I'll talk to him later, thanks."
        $ nixon_ending_points +=1
    else:
        if Quest_KD == True:
            jump day_01_galley_herc_02 #starts KD quest dialogue
        else:
            show screen frame_text_02
            screen frame_text_02:
                frame:
                    xpadding 40
                    ypadding 20
                    xalign 0.5
                    yalign 0.5
                    text "Tin doesn't seem to trust us."
            pause 2.0
            hide screen frame_text_02
            tin "..."
            tin "I'd be careful around Nixon, just so you know. He's been prying in the wrong places lately.."
            h " Good to know."
    hide h
    $ Day_01_h_Conversation = True
    jump day_01_center    



label day_01_center:

    #scene ship_screen_center with dissolve
    scene hall_center with dissolve
    call screen shipscreen_nav_center

    screen shipscreen_nav_center():
        #add "HALL_CENTER"
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


        # imagebutton auto "ciara_cd_%s":
        #     focus_mask True
        #     hovered SetVariable("screen_tooltip", "Iconic CD")
        #     unhovered SetVariable("screen_tooltip", "")
        #     action Jump("click_on_cd")

        imagebutton auto "radio_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "choose what is on the radio")
            unhovered SetVariable("screen_tooltip", "")
            action Jump("click_on_radio")


label day_01_audio_puzzle:
    
    scene hall_right
    call screen engine_room

    screen engine_room():
        add "engineroom_poster"
        imagebutton:
            focus_mask True
            xalign 0.5
            yalign 0.5
            idle "engine_chiptune_poster.png"
            hovered SetVariable("screen_tooltip", "A poster for a song that seems familiar.")
            unhovered SetVariable("screen_tooltip", "")
            action Jump("day_01_audio_puzzle_01")
    
        imagebutton:
            focus_mask True
            xalign 0.5
            yalign 0.5
            idle "engine_jazz_poster.png"
            hovered SetVariable("screen_tooltip", "A poster for a song that seems familiar.")
            unhovered SetVariable("screen_tooltip", "")
            action Jump("day_01_audio_puzzle_02")

        imagebutton:
            focus_mask True
            xalign 0.5
            yalign 0.5
            idle "engine_metal_poster.png"
            hovered SetVariable("screen_tooltip", "A poster for a song that seems familiar.")
            unhovered SetVariable("screen_tooltip", "")
            action Jump("day_01_audio_puzzle_03")
    #show clickables - 3 posters, 1 door

        imagebutton:
            focus_mask True
            xalign 0.5
            yalign 0.5
            idle "engine_code_door.png"
            hovered SetVariable("screen_tooltip", "A door with a code entry for four numbers.")
            unhovered SetVariable("screen_tooltip", "")
            action Jump("day_01_audio_puzzle_04")
    # say - look at the radio ad, which one am i listening to now?
    # click on each poster, bring up close-up, text "looks like a poster for chiptune..."
    # click on door
    # input 4 numbers
    # open the door -> new area
    # narrator describing 'to be continued...'
    jump day_01_center

label day_01_audio_puzzle_01:
    # poster 01 chiptune
    scene hall_right
    show screen_engine_chiptune_poster
    pause 2.0
    "Looks like a poster for that chiptune radio station."
    jump day_01_audio_puzzle

label day_01_audio_puzzle_02:
    # poster 02 jazz
    scene hall_right
    show screen_engine_jazz_poster
    pause 2.0
    "Looks like a poster for that jazz radio station."
    jump day_01_audio_puzzle

label day_01_audio_puzzle_03:
    # poster 03 metal
    scene hall_right
    show screen_engine_metal_poster
    pause 2.0
    "Looks like a poster for that metal radio station."
    jump day_01_audio_puzzle

label day_01_audio_puzzle_04:
    # pop up number entry box
    scene hall_right
    show screen_engine_code_door
    pause 2.0
    # "It's asking for a 4-digit number..."
    default code_input = "0000"
    $ code_input = renpy.input("It's asking for a 4-digit number...", default="0000", allow="0123456789", length=4)

    # python:
    #     code_input = renpy.input("It's asking for a 4-digit number...", default="0000", allow="0123456789", length=4)
    #     #code_input = code_input.strip()

    #     if not code_input:
    #         code_input = "0000"

    if code_input == "1035":
        jump day_01_audio_puzzle_04_success
    else:
        jump day_01_audio_puzzle_04_fail


label day_01_audio_puzzle_04_fail:
    "Ah, that wasn't it. Maybe I can try again."
    jump day_01_audio_puzzle_04

label day_01_audio_puzzle_04_success:
    "The door opens."
    show tin surprised at left 
    tin "They hid a code in the radio station...? Wow. Okay. Let's see what we've been missing..."
    play music "audio/evilsanta.ogg" fadeout 3.0 fadein 3.0
    pause 3.0
    """
    There were a lot of things we discovered that day.

    The fate of Jeffany.

    What happens when you piss off evil Santa.

    The exact diet of orcas.

    No matter who we help take control the of the ship -- the North Pole Toymakers Union, the Clause Corp gremlins, or otherwise,
    We've still gotta make it off this ship alive.

    And the Entire Nation of Switzerland is really not helping.

    The mystery continues. Santa sucks. Elves deserve better.

    (The End)
    
    """
    pause 5.0
    $ renpy.full_restart()
    # door opens
    # long monologue + santa music play



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
    show shipscreen_radio
    "Choose the tunes"
    call screen radio_choose

    

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
            textbutton "103.5" action Jump("radio_1035")
        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            textbutton "104.9" action Jump("radio_1049")
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
    play music "audio/radio_chiptune.ogg" fadeout 2.0 fadein 2.0
    "playing 101.9 - your favorite elf streamer's favorite radio station."
    jump call_hide_screens_ui

label radio_1035:
    play music "audio/radio_metal.ogg" fadeout 2.0 fadein 2.0
    pause 3.0
    "hah! I feel like I've seen a poster for this song on the walls somewhere weird..." #directing player to engine room
    pause 1.0
    jump call_hide_screens_ui

label radio_1049:
    play music "audio/radio_jazz.ogg" fadeout 2.0 fadein 2.0
    "playing 104.9 - only the classics for the elves who remember the good old reindeer days."
    jump call_hide_screens_ui  

label turn_off_radio:
    stop music fadeout 2.0
    play music "audio/tension01.ogg" fadeout 2.0 fadein 10.0 volume 0.35
    queue music "audio/tension01.ogg"
    "Music seems a little inappropriate at the moment."
    jump call_hide_screens_ui
    

label call_hide_screens_ui:
    hide radio_choose
    jump day_01_center