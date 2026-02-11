# Agent Integration Map - 에이전트 간 데이터 흐름 및 의존성

## Data Flow Matrix

### Division 1 → Other Divisions
```
MARKET-ANALYST
  → CFO-TAX:          매출 예측치, 시장 성장률
  → COMPETITOR-INTEL:  구역별 경쟁사 위치
  → IR-RELATIONS:      TAM/SAM/SOM 데이터
  → B2B-SALES:         상권별 B2B 수요

COMPETITOR-INTEL
  → MENU-RD:           경쟁사 메뉴/가격 트렌드
  → PERFORMANCE-MARKETING: 차별화 메시지
  → IR-RELATIONS:      경쟁 우위 증거
  → B2B-SALES:         경쟁사 B2B 현황

IR-RELATIONS
  → ALL DIVISIONS:     IR 요구사항, 투자자 기대치
  → LEGAL-COMPLIANCE:  투자 계약 검토 요청
```

### Division 2 → Other Divisions
```
SCM-ENGINEER
  → CFO-TAX:           설비 투자비, 원가 데이터
  → QUALITY-CONTROL:   공정별 품질 기준
  → WORKFLOW-AUTOMATION: 생산 프로세스 자동화 요건
  → HR-TRAINING:       생산 인력 교육 요건

KOREAN-FOOD (NEW)
  ↔ GEORGIAN-FOOD:     퓨전 메뉴 공동 개발
  → MENU-RD:           한국 정통 레시피, 도시락/치킨 라인업
  → SCM-ENGINEER:      식재료 수급 요건, 조리 공정
  → QUALITY-CONTROL:   한국식 조리 품질 기준
  → CFO-TAX:           메뉴별 원가 데이터

GEORGIAN-FOOD (NEW)
  ↔ KOREAN-FOOD:       퓨전 메뉴 공동 개발
  → MENU-RD:           조지아 현지화 레시피, 입맛 분석
  → SCM-ENGINEER:      현지 식재료 소싱 정보
  → PERFORMANCE-MARKETING: 조지아어 메뉴 설명, 현지화 USP
  → CRM-SPECIALIST:    조지아 고객 식문화 인사이트

MENU-RD
  ← KOREAN-FOOD:       한국 정통 레시피, 시간대별 전략
  ← GEORGIAN-FOOD:     조지아 현지화 퓨전 레시피
  → SCM-ENGINEER:      레시피 → 공정 요건
  → QUALITY-CONTROL:   메뉴별 품질 기준
  → CFO-TAX:           메뉴별 원가/마진
  → PERFORMANCE-MARKETING: 메뉴 USP, 신메뉴

QUALITY-CONTROL
  → LEGAL-COMPLIANCE:  식품 규정 확인
  → HR-TRAINING:       위생 교육 커리큘럼
  → AI-CS:             품질 관련 고객 응대 기준
```

### Division 3 → Other Divisions
```
B2B-SALES
  → SCM-ENGINEER:      B2B 물량 기반 생산 계획
  → CFO-TAX:           B2B 매출/수금 예측
  → LEGAL-COMPLIANCE:  납품 계약서 검토

PERFORMANCE-MARKETING
  → CRM-SPECIALIST:    리드 데이터
  → CFO-TAX:           마케팅 예산/ROI
  → WORKFLOW-AUTOMATION: 마케팅 자동화 요건

CRM-SPECIALIST
  → AI-CS:             고객 이력/등급 공유
  → WORKFLOW-AUTOMATION: CRM 자동화 요건
  → CFO-TAX:           CLV 기반 매출 예측
  → MENU-RD:           고객 선호 메뉴 데이터
```

### Division 4 → Other Divisions
```
WORKFLOW-AUTOMATION
  → IT-INFRA:          인프라 요구사항
  → CFO-TAX:           자동 정산 데이터

AI-CS
  → WORKFLOW-AUTOMATION: 챗봇-POS 연동
  → IT-INFRA:          챗봇 인프라 요구
  → MENU-RD:           고객 피드백 데이터

IT-INFRA
  → CFO-TAX:           IT 투자 비용
  → LEGAL-COMPLIANCE:  데이터 보호 규정
  → ALL AGENTS:        시스템 통합 지원
```

### Division 5 → Other Divisions
```
CFO-TAX
  → IR-RELATIONS:      재무제표, 손익분석
  → LEGAL-COMPLIANCE:  세무 규정 확인
  → GEORGIA-LEGAL:     조지아 세법 문의

LEGAL-COMPLIANCE
  → CFO-TAX:           세무 규정 가이드
  → HR-TRAINING:       노동법 기준
  → GEORGIA-LEGAL:     조지아 법률 실무 확인

GEORGIA-LEGAL (NEW)
  → LEGAL-COMPLIANCE:  조지아 법률 상세 정보
  → CFO-TAX:           조지아 세법/IE 규정
  → HR-TRAINING:       조지아 노동법 (휴가/공휴일)
  → QUALITY-CONTROL:   조지아 식품안전법
  → ALL AGENTS:        조지아 법적 리스크 자문

HR-TRAINING
  → CFO-TAX:           인건비 데이터
  → SCM-ENGINEER:      인력 배치 계획
  → AI-CS:             CS 교육 연계
  → GEORGIA-LEGAL:     노동법 확인 요청
```

## Parallel Execution Groups

### 독립 실행 가능 그룹
```
Group A (동시 실행):
  - MARKET-ANALYST: 시장 데이터 수집
  - LEGAL-COMPLIANCE: 규제 환경 조사
  - KOREAN-FOOD: 한국 메뉴 레시피/라인업 설계
  - GEORGIAN-FOOD: 조지아 입맛 분석/퓨전 메뉴 제안

Group B (Group A 완료 후):
  - COMPETITOR-INTEL: 경쟁분석 (시장 데이터 필요)
  - MENU-RD: 메뉴 포트폴리오 통합 (KOREAN-FOOD + GEORGIAN-FOOD 결과 필요)
  - SCM-ENGINEER: 공정설계 (메뉴 확정 필요)
  - CFO-TAX: 재무모델링 (데이터 수집 완료 필요)

Group C (Group B 완료 후):
  - PERFORMANCE-MARKETING: 마케팅 전략
  - B2B-SALES: B2B 전략
  - WORKFLOW-AUTOMATION: 자동화 설계

Group D (Group C 완료 후):
  - IR-RELATIONS: 전체 통합 및 Pitch Deck
  - CRM-SPECIALIST: CRM 전략
  - AI-CS: CS 설계
```

## Conflict Resolution
- 수치 불일치: CFO-TAX가 최종 판단
- 전략 충돌: IR-RELATIONS가 투자자 관점에서 결정
- 법적 이슈: LEGAL-COMPLIANCE가 우선
- **조지아 현지법**: GEORGIA-LEGAL이 우선 (현지 전문가)
- 품질 이슈: QUALITY-CONTROL이 우선
