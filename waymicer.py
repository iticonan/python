# Python script to create keyboard shortcuts to move mouse pointer on sway.
# How to use: edit grid, mods(modifier keys), and res (resolution) to your settings and run script
# Copy/Paste output to sway configuration file

grid = [ # A rectangular character map. No gaps. No repeats.
    '1234567890',
    'qwertyuiop',
    'asdfghjkl;',
    'zxcvbnm,./',
]
#      [(x-axis-mods),(y-axis mods)]
# mods = [("Mod1+",),("Mod4+","Control+")]
mods = [[],("Mod5+","Control+")]
res = (1920, 1080);
solo = True

lenxm = len(mods[0])
lenym = len(mods[1])
stepx = res[0]/len(grid[0])/ ( (1 if lenxm == 0 else lenxm+1) if solo else pow(2,lenxm))
stepy = res[1]/len(grid)/    ( (1 if lenym == 0 else lenym+1) if solo else pow(2,lenym))
# print("lenxm:%d\tlenym:%d\tstepx:%d\tstepy:%d" % (lenxm, lenym, stepx, stepy))

def parse( ch ):
    if ch == ';': return 'semicolon'
    if ch == ',': return 'comma'
    if ch == '.': return 'period'
    if ch == '/': return 'slash'
    if ch == "'": return 'apostrophe'
    if ch == '[': return 'bracketleft'
    if ch == "]": return 'bracketright'
    if ch == "-": return 'minus'
    if ch == "=": return 'equal'
    if ch == "\\": return 'backslash'
    return ch

def modifs( i, m ):
    if solo:
        return "" if len(m) == 0 or len(m) == i else m[i]
    bools = format(i, "0%db" % len(m) )
    ans = ""
    for i in range(0, len(m)):
        if bools[i] == '1': 
            ans += m[i]
    return ans

def xpos( x, offset):
    return stepx/2 + stepx*x + offset*res[0]/ (lenxm+1 if solo else pow(2, lenxm) )

def ypos( y, offset):
    return stepy/2 + stepy*y + offset*res[1]/ (lenym+1 if solo else pow(2, lenym) )

template = 'bindsym SunProps+%s%s%s \t\t  seat "-" cursor set %d %d'
for mx in range(0, lenxm + 1 if solo else lenxm*2 ):
    for my in range(0,lenym + 1 if solo else lenym*2):
        for y in range(0, len(grid)):
            for x in range(0,len(grid[0])):
                # print ("mx:%d\tmy:%d\ty:%d\tx:%d " %(mx,my,y,x))
                print (template % (modifs(my, mods[1]), modifs(mx, mods[0]), 
                                   parse(grid[y][x]), xpos(x, mx), ypos(y, my)))
