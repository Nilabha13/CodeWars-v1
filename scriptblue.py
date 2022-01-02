from random import randint, choice
base_def = 0
line_robo_alive = [True]*13
robo_count = 0

i = 16
j = 32
k = 6

baseX = None
baseY = None
attackersPosAssumed = False
originMirrorPosAssumed = False
xMirrorPosAssumed = False
yMirrorPosAssumed = False
diagonal1PosAssumed = False
diagonal2PosAssumed = False

lineRobotsPosAssumed = [False]*13

en_nw = [2,3,4,4,]
en_n = []
en_ne = []
en_e = []
en_se = []
en_s = []
en_sw = []
en_w = []

robo_virus_save_check = [True]*30
robo_virus_save = []

#########################################

# signal for the newly created robot
def cr_robo_sig():
        global robo_count
        robo_count += 1
        signal = 'id=' + str(robo_count).zfill(2)
        # robo_list.append(robo_count)
        return signal

#################################################

def ActRobot(robot):
        robotX, robotY = robot.GetPosition()
        X, Y = robot.GetDimensionX(), robot.GetDimensionY()

        # getting the robot signal        
        sig=robot.GetInitialSignal()
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
        p_list = [p_n, p_ne, p_e, p_se, p_s, p_sw, p_w, p_nw]

        # tracking multiple enemies
        count = 0
        for l in p_list:
            if l == 'enemy':
                count+=1
        if count > 1:
            robot.setSignal("db" + str(robotX) + str(robotY)) #Abhijit : replaced double with db to avoid conflict
        else:
            robot.setSignal(robot.GetInitialSignal())    


        roboid = sig[3:5] #Abhijit : I changed this
        

        # robots 17-28 will gang up on the enemy base when it is found
        if int(roboid) > 16 and int(roboid) < 32:
                base_signal = robot.GetCurrentBaseSignal()
                if len(base_signal) == 6 :
                        if base_signal[:2] == 'eb' :
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
                        else :
                                if int(roboid) > 16 and int(roboid) < 22 :
                                        double_robotX = int(base_signal[2:4])
                                        double_robotY = int(base_signal[4:])
                                        diffX = abs(double_robotX - robotX)
                                        diffY = abs(double_robotY - robotY)
                                        if diffX + diffY == 1:
                                                robot.DeployVirus(robot.GetVirus()*0.4)
                                                return 0
                                        else:
                                                if robotX < double_robotX:
                                                        return 2
                                                elif robotX > double_robotX:
                                                        return 4
                                                elif robotY < double_robotY:
                                                        return 3
                                                else:
                                                        return 1
                
        #defenceRobots_1
        elif int(roboid) > 0 and int(roboid) < 9:
                global i
                if "enemy" in p_list:
                        if robot.GetVirus() > 1200:
                                robot.DeployVirus(1000)
                        elif robot.GetVirus() > 800:
                                robot.DeployVirus(600)
                        elif robot.GetVirus() > 300:
                                robot.DeployVirus(200)

                if "enemy-base" in p_list:
                        robot.DeployVirus(robot.GetVirus())                
                if i > 0:                
                    if int(roboid) == 1:  #nw
                            robotX, robotY = robot.GetPosition()
                            posX=baseX-1
                            posY=baseY-1
                            if(robotX>posX):
                                    i-=1 
                                    return 4
                            if(robotY>posY):
                                    i-=1  
                                    return 1
                    elif int(roboid) == 2:  #ne
                            robotX, robotY = robot.GetPosition()
                            posX=baseX+1
                            posY=baseY-1
                            if(robotX<posX):
                                    i-=1  
                                    return 2
                            if(robotY>posY):
                                    i-=1  
                                    return 1
                    elif int(roboid) == 3:  #sw
                            robotX, robotY = robot.GetPosition()
                            posX=baseX-1
                            posY=baseY+1
                            if(robotX>posX):
                                    i-=1  
                                    return 4
                            if(robotY<posY):
                                    i-=1  
                                    return 3
                    elif int(roboid) == 4:  #se
                            robotX, robotY = robot.GetPosition()
                            posX=baseX+1
                            posY=baseY+1
                            if(robotX<posX):
                                    i-=1  
                                    return 2
                            if(robotY<posY):
                                    i-=1  
                                    return 3
                    elif int(roboid) == 5:  #n
                            robotX, robotY = robot.GetPosition()
                            posX=baseX
                            posY=baseY-1
                            if(robotX>posX):
                                    i-=1  
                                    return 4
                            if(robotY>posY):
                                    i-=1  
                                    return 1
                    elif int(roboid) == 6:  #s
                            robotX, robotY = robot.GetPosition()
                            posX=baseX
                            posY=baseY+1
                            if(robotX<posX):
                                    i-=1  
                                    return 2
                            if(robotY>posY):
                                    i-=1  
                                    return 1
                    elif int(roboid) == 7:  #w
                            robotX, robotY = robot.GetPosition()
                            posX=baseX-1
                            posY=baseY
                            if(robotX>posX):
                                    i-=1  
                                    return 4
                            if(robotY<posY):
                                    i-=1  
                                    return 3
                    elif int(roboid) == 8:  #e
                            robotX, robotY = robot.GetPosition()
                            posX=baseX+1
                            posY=baseY
                            if(robotX<posX):
                                    i-=1  
                                    return 2
                            if(robotY<posY):
                                    i-=1  
                                    return 3
                else:
                    #Rotation
                    deltaX = robotX - baseX
                    deltaY = robotY - baseY
                    delta = (deltaX, deltaY)

                    if delta == (0, -1):
                            return 2
                    elif delta == (1, -1):
                            return 3
                    elif delta == (1, 0):
                            return 3
                    elif delta == (1, 1):
                            return 4
                    elif delta == (0, 1):
                            return 4
                    elif delta == (-1, 1):
                            return 1
                    elif delta == (-1, 0):
                            return 1
                    elif delta == (-1, -1):
                            return 2

        #defenceRobots_2
        elif int(roboid) > 8 and int(roboid) < 17:
                global j
                if "enemy" in p_list:
                        if robot.GetVirus() > 1200:
                                robot.DeployVirus(1000)
                        elif robot.GetVirus() > 800:
                                robot.DeployVirus(600)
                        elif robot.GetVirus() > 300:
                                robot.DeployVirus(200)

                if "enemy-base" in p_list:
                        robot.DeployVirus(robot.GetVirus())                
                if j > 0:                
                    if int(roboid) == 9:  #nw
                            robotX, robotY = robot.GetPosition()
                            posX=baseX-2
                            posY=baseY-2
                            if(robotX>posX):
                                    i-=1 
                                    return 4
                            if(robotY>posY):
                                    i-=1  
                                    return 1
                    elif int(roboid) == 10:  #ne
                            robotX, robotY = robot.GetPosition()
                            posX=baseX+2
                            posY=baseY-2
                            if(robotX<posX):
                                    i-=1  
                                    return 2
                            if(robotY>posY):
                                    i-=1  
                                    return 1
                    elif int(roboid) == 11:  #sw
                            robotX, robotY = robot.GetPosition()
                            posX=baseX-2
                            posY=baseY+2
                            if(robotX>posX):
                                    i-=1  
                                    return 4
                            if(robotY<posY):
                                    i-=1  
                                    return 3
                    elif int(roboid) == 12:  #se
                            robotX, robotY = robot.GetPosition()
                            posX=baseX+2
                            posY=baseY+2
                            if(robotX<posX):
                                    i-=1  
                                    return 2
                            if(robotY<posY):
                                    i-=1  
                                    return 3
                    elif int(roboid) == 13:  #n
                            robotX, robotY = robot.GetPosition()
                            posX=baseX
                            posY=baseY-2
                            if(robotX>posX):
                                    i-=1  
                                    return 4
                            if(robotY>posY):
                                    i-=1  
                                    return 1
                    elif int(roboid) == 14:  #s
                            robotX, robotY = robot.GetPosition()
                            posX=baseX
                            posY=baseY+2
                            if(robotX<posX):
                                    i-=1  
                                    return 2
                            if(robotY>posY):
                                    i-=1  
                                    return 1
                    elif int(roboid) == 15:  #w
                            robotX, robotY = robot.GetPosition()
                            posX=baseX-2
                            posY=baseY
                            if(robotX>posX):
                                    i-=1  
                                    return 4
                            if(robotY<posY):
                                    i-=1  
                                    return 3
                    elif int(roboid) == 16:  #e
                            robotX, robotY = robot.GetPosition()
                            posX=baseX+2
                            posY=baseY
                            if(robotX<posX):
                                    i-=1  
                                    return 2
                            if(robotY<posY):
                                    i-=1  
                                    return 3
                else:
                    #Rotation
                    deltaX = robotX - baseX
                    deltaY = robotY - baseY
                    delta = (deltaX, deltaY)

                    if delta == (2, -2) or delta == (1, -2) or delta == (0, -2) or delta == (-1, -2) :
                            return 4
                    elif delta == (-2, -2) or delta == (-2, -1) or delta == (-2, 0) or delta == (-2, 1) :
                            return 3
                    elif delta == (-2, 2) or delta == (-1, 2) or delta == (0, 2) or delta == (1, 2) :
                            return 2
                    elif delta == (2, 2) or delta == (2, 1) or delta == (2, 0) or delta == (2, -1) :
                            return 1                
            
        #attackers
        if int(roboid) > 16 and int(roboid) < 22:
                global attackersPosAssumed
                if(robotX >= baseX-1):
                        return 4

                if "enemy-base" in p_list:
                        robot.DeployVirus(robot.GetVirus())

                # scan n
                if p_n == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)       
                        if attackersPosAssumed:
                            return 3
                        if robotX > X//4:
                            return 4    
                        else:
                            attackersPosAssumed = True    
                elif p_n == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)
                        robot.setSignal('eb' + x + y)
                        return 0
                                        
                # scan s
                if p_s == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)       
                        if attackersPosAssumed:
                            return 1
                        if robotX > X//4:
                            return 4    
                        else:
                            attackersPosAssumed = True 
                elif p_s == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                  
                        robot.setSignal('eb' + x + y)
                        return 0        

                # scan e
                if p_e == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)       
                        if attackersPosAssumed:
                            return 4
                        if robotX > X//4:
                            return 4    
                        else:
                            attackersPosAssumed = True
                elif p_e == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan w
                if p_w == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)       
                        if attackersPosAssumed:
                            return 2
                        if robotX > X//4:
                            return 4    
                        else:
                            attackersPosAssumed = True
                elif p_w == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan ne
                if p_ne == 'enemy':  
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)       
                        if attackersPosAssumed:
                            return 3
                        if robotX > X//4:
                            return 4    
                        else:
                            attackersPosAssumed = True
                elif p_ne == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan se
                if p_se == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)       
                        if attackersPosAssumed:
                            return 1
                        if robotX > X//4:
                            return 4    
                        else:
                            attackersPosAssumed = True
                elif p_se == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan nw
                if p_nw == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)       
                        if attackersPosAssumed:
                            return 3
                        if robotX > X//4:
                            return 4    
                        else:
                            attackersPosAssumed = True
                elif p_nw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan sw
                if p_sw == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)       
                        if attackersPosAssumed:
                            return 1
                        if robotX > X//4:
                            return 4    
                        else:
                            attackersPosAssumed = True
                elif p_sw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                            
                if attackersPosAssumed:                 
                    return randint(1,4)            


        #OriginMirror
        elif int(roboid) > 21 and int(roboid) < 24:
                posX = X - baseX
                posY = Y - baseY
                global originMirrorPosAssumed
                
                if "enemy-base" in p_list:
                        robot.DeployVirus(robot.GetVirus())

                # scan n
                if p_n == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)           
                elif p_n == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)
                        robot.setSignal('eb' + x + y)
                        return 0        
                        
                # scan s
                if p_s == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500) 
                elif p_s == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                  
                        robot.setSignal('eb' + x + y)
                        return 0         

                # scan e
                if p_e == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_e == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan w
                if p_w == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_w == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan ne
                if p_ne == 'enemy':  
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_ne == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan se
                if p_se == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_se == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan nw
                if p_nw == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_nw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan sw
                if p_sw == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_sw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0

                if not originMirrorPosAssumed:
                    if robotX > posX:
                        return 4
                    elif robotX < posX:
                        return 2
                    elif robotY > posY:
                        return 1
                    elif robotY < posY:
                        return 3
                    else:
                        originMirrorPosAssumed = True                          
                else:            
                    return randint(1,4)

        #XMirror
        elif int(roboid) > 23 and int(roboid) < 26:
                posX = baseX
                posY = Y - baseY
                global xMirrorPosAssumed
                
                if "enemy-base" in p_list:
                        robot.DeployVirus(robot.GetVirus())

                # scan n
                if p_n == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)           
                elif p_n == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)
                        robot.setSignal('eb' + x + y)
                        return 0        
                        
                # scan s
                if p_s == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500) 
                elif p_s == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                  
                        robot.setSignal('eb' + x + y)
                        return 0         

                # scan e
                if p_e == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_e == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan w
                if p_w == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_w == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan ne
                if p_ne == 'enemy':  
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_ne == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan se
                if p_se == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_se == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan nw
                if p_nw == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_nw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan sw
                if p_sw == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_sw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0

                if not xMirrorPosAssumed:
                    if robotX > posX:
                        return 4
                    elif robotX < posX:
                        return 2
                    elif robotY > posY:
                        return 1
                    elif robotY < posY:
                        return 3
                    else:
                        xMirrorPosAssumed = True                          
                else:            
                    return randint(1,4)

        #YMirror
        elif int(roboid) > 25 and int(roboid) < 28:
                posX = X - baseX
                posY = baseY
                global yMirrorPosAssumed
                
                if "enemy-base" in p_list:
                        robot.DeployVirus(robot.GetVirus())

                # scan n
                if p_n == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)           
                elif p_n == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)
                        robot.setSignal('eb' + x + y)
                        return 0        
                        
                # scan s
                if p_s == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500) 
                elif p_s == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                  
                        robot.setSignal('eb' + x + y)
                        return 0         

                # scan e
                if p_e == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_e == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan w
                if p_w == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_w == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan ne
                if p_ne == 'enemy':  
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_ne == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan se
                if p_se == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_se == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan nw
                if p_nw == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_nw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan sw
                if p_sw == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_sw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0

                if not yMirrorPosAssumed:
                    if robotX > posX:
                        return 4
                    elif robotX < posX:
                        return 2
                    elif robotY > posY:
                        return 1
                    elif robotY < posY:
                        return 3
                    else:
                        yMirrorPosAssumed = True                          
                else:            
                    return randint(1,4)
        
        #diagonal1mirror
        elif int(roboid) > 27 and int(roboid) < 30:
                posY = (2*X*Y*baseX + Y*Y*baseY - X*X*baseY) // (X*X + Y*Y)
                posX = (2*X*Y*baseY + X*X*baseX - Y*Y*baseX) // (X*X + Y*Y)
                global diagonal1PosAssumed
                
                if "enemy-base" in p_list:
                        robot.DeployVirus(robot.GetVirus())

                # scan n
                if p_n == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)           
                elif p_n == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)
                        robot.setSignal('eb' + x + y)
                        return 0        
                        
                # scan s
                if p_s == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500) 
                elif p_s == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                  
                        robot.setSignal('eb' + x + y)
                        return 0         

                # scan e
                if p_e == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_e == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan w
                if p_w == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_w == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan ne
                if p_ne == 'enemy':  
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_ne == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan se
                if p_se == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_se == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan nw
                if p_nw == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_nw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan sw
                if p_sw == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                             robot.DeployVirus(500)
                elif p_sw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0

                if not diagonal1PosAssumed:
                    if robotX > posX:
                        return 4
                    elif robotX < posX:
                        return 2
                    elif robotY > posY:
                        return 1
                    elif robotY < posY:
                        return 3
                    else:
                        diagonal1PosAssumed = True                          
                else:            
                    return randint(1,4)
        
        #diagonal2mirror
        elif int(roboid) > 29 and int(roboid) < 32:
                posX = (baseX*X*X + 2*X*Y*Y - baseX*Y*Y - 2*baseY*X*Y) // (X*X + Y*Y)
                posY = (baseY*Y*Y + 2*Y*X*X - baseY*X*X - 2*baseX*X*Y) // (X*X + Y*Y)
                global diagonal2PosAssumed
                
                if "enemy-base" in p_list:
                        robot.DeployVirus(robot.GetVirus())

                # scan n
                if p_n == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)           
                elif p_n == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)
                        robot.setSignal('eb' + x + y)
                        return 0        
                        
                # scan s
                if p_s == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500) 
                elif p_s == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                  
                        robot.setSignal('eb' + x + y)
                        return 0         

                # scan e
                if p_e == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_e == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan w
                if p_w == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_w == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan ne
                if p_ne == 'enemy':  
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_ne == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan se
                if p_se == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_se == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan nw
                if p_nw == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)
                elif p_nw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan sw
                if p_sw == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                             robot.DeployVirus(500)
                elif p_sw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0

                if not diagonal2PosAssumed:
                    if robotX > posX:
                        return 4
                    elif robotX < posX:
                        return 2
                    elif robotY > posY:
                        return 1
                    elif robotY < posY:
                        return 3
                    else:
                        diagonal2PosAssumed = True                          
                else:            
                    return randint(1,4)
        

        #scouters
        elif int(roboid) == 32:
                if(robotX <= baseX):
                        return 2

                if "enemy-base" in p_list:
                        robot.DeployVirus(robot.GetVirus())

                # scan n
                if p_n == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)       
                        return 3     
                elif p_n == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)
                        robot.setSignal('eb' + x + y)
                        return 0        
                        
                # scan s
                if p_s == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)       
                        return 3 
                elif p_s == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                  
                        robot.setSignal('eb' + x + y)
                        return 0         

                # scan e
                if p_e == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)       
                        return 3
                elif p_e == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan w
                if p_w == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)       
                        return 3
                elif p_w == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan ne
                if p_ne == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)       
                        return 3
                elif p_ne == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan se
                if p_se == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)       
                        return 3
                elif p_se == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan nw #
                if p_nw == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)       
                        return 3
                elif p_nw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan sw
                if p_sw == 'enemy':
                        if(robot.GetVirus()>800):
                             robot.DeployVirus(800)
                        else:
                            robot.DeployVirus(500)       
                        return 3
                elif p_sw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                        
                return randint(1,4)
        else:
            global k
            scout2X = baseX + 1
            scout3X = baseX + 3
            if "enemy-base" in p_list:
                        robot.DeployVirus(robot.GetVirus())

            # scan n
            if p_n == 'enemy':
                    if(robot.GetVirus()>800):
                         robot.DeployVirus(800)
                    else:
                            robot.DeployVirus(500)           
            elif p_n == 'enemy-base':
                    x = str(robotX).zfill(2)
                    y = str(-1 + robotY).zfill(2)
                    robot.setSignal('eb' + x + y)
                    return 0        
                        
            # scan s
            if p_s == 'enemy':
                    if(robot.GetVirus()>800):
                         robot.DeployVirus(800)
                    else:
                        robot.DeployVirus(500) 
            elif p_s == 'enemy-base':
                    x = str(robotX).zfill(2)
                    y = str(1 + robotY).zfill(2)                  
                    robot.setSignal('eb' + x + y)
                    return 0         

            # scan e
            if p_e == 'enemy':
                    if(robot.GetVirus()>800):
                         robot.DeployVirus(800)
                    else:
                        robot.DeployVirus(500)
            elif p_e == 'enemy-base':
                    x = str(1 + robotX).zfill(2)
                    y = str(robotY).zfill(2)                
                    robot.setSignal('eb' + x + y)
                    return 0
                
            # scan w
            if p_w == 'enemy':
                    if(robot.GetVirus()>800):
                         robot.DeployVirus(800)
                    else:
                        robot.DeployVirus(500)
            elif p_w == 'enemy-base':
                    x = str(-1 + robotX).zfill(2)
                    y = str(robotY).zfill(2)                
                    robot.setSignal('eb' + x + y)
                    return 0
                
            # scan ne
            if p_ne == 'enemy':  
                    if(robot.GetVirus()>800):
                         robot.DeployVirus(800)
                    else:
                        robot.DeployVirus(500)
            elif p_ne == 'enemy-base':
                    x = str(1 + robotX).zfill(2)
                    y = str(-1 + robotY).zfill(2)                 
                    robot.setSignal('eb' + x + y)
                    return 0
            
            # scan se
            if p_se == 'enemy':
                    if(robot.GetVirus()>800):
                        robot.DeployVirus(800)
                    else:
                        robot.DeployVirus(500)
            elif p_se == 'enemy-base':
                    x = str(1 + robotX).zfill(2)
                    y = str(1 + robotY).zfill(2)                 
                    robot.setSignal('eb' + x + y)
                    return 0
                
            # scan nw
            if p_nw == 'enemy':
                    if(robot.GetVirus()>800):
                         robot.DeployVirus(800)
                    else:
                        robot.DeployVirus(500)
            elif p_nw == 'enemy-base':
                    x = str(-1 + robotX).zfill(2)
                    y = str(-1 + robotY).zfill(2)                 
                    robot.setSignal('eb' + x + y)
                    return 0
            
            # scan sw
            if p_sw == 'enemy':
                    if(robot.GetVirus()>800):
                         robot.DeployVirus(800)
                    else:
                        robot.DeployVirus(500)
            elif p_sw == 'enemy-base':
                    x = str(-1 + robotX).zfill(2)
                    y = str(1 + robotY).zfill(2)                 
                    robot.setSignal('eb' + x + y)
                    return 0

            if k > 0:
                if int(roboid) == 33:
                    if(robotX < scout2X):
                        k-=1
                        return 2
                    else:
                        k-=1
                        return 0
                elif int(roboid) == 34:
                    if(robotX < scout3X):
                        k-=1
                        return 2
                    else:
                        k-=1
                        return 0
            else:
                if int(roboid) == 33:
                    if robotX == scout2X:
                        return 1
                    elif robotY == 2:
                        return 2
                    elif robotX == X-2:
                        return 3
                    elif robotY == Y-2:
                        return 4
                elif int(roboid) == 34:
                    if robotX == scout3X:
                        return 1
                    elif robotY == 4:
                        return 2
                    elif robotX == X-4:
                        return 3
                    elif robotY == Y-4:
                        return 4       

        
        return randint(1,4)

def ActBase(base):
        
        global baseX
        global baseY
        global robo_list
        baseX, baseY = base.GetPosition()

        los = base.GetListOfSignals()
        for id in range(1, 14):
                if ("id=" + str(id).zfill(2)) not in los:
                        line_robo_alive[id-1] = False
        
        for l in los:
                if len(l) == 6:
                        base.SetYourSignal(l)
                        break
                elif len(l) == 10:
                        base.SetYourSignal(l)
                        break
                else:
                    base.SetYourSignal('')    
        
        # > defining some functions for base  
        # create robots with unique IDs
        
        #scan nbh
        p_n = base.investigate_up()
        p_ne = base.investigate_ne()
        p_e = base.investigate_right()
        p_se = base.investigate_se()
        p_s = base.investigate_down()
        p_sw = base.investigate_sw()
        p_w = base.investigate_left()
        p_nw = base.investigate_nw()
        p_list = [p_n, p_ne, p_e, p_se, p_s, p_sw, p_w, p_nw]
        
        if "enemy" in p_list:
                if base.GetVirus() > 1000:
                        base.DeployVirus(1000)
                elif base.GetVirus() > 700:
                        base.DeployVirus(700)
                elif base.GetVirus() > 500:
                        base.DeployVirus(500)
                else:
                        base.DeployVirus(base.GetVirus())
                                        
        
        while base.GetElixir() > 300:
                new_sig = cr_robo_sig()  
                base.create_robot(new_sig)

        return

