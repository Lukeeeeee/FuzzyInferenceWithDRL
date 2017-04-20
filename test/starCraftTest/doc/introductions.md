##state 
###poperties in object state
  // setup
  int lag_frames; // number of frames from order to execution
  int map_size[2];  // build tile resolution

  string map_name; // Name on the current map
  int player_id;
  int neutral_id;
  bool replay;

  // game state
  Frame* frame; // this will allow for easy reset (XXX)
  string frame_string;
  vector<int> deaths;
  int frame_from_bwapi;
  int battle_frame_count; // if micro mode

  bool game_ended; // did the game end?
  bool game_won;   // did the game won?

  bool battle_just_ended;
  bool battle_won;
  bool waiting_for_restart;
  int last_battle_ended;


  // Alive units in this frame. Used to detect end-of-battle in micro mode. If
  // the current frame is the end of a battle, this will contain all units that
  // were alive when the battle ended (which is not necessarily the current
  // frame due to frame skipping on the serv side). Note that this map ignores
  // onlyConsiderUnits_.
  // Maps unit id to player id
  std::unordered_map<int32_t, int32_t> aliveUnits;

  // Like aliveUnits, but containing only units of types in onlyConsiderUnits.
  // If onlyConsiderUnits is empty, this map is invalid.
  std::unordered_map<int32_t, int32_t> aliveUnitsConsidered;

  // Bots might want to use this map instead of frame->units because:
  // - Unknown unit types are not present (e.g. map revealers)
  // - Units reported as dead are not present (important if the server performs
  //   frame skipping. In that case, frame->units will still contain all units
  //   that have died since the last update.
  // - In micro mode and with frame skipping, deaths are only applied until the
  //   battle is considered finished, i.e. it corresponds to aliveUnits.
  
  Unit units[int player id][int index];

###Unit
  
int id            //unit id
int x 			  //position x
int y 			  //position y
int flags	      //unit's nickname
int health 		  //HP
int max_health 	  //max HP
int shield 		  //unit`s shield
int max_shield    //unit`s max shield
int energy 		  
int maxCD
int groundCD 	  //to ground attack`s CD
int airCD  	   	  //to air attack`s CD
int visible 	  //is visible?
int type 		  //unit`s type
int armor 		
int shieldArmor
int size
int pixel_x
int pixel_y
int pixel_size_x
int pixel_size_y
int groundATK 	  //to ground attack damage per times
int airATK 		  //to air attack damage per times
int groundDmgType 
int airDmgType
int groundRange
int airRange
int orders
int command
int velocityX    //speed x
int velocityY	 //speed y
int playerId     //belongs to player`s id
int resources

##Commands
commands can be constructed in this way:
attack:
[tcc.command_unit_protected,unit.id,tcc.commandtypes.Attack_Unit,target.id]
move:
[tcc.command_unit_protected,unit.id,tcc.commandtypes.Move,targetPos.x,targetPos.y]

and append these commands into action[]
