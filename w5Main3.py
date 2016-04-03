@startuml
title Conditional -Who is winner the RockScissorsPaper?
start
:get userA input a;
:get userB input b;
if (rock win);
  :rock or scissors;
  :rock select user is winner;
elseif (paper win);
  :paper or rock;
  :paper select user is winner;
elseif (scissors win);
  :scissors or paper;
  :scissors select user is winner;
elseif (draw);
  :rock or rock;
  :scissors or scissors;
  :paper or paper;
  :No winner;
endif
stop
@enduml