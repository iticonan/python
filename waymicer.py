# this creates keyboard shortcuts for absolute mouse positioning on sway.
# basic use: edit res (resolution) to match your monitor and run

# best I could find for wayland (correspond to F13-F18). Must be same length
xmain = ['XF86Tools','XF86Launch5','XF86Launch6']
ymain = ['XF86Launch7','XF86Launch8','XF86Launch9']

grid = [ # Filler chars. just ensure same length arrays and no repeatsMod4
    '12345',
    'qwert',
    'asdfg',
    'zxcvb',
]
res = (1920, 1080); #note: scale depending. e.g. 2 scaling halves resolution

#note: optional if extra granularity needed
# must be all unique modifiers of size len(xmain) x len(ymain) 
mods = [['F19'      ,'Mod4',    'Mod5'],
        ['Shift'   ,'Control' , 'Mod1'],
        ['F23'   ,'XF86Tools' , 'F24' ]]

linear = ['Mod1','Mod5','Control','Mod4','Shift']
hor = ['h','j','k','l','semicolon','p']
ver = ['g','f','d','s','a','q']

zoneW = res[0]/len(xmain)
zoneH = res[1]/len(ymain)
stepx = zoneW/len(grid[0])
stepy = zoneH/len(grid)

def xpos( x, offset):
    return x*zoneW + offset*stepx + stepx/2

def ypos( y, offset):
    return y*zoneH + offset*stepy + stepy/2

def sxpos( x, sx, offset):
    subx = len(xmain)-1
    return x*zoneW + sx*zoneW/subx + offset*stepx/subx + stepx/subx/2

def sypos( y, sy, offset):
    suby = len(ymain)
    return y*zoneH + sy*zoneH/suby + offset*stepy/suby + stepy/suby/2

template = 'bindsym %s+%s+%s \t\t  seat "-" cursor set %d %d'
subtempl = 'bindsym %s+%s+%s+%s \t\t  seat "-" cursor set %d %d'
for my in range(0, len(ymain) ):
    for mx in range(0, len(xmain)):
        for y in range(0, len(grid)):
            for x in range(0,len(grid[0])):
                # print ("mx:%d\tmy:%d\ty:%d\tx:%d " %(mx,my,y,x))
                print (template % (xmain[mx],  ymain[my], grid[y][x], 
                                   xpos(mx,x ), ypos(my,y) ))
        # if extra granularity not wanted comment everything below here
        iterx = list(range(len(mods)))
        iterx.pop(mx)
        itery = list(range(len(mods[0])))
        for sy in range(0, len(itery)):
            for sx in range(0, len(iterx)):
                # calculate modifier from sx and sy
                mod = mods[my][mx]
                for y in range(0, len(grid)):
                    for x in range(0,len(grid[0])):
                    # print ("mx:%d\tmy:%d\ty:%d\tx:%d " %(mx,my,y,x))
                        print (subtempl % (mod, xmain[iterx[sx]], ymain[itery[sy]], grid[y][x], 
                                   sxpos(mx, sx, x ), sypos(my, sy, y) ))

for m in range(0, len(linear)):
    common = 'XF86Launch7+XF86Launch8+XF86Launch9+'
    for v in range(0, len(ver)):
        templ = 'bindsym %s%s+%s seat - cursor move 0 -%d; seat - cursor move 0 %d'
        segy = res[1]/len(linear)
        move = m*segy + v*segy/len(ver)
        print (templ % (common, linear[m], ver[v], res[1], move ))
    for h in range(0, len(hor)):
        templ = 'bindsym %s%s+%s seat - cursor move -%d 0; seat - cursor move %d 0'
        segx = res[0]/len(linear)
        move = m*segx + h*segx/len(hor)
        print (templ % (common, linear[m], hor[h], res[0], move ))
