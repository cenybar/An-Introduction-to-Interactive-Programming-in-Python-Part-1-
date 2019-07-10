# template for "Stopwatch: The Game"
import simplegui
# define global variables
count = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
#def format(t):
    #pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
def stop():
    timer.stop()
def reset():
    global count
    count = 0
    timer.stop()
# define event handler for timer with 0.1 sec interval
def tick():
    global count
    count += 1
    

# define draw handler
def draw_handler(frame):
    frame.draw_text(str(count),(100,100),20,"White")
    
# create frame
frame = simplegui.create_frame("Stop-watch", 200, 200)
frame.set_draw_handler(draw_handler)
frame.add_button("Start",start,50)
frame.add_button("Stop",stop,50)
frame.add_button("Reset",reset,50)

# register event handlers
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()
 

# Please remember to review the grading rubric
