@startuml

title  <BMI calculator> 


start

:bmi=weight/ (height*height); 
if(bmi=<18.5)
:Under weight;
elseif(18.5<bmi=<23)
:nomarl weight;
elseif(23<bmi=<25)
:over weight;
elseif(25<bmi=<30)
:obesity;
elseif(30<bmi=<35)
:very obesity;
else (35<bmi)
  :extremly obesity;
endif
stop

@enduml