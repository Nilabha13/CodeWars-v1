from random import randint, choice
base_def = 0
robo_list = []
robo_count = 0

baseX = None
baseY = None

lineRobotsPosAssumed = [False]*13

#########################################

# signal for the newly created robot
def cr_robo_sig():
        global robo_count
        global robo_list
        robo_count += 1
        signal = 'id=' + str(robo_count).zfill(2)
        # robo_list.append(robo_count)
        return signal

def side_scouts():
        pass

#################################################




# > defining some functions for the robots




def ActRobot(robot):
        robotX, robotY = robot.GetPosition()
        
        


        
        # scanning the neighbourhood
        sig=robot.GetYourSignal()
        if sig == '':
                robot.setSignal(robot.GetInitialSignal())
                sig = robot.GetYourSignal()
        
        
        
        p_n = robot.investigate_up()
        p_ne = robot.investigate_ne()
        p_e = robot.investigate_right()
        p_se = robot.investigate_se()
        p_s = robot.investigate_down()
        p_sw = robot.investigate_sw()
        p_w = robot.investigate_left()
        p_nw = robot.investigate_nw()
        p_list = [p_n, p_ne, p_e, p_se, p_s, p_sw, p_w, p_nw]

        # forming the line
        #for i in range(1, 38, 3):
        # pos_line.append(i)
        
        line_pos = [1,4,7,10,13,16,19,22,25,28,31,34,37]

        # lineRobots
        if int(sig[3:5]) > 0 and int(sig[3:5]) < 14:

                for l in line_pos:
                        if int(sig[3:5]) == (l//3)+1 :
                                if robotY>l :
                                        return 1
                                elif robotY<l :
                                        return 3
                                else:
                                        global lineRobotsPosAssumed
                                        lineRobotsPosAssumed[l//3] = True
                                        
                if all(lineRobotsPosAssumed):
                        #here
                        print('hi')
                               

        
        #attackers
        if int(sig[3:5]) > 13 and int(sig[3:5]) < 22:
                if(robotX >= baseX-1):
                        return 4
                # scan n
                if p_n == 'enemy':
                        if(robot.GetVirus()>300):
                             robot.DeployVirus(300)  
                        return 3     
                elif p_n == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)
                        robot.setSignal('eb' + x + y)
                        return 0
                                        
                # scan s
                if p_s == 'enemy':
                        if(robot.GetVirus()>300):
                             robot.DeployVirus(300)
                        return 1 
                elif p_s == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                  
                        robot.setSignal('eb' + x + y)
                        return 0        

                # scan e
                if p_e == 'enemy':
                        if(robot.GetVirus()>300):
                             robot.DeployVirus(300)
                        return 4
                elif p_e == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan w
                if p_w == 'enemy':
                        if(robot.GetVirus()>300):
                             robot.DeployVirus(300)
                        return 2
                elif p_w == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan ne
                if p_ne == 'enemy':  
                        if(robot.GetVirus()>300):
                             robot.DeployVirus(300)
                        return 3
                elif p_ne == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan se
                if p_se == 'enemy':
                        if(robot.GetVirus()>300):
                             robot.DeployVirus(300)
                        return 1
                elif p_se == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan nw #
                if p_nw == 'enemy':
                        if(robot.GetVirus()>300):
                             robot.DeployVirus(300)
                        return 3
                elif p_nw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan sw
                if p_sw == 'enemy':
                        if(robot.GetVirus()>300):
                             robot.DeployVirus(300)
                        return 1
                elif p_sw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                            
                return randint(1,4)            


        #side_scouters
        elif int(sig[3:5]) > 21 and int(sig[3:5]) < 27:
                robotX, robotY = robot.GetPosition()
                if(robotX <= baseX):
                        return 2
                # scan n
                if p_n == 'enemy':
                        if(robot.GetVirus()>300):
                             robot.DeployVirus(300)  
                        return 3     
                elif p_n == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)
                        robot.setSignal('eb' + x + y)
                        return 0        
                        
                # scan s
                if p_s == 'enemy':
                        if(robot.GetVirus()>300):
                             robot.DeployVirus(300)
                        return 1 
                elif p_s == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                  
                        robot.setSignal('eb' + x + y)
                        return 0         

                # scan e
                if p_e == 'enemy':
                        if(robot.GetVirus()>300):
                             robot.DeployVirus(300)
                        return 4
                elif p_e == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan w
                if p_w == 'enemy':
                        if(robot.GetVirus()>300):
                             robot.DeployVirus(300)
                        return 2
                elif p_w == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan ne
                if p_ne == 'enemy':  
                        if(robot.GetVirus()>300):
                             robot.DeployVirus(300)
                        return 3
                elif p_ne == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan se
                if p_se == 'enemy':
                        if(robot.GetVirus()>300):
                             robot.DeployVirus(300)
                        return 1
                elif p_se == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan nw #
                if p_nw == 'enemy':
                        if(robot.GetVirus()>300):
                             robot.DeployVirus(300)
                        return 3
                elif p_nw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan sw
                if p_sw == 'enemy':
                        if(robot.GetVirus()>300):
                             robot.DeployVirus(300)
                        return 1
                elif p_sw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                        
                return randint(1,4) #why do we have this still?
        
        #defenceRobots
        elif int(sig[3:5]) > 26 and int(sig[3:5]) < 31:
                if "enemy" in p_list:
                        if robot.GetVirus() > 800:
                                robot.DeployVirus(600)
                        elif robot.GetVirus() > 600:
                                robot.DeployVirus(300)
                        elif robot.GetVirus() > 300:
                                robot.DeployVirus(100)
                                
                if int(sig[3:5]) == 27:  #nw
                        robotX, robotY = robot.GetPosition()
                        posX=baseX-1
                        posY=baseY-1
                        if(robotX>posX): 
                                return 4
                        if(robotY>posY): 
                                return 1
                elif int(sig[3:5]) == 28:  #ne
                        robotX, robotY = robot.GetPosition()
                        posX=baseX+1
                        posY=baseY-1
                        if(robotX<posX): 
                                return 2
                        if(robotY>posY): 
                                return 1
                elif int(sig[3:5]) == 29:  #sw
                        robotX, robotY = robot.GetPosition()
                        posX=baseX-1
                        posY=baseY+1
                        if(robotX>posX): 
                                return 4
                        if(robotY<posY): 
                                return 3
                elif int(sig[3:5]) == 30:  #se
                        robotX, robotY = robot.GetPosition()
                        posX=baseX+1
                        posY=baseY+1
                        if(robotX<posX): 
                                return 2
                        if(robotY<posY): 
                                return 3

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
        

        
        return 

def ActBase(base):
        global baseX
        global baseY
        baseX, baseY = base.GetPosition()
        
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
                if base.GetVirus() > 800:
                        base.DeployVirus(800)
                elif base.GetVirus() > 500:
                        base.DeployVirus(200)
                elif base.GetVirus() > 300:
                        base.DeployVirus(100)
                elif base.GetVirus() > 100:
                        base.DeployVirus(50)
                else:
                        base.DeployVirus(base.GetVirus())
                                        
        
        
        
        
        
        while base.GetElixir() > 500:
                new_sig = cr_robo_sig()  
                base.create_robot(new_sig)

        return

