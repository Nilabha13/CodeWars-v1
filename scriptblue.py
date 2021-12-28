from random import randint, choice
base_def = 0
line_robo_alive = [True]*13
robo_count = 0
end_reached = False

i = 16

baseX = None
baseY = None

lineRobotsPosAssumed = [False]*13

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
        
        # scanning the neighbourhood
        sig=robot.GetInitialSignal()
        if sig == '':
                robot.setSignal(robot.GetInitialSignal())
                sig = robot.GetInitialSignal()
        
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
        
        count = 0
        for l in p_list:
                if l == 'enemy' or l == 'enemy-base':
                        count = count + 1
        if count > 1:
                robot.setSignal('double' + str(robotX) + str(robotY))
        else:
                robot.setSignal(robot.GetInitialSignal())

        # line_pos = [1,4,7,10,13,16,]
        # line_pos = [18,19,21,22,18,19,20,21,22,18,19,21,22,]
        line_pos = [14,15,16,17,18,19,20,21,22,23,24,25,26]

        signal_3_5 = sig[3:5] #Vinu: I changed this

        # code for final attack when enemy base is found
        if int(signal_3_5) > 0 and int(signal_3_5) < 22:
                base_signal = robot.GetCurrentBaseSignal()
                if len(base_signal) == 6:
                        enemy_baseX = int(base_signal[2:4])
                        enemy_baseY = int(base_signal[4:])
                        diffX = abs(enemy_baseX - robotX)
                        diffY = abs(enemy_baseY - robotY)
                        if diffX + diffY == 1:
                                f = 0.6
                                robot.DeployVirus(robot.GetVirus()*0)
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

        # lineRobots

        if int(signal_3_5) > 0 and int(signal_3_5) < 14:
                global end_reached

                if not end_reached and robotX == int(robot.GetDimensionX()/4):
                        end_reached = True
                
                if "enemy" in p_list:
                        # if robot.GetVirus() > 1200:
                        #         robot.DeployVirus(robot.GetVirus()*f)
                        # elif robot.GetVirus() > 600:
                        #         robot.DeployVirus(400)
                        #robot.DeployVirus(robot.GetVirus()*0.5)
                        pass

                if "enemy-base" in p_list:
                        f = 0.4
                        #robot.DeployVirus(robot.GetVirus())

                        # x,y below denote the coordinates of enemy base when found
                        x, y = None, None
                        if p_n == 'enemy-base':
                                x = str(robotX).zfill(2)
                                y = str(robotY-1).zfill(2)           
                        
                        if p_s == 'enemy-base':
                                x = str(robotX).zfill(2)
                                y = str(robotY+1).zfill(2)    

                        if p_w == 'enemy-base':
                                x = str(robotX-1).zfill(2)
                                y = str(robotY).zfill(2) 
                        
                        if p_e == 'enemy-base':
                                x = str(robotX+1).zfill(2)
                                y = str(robotY).zfill(2)  
                        
                        if p_se == 'enemy-base':
                                x = str(robotX+1).zfill(2)
                                y = str(robotY+1).zfill(2)   
                        
                        if p_sw == 'enemy-base':
                                x = str(robotX-1).zfill(2)
                                y = str(robotY+1).zfill(2)   
                        
                        if p_ne == 'enemy-base':
                                x = str(robotX+1).zfill(2)
                                y = str(robotY-1).zfill(2)   
                        
                        if p_nw == 'enemy-base':
                                x = str(robotX-1).zfill(2)
                                y = str(robotY-1).zfill(2)   

                        robot.setSignal('eb'+x+y)
                        return 0
                
                # global lineRobotsPosAssumed
                # global line_robo_alive               
 
                # for l in line_pos:
                #         if int(signal_3_5) == (l//3)+1 :
                #                 if robotY>l :
                #                         return 1
                #                 elif robotY<l :
                #                         return 3
                #                 else:
                #                         lineRobotsPosAssumed[l//3] = True
 
                # formation_assembled = True
                # for id in range(1, 14):
                #         if line_robo_alive[id-1] and not lineRobotsPosAssumed[id-1]:
                #                 print("ID: " + str(id))
                #                 formation_assembled = False
                #                 break      
                # # print(formation_assembled)
                # # in above code, if a robot has assumed it's own position, then stay there
                # # if all robots are in formation, then move the line
                if end_reached:
                        return randint(1,4)
                else:
                        return 4        
                # if formation_assembled :
                #         return 4
                # else:
                #         return 0        
        
        #attackers
        if int(signal_3_5) > 13 and int(signal_3_5) < 22:

                base_signal = robot.GetCurrentBaseSignal()
                if len(base_signal) == 10:
                        enemy_baseX = int(base_signal[6:8])
                        enemy_baseY = int(base_signal[8:])
                        diffX = abs(enemy_baseX - robotX)
                        diffY = abs(enemy_baseY - robotY)
                        if diffX + diffY == 1:
                                f = 0.4
                                robot.DeployVirus(robot.GetVirus()*0)
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

                if(robotX >= baseX-1):
                        return 4

                if "enemy-base" in p_list:
                        f = 0.4
                        robot.DeployVirus(robot.GetVirus())

                # scan n
                if p_n == 'enemy':
                        if(robot.GetVirus()>600):
                             robot.DeployVirus(600)  
                        return 3     
                elif p_n == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)
                        robot.setSignal('eb' + x + y)
                        return 0
                                        
                # scan s
                if p_s == 'enemy':
                        if(robot.GetVirus()>600):
                             robot.DeployVirus(600)
                        return 1 
                elif p_s == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                  
                        robot.setSignal('eb' + x + y)
                        return 0        

                # scan e
                if p_e == 'enemy':
                        if(robot.GetVirus()>600):
                             robot.DeployVirus(600)
                        return 4
                elif p_e == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan w
                if p_w == 'enemy':
                        if(robot.GetVirus()>600):
                             robot.DeployVirus(600)
                        return 2
                elif p_w == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan ne
                if p_ne == 'enemy':  
                        if(robot.GetVirus()>600):
                             robot.DeployVirus(600)
                        return 3
                elif p_ne == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan se
                if p_se == 'enemy':
                        if(robot.GetVirus()>600):
                             robot.DeployVirus(600)
                        return 1
                elif p_se == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan nw #
                if p_nw == 'enemy':
                        if(robot.GetVirus()>600):
                             robot.DeployVirus(600)
                        return 3
                elif p_nw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan sw
                if p_sw == 'enemy':
                        if(robot.GetVirus()>600):
                             robot.DeployVirus(600)
                        return 1
                elif p_sw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                            
                return randint(1,4)            

        #side_scouters
        elif int(signal_3_5) > 21 and int(signal_3_5) < 27:
                robotX, robotY = robot.GetPosition()
                if(robotX <= baseX):
                        return 2

                if "enemy-base" in p_list:
                        f = 0.5
                        robot.DeployVirus(robot.GetVirus())
                #Abhijit: i think the above 3 lines are not necessary, maybe just for safety reasons 

                # scan n
                if p_n == 'enemy':
                        if(robot.GetVirus()>600):
                             robot.DeployVirus(600)  
                        return 3     
                elif p_n == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)
                        robot.setSignal('eb' + x + y)
                        return 0        
                        
                # scan s
                if p_s == 'enemy':
                        if(robot.GetVirus()>600):
                             robot.DeployVirus(600)
                        return 1 
                elif p_s == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                  
                        robot.setSignal('eb' + x + y)
                        return 0         

                # scan e
                if p_e == 'enemy':
                        if(robot.GetVirus()>600):
                             robot.DeployVirus(6600)
                        return 4
                elif p_e == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan w
                if p_w == 'enemy':
                        if(robot.GetVirus()>600):
                             robot.DeployVirus(600)
                        return 2
                elif p_w == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan ne
                if p_ne == 'enemy':  
                        if(robot.GetVirus()>600):
                             robot.DeployVirus(600)
                        return 3
                elif p_ne == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan se
                if p_se == 'enemy':
                        if(robot.GetVirus()>600):
                             robot.DeployVirus(600)
                        return 1
                elif p_se == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan nw #
                if p_nw == 'enemy':
                        if(robot.GetVirus()>600):
                             robot.DeployVirus(600)
                        return 3
                elif p_nw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan sw
                if p_sw == 'enemy':
                        if(robot.GetVirus()>600):
                             robot.DeployVirus(600)
                        return 1
                elif p_sw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                        
                return randint(1,4) # why do we have this still? #Abhijit: rather, we can sweep of the back-side area systematically
        
        #defenceRobots
        elif int(signal_3_5) > 26 and int(signal_3_5) < 35:
                if "enemy" in p_list:
                        if robot.GetVirus() > 1600:
                                robot.DeployVirus(1600)
                        elif robot.GetVirus() > 1200:
                                robot.DeployVirus(1000)
                        elif robot.GetVirus() > 600:
                                robot.DeployVirus(400)

                if "enemy-base" in p_list:
                        f = 0.8
                        robot.DeployVirus(robot.GetVirus())                
                #Abhijit: i think the above 3 lines are not necessary, maybe just for safety reasons 
                global i
                if i > 0:
                        if int(signal_3_5) == 27:  #nw
                                robotX, robotY = robot.GetPosition()
                                posX=baseX-1
                                posY=baseY-1
                                if(robotX>posX): 
                                        i-=1
                                        return 4
                                elif(robotY>posY):
                                        i-=1 
                                        return 1
                                else:
                                        i-=1
                                        return 0
                        elif int(signal_3_5) == 28:  #ne
                                robotX, robotY = robot.GetPosition()
                                posX=baseX+1
                                posY=baseY-1
                                if(robotX<posX): 
                                        i-=1
                                        return 2
                                elif(robotY>posY): 
                                        i-=1
                                        return 1
                                else:
                                        i-=1
                                        return 0
                        elif int(signal_3_5) == 29:  #sw
                                robotX, robotY = robot.GetPosition()
                                posX=baseX-1
                                posY=baseY+1
                                if(robotX>posX): 
                                        i-=1
                                        return 4
                                elif(robotY<posY): 
                                        i-=1
                                        return 3
                                else:
                                        i-=1
                                        return 0
                        elif int(signal_3_5) == 30:  #se
                                robotX, robotY = robot.GetPosition()
                                posX=baseX+1
                                posY=baseY+1
                                if(robotX<posX): 
                                        i-=1
                                        return 2
                                elif(robotY<posY): 
                                        i-=1
                                        return 3
                                else:
                                        i-=1
                                        return 0
                        elif int(signal_3_5) == 31:  #n
                                robotX, robotY = robot.GetPosition()
                                posX=baseX
                                posY=baseY-1        
                                if(robotY>posY): 
                                        i-=1
                                        return 1
                                else:
                                        i-=1
                                        return 0
                        elif int(signal_3_5) == 32:  #s
                                robotX, robotY = robot.GetPosition()
                                posX=baseX
                                posY=baseY+1
                                if(robotY<posY): 
                                        i-=1
                                        return 3
                                else:
                                        i-=1
                                        return 0
                        elif int(signal_3_5) == 33:  #w
                                robotX, robotY = robot.GetPosition()
                                posX=baseX-1
                                posY=baseY
                                if(robotX>posX): 
                                        i-=1
                                        return 4
                                else:
                                        i-=1
                                        return 0
                        elif int(signal_3_5) == 34:  #e
                                robotX, robotY = robot.GetPosition()
                                posX=baseX+1
                                posY=baseY
                                if(robotX<posX): 
                                        i-=1
                                        return 2
                                else:
                                        i-=1
                                        return 0
                else:
                        # print("SSSSSS") 
                        # return 0
                        
                        # Rotation for the defence robots

                        #  0 : Let the robot stay where it is
                        #  1 : Let the robot move up
                        #  2 : Let the robot move right
                        #  3 : Let the robot move down
                        #  4 : Let the robot move left

                        # r r r
                        # r b r
                        # r r r


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
                
                        #Vinu : smaller way and easily editable
                        #outp = {(0, -1) : 2, (1, -1) : 3, (1, 0) : 3, (1, 1) : 4, (0, 1) : 4, (-1, 1) : 1, (-1, 0) : 1, (-1, -1) : 2} 
                        # return outp[delta]
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
                if len(l) == 10:
                        base.SetYourSignal(l)
                        break
                else:
                        base.SetYourSignal('')
                        
                
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
                if base.GetVirus() > 1600:
                        base.DeployVirus(1600)
                elif base.GetVirus() > 1000:
                        base.DeployVirus(400)
                elif base.GetVirus() > 600:
                        base.DeployVirus(200)
                elif base.GetVirus() > 200:
                        base.DeployVirus(100)
                else:
                        base.DeployVirus(base.GetVirus())
                                        
        # create robots with unique IDs
        while base.GetElixir() > 300:
                new_sig = cr_robo_sig()  
                base.create_robot(new_sig)

        return

