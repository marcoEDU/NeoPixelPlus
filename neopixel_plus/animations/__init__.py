try:
    from neopixel_plus.animations.beats_up_and_down import BeatsUpAndDown
    from neopixel_plus.animations.light_up import LightUp
    from neopixel_plus.animations.moving_dot import MovingDot
    from neopixel_plus.animations.rainbow import RainbowAnimation
    from neopixel_plus.animations.transition import Transition
except ImportError:
    from animations.beats_up_and_down import BeatsUpAndDown
    from animations.light_up import LightUp
    from animations.moving_dot import MovingDot
    from animations.rainbow import RainbowAnimation
    from animations.transition import Transition
