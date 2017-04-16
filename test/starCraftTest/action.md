|name|arguments|description|
|----|---------|-----------|
|attack|{int type,int uid,int targetID}|type=0;attack target|
|move|{int type,int uid,int x,int y}|type=1;move to point (x,y)|
|hold|{int type,int uid}|type=2;stay at the current point|
|stop|{int type,int uid}|type=3;stop all actions|
|patrol|{int type,int uid,int x,int y}|type=4;walk around from current point to point (x,y)|

note:all position points range 0<x<y<63 (max value depends on different maps),uid and target id must be valid.
API example:
table action={
	{0,1,10},
	{1,2,50,50},
	{2,4},
	{3,5},
	{4,6,60,60},
}