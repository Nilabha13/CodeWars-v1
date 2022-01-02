from random import randint
robo_count = 0

#enemy_database = []

del_x = [-1,0,1,1,1,0,-1,-1]
del_y = [-1,-1,-1,0,1,1,1,0]

###########################################

# signal for the newly created robot
def cr_robo_sig():
        global robo_count
        robo_count += 1
        signal = 'id=' + str(robo_count).zfill(2)
        return signal

###########################################

def ActRobot(robot):
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
                robot.DeployVirus(1200)
                   
        if "enemy-base" in p_list:
                robot.DeployVirus(robot.GetVirus())
                for i in range(len(p_list)):
                     if p_list[i] == 'enemy-base':
                             robot.setSignal('eb'+str(robotX+del_x[i]).zfill(2)+str(robotY+del_y[i]).zfill(2))                      

        # NW squad
        if roboid>=1 and roboid<=9:
                if robotX >= baseX:
                        return 4
                if robotY >= baseY:
                        return 1
                return randint(1,4)  
        # NE squad
        if roboid>=9 and roboid<=18:
                if robotX <= baseX:
                        return 2
                if robotY >= baseY:
                        return 1
                return randint(1,4)
        # SE squad
        if roboid>=18 and roboid<=27:
                if robotX <= baseX:
                        return 2
                if robotY <= baseY:
                        return 3
                return randint(1,4)
        # SW squad
        if roboid>=27 and roboid<=36:
                if robotX >= baseX:
                        return 4
                if robotY <= baseY:
                        return 3
                return randint(1,4)

        # final gang up
        if roboid>=1 and roboid <=36:
                base_signal = robot.GetCurrentBaseSignal()
                if len(base_signal) == 6:
                        enemy_baseX = int(base_signal[2:4])
                        enemy_baseY = int(base_signal[4:])
                        diffX = abs(enemy_baseX - robotX)
                        diffY = abs(enemy_baseY - robotY)
                        if diffX + diffY == 1:
                                robot.DeployVirus(robot.GetVirus())
                                return 0
                        else:
                                if robotX < enemy_baseX:
                                        return 2
                                elif robotX > enemy_baseX:
                                        return 4
                                elif robotY < enemy_baseY:
                                        return 3
                                else:
                                        return 1
        
        
def ActBase(base):
        global baseX
        global baseY

        baseX, baseY = base.GetPosition()
        baseX = int(baseX)
        baseY = int(baseY)

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
                base.DeployVirus(2000)
        if "enemy-base" in p_list:
                base.DeployVirus(base.GetVirus())                                

        while base.GetElixir() > 200:
                new_sig = cr_robo_sig()  
                base.create_robot(new_sig)

        return
