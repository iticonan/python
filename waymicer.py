# this creates keyboard shortcuts for absolute mouse positioning on sway.
# basic use: edit res (resolution) to match your monitor and run

# best I could find for wayland (correspond to F13-F18). Must be same length
xmain = ['XF86Tools','XF86Launch5','XF86Launch6']
ymain = ['XF86Launch7','XF86Launch8','XF86Launch9']

grid = [ # Filler chars. just ensure same length arrays and no repeats
    '12345',
    'qwert',
    'asdfg',
    'zxcvb',
]
res = (1080, 720); #note: scale depending. e.g. 2 scaling halves resolution

zoneW = res[0]/len(xmain)
zoneH = res[1]/len(ymain)
stepx = zoneW/len(grid[0])
stepy = zoneH/len(grid)

def xpos( x, offset):
    return x*zoneW + offset*stepx + stepx/2

def ypos( y, offset):
    return y*zoneH + offset*stepy + stepy/2

template = 'bindsym %s+%s+%s \t\t  seat "-" cursor set %d %d'
for my in range(0, len(ymain) ):
    for mx in range(0, len(xmain)):
        for y in range(0, len(grid)):
            for x in range(0,len(grid[0])):
                # print ("mx:%d\tmy:%d\ty:%d\tx:%d " %(mx,my,y,x))
                print (template % ( ymain[my], xmain[mx], grid[y][x], 
                                   xpos(mx,x ), ypos(my,y) ))
