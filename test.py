from DriverInterface import DriverInterface
import time
from Move import Move
import Config as config

def di_test():
    d = DriverInterface()

    sd = 0.5
    sc = int(round(5/sd))

    d.execute(sd, sc)
    time.sleep(1)

    sd = 0.2
    sc = int(round(5/sd))

    d.execute(sd, sc)
    time.sleep(1)

    sd = 0.1
    sc = int(round(5/sd))

    d.execute(sd, sc)
    time.sleep(1)

    sd = 0.05
    sc = int(round(5/sd))

    d.execute(sd, sc)
    time.sleep(1)

    sd = 0.01
    sc = int(round(5/sd))

    d.execute(sd, sc)
    time.sleep(1)

    sd = 0.005
    sc = int(round(5/sd))

    d.execute(sd, sc)
    time.sleep(1)

    sd = 0.001
    sc = int(round(5/sd))

    d.execute(sd, sc)
    time.sleep(1)

    d.sleep(1)

def move_test():
    print("Beginning Move.py Test")
    time.sleep(0.5)
    s = 1
    e = 0.5
    d = 4
    print("start = " + str(s))
    print("end = " + str(e))
    print("duration = " + str(d))
    m = Move()
    m.start_pos = s
    m.end_pos = e
    m.duration = d
    time.sleep(0.5)
    print("Executing...")
    m.execute_move()

    d.sleep(1)

def current_test(n, t):
    print("Beginning current test")
    time.sleep(0.5)
    
    d = DriverInterface()

    ms = 0
    print(ms)
    d.set_step(ms)
    d.execute(0.001 * n, int(round(t * 10000 / n)))

    time.sleep(1)

    ms = 1
    print(ms)
    d.set_step(ms)
    d.execute(0.001 * n, int(round(t * 10000 / n)))

    time.sleep(1)

    ms = 2
    print(ms)
    d.set_step(ms)
    d.execute(0.001 * n, int(round(t * 10000 / n)))

    time.sleep(1)

    ms = 3
    print(ms)
    d.set_step(ms)
    d.execute(0.001 * n, int(round(t * 10000 / n)))

    time.sleep(1)

    ms = 4
    print(ms)
    d.set_step(ms)

    d.execute(0.001 * n, int(round(t * 10000 / n)))

    d.sleep(1)
    
def basic_test(step_delay, step_count, direc, ms):
    print("Basic test started")
    
    d = DriverInterface()

    d.set_step(ms)
    d.set_dir(direc)
    d.execute(step_delay, step_count)

    d.sleep(1)

    print("Finished.")

def side_to_side(step_delay, ms):
    print("Side to side test started")

    d = DriverInterface()

    dist = 0.3 # +/-
    step_count = dist * config.DIST_TO_STEPS
    d.set_step(ms)
    
    #prologue
    d.set_dir(0)
    d.execute(step_delay, step_count)
    for _ in range(5):
        d.set_dir(0)
        d.execute(step_delay, 2 * step_count)

        time.sleep(0.3)

        d.set_dir(1)
        d.execute(step_delay, 2 * step_count)
    d.set_dir(0)
    d.execute(step_delay, step_count)

    d.sleep(1)

    print("Finished.")
