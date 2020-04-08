"마크다운 사용법"  으로 검색하면 간단한 포맷 명령어들을 볼 수 있습니다. 몇가지만 사용하면 되니 활용바랍니다.
아래 제목 명칭은 적절히 수정바랍니다.
github에 프로젝트 리포지토리를 하나만들고, 팀원들간 committer권한 역할자를 정하고,
내용 수정에 대해서는 pull request 방식으로 합니다.
github 사용법은 한글로도 많으니 적절한것 하나를 찾아 숙지 바랍니다. 
소프트웨어 개발자 혹은 소프트웨어 개발자를 이해하는데 있어서 매우 중요한 경험이 될 것이고, 투자 가치가 있습니다 

```
  git add
  git commit
  git push
  pull-request 
```

# 공식 프로젝트명, 팀명, 제품서비스등 결과물에 대한 브랜드명
프로젝트 명은 self-descriptive하게 합니다. 
보통 논문제목은 이런 식: 
http://www.kiise.or.kr/conference02/cf04/notice.asp?no=116  

프로젝트명도 self-descriptive하게 대략 논문제목처럼 하는데 차이가 있다면 논문제목은 내용만 표시하는데, 여기서는 결과물의 형태를 명시 합니다. 예를 들자면,

  ooo한 oooo  서비스
  ooo를 위한 ooo 솔루션
  oo를 이한    제품
  
  제품은 돈받고 파는 물건을 생각하면 되고, 서비스는 네플릭스 같이 유료로 온라인으로 뭔가 이용하는 서비스를 생각하면 되고, 
  솔루션은 소비자가 일반인이 아닌 기업을 말하는데, 본 과목의 주어진 조건이 "보통의 일반인이 공감할 수 있는 무엇을 만든다" 라는 것이니
  원천기술개발 성 일은 대상외로 삼기 바랍니다.
  
  그리고 
  
# 어떤것을 만들고자 하는 것인지, 풀고자 하는문제, Pain Point
  
  어떤 문제를 풀고하 하는지, 상식에 입각해서 그렇네~  라는 공감을 이끌어낼 수 있는 내용을
  기술합니다.  그래서, 그 문제의 해결책이 없는 지금시점
  사람들은 어떻게 그 문제를 회피하는지,  어떤 불편함, 고통을 받고 있는지 실감나게 기술합니다.
  
# 어떻게 푸는가?
  
  그래서, 어떤 기술을 적용해서 어떤 방식으로 풀어내겠다는 것인지
  역시 엔지니어링 센스가 있는 사람이 이해할 수 있는 수준에서
  기술합니다.
  
# (예상)시스템 구성도
  
  대략 7~8개의 빌딩블록으로,  그리고 빌딩블록중에는 클라이언트 사이드가 있고, 서버사이드가 있겠고,
  클라이언트 사이드이네느 뭔지 센서가 있겠고, 인터넷 그리모 들어가겠고,  서버사이드에는 database도 있겠고,
  AI 분석 부분도 있겠고, 분석결과를 소비자에게 전달,연결하는 앱이든 액튜에이터든 그런게 있을 것 같습니다.
  
  각 블록다이어그램에 구체적 명칭을 씁니다.  명칭의 예는, esp32보드,  aws ubuntu, node.js/express, GPS센서, 자이로/가속기센서, ... 등등
  대략 이런 정도 느낌을 주면 됩니다. [->링크보기](https://www.google.com/search?q=%ED%81%B4%EB%9D%BC%EC%9D%B4%EC%96%B8%ED%8A%B8+%EC%84%9C%EB%B2%84+%EC%8B%9C%EC%8A%A4%ED%85%9C+%EA%B5%AC%EC%84%B1%EB%8F%84+%EA%B7%B8%EB%A6%AC%EA%B8%B0&tbm=isch&ved=2ahUKEwjM64WJptjoAhVWyosBHeFSC3QQ2-cCegQIABAA&oq=%ED%81%B4%EB%9D%BC%EC%9D%B4%EC%96%B8%ED%8A%B8+%EC%84%9C%EB%B2%84+%EC%8B%9C%EC%8A%A4%ED%85%9C+%EA%B5%AC%EC%84%B1%EB%8F%84+%EA%B7%B8%EB%A6%AC%EA%B8%B0&gs_lcp=CgNpbWcQA1CgpAFY1tIBYJDUAWgIcAB4BoABcogBuB6SAQUxMC4yOJgBAKABAaoBC2d3cy13aXotaW1n&sclient=img&ei=_HuNXsz9HdaUr7wP4aWtoAc&bih=1098&biw=1214#imgrc=g0kmuPL1x7CRtM)
 
  
# 기대성과
  
  기대성과는 쓸만할것 같다.  사회적 취약자들을 위한 무엇으로서 가치가 있을 것 같다. 돈벌 수 있을것 같다등, 
  누가 이걸가지고 어떤 득을 볼지 최대한 상상해서 잘 씁니다.
  
# Teams
  
  팀구성원의 이름과 역할,  핵심기여역량, 사진을 넣어주세요.
  committer 역할은 누가 하는지 명시.

# 개발환경

  github, slack 외 사용하는 도구들을 설명합니다.
  github 중심의 pull request 방식으로 agile 개발한다는 내용이 포함되어야 합니다.
  그리고, pull request history 는 점수산정의 한 요소가 됩니다.
  
  * 4~5개 항목으로 날자와 마일스톤 정리해 주세요.  하드웨어 작동테스트 라든지 등 항목.  demo day는 (잠정) 6월8일입니다 
  
  
