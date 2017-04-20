{
  resources :
    {
      0 : 
        {
          total_psi : 0
          ore : 0
          used_psi : 10
          gas : 0
        }
    }
  actions : {...}
  is_terminal : false   //whether battle is ended
  reward : 0
  state : 
    {
      0 :                          //player ID
        {
          0 :                      //unit ID
            {
              lifted : false      //air or ground target         
              pixel_size_x : 27
              detected : true     //is found or not
              gwcd : 0            //to ground weapon cd
              idle : true         
              awrange : 0         //to air weapon range
              order : 23          //
              type : 101          //unit type
              position :          //position
                {
                  1 : 32          
                  2 : 32
                }
              targetpos :         //target position
                {
                  1 : 32
                  2 : 32
                }
              energy : 0          //energy
              size : 0            //size
              resource : 0        
              gwdmgtype : 5       //to ground damage type
              pixel_y : 256       
              shieldArmor : 0     //
              awattack : 0        //air attack power
              playerId : 0        //player id
              visible : 1         //is visible
              velocity :          //current speed
                {
                  1 : 0
                  2 : 0
                }
              hp : 1              //current hp,1 means dead
              awdmgtype : 5       //to air damage type
              orders : 
                {
                  1 : {...}
                }
              max_hp : 1          //max hp,1 means dead
              target : -1         //target id
              armor : 0           //defense armor power
              max_shield : 0      //max shield
              maxcd : 0           
              gwattack : 0        //to ground attack power
              shield : 0          //current shield
              awcd : 0            //to air weapon cd
              pixel_x : 256       
              gwrange : 0         //to ground weapon range
              pixel_size_y : 31
            }
          89 :                    //alive sample
            {
              lifted : false
              pixel_size_x : 17
              detected : true
              gwcd : 6
              idle : false
              awrange : 16
              order : 10
              type : 0
              position : 
                {
                  1 : 91
                  2 : 141
                }
              targetpos : 
                {
                  1 : 91
                  2 : 141
                }
              energy : 0
              size : 1
              resource : 0
              gwdmgtype : 3
              pixel_y : 1128
              shieldArmor : 0
              awattack : 6
              playerId : 0
              visible : 1
              velocity : 
                {
                  1 : 0
                  2 : 0
                }
              hp : 16
              awdmgtype : 3
              orders : 
                {
                  1 : {...}
                }
              max_hp : 40
              target : 91
              armor : 0
              max_shield : 0
              maxcd : 15
              gwattack : 6
              shield : 0
              awcd : 6
              pixel_x : 732
              gwrange : 16
              pixel_size_y : 20
            }
        }
      1 :                         //player id=1 :enemy
        {
          88 : 
            {
              lifted : false
              pixel_size_x : 17
              detected : true
              gwcd : 5
              idle : false
              awrange : 16
              order : 10
              type : 0
              position : 
                {
                  1 : 110
                  2 : 138
                }
              targetpos : 
                {
                  1 : 110
                  2 : 138
                }
              energy : 0
              size : 1
              resource : 0
              gwdmgtype : 3
              pixel_y : 1104
              shieldArmor : 0
              awattack : 6
              playerId : 1
              visible : 1
              velocity : 
                {
                  1 : 0
                  2 : 0
                }
              hp : 40
              awdmgtype : 3
              orders : 
                {
                  1 : {...}
                }
              max_hp : 40
              target : 95
              armor : 0
              max_shield : 0
              maxcd : 15
              gwattack : 6
              shield : 0
              awcd : 5
              pixel_x : 880
              gwrange : 16
              pixel_size_y : 20
            }
          86 : 
            {
              lifted : false
              pixel_size_x : 17
              detected : true
              gwcd : 2
              idle : false
              awrange : 16
              order : 10
              type : 0
              position : 
                {
                  1 : 108
                  2 : 135
                }
              targetpos : 
                {
                  1 : 108
                  2 : 135
                }
              energy : 0
              size : 1
              resource : 0
              gwdmgtype : 3
              pixel_y : 1080
              shieldArmor : 0
              awattack : 6
              playerId : 1
              visible : 1
              velocity : 
                {
                  1 : 0
                  2 : 0
                }
              hp : 40
              awdmgtype : 3
              orders : 
                {
                  1 : {...}
                }
              max_hp : 40
              target : 89
              armor : 0
              max_shield : 0
              maxcd : 15
              gwattack : 6
              shield : 0
              awcd : 2
              pixel_x : 868
              gwrange : 16
              pixel_size_y : 20
            }
          91 : 
            {
              lifted : false
              pixel_size_x : 17
              detected : true
              gwcd : 10
              idle : false
              awrange : 16
              order : 10
              type : 0
              position : 
                {
                  1 : 107
                  2 : 141
                }
              targetpos : 
                {
                  1 : 107
                  2 : 141
                }
              energy : 0
              size : 1
              resource : 0
              gwdmgtype : 3
              pixel_y : 1128
              shieldArmor : 0
              awattack : 6
              playerId : 1
              visible : 1
              velocity : 
                {
                  1 : 0
                  2 : 0
                }
              hp : 22
              awdmgtype : 3
              orders : 
                {
                  1 : {...}
                }
              max_hp : 40
              target : 89
              armor : 0
              max_shield : 0
              maxcd : 15
              gwattack : 6
              shield : 0
              awcd : 10
              pixel_x : 860
              gwrange : 16
              pixel_size_y : 20
            }
          92 : 
            {
              lifted : false
              pixel_size_x : 17
              detected : true
              gwcd : 16
              idle : false
              awrange : 16
              order : 10
              type : 0
              position : 
                {
                  1 : 107
                  2 : 138
                }
              targetpos : 
                {
                  1 : 107
                  2 : 138
                }
              energy : 0
              size : 1
              resource : 0
              gwdmgtype : 3
              pixel_y : 1104
              shieldArmor : 0
              awattack : 6
              playerId : 1
              visible : 1
              velocity : 
                {
                  1 : 0
                  2 : 0
                }
              hp : 22
              awdmgtype : 3
              orders : 
                {
                  1 : {...}
                }
              max_hp : 40
              target : 89
              armor : 0
              max_shield : 0
              maxcd : 15
              gwattack : 6
              shield : 0
              awcd : 16
              pixel_x : 860
              gwrange : 16
              pixel_size_y : 20
            }
          90 : 
            {
              lifted : false
              pixel_size_x : 17
              detected : true
              gwcd : 6
              idle : false
              awrange : 16
              order : 10
              type : 0
              position : 
                {
                  1 : 110
                  2 : 141
                }
              targetpos : 
                {
                  1 : 110
                  2 : 141
                }
              energy : 0
              size : 1
              resource : 0
              gwdmgtype : 3
              pixel_y : 1128
              shieldArmor : 0
              awattack : 6
              playerId : 1
              visible : 1
              velocity : 
                {
                  1 : 0
                  2 : 0
                }
              hp : 40
              awdmgtype : 3
              orders : 
                {
                  1 : {...}
                }
              max_hp : 40
              target : 95
              armor : 0
              max_shield : 0
              maxcd : 15
              gwattack : 6
              shield : 0
              awcd : 6
              pixel_x : 880
              gwrange : 16
              pixel_size_y : 20
            }
        }
    }
}
