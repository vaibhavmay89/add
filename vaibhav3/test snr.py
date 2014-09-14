from lxml import html 
import requests
import time
data = []



urls = ["http://www.sciencedirect.com/science/article/pii/S1631072112001581?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112001520?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112001532?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112001507?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112001490?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112001350?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112001349?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112001635?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112001374?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112001313?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112001301?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112001143?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112001295?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112001155?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112001027?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112001015?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112001416?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112001179?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112001271?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000745?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000757?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000654?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000642?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000666?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000617?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000629?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000630?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000691?np=y",
"http://www.sciencedirect.com/science/article/pii/S163107211200071X?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000721?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000678?np=y",
"http://www.sciencedirect.com/science/article/pii/S163107211200068X?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112001210?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112001040?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000708?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000575?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000289?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000423?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000733?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000526?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000435?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112001088?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000770?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000903?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000605?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000381?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000393?np=y",
"http://www.sciencedirect.com/science/article/pii/S163107211200040X?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000411?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000447?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000459?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000460?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000472?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000484?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000496?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000502?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000514?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000538?np=y",
"http://www.sciencedirect.com/science/article/pii/S163107211200054X?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000551?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000563?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000587?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000599?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000964?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000162?np=y",
"http://www.sciencedirect.com/science/article/pii/S163107211200023X?np=y",
"http://www.sciencedirect.com/science/article/pii/S163107211100194X?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072111001896?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072111001860?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072111001914?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072111001951?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072111001690?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072111001938?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072111001926?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072111001999?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072111001902?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072112000204?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072114001569?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072114000758?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072114001107?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072114001235?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072114001247?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072114001089?np=y",
"http://www.sciencedirect.com/science/article/pii/S1631072114001600?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963514001460?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963514001502?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963514001496?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963514001241?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963514001435?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963514001472?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963514001605?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963514001617?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963514001642?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963514001654?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963514001484?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513002239?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513002148?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513001738?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513001726?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513001805?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513001775?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513001799?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513001751?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513001787?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513001763?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513002069?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513001969?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513002033?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513002008?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513001970?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513002045?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513001982?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513002070?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513002082?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513002094?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351300215X?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513002197?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513001167?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000800?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000824?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000812?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000873?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351300085X?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000861?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000848?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000927?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000691?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000897?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000939?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513001064?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000885?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000903?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000940?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513001209?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000964?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000253?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000666?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000654?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351300068X?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000678?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000708?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000836?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000794?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513001003?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000721?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000460?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000459?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000538?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000472?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000526?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000484?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351300054X?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000496?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000514?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000502?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000769?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000563?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000174?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000150?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000186?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000198?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351300023X?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000216?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000277?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000265?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000241?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000204?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000289?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000228?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000290?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000411?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000423?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000447?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000435?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000605?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000319?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002579?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002580?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002415?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002610?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002397?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002609?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002555?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002592?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002567?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000022?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000149?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000137?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000162?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000125?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351300037X?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000046?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002324?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002336?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002300?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002348?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351200235X?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002373?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002403?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002361?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002312?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002294?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002385?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002543?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963513000083?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002439?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002099?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001823?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002063?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002075?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002105?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002117?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351200204X?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002166?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002129?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002087?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002130?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002178?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002142?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002154?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002506?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512002476?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001872?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001598?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001549?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001574?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001586?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001604?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001562?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001537?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001744?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001690?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001550?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001768?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001756?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351200177X?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001811?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001793?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001781?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001914?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001628?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001276?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001318?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001288?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351200129X?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351200132X?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001331?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001379?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001343?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001306?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001380?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001355?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001392?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001409?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001525?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001367?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001707?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001665?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001124?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001203?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000374?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000635?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351200060X?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351200057X?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000611?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000398?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000672?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000568?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000684?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000623?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000416?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000593?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000659?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000544?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000726?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000660?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000581?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000714?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000696?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000738?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351200074X?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000179?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000866?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351200088X?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000994?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000878?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001008?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351200101X?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000702?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001021?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000854?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512001161?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000908?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351200043X?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000647?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000532?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000556?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511002925?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003165?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003220?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003219?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003323?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003335?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003426?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003414?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003402?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003554?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351100358X?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003608?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003670?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003669?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003657?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003700?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003724?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003736?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511004067?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511004055?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511004031?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351100402X?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511004043?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511004110?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511004109?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000131?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351200012X?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000155?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000143?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000295?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000283?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000258?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000246?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000234?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000222?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000210?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000301?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000362?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000945?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000763?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000052?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003773?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003980?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511004158?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003955?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000180?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003931?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003803?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000064?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000192?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000040?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351100416X?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000209?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000271?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000313?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000167?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000325?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000337?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000118?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000349?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000386?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000404?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000428?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000520?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351200026X?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000350?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000106?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351200009X?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000088?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000039?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000027?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511004092?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511004080?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003566?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000076?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963512000805?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003827?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351100389X?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003190?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003207?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511002901?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003153?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351100327X?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003116?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003268?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003256?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003189?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003347?np=y",
"http://www.sciencedirect.com/science/article/pii/S092596351100330X?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003311?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003293?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003360?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003281?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003359?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003244?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003438?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003384?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003396?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003372?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003578?np=y",
"http://www.sciencedirect.com/science/article/pii/S0925963511003864?np=y"
]
missed = []
def filewriter(filename,row, filter = 1): 
	file = open (filename,"a")
	row = str(row)
	rejections = ["?np=y","http://www.sciencedirect.com/science/article/pii/","mailto:","[","]","'",'"']
	
	if filter == 1: 
		for rejection in rejections:
			row = row.replace(rejection,"") 
	file.write(str(row))
	file.write('\n')

mailing_list = []
total = len(urls)
for i in range(0,len(urls)):
	for attempts in range(0,3):
		try:
			page = requests.get(urls[i])
			break
		except:
			time.sleep(3*attempts)
			continue



	tree = html.fromstring(page.text)

	# print ("paper title:" + str(tree.xpath("//h1[@class = 'svTitle']/text()")))
	# print ("Journal Name: " + str(tree.xpath("//div[@class='title']/a[@class='cLink']/span/text()")))
	# print("authors" + str(tree.xpath('//li/a[@class = "authorName S_C_authorName"]/text()')))
	# print("\n\nAbstract" + str(tree.xpath("//p[@id='sp0005']/text()")) +"\n\n")
	try:
		emails = tree.xpath("//li/a[@class='auth_mail']/@href")
	except: 
		continue
	paperTitle = str(tree.xpath("//h1[@class = 'svTitle']/text()"))
	journal = str(tree.xpath("//div[@class='title']/a[@class='cLink']/span/text()"))
	authors = tree.xpath('//li/a[@class = "authorName S_C_authorName"]/text()')
	abstract = str(tree.xpath("//p[@id='sp0005']/text()"))
	# print(journal,paperTitle,authors,emails)
	for mail in emails: 
		mailing_list.append([journal,paperTitle,mail,authors])
		try:
			filewriter("mailing_list.txt",str(str(urls[i])+"|"+str(journal)+"|"+str(paperTitle)+"|"+str(mail)+"|"+str(authors)))
			##print(str(str(urls[i])+"|"+str(journal)+"|"+str(paperTitle)+"|"+str(mail)+"|"+str(authors)))
		except:
			missed.append(urls[i])
			filewriter("missed.txt",urls[i])

	print("Progress: " +  str(i*100/len(urls))+ "%, "  + str(i+1)  + " Papers have been crawled in which " +  str(len(mailing_list))  + " emails were discovered !")