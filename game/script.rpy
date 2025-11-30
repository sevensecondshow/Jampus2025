# The script of the game goes in this file.

define mc = Character('Tin', color="#c8ffc8", image="mc")
define n = Character('???', color="#c8ffc8")

image screen0 = "introscreen_ph.png"
image screen1 = "boat_placeholder.png"
# image character1 = "character1_ph.png"
# image character1_sad = "character1sad_ph.png"


label start:
    $ trust_points = 5
    scene screen0

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

    #show character1_sad at left
    mc sad "come on, at least let me be a little edgy if we’re at the end of the world."
    jump intro_02


label positive01:
    $ trust_points += 1

    scene screen1
    with fade

    mc neutral "you think so? that’s… kind of you, thanks"
    jump intro_02

label intro_02:
    #show character1 at left
    #with dissolve

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
    mc sad "oh- wow, i.. really? you’d take nixon’s deal?"
    mc "maybe let's change the subject."
    jump intro_03

label intro_03:

    if trust_points >= 5:

        mc neutral "you’re the only person i can lean on."
        mc "no matter what happens, you’re my partner for whatever that means these days."
        mc "5999 people left on earth, and you’re the only person i can trust."
        jump intro_04

    if trust_points <= 4:

        mc sad "you’re the only person i can lean on."
        mc "no matter what happens, you’re my partner for whatever that means these days."
        mc "..."
        mc "5999 people left on earth, and you’re the only person i can trust."
        jump intro_04
        
label intro_04:
    mc neutral "our shift is starting soon,"

    return
