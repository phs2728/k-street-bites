# Skill: /bp-review (사업계획서 검토 및 개선)

## Purpose
작성된 사업계획서의 품질을 투자자 관점에서 종합 검토하고 개선
(프레임워크 완성도 + 재무 정합성 + 리스크 체계 검증 포함)

## Activated Agents
- **Primary**: ALL 18 AGENTS (전문 분야별 검토)
- **Final**: IR-RELATIONS (최종 통합 피드백), RISK-MANAGER (리스크 검증)

## Review Dimensions

### 1. 투자자 관점 검토 (IR-RELATIONS)
```
체크리스트:
□ "왜 이 사업에 투자해야 하는가?" 명확한가?
□ 시장 기회의 크기가 설득력 있는가?
□ 팀(대표자)의 역량이 충분히 드러나는가?
□ 재무 수익이 매력적인가?
□ Exit Strategy가 현실적인가?
□ 경쟁 우위가 지속 가능한가?
```

### 2. 전략 프레임워크 검증 (VISION-ARCHITECT)
```
체크리스트:
□ 5대 핵심질문이 명확하게 답변되었는가?
□ BMC 9 Block이 빠짐없이 작성되었는가?
□ VRIO 분석 결과가 경쟁 전략과 일치하는가?
□ 비전/미션이 사업 전체와 정합적인가?
```

### 3. 시장 분석 검증 (MACRO-ANALYST + MARKET-ANALYST)
```
체크리스트:
□ PEST 분석이 조지아 특수성을 반영하는가?
□ 3C 분석 결과가 전략에 반영되었는가?
□ TAM/SAM/SOM 산출 논리가 타당한가?
□ 성장률 예측이 근거 있는가?
□ 타겟 시장이 충분히 구체적인가?
```

### 4. 경쟁 분석 검증 (COMPETITOR-INTEL)
```
체크리스트:
□ Porter 5 Forces 5개 항목이 모두 분석되었는가?
□ 5 Forces 종합 점수가 전략에 반영되었는가?
□ SWOT 크로스 분석이 완성되었는가?
□ 포지셔닝 맵이 설득력 있는가?
```

### 5. 재무 정합성 검증 (CFO-TAX)
```
체크리스트:
□ P&L, B/S, C/F 3종 재무제표가 상호 정합적인가?
□ P&L 매출 예측과 시장 데이터가 일치하는가?
□ B/S 자산총계 = 부채총계 + 자본총계인가?
□ C/F 기말 현금잔고가 B/S 현금과 일치하는가?
□ 비용 항목에 누락이 없는가?
□ BEP 산출이 정확한가?
□ ROI/NPV/IRR 산출이 정확한가?
□ 민감도 분석이 3개 시나리오를 포함하는가?
□ 세금 계산이 정확한가?
```

### 6. 운영 실현 가능성 (SCM-ENGINEER)
```
체크리스트:
□ Value Chain 분석이 완성되었는가?
□ 기술성 분석이 포함되었는가?
□ 생산 능력과 매출 목표가 일치하는가?
□ 원재료 조달이 실현 가능한가?
□ 설비 투자가 현실적인가?
```

### 7. 리스크 관리 검증 (RISK-MANAGER)
```
체크리스트:
□ Risk Map (확률×영향 매트릭스)이 완성되었는가?
□ Red Zone 리스크에 대한 대응 전략이 있는가?
□ 위기관리 매뉴얼 3단계가 작성되었는가?
□ 시나리오별 대응 프로세스가 구체적인가?
□ BCP(사업연속성계획)가 포함되었는가?
```

### 8. 법적 리스크 점검 (LEGAL-COMPLIANCE)
```
체크리스트:
□ 법인 설립 요건이 정확한가?
□ 필요 인허가가 모두 식별되었는가?
□ 노동법 준수 사항이 반영되었는가?
□ 지적재산권 보호 전략이 있는가?
```

### 9. 마케팅 실효성 (PERFORMANCE-MARKETING)
```
체크리스트:
□ STP 전략이 시장 분석 결과와 일치하는가?
□ 4P 마케팅 믹스가 완성되었는가?
□ 마케팅 예산이 현실적인가?
□ ROAS 목표가 달성 가능한가?
□ 채널 전략이 현지에 적합한가?
```

## Review Scoring

### 점수 체계 (각 항목 1-10점)
| 평가 영역 | 가중치 | 기준 |
|-----------|--------|------|
| 전략 프레임워크 | 15% | BMC, VRIO, 비전/미션 완성도 |
| 시장 분석 | 15% | PEST, 3C, TAM/SAM/SOM, 5 Forces |
| 경쟁 우위 | 10% | 차별화, 진입장벽, USP |
| 재무 타당성 | 25% | 재무제표 3종, ROI/NPV/IRR, 현실성 |
| 팀 역량 | 10% | 경험, 기술, 리더십 |
| 실행 계획 | 10% | 운영, Value Chain, 기술성 |
| 마케팅 전략 | 5% | STP, 4P, 채널 전략 |
| 리스크 관리 | 10% | Risk Map, 위기매뉴얼, BCP |

### 등급
- **A급** (85점+): 투자 유치 준비 완료
- **B급** (70-84점): 일부 보완 후 제출 가능
- **C급** (55-69점): 상당한 수정 필요
- **D급** (55점 미만): 전면 재작성 권고

## Output
- `output/review/review-report.md` - 종합 검토 보고서
- `output/review/framework-check.md` - 프레임워크 완성도 체크
- `output/review/financial-consistency.md` - 재무 정합성 보고
- `output/review/risk-assessment.md` - 리스크 평가 보고
- `output/review/score-card.md` - 점수 카드
- `output/review/improvement-list.md` - 개선 사항 리스트
- `output/review/final-checklist.md` - 최종 체크리스트

## Usage
```
/bp-review                      # 전체 검토
/bp-review --investor           # 투자자 관점만
/bp-review --framework          # 프레임워크 완성도만
/bp-review --financial          # 재무 검증만
/bp-review --risk               # 리스크 관리만
/bp-review --score              # 점수 산출만
/bp-review --improve            # 개선사항 도출만
```
