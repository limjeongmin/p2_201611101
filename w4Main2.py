%%plantuml
@startuml
start
:set how many turns;
:set how much to draw bigger;
:set angle;
:set start size;
repeat
if (i is divided by 2) then
    :draw bigger;
endif
:draw;
repeat while(turns)
stop
@enduml