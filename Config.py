# bluetooth device attributes
DEVICE_NAME = "TT Camera Slider"

MIN_POS = 0.15
MAX_POS = 1.35
MIN_SPEED = 0.01147074017
MAX_SPEED = 0.18353184282

# motor attributes
STEP_ANGLE = 1.8
VEL_TO_RPS = 9.88319028614 # 1/(2pi(r))
DIST_TO_STEPS = 1976.63805723 # (360)/(1.8*2pi(r)) ONLY for ms=0
RADIUS = 0.0161036

# move attributes
DEFAULT_VELOCITY = 0.1
SLEEP_BETWEEN_MOVE = 2

# compensation
DIST_TO_STEPS_E = 2.58064516129
VEL_TO_RPS_E = 3.10816411107

# compound
DIST_TO_STEPS_C = DIST_TO_STEPS # * DIST_TO_STEPS_C
VEL_TO_RPS_C = VEL_TO_RPS * VEL_TO_RPS_E