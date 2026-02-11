# Skill: /bp-compile (최종 사업계획서 컴파일)

## Purpose
모든 에이전트의 산출물을 투자자 대상 사업계획서로 통합 편집

## Activated Agents
- **Primary**: IR-RELATIONS (총괄 편집), VISION-ARCHITECT (전략 방향)
- **Support**: ALL AGENTS (섹션별 검토)

## 사업계획서 최종 구조

### 표지 및 요약
1. **표지** - 사업명, 대표자, 날짜
2. **Executive Summary** (2-3페이지) - IR-RELATIONS

### 제1장: 사업 개요
3. **5대 핵심질문** (Why/What/How/Who/When) - VISION-ARCHITECT
4. **사업 비전 및 미션** - VISION-ARCHITECT
5. **사업 아이템 소개** - MENU-RD + SCM-ENGINEER
6. **핵심 USP** ("직접 뽑는 떡") - COMPETITOR-INTEL
7. **사업 모델 캔버스 (BMC)** - VISION-ARCHITECT
8. **VRIO 분석** - VISION-ARCHITECT

### 제2장: 시장 분석
9. **거시환경 분석 (PEST)** - MACRO-ANALYST
10. **3C 분석** - MACRO-ANALYST
11. **시장 규모** (TAM/SAM/SOM) - MARKET-ANALYST
12. **시장 트렌드** - MARKET-ANALYST
13. **Porter's 5 Forces** - COMPETITOR-INTEL
14. **SWOT 분석** - COMPETITOR-INTEL
15. **타겟 고객 페르소나** - MACRO-ANALYST + PERFORMANCE-MARKETING

### 제3장: 제품 및 서비스
16. **메뉴 포트폴리오** - MENU-RD
17. **현지화 전략** - MENU-RD
18. **품질 관리 체계 (HACCP)** - QUALITY-CONTROL
19. **제조 공정** - SCM-ENGINEER

### 제4장: 마케팅 전략
20. **STP 전략** - PERFORMANCE-MARKETING
21. **4P 마케팅 믹스** - PERFORMANCE-MARKETING
22. **디지털 마케팅** - PERFORMANCE-MARKETING
23. **K-Culture 팬덤 마케팅** - PERFORMANCE-MARKETING
24. **B2B 전략** - B2B-SALES
25. **CRM 전략** - CRM-SPECIALIST

### 제5장: 운영 계획
26. **상권 분석 및 입지** - MARKET-ANALYST
27. **Value Chain 분석** - SCM-ENGINEER
28. **기술성 분석** - SCM-ENGINEER
29. **공급망 관리** - SCM-ENGINEER
30. **IT 및 자동화** - WORKFLOW-AUTOMATION + IT-INFRA
31. **고객 서비스** - AI-CS

### 제6장: 조직 및 인력
32. **조직도** - HR-TRAINING
33. **채용 계획** - HR-TRAINING
34. **교육 프로그램** - HR-TRAINING
35. **대표자 소개** - IR-RELATIONS

### 제7장: 재무 계획
36. **초기 투자 비용 (CAPEX)** - CFO-TAX
37. **매출 예측** - CFO-TAX
38. **추정 손익계산서 (P&L)** - CFO-TAX
39. **추정 재무상태표 (B/S)** - CFO-TAX
40. **추정 현금흐름표 (C/F)** - CFO-TAX
41. **BEP 분석** - CFO-TAX
42. **수익성 분석 (ROI/NPV/IRR)** - CFO-TAX
43. **민감도 분석** - CFO-TAX
44. **투자 제안 및 자금 조달** - CFO-TAX
45. **세금 최적화** - CFO-TAX

### 제8장: 성장 전략
46. **성장 로드맵** - IR-RELATIONS + VISION-ARCHITECT
47. **확장 계획** (2호점) - MARKET-ANALYST
48. **프랜차이즈 가능성** - IR-RELATIONS

### 제9장: 리스크 관리
49. **Risk Map** (확률×영향 매트릭스) - RISK-MANAGER
50. **위기관리 매뉴얼** (예방→대응→복구) - RISK-MANAGER
51. **BCP (사업연속성계획)** - RISK-MANAGER
52. **법적 리스크** - LEGAL-COMPLIANCE
53. **재무 리스크** - CFO-TAX
54. **운영 리스크** - SCM-ENGINEER

### 부록
55. **상세 재무제표** - CFO-TAX
56. **법인 설립 가이드** - LEGAL-COMPLIANCE
57. **레시피 카드 (샘플)** - MENU-RD
58. **시장 조사 데이터** - MARKET-ANALYST
59. **Porter 5 Forces 상세** - COMPETITOR-INTEL

## Compilation Process
```
Step 1: 각 에이전트 산출물 수집 및 품질 검증
Step 2: 프레임워크 완성도 체크 (BMC/VRIO/PEST/3C/5F/STP/4P/재무3종/Risk Map)
Step 3: 섹션별 초안 병합
Step 4: 일관성 검증 (수치, 용어, 톤앤매너)
Step 5: Executive Summary 작성
Step 6: 시각자료 통합 (차트, 그래프, 표)
Step 7: 최종 교정 및 포맷팅
```

## Output
- `output/final/business-plan-full.md` - 전체 사업계획서
- `output/final/executive-summary.md` - Executive Summary
- `output/final/pitch-deck-outline.md` - Pitch Deck 구조

## Usage
```
/bp-compile                     # 전체 컴파일
/bp-compile --chapter [n]       # 특정 장만
/bp-compile --summary           # Executive Summary만
/bp-compile --pitch             # Pitch Deck만
```
