# Quick Reference - 빠른 참조 가이드

## 에이전트 호출 방법

### 직접 호출 (자연어)
특정 주제를 언급하면 관련 에이전트가 자동 활성화됩니다:
- "비전 미션 정리해줘" → VISION-ARCHITECT
- "거시환경 분석해줘" → MACRO-ANALYST
- "시장 규모 알려줘" → MARKET-ANALYST
- "경쟁사 분석해줘" → COMPETITOR-INTEL
- "마케팅 전략 세워줘" → PERFORMANCE-MARKETING
- "재무 계획 세워줘" → CFO-TAX
- "메뉴 개발하자" → MENU-RD
- "리스크 분석해줘" → RISK-MANAGER
- "자동화 설계해줘" → WORKFLOW-AUTOMATION

### 스킬 명령어
```
/bp-research     시장조사 (PEST, 3C, TAM/SAM/SOM, Porter 5F, SWOT)
/bp-financial    재무계획 (P&L, B/S, C/F, BEP, ROI/NPV/IRR, 투자제안)
/bp-strategy     전략수립 (비전/미션, BMC, VRIO, 경쟁전략, 로드맵)
/bp-operations   운영계획 (제조공정, Value Chain, 기술성, HACCP)
/bp-marketing    마케팅전략 (STP, 4P, 디지털, 팬덤, CRM, B2B)
/bp-compile      사업계획서 최종 컴파일
/bp-review       검토 및 개선
```

### 서브옵션 예시
```
/bp-financial --bep              BEP만 분석
/bp-financial --roi              ROI/NPV/IRR만 분석
/bp-financial --bs               재무상태표(B/S)만
/bp-marketing --stp              STP 전략만
/bp-marketing --4p               4P 마케팅믹스만
/bp-marketing --fandom           K-Culture 팬덤만
/bp-research --pest              PEST 분석만
/bp-research --5forces           Porter 5 Forces만
/bp-research --competition       경쟁분석만
/bp-strategy --bmc               BMC만
/bp-strategy --vrio              VRIO만
/bp-operations --valuechain      Value Chain만
/bp-compile --chapter 7          제7장(재무)만
/bp-review --score               점수 산출만
/bp-review --risk                리스크 부문만
```

## 추천 작업 순서
```
1단계: /bp-strategy --vision     → 비전/미션, 5대 핵심질문
2단계: /bp-research              → PEST, 3C, 시장 데이터 수집
3단계: /bp-strategy              → BMC, VRIO, 전략 프레임워크
4단계: /bp-operations            → 운영 계획, Value Chain, 기술성
5단계: /bp-marketing             → STP, 4P, 마케팅 전략
6단계: /bp-financial             → 재무제표 3종, BEP, ROI/NPV/IRR
7단계: /bp-review --risk         → 리스크 분석 (Risk Map, 위기매뉴얼)
8단계: /bp-compile               → 사업계획서 통합
9단계: /bp-review                → 최종 검토 및 보완
```

## 팀별 핵심 산출물

| 팀 | 핵심 산출물 |
|----|-----------|
| Team 1: 전략기획 | 비전/미션, BMC, VRIO, Pitch Deck |
| Team 2: 시장/마케팅 | PEST, 3C, Porter 5F, STP, 4P, CRM |
| Team 3: 기술/운영 | 메뉴, 공정, Value Chain, HACCP |
| Team 4: 재무/회계 | P&L, B/S, C/F, BEP, ROI/NPV/IRR |
| Team 5: 리스크 | Risk Map, 위기관리매뉴얼, BCP, 법무 |
| Team 6: 테크/자동화 | 자동화, 챗봇, IT인프라 |

## 프레임워크 → 에이전트 매핑

| 프레임워크 | 에이전트 |
|-----------|---------|
| BMC / VRIO | VISION-ARCHITECT |
| PEST / 3C | MACRO-ANALYST |
| TAM/SAM/SOM | MARKET-ANALYST |
| Porter 5 Forces | COMPETITOR-INTEL |
| STP / 4P | PERFORMANCE-MARKETING |
| Value Chain / 기술성 | SCM-ENGINEER |
| 재무제표 3종 / BEP / ROI | CFO-TAX |
| Risk Map / BCP | RISK-MANAGER |
