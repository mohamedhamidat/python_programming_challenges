# SimpleGUI program template
#http://www.codeskulptor.org/#user41_B9FrEv1QjR_12.py
# Import the module
import simplegui
import random 
# Define global variables (program state)
canvas_width=300
canvas_height=300
margin=20
w_car=20
h_car=30
margin_down=50
pos_a=[(canvas_width/2)+25,canvas_height-25]
pos_b=[(canvas_width/2)-25,canvas_height-25]
#pos_c=[canvas_width/2,(canvas_height-h_car)-h_car]
c_w=10 #cercle width
radius=20
line_width=5
c_posi=[canvas_width/2, 0] #cercle position

interval=40
current_key= ' '
# Define "helper" functions
#psotion de départ et aprés avoir passé en bas
def c_position_debut():
    x=random.randrange(margin+line_width+radius, canvas_width-(margin+line_width+radius))
    c_posi[0] = x
    c_posi[1] = 0
    

#car position
def car_position_debut():
    global pos_a, pos_b
    pos_a=[(canvas_width/2)+25,canvas_height-25]
    pos_b=[(canvas_width/2)-25,canvas_height-25]

# cercle movement
def c_position_tick():
    c_posi[1] +=5 
    if c_posi[1]>=canvas_height+radius: 
        c_position_debut()
    if abs (pos_b[1]-c_posi[1])<=radius+c_w and \
    abs (pos_b[0]-c_posi[0])<=radius+c_w or\
    abs (pos_a[1]-c_posi[1])<=radius+c_w and \
    abs (pos_a[0]-c_posi[0])<=radius+c_w :
        
        c_position_debut()
        car_position_debut()

    
#key up sapce

def keyup(key): 
    global corrent_key
    corrent_key= " "

def keydown(key):
    global c_posi, pos_a, pos_b
    vel = 10
    if key == simplegui.KEY_MAP["left"]:
        pos_a[0] -= vel
        pos_b[0] -= vel
        if pos_b[0] <= 24 :
            car_position_debut()
            c_position_debut()
    elif key == simplegui.KEY_MAP["right"]:
        pos_a[0] += vel
        pos_b[0] += vel
        if pos_a[0] >= canvas_width-20 :
            car_position_debut()
            c_position_debut()
    elif key == simplegui.KEY_MAP["down"]:
        pos_a[1] += vel
        pos_b[1] += vel
        if pos_a[1] >= canvas_height:
            car_position_debut()
            c_position_debut()
    elif key == simplegui.KEY_MAP["up"]:
        pos_a[1] -= vel 
        pos_b[1] -= vel
        if pos_b[1] <= 25:
            car_position_debut()
            c_position_debut()


    
# Define event handler functions

#draw tow lines from margin left to margin right

def draw(canvas):
    canvas.draw_line([margin, 0], [margin, canvas_height], 5, 'Blue')
    canvas.draw_line([canvas_width-margin, 0], [canvas_width-margin, canvas_height], 5, 'Blue')
    canvas.draw_polygon([pos_a, pos_b], 50, 'Yellow')    
    canvas.draw_circle(c_posi, radius, c_w, 'Green','Blue')
    
# Create a frame

frame = simplegui.create_frame('Testing', canvas_width, canvas_height)

# Register event handlers
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)
timer= simplegui.create_timer(interval,c_position_tick)

# Start frame and timers

c_position_debut()
frame.start()
timer.start()