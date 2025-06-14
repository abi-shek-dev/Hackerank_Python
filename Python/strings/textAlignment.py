t = int(input()) 
assert t % 2 == 1
total_width = t * 6
ch = 'H'         

def cone(aligned_left: bool = False, pointing_down: bool = False):
    width = t * 2 - 1
    layer_gen = range(t)
    align = '>' if aligned_left else '<'
    if pointing_down:
        layer_gen = reversed(layer_gen)
        
    for layer in layer_gen:
        unaligned_layer = f"{ch * (1 + layer * 2): ^{width}}"
        print(f"{unaligned_layer:{align}{total_width - 1}}")

def pillars():
    for layer in range(t + 1):
        print(f"{ch * t: ^{t*2}}{ch * t:^{total_width}}")
        
def middle_belt():
    for i in range((t + 1) // 2):
        print(f"{ch * t * 5: ^{total_width}}")

cone()                                      
pillars()                                   
middle_belt()                               
pillars()                                   
cone(aligned_left=True, pointing_down=True) 