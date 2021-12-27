from random import randint

robo_count = 0
robots = []

def master():
        # abcxyz

        def cr_robo_sig():
                robo_count += 1
                if robo_count<10:
                        signal = 'iid=0' + robo_count
                elif robo_count>9 and robo_count<31:
                        signal = 'iid=' + robo_count
                
                return signal

        # scanning the neighbourhood
        def scan_nbh():
                # scan n
                p = robot.investigate_up()
                sig_n = ''
                if p == 'enemy':
                        x = robot.GetDimensionX() 
                        y = 1 + robot.GetDimensionY()
                        if x<10:
                                x = '0' + x  
                        if y<10:
                                y = '0' + y                  
                        sig_n = 'en' + x + y
                elif p == 'enemy-base':
                        x = robot.GetDimensionX() 
                        y = 1 + robot.GetDimensionY()
                        if x<10:
                                x = '0' + x  
                        if y<10:
                                y = '0' + y                  
                        sig_n = 'eb' + x + y
                # scan s
                p = robot.investigate_down()
                sig_s = ''
                if p == 'enemy':
                        x = robot.GetDimensionX() 
                        y = -1 + robot.GetDimensionY()
                        if x<10:
                                x = '0' + x  
                        if y<10:
                                y = '0' + y                  
                        sig_s = 'en' + x + y
                elif p == 'enemy-base':
                        x = robot.GetDimensionX() 
                        y = -1 + robot.GetDimensionY()
                        if x<10:
                                x = '0' + x  
                        if y<10:
                                y = '0' + y                  
                        sig_s = 'eb' + x + y
                # scan e
                p = robot.investigate_right()
                sig_e = ''
                if p == 'enemy':
                        x = 1 + robot.GetDimensionX() 
                        y = robot.GetDimensionY()
                        if x<10:
                                x = '0' + x  
                        if y<10:
                                y = '0' + y                  
                        sig_e = 'en' + x + y
                elif p == 'enemy-base':
                        x = 1 + robot.GetDimensionX() 
                        y = robot.GetDimensionY()
                        if x<10:
                                x = '0' + x  
                        if y<10:
                                y = '0' + y                  
                        sig_e = 'eb' + x + y
                # scan w
                p = robot.investigate_left()
                sig_w = ''
                if p == 'enemy':
                        x = -1 + robot.GetDimensionX() 
                        y = robot.GetDimensionY()
                        if x<10:
                                x = '0' + x  
                        if y<10:
                                y = '0' + y                  
                        sig_w = 'en' + x + y
                elif p == 'enemy-base':
                        x = -1 + robot.GetDimensionX() 
                        y = robot.GetDimensionY()
                        if x<10:
                                x = '0' + x  
                        if y<10:
                                y = '0' + y                  
                        sig_w = 'eb' + x + y
                # scan ne
                p = robot.investigate_ne()
                sig_ne = ''
                if p == 'enemy':
                        x = 1 + robot.GetDimensionX() 
                        y = 1 + robot.GetDimensionY()
                        if x<10:
                                x = '0' + x  
                        if y<10:
                                y = '0' + y                  
                        sig_ne = 'en' + x + y
                elif p == 'enemy-base':
                        x = 1 + robot.GetDimensionX() 
                        y = 1 + robot.GetDimensionY()
                        if x<10:
                                x = '0' + x  
                        if y<10:
                                y = '0' + y                  
                        sig_ne = 'eb' + x + y
                # scan se
                p = robot.investigate_se()
                sig_se = ''
                if p == 'enemy':
                        x = 1 + robot.GetDimensionX() 
                        y = -1 + robot.GetDimensionY()
                        if x<10:
                                x = '0' + x  
                        if y<10:
                                y = '0' + y                  
                        sig_se = 'en' + x + y
                elif p == 'enemy-base':
                        x = 1 + robot.GetDimensionX() 
                        y = -1 + robot.GetDimensionY()
                        if x<10:
                                x = '0' + x  
                        if y<10:
                                y = '0' + y                  
                        sig_se = 'eb' + x + y
                # scan nw
                p = robot.investigate_nw()
                sig_nw = ''
                if p == 'enemy':
                        x = -1 + robot.GetDimensionX() 
                        y = 1 + robot.GetDimensionY()
                        if x<10:
                                x = '0' + x  
                        if y<10:
                                y = '0' + y                  
                        sig_nw = 'en' + x + y
                elif p == 'enemy-base':
                        x = -1 + robot.GetDimensionX() 
                        y = 1 + robot.GetDimensionY()
                        if x<10:
                                x = '0' + x  
                        if y<10:
                                y = '0' + y                  
                        sig_nw = 'eb' + x + y
                # scan sw
                p = robot.investigate_sw()
                sig_sw = ''
                if p == 'enemy':
                        x = -1 + robot.GetDimensionX() 
                        y = -1 + robot.GetDimensionY()
                        if x<10:
                                x = '0' + x  
                        if y<10:
                                y = '0' + y                  
                        sig_sw = 'en' + x + y
                elif p == 'enemy-base':
                        x = -1 + robot.GetDimensionX() 
                        y = -1 + robot.GetDimensionY()
                        if x<10:
                                x = '0' + x  
                        if y<10:
                                y = '0' + y                  
                        sig_sw = 'eb' + x + y

                return (sig_n + sig_ne + sig_e + sig_se + sig_s + sig_sw + sig_w + sig_nw)







# > defining some functions for the robots



def ActRobot(robot):
        # def robo_sig():
        #         if robot.GetCurrentBaseSignal()[0:3] == 'iid':
        #                 initial()
        
        return

def ActBase(base):
        

        # > defining some functions for base  
        # create robots with unique IDs
        
        if base.GetElixir() > 500:
                new_sig = master.cr_robo_sig()    
                base.create_robot(new_sig)

        return

