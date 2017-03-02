"""
 B__ __ __ __C
 |           |
 |           |
 |           |
A|__ __ __ __|D
 We could define 12 block operators,d2xy_bc,d2xy_cb,d2xy_ab,
 d2xy_ba,d2xy_ad,d2xy_da,d2xy_cd,d2xy_dc,d2xy_ac,d2xy_ca,
 d2xy_bd,d2xy_db
"""

def hcindex2xy_ad(hcindex,N):

    assert(hcindex <= N**2 - 1)
    positions = ([0,0],[0,1],[1,1],[1,0]) #tuple

    #The last two corresponds to which point of posotions
    last2bits     = hcindex & 3
    cor_position  = positions[last2bits]
    x = cor_position[0]
    y = cor_position[1]

    subsuqarebits = hcindex>>2 # cooresponding to the subsuqare
    m = 0
    while(m <= N):
          m  = 4  # because the first four points have been given
          m2 = m/2
          case = subsuqarebits & 3 # the last two bits
    # in the  quadrant named zero,do flip
        if   case == 0:
           tmp = x
           x   = y
           y   = tmp
    # in the quadrant named one,do transformation
        elif case == 1:
           y   = y + m2 # keep x unchanged
    # in the quadrant named two,do another transformation
        elif case == 2:
           x  = x + m2
           y  = y + m2
    # in the quadrant named three, do rotation around y=-x and transformation
        elif case == 3:
            temp = y
            y    = m2 -1-x
            x    = m2 -1-temp
            x    = x + m2
    # default case
        else:
            print 'The last2bits:',case,' is not anyone of [0,1,2,3]'
            sys.exit('last2bits error')

          subsuqarebits = subsuqarebits>>2 # case /=4,remove the last two bits
          m   *= 2 # iteration,grow 2 times on one direction
    return x,y
