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

relative = [
    '_78901',
    'yuiopq',
    'hjklas',
    'nmzxcv']
xf86 = {';': "semicolon", "'": "apostrophe", '[':"bracketleft", '.':"period",
        ',':"comma", "/": "slash", '-': "minus"} 

zoneW = res[0]/len(xmain)
zoneH = res[1]/len(ymain)
stepx = zoneW/len(grid[0])
stepy = zoneH/len(grid)

def xpos( x, offset):
    return x*zoneW + offset*stepx + stepx/2

def ypos( y, offset):
    return y*zoneH + offset*stepy + stepy/2

templ = 'bindsym %s+%s \t seat - cursor move %d %d'
print (templ % (xmain[0], xmain[1], -1*stepx/3, 0 ))
print (templ % (xmain[1], xmain[2],   stepx/3,  0 ))
print (templ % (ymain[0], ymain[1], 0, -1*stepy/3 ))
print (templ % (ymain[1], ymain[2], 0,   stepy/3, ))

templ = 'bindsym %s+%s+%s \t seat - cursor move %d %d'
print (templ % (xmain[0], ymain[0],'u', -stepx/3,-stepy/3 ))
print (templ % (xmain[2], ymain[0],'o',  stepx/3,-stepy/3 ))
print (templ % (xmain[0], ymain[2],'m', -stepx/3, stepy/3 ))
print (templ % (xmain[2], ymain[2],'period',stepx/3, stepy/3 ))

template = 'bindsym %s+%s+%s \t\t  seat "-" cursor set %d %d'
for my in range(0, len(ymain) ):
    for mx in range(0, len(xmain)):
        for y in range(0, len(grid)):
            for x in range(0,len(grid[0])):
                # print ("mx:%d\tmy:%d\ty:%d\tx:%d " %(mx,my,y,x))
                print (template % (xmain[mx],  ymain[my], grid[y][x], 
                                   xpos(mx,x ), ypos(my,y) ))

templ = "bindsym %s+%s+%s seat - cursor move -%d 0; seat - cursor move %d 0"
rlen = sum([len(x)-x.count('_') for x in relative])
idx = 0
for y in range(0, len(relative)):
    for x in range(0, len(relative[y])):
        if relative[y][x] != '_':
            print( templ % (xmain[0], xmain[2], relative[y][x], res[0],
                            idx*res[0]/rlen+res[0]/rlen/2) )
            idx = idx + 1
idx = 0
templ = "bindsym %s+%s+%s seat - cursor move 0 -%d; seat - cursor move 0 %d"
for x in range(0, len(relative[0])):
    for y in range(0, len(relative)):
        if relative[y][x] != '_':
            print( templ % (ymain[0], ymain[2], relative[y][x], res[1],
                            idx*res[1]/rlen+res[1]/rlen/2) )
            idx = idx + 1
