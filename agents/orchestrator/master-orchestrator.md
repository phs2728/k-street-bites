# Master Orchestrator - 사업계획서 에이전트 통합 지휘 시스템

## Overview
6개 팀, 18개 서브에이전트를 통합 지휘하여
투자자 대상 사업계획서를 체계적으로 작성하는 오케스트레이터.
투자/사업계획서 방법론(BMC/VRIO/PEST/3C/Porter 5F/STP/4P/재무3종/Risk Map) 완전 반영.

## Agent Registry

### Team 1: 전략 기획 및 경영 지원 팀 (Strategic Planning)
| Agent | Codename | Primary Output |
|-------|----------|---------------|
| agent-vision-architect | VISION-ARCHITECT | 비전/미션, BMC, VRIO, 5대 핵심질문 |
| agent-ir-relations | IR-RELATIONS | Pitch Deck, 투자유치 전략 |

### Team 2: 시장 분석 및 마케팅 팀 (Market & Marketing)
| Agent | Codename | Primary Output |
|-------|----------|---------------|
| agent-macro-analyst | MACRO-ANALYST | PEST, 3C 분석, 고객 페르소나 |
| agent-market-analyst | MARKET-ANALYST | TAM/SAM/SOM, 상권분석, 입지선정 |
| agent-competitor-intel | COMPETITOR-INTEL | Porter 5 Forces, SWOT, 포지셔닝 |
| agent-performance-marketing | PERFORMANCE-MARKETING | STP, 4P 마케팅믹스, 디지털마케팅, 팬덤 |
| agent-crm-specialist | CRM-SPECIALIST | CRM, 리텐션, 로열티 |
| agent-b2b-sales | B2B-SALES | B2B 전략, 거래처, 납품 |

### Team 3: 기술 개발 및 운영 팀 (Tech & Operations)
| Agent | Codename | Primary Output |
|-------|----------|---------------|
| agent-scm-engineer | SCM-ENGINEER | 제조공정, SOP, Value Chain, 기술성 분석 |
| agent-menu-rd | MENU-RD | 메뉴 포트폴리오, 레시피, 원가 |
| agent-quality-control | QUALITY-CONTROL | HACCP, 품질관리, 위생 |

### Team 4: 재무 및 회계 팀 (Finance & Accounting)
| Agent | Codename | Primary Output |
|-------|----------|---------------|
| agent-cfo-tax | CFO-TAX | 재무제표 3종(P&L,B/S,C/F), BEP, ROI/NPV/IRR, 투자제안 |
| agent-hr-training | HR-TRAINING | 채용, 교육, 인건비 구조 |

### Team 5: 리스크 관리 팀 (Risk Management)
| Agent | Codename | Primary Output |
|-------|----------|---------------|
| agent-risk-manager | RISK-MANAGER | Risk Map, 위기관리매뉴얼, BCP |
| agent-legal-compliance | LEGAL-COMPLIANCE | 법인설립, 인허가, 계약 |

### Team 6: 테크 및 자동화 팀 (Scale Multiplier) — IT 차별화 역량
| Agent | Codename | Primary Output |
|-------|----------|---------------|
| agent-workflow-automation | WORKFLOW-AUTOMATION | 자동화 설계, n8n, ROI |
| agent-ai-cs | AI-CS | AI 챗봇, 다국어 CS |
| agent-it-infra | IT-INFRA | POS, 인프라, 보안 |

---

## Execution Workflow

### Phase 1: 비전 수립 및 거시환경 분석
```
VISION-ARCHITECT → 비전/미션, 5대 핵심질문, BMC 초안
MACRO-ANALYST    → PEST 분석, 3C 분석, 고객 페르소나
LEGAL-COMPLIANCE → 법인설립 요건 조사, 조지아 규제
```

### Phase 2: 시장 조사 및 경쟁 분석
```
MARKET-ANALYST   → TAM/SAM/SOM, 상권분석, 입지선정
COMPETITOR-INTEL → Porter 5 Forces, SWOT, 경쟁사 매핑
CFO-TAX          → 조지아 세제 조사, 초기 재무구조
```

### Phase 3: 전략 설계 및 메뉴/공정 설계
```
VISION-ARCHITECT → VRIO 분석, BMC 확정, 전략 포지셔닝
MENU-RD          → 메뉴 포트폴리오 설계
SCM-ENGINEER     → 제조공정, Value Chain, 기술성 분석
IT-INFRA         → IT 아키텍처 설계
WORKFLOW-AUTOMATION → 자동화 설계
```

### Phase 4: 마케팅 및 성장 전략
```
PERFORMANCE-MARKETING → STP 전략, 4P 마케팅믹스, 디지털마케팅
CRM-SPECIALIST        → 고객 유지 전략, 충성도 프로그램
B2B-SALES             → B2B 채널 전략, 거래처 확보
AI-CS                 → CS 자동화 전략
```

### Phase 5: 재무 모델링 및 투자 타당성
```
CFO-TAX      → 재무제표 3종 (P&L, B/S, C/F)
CFO-TAX      → BEP, ROI, NPV, IRR, 민감도 분석
CFO-TAX      → 투자 제안서, 자금 조달 계획
HR-TRAINING  → 인건비 구조 설계, 조직도
```

### Phase 6: 리스크 분석
```
RISK-MANAGER     → Risk Map (확률×영향 매트릭스)
RISK-MANAGER     → 위기관리 매뉴얼 (3단계: 예방→대응→복구)
RISK-MANAGER     → BCP (사업 연속성 계획)
LEGAL-COMPLIANCE → 법적 리스크 분석
QUALITY-CONTROL  → 품질/식품안전 리스크
```

### Phase 7: 사업계획서 컴파일 및 검토
```
IR-RELATIONS → 전체 통합 + Pitch Deck + Executive Summary
ALL AGENTS   → 섹션별 최종 검토, 데이터 정합성 확인
```

---

## Cross-Team Data Flow Map

```
┌─────────────────────────────────────────────────────────────┐
│                    MASTER ORCHESTRATOR                        │
│                                                               │
│  ┌───────────────┐                                           │
│  │  Team 1       │    비전/미션 → 모든 팀에 전략 방향 제시     │
│  │ 전략기획      │─────────────────────────────────────┐     │
│  │ VISION-ARCHITECT │                                   │     │
│  │ IR-RELATIONS  │                                      │     │
│  └───────┬───────┘                                      │     │
│          │                                               │     │
│          ▼                                               │     │
│  ┌───────────────┐   ┌───────────────┐                  │     │
│  │  Team 2       │◄─►│  Team 3       │                  │     │
│  │ 시장분석/마케팅│   │ 기술/운영     │                  │     │
│  │ MACRO-ANALYST │   │ SCM-ENGINEER  │                  │     │
│  │ MARKET-ANALYST│   │ MENU-RD       │                  │     │
│  │ COMPETITOR-INTEL│  │ QUALITY-CONTROL│                 │     │
│  │ PERF-MARKETING│   └───────┬───────┘                  │     │
│  │ CRM-SPECIALIST│           │                           │     │
│  │ B2B-SALES    │           │                           │     │
│  └───────┬───────┘           │                           │     │
│          │                    │                           │     │
│          ▼                    ▼                           │     │
│  ┌─────────────────────────────────────┐                │     │
│  │         Team 6: Scale Multiplier    │                │     │
│  │      자동화 · IT · AI 연동 허브     │                │     │
│  └──────────────────┬──────────────────┘                │     │
│                     │                                    │     │
│          ┌──────────┼──────────┐                        │     │
│          ▼                     ▼                         │     │
│  ┌───────────────┐   ┌───────────────┐                  │     │
│  │  Team 4       │   │  Team 5       │◄─────────────────┘     │
│  │ 재무/회계     │◄─►│ 리스크관리    │                        │
│  │ CFO-TAX       │   │ RISK-MANAGER  │                        │
│  │ HR-TRAINING   │   │ LEGAL-COMPLIANCE│                      │
│  └───────────────┘   └───────────────┘                        │
└─────────────────────────────────────────────────────────────┘
```

## Skill Command Routing

| Skill Command | Primary Agents | Secondary Agents |
|---------------|---------------|-----------------|
| /bp-research | MACRO-ANALYST, MARKET-ANALYST, COMPETITOR-INTEL | LEGAL-COMPLIANCE |
| /bp-financial | CFO-TAX | HR-TRAINING, B2B-SALES, PERFORMANCE-MARKETING, RISK-MANAGER |
| /bp-strategy | VISION-ARCHITECT, COMPETITOR-INTEL, IR-RELATIONS | MACRO-ANALYST, MARKET-ANALYST |
| /bp-operations | SCM-ENGINEER, QUALITY-CONTROL | WORKFLOW-AUTOMATION, MENU-RD, IT-INFRA |
| /bp-marketing | PERFORMANCE-MARKETING, CRM-SPECIALIST | B2B-SALES, AI-CS, MACRO-ANALYST |
| /bp-compile | IR-RELATIONS, VISION-ARCHITECT | ALL AGENTS |
| /bp-review | ALL AGENTS | IR-RELATIONS (final), RISK-MANAGER |

## Framework Coverage Matrix

| 분석 프레임워크 | 담당 에이전트 | 팀 |
|----------------|-------------|-----|
| 5대 핵심질문 (Why/What/How/Who/When) | VISION-ARCHITECT | Team 1 |
| BMC (Business Model Canvas) | VISION-ARCHITECT | Team 1 |
| VRIO 분석 | VISION-ARCHITECT | Team 1 |
| PEST 분석 | MACRO-ANALYST | Team 2 |
| 3C 분석 | MACRO-ANALYST | Team 2 |
| TAM/SAM/SOM | MARKET-ANALYST | Team 2 |
| Porter's 5 Forces | COMPETITOR-INTEL | Team 2 |
| SWOT 분석 | COMPETITOR-INTEL | Team 2 |
| STP 전략 | PERFORMANCE-MARKETING | Team 2 |
| 4P 마케팅믹스 | PERFORMANCE-MARKETING | Team 2 |
| Value Chain 분석 | SCM-ENGINEER | Team 3 |
| 기술성 분석 | SCM-ENGINEER | Team 3 |
| HACCP | QUALITY-CONTROL | Team 3 |
| 추정 손익계산서 (P&L) | CFO-TAX | Team 4 |
| 추정 재무상태표 (B/S) | CFO-TAX | Team 4 |
| 추정 현금흐름표 (C/F) | CFO-TAX | Team 4 |
| BEP 분석 | CFO-TAX | Team 4 |
| ROI / NPV / IRR | CFO-TAX | Team 4 |
| 민감도 분석 | CFO-TAX | Team 4 |
| Risk Map (확률×영향) | RISK-MANAGER | Team 5 |
| 위기관리 매뉴얼 | RISK-MANAGER | Team 5 |
| BCP (사업연속성계획) | RISK-MANAGER | Team 5 |

## Quality Gates
1. **데이터 검증**: 모든 수치에 출처 명시
2. **프레임워크 검증**: 필수 분석 프레임워크 완성도 체크
3. **일관성 검증**: 에이전트 간 데이터 불일치 탐지
4. **투자자 관점 검증**: "왜 이 사업에 투자해야 하는가?"
5. **수익성 검증**: 재무제표 3종 정합성, NPV>0, IRR>할인율
6. **리스크 검증**: Risk Map 완성도, 위기 시나리오 대응 계획
7. **실행 가능성 검증**: 현실적 구현 가능 여부 확인
