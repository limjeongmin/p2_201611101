@startuml
title Conditional - grade A-F
start
:get user input marks;
if(90<= marks <=100)
:grade=A;
elseif(80<=marks <90)
:grade=B;
elseif(user marks 70<= marks <80)
:grade=C;
elseif(user marks 60<= marks <70)
:grade=D;
elseif(user marks 50<= marks <60)
:grade=E;
else(user marks marks<50)
:grade=F;
endif
:print grade;
stop
@enduml