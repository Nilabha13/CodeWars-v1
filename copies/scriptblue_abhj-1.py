from random import randint
robo_count = 0
#closest = None
ret = []

"""
nw_sq = [1,2,3]
n_sq = [4,5,6]
ne_sq = [7,8,9]
e_sq = [10,11,12]
se_sq = [13,14,15]
s_sq = [16,17,18]
sw_sq = [19,20,21]
w_sq = [22,23,24]
"""

i_form_check =  [False]*24
f_form_check =  [True]*24

enemy_database = []

del_x = [-1,0,1,1,1,0,-1,-1]
del_y = [-1,-1,-1,0,1,1,1,0]
###########################################

# signal for the newly created robot
def cr_robo_sig():
        global robo_count
        robo_count += 1
        signal = 'id=' + str(robo_count).zfill(2)
        # robo_list.append(robo_count)
        return signal

###########################################

def ActRobot(robot):
        global enemy_database
        global i_form_x
        global i_form_y
        global i_form_check
        global f_form_check
        global closest
        global p
        p=0

        # i_form_x = [-2,-3,-4,0,0,0,2,3,4,2,3,4,2,3,4,0,0,0,-2,-3,-4,-2,-3,-4]
        # i_form_y = [-2,-3,-4,-2,-3,-4,-2,-3,-4,0,0,0,2,3,4,2,3,4,2,3,4,0,0,0]
        i_form_x = [-2,-3,0,0,2,3,2,3,2,3,0,0,-2,-3,-2,-3]
        i_form_y = [-2,-3,-2,-3,-2,-3,0,0,2,3,2,3,2,3,0,0]

        robotX, robotY = robot.GetPosition()
        robotX = int(robotX)
        robotY = int(robotY)
        # getting the robot signal        
        sig=robot.GetYourSignal()
        if sig == '':
                robot.setSignal(robot.GetInitialSignal())
                sig = robot.GetYourSignal()
        # ofc this function is only called by'alive' robots
        # so signal being blank can only mean a new robot popped up
        
        # scanning the neighbourhood
        p_n = robot.investigate_up()
        p_ne = robot.investigate_ne()
        p_e = robot.investigate_right()
        p_se = robot.investigate_se()
        p_s = robot.investigate_down()
        p_sw = robot.investigate_sw()
        p_w = robot.investigate_left()
        p_nw = robot.investigate_nw()
        p_list = [p_nw, p_n, p_ne, p_e, p_se, p_s, p_sw, p_w]

        roboid = int(sig[3:5]) #Abhijit : I changed this
        
        if "enemy" in p_list:
                robot.DeployVirus(0.8*robot.GetVirus())
                for i in range(len(p_list)):
                     if p_list[i] == 'enemy':
                             enemy_database.append(str(robotX+del_x[i]).zfill(2)+str(robotY+del_y[i]).zfill(2))
        if "enemy-base" in p_list:
                robot.DeployVirus(robot.GetVirus())
                for i in range(len(p_list)):
                     if p_list[i] == 'enemy-base':
                             robot.setSignal('eb'+str(robotX+del_x[i]).zfill(2)+str(robotY+del_y[i]).zfill(2))                      

        # Defend and Attack squad
        if roboid>=1 and roboid<=16:
                if all(i_form_check) == True and roboid%3 != 0:
                        if f_form_check[roboid-1] == True:
                                f_form_check[roboid-1] = False
                                return randint(1,4)
                        else:
                                f_form_check[roboid-1] = True
                                if robotX > baseX + i_form_x[roboid-1]:
                                        return 4
                                elif robotX < baseX + i_form_x[roboid-1]:
                                        return 2
                                if robotY > baseY + i_form_y[roboid-1]:
                                        return 1
                                elif robotY < baseY + i_form_y[roboid-1]:
                                        return 3
                else:
                        diffX = (robotX - baseX) - i_form_x[roboid-1]
                        diffY = (robotY - baseY) - i_form_y[roboid-1]

                        if diffX > 0:
                                return 4
                        elif diffX < 0:
                                return 2
                        if diffY > 0:
                                return 1
                        elif diffY < 0:
                                return 3
                        # else
                        i_form_check[roboid-1] = True
                        return 0
                        
        # Scout squad
        if roboid>=17 and roboid<=28:
                if "enemy" in p_list:
                        robot.DeployVirus(0.8*robot.GetVirus())
                for i in range(len(p_list)):
                     if p_list[i] == 'enemy':
                             enemy_database.append(str(robotX+del_x[i]).zfill(2)+str(robotY+del_y[i]).zfill(2))
                if "enemy-base" in p_list:
                        robot.DeployVirus(robot.GetVirus())
                for i in range(len(p_list)):
                     if p_list[i] == 'enemy-base':
                             robot.setSignal('eb'+str(robotX+del_x[i]).zfill(2)+str(robotY+del_y[i]).zfill(2))                      

                print(closest)
                # wall-check
                if closest == 'left'and robotX >= baseX:
                        return 4
                elif robotX < baseX:
                        return randint(1,3)
                if closest == 'up'and robotY >= baseY:
                        return 1
                elif robotY < baseY:
                        return randint(2,4)
                if closest == 'right'and robotX <= baseX:
                        return 2
                elif robotX < baseX:
                        p = randint(1,3)
                        if p==2:
                                p += 2
                        return p
                if closest == 'down' and robotY <= baseY:
                        return 3
                elif closest == 'down' and robotY < baseY:
                        p = randint(1,3)
                        if p==3:
                                p += 1
                        return p                              

        #return randint(1,4)

def ActBase(base):
        global baseX
        global baseY
        global robo_list
        global closest

        baseX, baseY = base.GetPosition()
        baseX = int(baseX)
        baseY = int(baseY)

        # finding the closest wall to our base
        global tmpX
        global tmpX_ori
        global tmpY
        global tmpY_ori
        tmpX = 0
        tmpX_ori = ''
        tmpY = 0
        tmpY_ori = ''

        if baseX >= 20:
                tmpX = 40-baseX
                tmpX_ori = 'right'
        elif baseX <19:
                tmpX = baseX
                tmpX_ori = 'left'

        if baseY >= 20:
                tmpY = 40-baseY
                tmpY_ori = 'down'
        elif baseY < 19:
                tmpY = baseY
                tmpY_ori = 'up'
        
        if tmpY <= tmpX :
                closest = tmpY_ori
        elif tmpX < tmpY :
                closest = tmpX_ori
        
        #scan neighbourhood
        p_n = base.investigate_up()
        p_ne = base.investigate_ne()
        p_e = base.investigate_right()
        p_se = base.investigate_se()
        p_s = base.investigate_down()
        p_sw = base.investigate_sw()
        p_w = base.investigate_left()
        p_nw = base.investigate_nw()
        p_list = [p_nw, p_n, p_ne, p_e, p_se, p_s, p_sw, p_w]
        
        
        if "enemy" in p_list:
                base.DeployVirus(0.8*base.GetVirus())
        if "enemy-base" in p_list:
                base.DeployVirus(base.GetVirus())                                

        while base.GetElixir() > 600:
                new_sig = cr_robo_sig()  
                base.create_robot(new_sig)

        return
